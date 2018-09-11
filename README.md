# IPTracker
This is a client and server. The server tracks device details. The client collects and sends details and posts them to the server and waits to see if the server will respond with a current list.

Version control for this project on github.schneider-electric.com

-------------------------------------

## History

In the manufacturing area there are many devices and all of the networking infrastructure is managed by Schneider Digital. When we are working with a new industrial device it can get lost because it isn't going to be allocated a dynamic IP using DHCP. The server script can run on our existing application server WVCA41814 and collect changes to the network from devices that have the client installed. Our web server VM is tracked by local DNS so we can use it as the tracker.

## Installation

Create a virtual environment to install the dependencies
`python -m venv env`

Activate the virtual environment. Should look approx like this.
Linux: `source env/bin/activate`
Windows: `env/Scripts/activate.bat`

pip install from the requirements.txt into the env.
`pip install -r requirements.txt --proxy http://gateway.schneider.zscaler.net:80`

When pip installing dependencies be sure to add them to requirements.txt afterward using  `pip freeze > requirements.txt`. (assuming you are trying to contribute to this repo.)

You secretly run this without having a cmd window open in windows.
 
 1. Make a shortcut to client.vbs
 2. Put the shortcut into the startup folder so that it will be loaded when Windows starts.
	`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`
