# this client checks to see if the current system information is up to date or if there has been a change to the network. If there is a change it will request a fresh copy of the list and submit a change if the machine's information is out-of-date.
import urllib.request

SERVER = "localhost"
PORT = 1337

# Build once and use many times. Reduces string concat later.
BASE_URL = "http://%s:%i" % (SERVER, PORT)

def setInfo(mac, ip, name, location):
	url = "%s/set/%s/%s/%s/%s" % (BASE_URL, mac, ip, name, location)
	# read from the url to submit the data and decode its contents because the contents is a list of all devices.
	return urllib.request.urlopen(url).read().decode()

def getMasterList():
	url = "%s/get" % (BASE_URL)
	return urllib.request.urlopen(url).read().decode()

def getTime():
	url = "%s/time" % (BASE_URL)
	return urllib.request.urlopen(url).read().decode()

def removeInfo(mac):
	url = "%s/remove/%s" % (BASE_URL, mac)
	return urllib.request.urlopen(url).read().decode()

def startClient():
	print(setInfo("foo", "bar", "baz", "qux"))
	print(getMasterList())
	print(getTime())
	print(setInfo("foo", "bar", "baz", "qux"))
	print(getTime())
	print(removeInfo("foo"))
	print(getTime())
	print(getTime())
	print(getMasterList())
