from bottle import route, run, error, static_file
from storage_handler import StorageHandler

storage = StorageHandler()
def startServer():
	@error(404)
	def error404(error):
		return static_file('api.html', root='app/static')

	@route('/time')
	def getUpdateTime():
		return storage.getUpdateTime()

	@route('/list')
	def getMasterList():
		return storage.getMasterList()

	@route('/get/<mac>')
	def getDevice(mac):
		return storage.getDevice(mac)
	
	@route('/reset')
	def resetSystem(mac):
		return storage.reset()

	@route('/set/<mac>/<ip>/<name>/<location>')
	def setDevice(mac, ip, name, location):
		storage.setDevice(mac, ip, name, location)
		return storage.setDevice(mac, ip, name, location)

	run(reloader=True, host='localhost', port=1337)