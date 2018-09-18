# this client checks to see if the current system information is up to date or if there has been a change to the network. If there is a change it will request a fresh copy of the list and submit a change if the machine's information is out-of-date.
from urllib import request
from urllib.parse import quote
import platform
import os
import netifaces
from time import sleep
import json

SERVER = "wvca41814"
# SERVER = "wvca41814"# for local development
PORT = 1337
# Build once and use many times. Reduces string concat later.
BASE_URL = "http://%s:%i" % (SERVER, PORT)

# get the machine's location for use from the static file this stays constant until the script is restarted
f = open('{0}{1}static{1}location.txt'.format(os.path.dirname(os.path.realpath(__file__)), os.path.sep), 'r')
LOCATION = f.readline().strip() 
print(LOCATION)
f.close()

def getMasterList():
	url = "%s/get" % (BASE_URL)
	return json.loads(request.urlopen(url).read().decode())

def getTime():
	url = "%s/time" % (BASE_URL)
	print("Getting server time")
	return request.urlopen(url).read().decode()

def getMachineInfo():
	print("Collecting machine info.")
	# determine OS
	unvalidated = {} # A place to put uncertain results
	validated = {} # A place to put clean retunable results

		# it is named like this because the os name is nt if it is running a version of windows.
	for interface in netifaces.interfaces():
		collector = {}
		# Save the MAC address if it exists
		if netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'] != '':
			collector['MAC'] = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
		# If the MAC address is blank then move on. MAC is a primary key so is mandatory. Don't continue with this one unless we have some place in the dict to save it
		if 'MAC' not in collector.keys():
			continue
		
		# # collect the IPV6 address TODO: We don't support IPv6 yet
		# if 23 in netifaces.ifaddresses(interface):
		# 	# there is an ipv6 address so we copy the ipv6 first and let the next part overwrite the ipv6 if it exists.
		# 	collector['IP'] = netifaces.ifaddresses(interface)[23][0]['addr']
		# Save the IPv4 if it exists
		if 2 in netifaces.ifaddresses(interface) and netifaces.ifaddresses(interface)[2][0]['addr'] != '':
			collector['IP'] = netifaces.ifaddresses(interface)[2][0]['addr']
		# save the machine name
		collector['name'] = platform.node()
		# Save location
		collector['location'] = LOCATION

		# save the collector into it
		unvalidated[collector['MAC']] = collector
	# print(unvalidated)

	# check each card for valid info and if they are valid add them to the validated list
	for network_card in unvalidated:
		# check that the entry has all neccesary keys
		if 'MAC' not in unvalidated[network_card].keys() or 'IP' not in unvalidated[network_card].keys() or 'name' not in unvalidated[network_card].keys() or 'location' not in unvalidated[network_card].keys():
			# we have discovered that the entry has missing information
			continue
		elif '127.0.0.1' in unvalidated[network_card]['IP'] or '::1' == unvalidated[network_card]['IP']:
			# we have discovered that this is localhost for ipv4 or ipv6. We don't need these
			continue
		elif '00:00:00:00:00:00' == unvalidated[network_card]['MAC']:
			# blank MAC address. This is useless.
			continue
		elif unvalidated[network_card]['IP'][:7] != '10.168.':
			# if the IP is not in the company subnet we can't use it. (maybe it is a virtual network card or something.)
			continue
		else:
			#if it gets this far it is valid
			validated[network_card] = unvalidated[network_card]
	# print(validated)
	return validated

def setInfo(mac, ip, name, location):
	url = "%s/set/%s/%s/%s/%s" % (BASE_URL, quote(mac), quote(ip), quote(name), quote(location)) 
	print(url)
	# read from the url to submit the data and decode its contents because the contents is a list of all devices.
	print("Setting info on server")
	return request.urlopen(url).read().decode()

def removeInfo(mac):
	url = "%s/remove/%s" % (BASE_URL, mac)
	print("Removing information")
	return request.urlopen(url).read().decode()

def startClient():
	# Collect current machine info
	machineInfo = getMachineInfo()
	# get the master list. this should show last submitted time 
	masterList = getMasterList()
	updateTime = getTime()

	# print(machineInfo['54:e1:ad:b1:e5:bb'])
	# print(masterList['54:e1:ad:b1:e5:bb'])

	# if machineInfo['54:e1:ad:b1:e5:bb'] == masterList['54:e1:ad:b1:e5:bb']:
	# 	print("Woop!")

	# submit all valid network connections
	for network_card in machineInfo:
		setInfo(machineInfo[network_card]['MAC'], machineInfo[network_card]['IP'], machineInfo[network_card]['name'], machineInfo[network_card]['location'])
	


	# # every minute check the hardware and the timestamp
	# while True:
	# 	# submit all valid network connections
	# 	for network_card in machineInfo:
	# 		print('the entry')
	# 		print(machineInfo[network_card])
	# 		print('the master list')
	# 		print(masterList)

	# 		setInfo(machineInfo[network_card][0], machineInfo[network_card][1], machineInfo[network_card][2], machineInfo[network_card][3])
		
	# 	# sleep and check again later
	# 	sleep(3)

	# 	# collect the machine info again and respond to changes
	# 	machineInfoTemp = getMachineInfo()
	# 	if machineInfo != machineInfoTemp:
	# 		machineInfo = machineInfoTemp
	# 		# resubmit all of the machine info
	# 		for m in machineInfo:
	# 			setInfo(m[0], m[1], m[2], m[3])

	# 	# if the timestamp is not equal to the old timestamp 
	# 	if updateTime != getTime():
	# 		# get the server's masterlist
	# 		masterList = getMasterList()
			
	# 		# check master list to be sure that client info is up to date.
	# 		for m in machineInfo:
	# 			# the info contained at the dictionary key for the MAC should be identical to the info that we have.
	# 			if masterlist[m[0]] != m:
	# 				setInfo(m[0], m[1], m[2], m[3])

	# 		# save the timestamp of the master list as the new timestamp
	# 		updateTime = getTime()


if __name__ == "__main__":
	startClient()