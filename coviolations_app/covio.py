import subprocess
import json
import yaml
import requests
from git import Repo


def _read_violation(command):
    """Read violation"""
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    proc.wait()
    return proc.stdout.read()


def main():
    config = yaml.load(open('.covio.yaml'))
    repo = Repo('.')
    hash, branch = repo.head.commit.name_rev.split(' ')
    request = {
        'project': config['project'],
        'service': config['service'],
        'violations': [
            {
                'name': name,
                'raw': _read_violation(command),
            } for name, command in config['violations'].items()
        ],
        'commit': {
            'hash': hash,
            'branch': branch,
            'author': repo.head.commit.author.name,
            'summary': repo.head.commit.summary,
        }
    }
    requests.post(
        config['endpoint'], data=json.dumps(request),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        },
    )
