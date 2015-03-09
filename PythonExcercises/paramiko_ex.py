#!/usr/bin/python

import paramiko

ssh = paramiko.client.SSHClient()

''' 
The default policy is to reject all unknown servers - i.e. RejectPolicy is used
AutoAddPolicy - automatically adds the hostname and new host key to the local HostKeys object.
'''
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())

''' connect to the server '''
ssh.connect(hostname='hostname', port=22, username='user', password='passwd')


'''Execute a command on a host '''
stdin, stdout, stderr = ssh.exec_command('df -k')

print stdout.read()

''' close connection '''
ssh.close()