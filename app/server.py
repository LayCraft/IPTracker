from bottle import route, run, template
import json
from storage_handler import StorageHandler

storage = StorageHandler()
def startServer():

	@route('/get/<mac>')
	def getDevice(mac):
		return storage.getDevice(mac)

	@route('/')
	def getMasterList():
		return storage.getMasterList()
	
	@route('/remove/<mac>')
	def removeDevice(mac):
		storage.removeDevice(mac)
		return storage.getMasterList()

	@route('/set/<mac>/<ip>/<name>/<location>')
	def setDevice(mac, ip, name, location):
		storage.setDevice(mac, ip, name, location)
		return storage.getMasterList()

	run(host='localhost', port=8080)