# this is supposed to be a class that accesses and sets the current information about the IPs it only runs in RAM and doesn't keep records.

from typing import Dict

class StorageHandler:
	# Should be a collection of devices in a dictionary. The key for the devices is the dict
	collection: dict = {}

	def __init__(self):
		print("Storage handler successfully created.")

	def removeDevice(self, mac:str):
		# remove the mac address from the dictionary
		print("Device deleted from master collection")
		del self.collection[mac]
	
	def getDevice(self, mac:str):
		return self.collection[mac]
	
	def setDevice(self, mac:str, ip:str, name:str, location:str):
		device = {}
		device["MAC"] = mac
		device["IP"] = ip
		device["name"] = name
		device["location"] = location
		self.collection[device["MAC"]] = device
	
	def getMasterList(self):
		return self.collection

if __name__ == "__main__":
	# I should put in some tests here