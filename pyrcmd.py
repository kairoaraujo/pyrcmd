#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import content

import paramiko
import time
import socket


class SSH(object):
    """ Connect and execute command to a client server

        Attributes:
        IP          IP or Hostname to client server
        User        User used to connect using ssh
        passwd      Password used to connect to ssh
        timeout     Timeout to Connect (Hostname is valid and has route to host),
                    default value for timeout is 30
        Return: Disctionary (Array) with Return Code, Std output and Std Error

        Exceptions: AuthFailure : Client-> Server Problem with Authentication
                    BadHostKey: Host Key does not match
                    SshProtocol: Problem of SSH2 Negotiation
                    TimeOut: Timeout while trying to connect to a valid address
    """

    def __init__(self, ip, user, passwd, timeout=30):
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.timeout = timeout

    def execute(self, command):
        seconds_to_timeout = 1
        try:
            test_resovler = socket.gethostbyname(self.ip)
        except socket.gaierror:
            raise ValueError("DNSLookupFailure")
        while True:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(
                        paramiko.AutoAddPolicy())
                client.connect(self.ip, username=self.user, password=self.passwd, timeout=self.timeout)
                break
            except paramiko.AuthenticationException:
                raise ValueError("AuthFailure")
            except paramiko.BadHostKeyException:
                raise ValueError("BadHostKey")
            except paramiko.SSHException:
                raise ValueError("SshProtocol")
            except socket.timeout:
                raise ValueError("TimeOut")
            except:
                seconds_to_timeout += 1
                time.sleep(1)
            if seconds_to_timeout == 15:
                raise ValueError('TimeoutExecuting')
        command_response = {'return_code': '', 'stdout': '', 'stderr': ''}
        chan = client.get_transport().open_session()
        print("Valor de timeout %d" % self.timeout)
        chan.settimeout(self.timeout)
        chan.exec_command(command=command)
        command_response['return_code'] = chan.recv_exit_status()
        while chan.recv_ready():
            command_response['stdout'] += chan.recv(1024)

        while chan.recv_stderr_ready():
            command_response['stderr'] += chan.recv_stderr(1024)

        """
        Code for printing (test)
        """
        print("output")
        print(command_response['stdout'])
        print("error")
        print(command_response['stderr'])
        print("Exit Code")
        print(command_response['return_code'])
        print("fim")
        client.close()
        return command_response
