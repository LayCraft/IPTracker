from bottle import route, run, template
import json
from storage_handler import StorageHandler

storage = StorageHandler()
def startServer():
	
	@route('/')
	def displayApi():
		return "API listing here"

	@route('/list')
	def getMasterList():
		return storage.getMasterList()

	@route('/get/<mac>')
	def getDevice(mac):
		return storage.getDevice(mac)
	
	@route('/remove/<mac>')
	def removeDevice(mac):
		return storage.removeDevice(mac)
	
	@route('/reset')
	def resetSystem(mac):
		return storage.reset()

	@route('/set/<mac>/<ip>/<name>/<location>')
	def setDevice(mac, ip, name, location):
		storage.setDevice(mac, ip, name, location)
		return storage.setDevice(mac, ip, name, location)

	run(host='localhost', port=8080)