from plugin import plugin, require, PYTHON3

@require(python=PYTHON3)
@plugin("infob17104")
def infob17104(jarvis, s):
    """Prints student information menu"""
    jarvis.say("Welcome to the info plugin of Swapnil roll num B17104. Please select one of the options below:")
    jarvis.say("Type the letter in square brackets to execute:")
    jarvis.say("[F]ull name") # prints your full name
    jarvis.say("[H]ometown") # prints your hometown
    jarvis.say("Favourite [M]ovie") # prints your fav movie
    jarvis.say("Favourite [S]portsperson") # prints your fav sportspersonLaunch
    jarvis.say("[P]ython program written by me") # launch a (short)// python program)
    selectoption = input("Please enter your choice: ")
    if (selectoption=='F'):
        jarvis.say("Swapnil Rustagi")
    elif (selectoption=='H'):
        jarvis.say("Gurugram")
    elif (selectoption=='M'):
        jarvis.say("Iron Man")
    elif (selectoption=='S'):
        jarvis.say("None")
    elif (selectoption=='P'):
        jarvis.say("Executing a program to return minimum of two numbers")
        num1=input("First number: ")
        num2=input("Second number: ")
        jarvis.say("Minimum number: {}".format(min(num1, num2)))
    else:
        jarvis.say("Invalid input")

