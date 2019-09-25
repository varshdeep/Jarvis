from plugin import plugin


def sum(jarvis):
	jarvis.say("Give first number to add:")
	a = int(input())
	jarvis.say("Give second number to add:")
	b = int(input())
	jarvis.say("Sum = " + str(a+b))


@plugin("infob17110")
def infoB17110(jarvis, s):
	"""Get info about Varun Singh B17110"""
	jarvis.say("Welcome to the info plugin of Varun Singh roll num B17110. Please select one of the options below:\n[F]ull name // prints your full name\n[H]ometown // prints your hometown\nFavourite [M]ovie // prints your fav movie\nFavourite [S]portsperson // prints your fav sportsperson\nLaunch [P]ython program written by me // launch a (short) python program")
	option = input()
	if option == 'F':
		jarvis.say("Varun Singh")
	elif option == 'H':
		jarvis.say("Lucknow")
	elif option == 'M':
		jarvis.say("Avengers")
	elif option == 'S':
		jarvis.say("MS Dhoni")
	elif option == 'P':
		sum(jarvis)
	else:
		jarvis.say("Wrong input")
