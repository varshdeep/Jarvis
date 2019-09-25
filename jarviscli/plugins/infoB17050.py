from plugin import plugin
import os

@plugin('infob17050')
def infoB17050(jarvis, s):
	jarvis.say('Welcome to the info plugin of Neeraj roll num b17050. Please select one of the options below:')
	jarvis.say('')
	jarvis.say('[F]ull name')
	jarvis.say('[H]ometown')
	jarvis.say('Favourite [M]ovie')
	jarvis.say('Favourite [S]portsperson')
	jarvis.say('Launch [P]ython program written by me')
	c=input()
	if c=='F':
		jarvis.say('Neeraj Kumar Sharma')
	elif c=='H':
		jarvis.say('Jaipur')
	elif c=='M':
		jarvis.say('Avengers: Infinity War')
	elif c=='S':
		jarvis.say('M.S. Dhoni')
	elif c=='P':
		cmd = 'python3 b17050.py'
		os.system(cmd)
	else:
		jarvis.say('Invalid option')