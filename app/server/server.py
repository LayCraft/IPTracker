from bottle import route, run, error, static_file
from storage_handler import StorageHandler

storage = StorageHandler()
def startServer():
	@error(404)
	def error404(error):
		return static_file('api.html', root='app/server/static')

	@route('/time')
	def getUpdateTime():
		return storage.getUpdateTime()

	@route('/get')
	def getMasterList():
		return storage.getMasterList()

	@route('/remove/<mac>')
	def removeDevice(mac):
		return storage.removeDevice(mac)
	
	@route('/reset')
	def resetSystem():
		return storage.reset()

	@route('/set/<mac>/<ip>/<name>/<location>')
	def setDevice(mac, ip, name, location):
		storage.setDevice(mac, ip, name, location)
		return storage.setDevice(mac, ip, name, location)

	run(host='wvca41814', port=1337)
	# run(host='localhost', port=1337)# for development

if __name__ == "__main__":
	startServer()