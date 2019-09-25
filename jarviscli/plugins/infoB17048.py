from plugin import plugin
import os

@plugin("infob17048")
def infoB17048(jarvis, s):
    jarvis.say("Welcome to the info plugin of Khushi roll num B17048. Please select one of the options below:\n[F]ull name // prints your full name\n[H]ometown // prints your hometown\nFavourite [M]ovie // prints your fav movie\nFavourite [S]portsperson // prints your fav sportsperson\nLaunch [P]ython program written by me // launch a (short)// python program")
    inp = input()
    s=str("F")
    if inp == s:
        jarvis.say("Khushi Gupta")
    s1=str("H")
    s2=str("M")
    s3=str("S")
    s4=str("P")
    if inp == s1:
        jarvis.say("Alwar, Rajasthan")
    if inp == s2:
        jarvis.say("Harry Potter Series")
    if inp == s3:
        jarvis.say("M. S. Dhoni")
    if inp == s4:
        os.system("python /local/user/Jarvis/jarviscli/plugins/khushi.py")
        
	
