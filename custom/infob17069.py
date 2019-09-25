from plugin import plugin
import os

@plugin("infob17069")
def infob17069(jarvis, s):
	"""Repeats what you type"""
	jarvis.say("Welcome to the info plugin of Vipul Sharma B17069. Please select one of the options below.\n[F]ull name - prints your full name\n[H]ometown - prints your hometown\nFavourite [M]ovie - prints your fav movie\nFavourite [S]portsperson - prints your fav sportsperson\nLaunch [P]ython program written by me - Launch a (short) python program");
	s = input()
	if s=="F":
		print("Vipul Sharma")
	elif s=="H":
		print("Dharamshala")
	elif s=="M":
		print("The Social Network")
	elif s=="S":
		print("Rohit Sharma")
	elif s=="P":
		os.system("python3 ./custom/file 1")
	else:
		print("Enter F, H, M, S or P")