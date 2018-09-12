# this is a main entry to decide whether you are running the script's client or if you are running it as a server.
import sys
from device import Device
from storage_handler import StorageHandler

# import the two different routes through the program
import server
import client

if __name__ == "__main__":
	# if the args length is long enough check for the server command
	if len(sys.argv) > 1 and sys.argv[1] == "server":
		print("Running the server")
		server.startServer()

	# otherwise just run the client
	else:
		print("Running the client")
		client.startClient()