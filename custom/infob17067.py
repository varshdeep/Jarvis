
import os
from plugin import plugin




@plugin("infob17067")
def infob17064(jarvis, s):
    """Repeats what you type"""
    jarvis.say('Welcome to info plugin of Varshdeep singh roll no b17067. Please select one of the options below: F/H/M/S/P \n')
    jarvis.say('F : to know my nam      e')
    jarvis.say('H : to know my hometown')
    jarvis.say('M : to know my favorite movie')
    jarvis.say('S : to know my favorite sportsman')
    jarvis.say('D : to run my program in Desktop directory\n')
    flag=jarvis.input()
    if flag=='F':
    	jarvis.say('Varshdeep singh\n')
    elif flag=='H':
    	jarvis.say('Kota\n')
    elif flag=='M':
    	jarvis.say('Dropout\n')
    elif flag=='S':
    	jarvis.say('Ronaldo\n')
    elif flag=='D':
    	jarvis.say('My Program  : \n\n')
    	os.system("python /local/user/Desktop/prog.py")
    jarvis.say(s)