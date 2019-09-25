from plugin import plugin
from os import system
VALID_OPTIONS = ['F', 'H', 'M', 'S', 'P']

def prog(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

@plugin("infob17007")
def infob17007(jarvis, s):
    jarvis.say("Welcome to the info plugin of Ananya roll num B17007. Please select one of the options below:")
    jarvis.say("[F]ull name")
    jarvis.say("[H]ometown")
    jarvis.say("Favourite [M]ovie")
    jarvis.say("Favourite [S]portsperson")
    jarvis.say("Launch [P]ython program written by me")

    option=input()
    if option=='F':
        print("Ananya Shukla")
    elif option=='H':
        print("Lucknow")
    elif option=='H':
        print("Lucknow")
    elif option=='M':
        print("Coco")
    elif option=='S':
        print("MS Dhoni")
    elif option=='P':
        print("Program to find if a number is even or odd. Enter a number")
        num=int(input())
        prog(num)
    else:
        print("Invalid input")
