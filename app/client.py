# this client checks to see if the current system information is up to date or if there has been a change to the network. If there is a change it will request a fresh copy of the list and submit a change if the machine's information is out-of-date.
import urllib.request
import platform
import os
import netifaces
from time import sleep

SERVER = "localhost"
PORT = 1337

# Build once and use many times. Reduces string concat later.
BASE_URL = "http://%s:%i" % (SERVER, PORT)

# get the machine's location for use from the static file this stays constant until the script is restarted
f = open('{0}{1}static{1}location.txt'.format(os.path.dirname(os.path.realpath(__file__)), os.path.sep), 'r')
location = f.readline()
f.close()

def setInfo(mac, ip, name, location):
	url = "%s/set/%s/%s/%s/%s" % (BASE_URL, mac, ip, name, location)
	# read from the url to submit the data and decode its contents because the contents is a list of all devices.
	print("Setting info on server")
	return urllib.request.urlopen(url).read().decode()

def getMasterList():
	url = "%s/get" % (BASE_URL)
	return urllib.request.urlopen(url).read().decode()

def getTime():
	url = "%s/time" % (BASE_URL)
	print("Getting server time")
	return urllib.request.urlopen(url).read().decode()

def removeInfo(mac):
	url = "%s/remove/%s" % (BASE_URL, mac)
	print("Removing information")
	return urllib.request.urlopen(url).read().decode()

def getMachineInfo():
	print("Collecting machine info.")
	# determine OS
	unvalidated = getInfo()
	validated = {}
	# check each card for valid info and if they are valid add them to the validated list
	for network_interface in unvalidated:
		if '' in network_interface:
			# missing information
			continue
		elif '127.0.0.1' in network_interface:
			# localhost for ipv4
			continue
		elif '::1' == network_interface[1]:
			# localhost for ipv6
			continue
		elif '00:00:00:00:00:00' == network_interface[0]:
			# blank MAC address
			continue
		else:
			validated[network_interface[0]] = network_interface 

	# print(os.name) # should always return "nt" or "posix"
	return validated

def getInfo():
	identifiers = {}
	# it is named like this because the os name is nt if it is running a version of windows.
	for interface in netifaces.interfaces():
		# make a list of 4 emptystring elements
		collector = ['']*4

		# copy the MAC address into the first slot
		collector[0] = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
		# print(netifaces.ifaddresses(interface))
		# If the MAC address is blank then move on. MAC is a primary key so is mandatory
		if collector[0] == '':
			continue
		
		# collect the IP addresses
		if 23 in netifaces.ifaddresses(interface):
			# there is an ipv6 address so we copy the ipv6 first and let the next part overwrite the ipv6 if it exists.
			collector[1] = netifaces.ifaddresses(interface)[23][0]['addr']
		# if there is the ipv4 element and it isn't blank then we overwrite the ipv6 address
		if 2 in netifaces.ifaddresses(interface) and netifaces.ifaddresses(interface)[2][0]['addr'] != '':
			collector[1] = netifaces.ifaddresses(interface)[2][0]['addr']
		
		# save the machine name
		collector[2] = platform.node()
		collector[3] = location

		# save the collector into it
		identifiers[collector[0]] = collector
		# print(collector)
	return identifiers



def startClient():

	# Intial data load
	updateTime = getTime()
	masterList = getMasterList()
	machineInfo = getMachineInfo()




	# every minute check the hardware and the timestamp
	while True:
		# collect the machine info again and respond to changes
		machineInfoTemp = getMachineInfo()
		if machineInfo != machineInfoTemp:
			machineInfo = machineInfoTemp
			# resubmit all of the machine info
			for m in machineInfo:
				setInfo(m[0], m[1], m[2], m[3])

		# if the timestamp is not equal to the old timestamp 
		if updateTime != getTime():
			# get the server's masterlist
			masterList = getMasterList()
			
			# check master list to be sure that client info is up to date.
			for m in machineInfo:
				# the info contained at the dictionary key for the MAC should be identical to the info that we have.
				if masterlist[m[0]] != m:
					setInfo(m[0], m[1], m[2], m[3])

			# save the timestamp of the master list as the new timestamp
			updateTime = getTime()
		# sleep and check again later
		# sleep(60)