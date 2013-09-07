import subprocess
import json
import yaml
import requests


def _read_violation(command):
    """Read violation"""
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    proc.wait()
    return proc.stdout.read()


def main():
    config = yaml.load(open('.covio.yaml'))
    request = {
        'project': config['project'],
        'service': config['service'],
        'violations': [
            {
                'name': name,
                'raw': _read_violation(command),
            } for name, command in config['violations'].items()
        ]
    }
    requests.post(
        config['endpoint'], data=json.dumps(request),
        headers={
            'Content-type': 'application/json',
            'Accept': 'text/plain',
        },
    )
