
' To execute it automatically at startup, open the %AppData%\Microsoft\Windows\Start Menu\Programs\Startup\ directory and add a shortcut to the app.vbs file. '
CreateObject("Wscript.Shell").Run "python app/server/server_forever.py", 0