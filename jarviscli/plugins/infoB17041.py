from plugin import LINUX, PYTHON3, plugin, require
import time as t
import os
@require(python=PYTHON3, platform=LINUX)
@plugin('infob17041')
def infob17041(jarvis, s):
	print("Welcome to the info plugin of <your_name> roll num <your_roll_num>. Please select one of the options below:");
	print("[F]ull name");
	print("[H]ometown");
	print("Favourite [M]ovie");
	print("Favourite [S]portperson");
	print("Launch [P]ython program");
	s = input()
	if(s=="F"):
		print("Dheeraj Yadav")
	elif (s=="H"):
		print("Delhi")
	elif (s=="M"):
		print("Dead Poets Society")
	elif (s=="S"):
		print("tourist")
	elif (s=="P"):
		os.system("python ./jarviscli/plugins/hello.py3")
	else:
		print("Command not found");