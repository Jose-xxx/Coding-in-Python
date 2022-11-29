#!/bin/python3

import sys #allows us to enter command line arguments, among other things
import socket
from datetime import datetime

#understanding arguments 
#python3 crappyscanner.py   <ip>
#             (Arg 0)      (Arg 1)  

#Define our target!
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate a host name to ipv4, if needed.
else: 
	print("invalid amount of arguments.")
	print("syntax: python3 crappyscanner.py <ip>")
	sys.exit() #it is important to exit because if not the process will continue
	
#adding a pretty banner
print("-" * 50)
print("scanning target "+target)
print("time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		#AFINET is ipv4 and SOCK_stream is your port
		result = s.connect_ex((target,port)) #returns error indicator
		print("check port {}".format(port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nexiting program")
	sys.exit()
	
except socket.gaierror:
	print("hostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("couldn't connect to server")
	sys.exit()
		
#version 1 of my crappy scanner!		
#it is veeerrryyy slow
