from bottle import route, run, template
import json
from storage_handler import StorageHandler

# @route('/<name>')
# def index(name):
# 	return template('<b>Hello {{name}}</b>', name=name)
storage = StorageHandler()
def startServer():
	@route('/')
	def masterList():
		return storage.getMasterList()

	@route('/<mac>/<ip>/<name>/<location>')
	def addDevice(mac, ip, name, location):
		storage.setDevice(mac, ip, name, location)

	run(host='localhost', port=8080)