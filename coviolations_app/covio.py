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


def main():
    config = yaml.load(open('.covio.yml'))
    request = {
        'project': config.get(
            'project',
            list(git.remote('-v'))[0].split(':')[1].split(' ')[0][:-4],
        ),
        'service': config.get('service', {'name': 'dummy'}),
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
    requests.post(
        config.get(
            'endpoint', 'http://coviolations.io/api/v1/tasks/',
        ), data=json.dumps(request),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        },
    )
