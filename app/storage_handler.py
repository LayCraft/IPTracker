# this is supposed to be a class that accesses and sets the current information about the IPs it only runs in RAM and doesn't keep records.

from typing import Dict

class StorageHandler:
	# Should be a collection of devices in a dictionary. The key for the devices is the mac address
	# The mac address is used because theoretically a machine could use two IP addresses if it has two network cards

	collection: dict = {}

	def __init__(self):
		print("RAM storage initialized. Neat")

	def removeDevice(self, mac:str):
		# remove the device at the mac address from the dictionary
		print("Device deleted from master collection")
		del self.collection[mac]
		return self.collection
	
	def getDevice(self, mac:str):
		return self.collection[mac]
	
	def setDevice(self, mac:str, ip:str, name:str, location:str):
		device = {}
		device["MAC"] = mac
		device["IP"] = ip
		device["name"] = name
		device["location"] = location
		self.collection[device["MAC"]] = device
		return self.collection
	
	def getMasterList(self):
		return self.collection

	def reset(self):
		self.collection = {}
		return self.collection
