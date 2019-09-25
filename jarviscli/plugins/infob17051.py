from plugin import plugin
import os

@plugin("infob17051")
def helloworld(jarvis, s):
    """Repeats what you type"""
    jarvis.say("Welcome to the info plugin of Prajjwal roll num B17051. Please select one of the options below: ")
    jarvis.say("[F]ull Name")
    jarvis.say("[H]ometown")
    jarvis.say("Favourite [M]ovie")
    jarvis.say("Favourite [S]portperson")
    jarvis.say("Launch [P]ython program written by me")

    inp = input()

    if inp == 'F' or inp == 'f':
    	jarvis.say("Prajjwal Jha")
    elif inp == 'H' or inp == 'h':
    	jarvis.say("Bhilai")
    elif inp == 'M' or inp == 'm':
    	jarvis.say("Sherlock Homes")
    elif inp == 'S' or inp == 's':
    	jarvis.say("Cristiano Ronaldo")
    elif inp == 'P' or inp == 'p':
    	os.system("python ./jarviscli/plugins/1.py3")
    else:
    	print("Wrong Option!!!")