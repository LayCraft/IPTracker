# this is supposed to be a class that accesses and sets the current information about the IPs
from typing import Dict

class StorageHandler:
	# Should be a collection of devices in a dictionary. The key for the devices is the dict
	collection: dict = {}

	def removeDevice(self, mac:str):
		# remove the mac address from the dictionary
		print("Device deleted from master collection")
		del self.collection['MAC']
	
	def getDevice(self, mac:str):
		return self.collection['MAC']
	
	def setDevice(self, device):
		device["MAC"] = device
	
	def getMasterList(self) -> Dict:
		return self.collection

if __name__ == "__main__":
	tester = StorageHandler()
	print(tester.getMasterList)