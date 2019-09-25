from plugin import plugin

@plugin("infob17052")
def infob17052(jarvis, s):
	''' Give info about B17062'''
	get_student_info(jarvis, s.upper())

def get_student_info(jarvis, argument):
	
	helptext = "Welcome to the info plugin of Priya roll num B17052.\n\
Please select one of the options below: \n \
	[F]ull name\n \
	[H]ometown\n \
	Favourite [M]ovie\n \
	Favourite [S]portsperson\n \
	Launch [P]ython program written by me\n"

	option = {	"F" : "Priya Singh",
				"H" : "Lucknow, Uttar Pradesh",
				"M" : "MSG 3",
				"S" : "M. S. Dhoni"
			 }.get(argument, "default")
	if argument == 'P':
		small_python_program(jarvis)
	elif option != "default":
		jarvis.say(option);
	else:
		jarvis.say(helptext)

def small_python_program(jarvis):
	# jarvis.say("Let me show you a magic trick.\n Enter a number between 1 and 9 : ")
	num = input("Let me show you a magic trick.\n Enter a number between 1 and 9 : ")
	jarvis.say("Now add 9 to the number and press enter")
	input()
	jarvis.say("Multiply 5 to the result and press enter")
	input()
	jarvis.say("Subtract 15 from the reult and press enter")
	input()
	# jarvis.say("Now tell me the result : ")
	input("Now tell me the result : ")
	jarvis.say("I'll tell you the number you picked at the start\nThe number was : " + num)

	
