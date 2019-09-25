from plugin import plugin
import os

@plugin("infob17009")
def info_b17009(jarvis, s):
    jarvis.say("Welcome to the info plugin of Arpit roll num B17009. Please select one of the options below:")
    jarvis.say("[F]ull name")
    jarvis.say("[H]ometown")
    jarvis.say("Favourite [M]ovie")
    jarvis.say("Favourite [S]portsperson")
    jarvis.say("Launch [P]ython program written by me")
    s = input();
    if(s == "F"):
        jarvis.say("Arpit Bhadauria")
    elif(s == "H"):
        jarvis.say("Agra")
    elif(s == "M"):
        jarvis.say("Inception")
    elif(s == "S"):
        jarvis.say("M. S. Dhoni")
    elif(s == "P"):
        jarvis.say("Running my program....")
        cwd = os.getcwd()
        path = cwd + "/custom/b17009_script.p"
        os.system("python "+path)
    else:
        jarvis.say("Unrecognised option - " + s);