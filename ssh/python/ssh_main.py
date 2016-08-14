#!/usr/bin/python

import paramiko
from sys import stderr, exit
from reverse_tunnel import reverse_forward_tunnel
from ssh_config import host, user, port, key_filename, remote_host, remote_port

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(host, username=user, key_filename=key_filename)
    except Exception as e:
        print >> stderr, "There was an exception connecting to %s:%s: %s" % (user, host, e)
        client.close()
        exit(1)

    try:
        reverse_forward_tunnel(remote_port, remote_host, port, client.get_transport())
    except Exception as e:
        print >> stderr, 'Port forwarding stopped due to exception: %s' % (e)
        exit(1)
except KeyboardInterrupt:
    print '\nPort forwarding stopped.'
    exit(0)
