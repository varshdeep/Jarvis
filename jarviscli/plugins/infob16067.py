from plugin import LINUX, PYTHON3, plugin, require
import os

@require(python=PYTHON3, platform=LINUX)
@plugin('infob16067')

def infob16067(jarvis,s):
	print ("Welcome to the info plugin of Palak roll num B16067. Please select one of the options below:")
	print ("[F]ull name")
	print ("[H]ometown")
	print ("Favourite [M]ovie")
	print ("Favourite [S]portsperson")
	print ("Launch [P]ython program written by me")
	c = jarvis.input()
	if c == 'F':
		print("Palak Gupta")
	elif c == 'H':
		print("Chandigarh")
	elif c == 'M':
		print("xyz")
	elif c == 'S':
		print("abc")
	elif c == 'P':
		os.system("python ~/Documents/Jarvis/jarviscli/plugins/mypythonprog.abc")
	else:
		print("Please select a valid option")
