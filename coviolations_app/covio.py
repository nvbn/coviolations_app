import subprocess
import json
import os
from sh import git
import yaml
import requests
import re


STDOUT = 0
STDERR = 1


def _read_violation(command, source=STDOUT):
    """Read violation"""
    proc = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.communicate()[source]


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


def get_branch():
    """Get branch"""
    attempts = [
        os.environ.get('TRAVIS_BRANCH'),
        os.environ.get('GIT_BRANCH', ''),
        git('rev-parse', '--abbrev-ref', 'HEAD').strip(),
    ]
    for attempt in attempts:
        if attempt:
            return re.sub(r'^origin/', '', attempt)


def _create_violation_dict(args):
    """Create violation dict"""
    name, data = args
    result = {
        'name': name,
    }
    if type(data) is dict:
        if 'stderr' in data:
            source = STDERR if data.pop('stderr') else STDOUT
        else:
            source = STDOUT
        result['raw'] = _read_violation(data.pop('command'), source)
        result.update(data)
    else:
        result['raw'] = _read_violation(data)
    return result


def main():
    config = yaml.load(open('.covio.yml'))

    maybe_project = list(git.remote('-v'))[0].split(':')[1].split(' ')[0][:-4]

    if maybe_project == '//':
        maybe_project = '/'.join(re.match(
            r'.*[/:](.*)/(.*).git \(.*\)', list(git.remote('-v'))[0]
        ).groups())
    elif maybe_project.find('/') == 0:
        maybe_project = '/'.join(maybe_project.split('/')[3:])

    request = {
        'project': config.get('project', maybe_project),
        'service': get_service(config),
        'violations': map(
            _create_violation_dict,
            config['violations'].items(),
        ),
        'commit': {
            'hash': gitlog('%H'),
            'branch': get_branch(),
            'author': gitlog('%aN'),
            'summary': gitlog('%s'),
        }
    }
    response = requests.post(
        config.get(
            'endpoint', 'https://coviolations.io/api/v1/tasks/raw/',
        ), data=json.dumps(request),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        },
    )
    print('Violations sent::{}::{}'.format(
        response.status_code, response.text,
    ))
