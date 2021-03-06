pyrcmd
######

Python Remote Commands


.. image:: https://travis-ci.org/marreta-sources/pyrcmd.svg?branch=master
    :target: https://travis-ci.org/marreta-sources/pyrcmd

:PyStorage:   Python Remote Commands toolkit
:Copyright:   Copyright (c) 2016 Bruno Costa, Kairo Araujo <coder@marreta.org>
:License:     BSD
:Development: https://github.com/marreta-sources/pyrcmd

.. contents::
    :local:
    :depth: 2
    :backlinks: none



Installing
==========

Using PIP (not available yet)
-----------------------------

Just run the PIP

.. code-block:: bash

    $ sudo pip install pyrcmd

From local
----------

Download the pyrcmd from PIP (not available yet) or from Marreco Github
http://github.com/marreta-sources/pyrcmd/ and uncompress

.. code-block:: bash

    $ python setup.py install


Using
=====

At the moment the pyrcmd supports commands over SSH.

SSH support
-----------

* Attributes:

   :Address: IP or Hostname to client server
   :User:        User used to connect using ssh
   :Passwd:      Password used to connect to ssh
   :timeout:     Timeout to Connect (Hostname is valid and has route to host), default value for timeout is 30

* Return:

   :returns: Dictionary (Array) with Return Code, Std output and Std Error

* Exceptions:

   :AuthFailure: Client to Server Problem with Authentication
   :BadHostKey: Host Key does not match
   :SshProtocol: Problem of SSH2 Negotiation
   :TimeOut: Timeout while trying to connect to a valid address
   :TimeoutExecuting: Timeout while trying to execute command.


* Sample:

Simple use:

>>> import pyrcmd
>>> remote = pyrcmd.SSH('192.168.0.1', 'foobar', 'Password1')
>>> remote_out = remote.execute('ls')
>>> print remote_out
{'return_code': 0, 'stderr': '', 'stdout': 'total 24\ndrwx------   3 kairo  users  512 Jan 30 11:31 .\ndrwx------  10 kairo  users  512 Jan 30 11:30 ..\n-rw-------   1 kairo  users    0 Jan 30 11:30 foobar.txt\ndrwx------   2 kairo  users  512 Jan 30 11:31 marretinha\n'}
>>> print remote_out['return_code']
0
>>> print remote_out['stdout']
total 24
drwx------   3 kairo  users  512 Jan 30 11:31 .
drwx------  10 kairo  users  512 Jan 30 11:30 ..
-rw-------   1 kairo  users    0 Jan 30 11:30 foobar.txt
drwx------   2 kairo  users  512 Jan 30 11:31 marretinha


Working with exceptions

>>> server = pyrcmd.SSH('192.168.0.1', 'foobar', 'i dont remember', timeout=10)
>>> try:
...     server.execute('whoami')
... except ValueError, exception_error:
...     print exception_error
...
AuthFailure


Contributing
============

1. Make the for from  https://github.com/marreta-sources/pyrcmd

2. Change the code

3. Test the code
    1. First check all the PEP8 recommendations and possible spells.

    2. Run tests with tox

    3. Create a http://travis-ci.com for your fork and verify the tests

4. Submit your code doing a pull request
    1. try to give us details about the code. We are newbies with Python and it
    will be help us.


