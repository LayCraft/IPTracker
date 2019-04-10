#!/usr/bin/python
from subprocess import Popen
'''
This script launches the server and prevents it from shutting down even after an exception  or crash. On *nix this needs chmod +x to be effective.
'''

while True:
	p = Popen("python app/server/server.py", shell=True)
	p.wait()