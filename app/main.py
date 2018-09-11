# this is a main entry to decide whether you are running the script's client or if you are running it as a server.
import sys

args = sys.argv
if __name__ == "__main__":
	# if the args length is long enough check for the server command
	if len(args) > 1 and args[1] == "server":
		print("Running the server")
	# otherwise just run the client
	else:
		print("Running the client")
