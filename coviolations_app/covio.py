import subprocess
import json
import os
from sh import git
import yaml
import requests


def _read_violation(command):
    """Read violation"""
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    proc.wait()
    return proc.stdout.read()


def gitlog(format):
    return str(git('--no-pager', 'log', "-1", pretty="format:%s" % format))


def get_service(config):
    """Get service"""
    if config.get('service'):
        return config['service']

    if os.environ.get('TRAVIS'):
        return {
            'name': 'travis_ci',
            'job_id': os.environ.get('TRAVIS_JOB_ID'),
            'pull_request_id': os.environ.get('TRAVIS_PULL_REQUEST'),
        }

    if os.environ.get('COVIO_TOKEN'):
        return {
            'name': 'token',
            'token': os.environ.get('COVIO_TOKEN'),
        }

    return {
        'name': 'dummy',
    }


def main():
    config = yaml.load(open('.covio.yml'))

    maybe_project = list(git.remote('-v'))[0].split(':')[1].split(' ')[0][:-4]

    if maybe_project.find('/') == 0:
        maybe_project = '/'.join(maybe_project.split('/')[3:])

    request = {
        'project': config.get('project', maybe_project),
        'service': get_service(config),
        'violations': [
            {
                'name': name,
                'raw': _read_violation(command),
            } for name, command in config['violations'].items()
        ],
        'commit': {
            'hash': gitlog('%H'),
            'branch': os.environ.get(
                'TRAVIS_BRANCH',
                git('rev-parse', '--abbrev-ref', 'HEAD').strip()),
            'author': gitlog('%aN'),
            'summary': gitlog('%s'),
        }
    }
    response = requests.post(
        config.get(
            'endpoint', 'http://coviolations.io/api/v1/tasks/',
        ), data=json.dumps(request),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        },
    )
    print('Violations sent::{}::{}'.format(
        response.status_code, response.text,
    ))
