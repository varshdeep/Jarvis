from plugin import plugin
from os import system

    

@plugin("infob17071")
def infoB(jarvis,s):
    """Repeats what you type"""
    

    def help():
        jarvis.say("[F]ull name")
        jarvis.say("[H]ometown")
        jarvis.say("Favourite [M]ovie")
        jarvis.say("Favourite [S]portsperson ")
        jarvis.say("Launch [P]ython program written by me ")
        jarvis.say("[E]xit ")
        jarvis.say("help")
        return 

    jarvis.say("Welcome to the info plugin of Aaditya Arora B17071 :")
    jarvis.say("Please select one of the options below : ")
    
    help()

    while 1:
        
        optn = jarvis.input()
        if optn == "E":
            break;
        elif optn == "F":
            jarvis.say("Aaditya Arora")
        elif optn == "H":
            jarvis.say("Mandsaur")
        elif optn == "M":
            jarvis.say("PK")
        elif optn == "S":
            jarvis.say("M. S. Dhoni")
        elif optn == "P":
            system("python3 /home/deep_thinker26/ad.py")
        elif optn == "help":
            help()
        else:
            jarivs.say("Random Commands, Unknown Answers -- see the menu :)")

    
