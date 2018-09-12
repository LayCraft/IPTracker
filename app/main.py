# this is a main script to decide whether you are running the script's client or if you are running it as a server.
import sys

if __name__ == "__main__":
	
	# if the args length is long enough check for the server command
	if len(sys.argv) > 1 and sys.argv[1] == "server":
		# I know it looks weird but only import the server if the args dictate. Otherwise it puts a blank version of the server into RAM and initializes the storage.
		import server
		print("Running the server")
		server.startServer()

	# otherwise just run the client
	else:
		# I know it looks weird but only import the client if server isn't specified. Otherwise it puts the client script into RAM.
		import client
		print("Running the client")
		client.startClient()