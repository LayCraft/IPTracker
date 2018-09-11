from bottle import route, run, template
import json
import storage_handler
from '../classes/device' import Device

# @route('/<name>')
# def index(name):
# 	return template('<b>Hello {{name}}</b>', name=name)

@route('/')
def masterList():
	test = Device()
	return "root"

run(host='localhost', port=8080)