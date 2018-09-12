class Device:
	# MAC address of device
	mac:str
	# IP address of device
	ip:str
	# machine name
	name:str
	# where is the device
	location:str
	

	def __init__(self, mac:str, ip:str, name:str, location:str):
		print("Device created!")
		self.ip = ip
		self.mac = mac
		self.name = name
		self.location = location