from plugin import plugin
import os

@plugin("infob17087")
def helloworld(jarvis, s):
    print('Welcome to the info plugin of Kriti roll num B17087. Please select one of the options below:\n')
    print('F-Full name\n')
    print('H-HomeTown\n')
    print('M-Favorite Movie\n')
    print('S-Favorite Sportsperson\n')
    print('P-Launch Python Programme\n')
    info = input()
    if(info == 'F'):
            jarvis.say('Full name-Kriti Mehta\n')
    elif(info == 'H'):
            jarvis.say('HomeTown-Sirsa\n')
    elif(info == 'M'):
            jarvis.say('Favorite Movie-Taare Zameen Par\n')
    elif(info == 'S'):
            jarvis.say('Favorite SportsPerson-Saina Nehwal\n') 
    elif(info == 'P'):
            #jarvis.say('Launch Python Project\n') 
            os.system("python /local/user/Jarvis-cs308/custom/a.py")     
    else:
            jarvis.say('Invalid Input\n')
            
            
    """Repeats what you type"""
    #jarvis.say(s)


