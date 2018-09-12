# this client checks to see if the current system information is up to date or if there has been a change to the network. If there is a change it will request a fresh copy of the list and submit a change if the machine's information is out-of-date.
import urllib.request
import json

SERVER = "localhost"
PORT = 1337

def setInfo(mac, ip, name, location):
	url = "http://%s:%i/set/%s/%s/%s/%s" % (SERVER, PORT, mac, ip, name, location)
	# read from the url to submit the data and decode its contents because the contents is a list of all devices.
	return urllib.request.urlopen(url).read().decode()

def getInfo():
	url = "http://%s:%i/get" % (SERVER, PORT)
	return urllib.request.urlopen(url).read().decode()


def startClient():
	print(setInfo("foo", "bar", "baz", "qux"))
	print(getInfo())