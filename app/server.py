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
		
		return "root"

	run(host='localhost', port=8080)