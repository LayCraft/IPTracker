# this client checks to see if the current system information is up to date or if there has been a change to the network. If there is a change it will request a fresh copy of the list and submit a change if the machine's information is out-of-date.
import urllib.request
import platform
import os
import sys
import netifaces

SERVER = "localhost"
PORT = 1337

# this collection of tuples is a place to put results
identifiers = []

# Build once and use many times. Reduces string concat later.
BASE_URL = "http://%s:%i" % (SERVER, PORT)

# get the machine's location for use from the static file this stays constant until the script is restarted
f = open('{0}{1}static{1}location.txt'.format(os.path.dirname(os.path.realpath(__file__)), os.path.sep), 'r')
location = f.readline()
f.close()

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

def getMachineInfo():
	# determine OS
	info = getNtInfo()
	# print(os.name) # should always return "nt" or "posix"
	# print(netifaces.interfaces())
	# print(netifaces.ifaddresses('{6B1D5DE4-5CA4-49E3-BFFE-8F2D390E9E0E}'))
	# query the machine the right way
	# return platform.system()
	return info

def getNtInfo():


	# it is named like this because the os name is nt if it is running a version of windows.
	interfaces = netifaces.interfaces()
	#print(interfaces) # make an ugly array of interface IDs ['{6B1D5DE4-5CA4-49E3-BFFE-8F2D390E9E0E}', '{9739C6A0-FFFC-4300-866C-499268613232}', '{199049E3-808B-40FE-811B-524006C5DB71}', '{EA7B8442-B8CB-40F9-8503-BE17E1934E6B}', '{F1D5BADB-4A4B-11E8-AF18-806E6F6E6963}']
	for interface in interfaces:
		# make a list of 4 emptystring elements
		collector = ['']*4

		# copy the mac address into the first slot
		collector[0] = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
		# print(netifaces.ifaddresses(interface))
			# If the mac address is blank then move on. MAC is a primary key so is mandatory
		if collector[0] == '':
			continue
		
		# collect the IP addresses
		if 23 in netifaces.ifaddresses(interface):
			# there is an ipv6 address so we copy the ipv6 first and let the next part overwrite the ipv6 if it exists.
			collector[1] = netifaces.ifaddresses(interface)[23][0]['addr']
		# if there is the ipv4 element and it isn't blank then we overwrite the ipv6 address
		if 2 in netifaces.ifaddresses(interface) and netifaces.ifaddresses(interface)[2][0]['addr'] != '':
			collector[1] = netifaces.ifaddresses(interface)[2][0]['addr']
		
		'''
		# Three ways to get your computer name. Saving for linux use later. All work in nt.
		platform.node()
		socket.gethostname()
		os.environ['COMPUTERNAME']
		'''

		# save the machine name
		collector[2] = platform.node()
		collector[3] = location

		# save the collector into it
		identifiers.append(collector)
		# print(collector)
	return identifiers



def startClient():
	# print(setInfo("foo", "bar", "baz", "qux"))
	# print(getMasterList())
	# print(getTime())
	# print(setInfo("foo", "bar", "baz", "qux"))
	# print(getTime())
	# print(removeInfo("foo"))
	# print(getTime())
	# print(getTime())
	# print(getMasterList())
	print(getMachineInfo())
	return None