import requests
import os

import json
from plugin import plugin, require


def myprog():
        print("My program")
        for i in range(5):
                print("Hello World ",i)

@plugin("infob17034")
class infob17034:

	def __call__(self, jarvis, s):
                prompt = 'Welcome to the info plugin of Aman Saxena roll num B17034. Please select one of the options below: \n  [F]ull name // prints your full name \n  [H]ometown // prints your fav movie \n  Favourite [M]ovie // prints your fav movie\n  Favourite [S]portsperson // prints your fav sportsperson\n  Launch [P]ython program written by me // launch a (short) python program\n'
                user_input = jarvis.input(prompt)

                if user_input == 'F':
                        jarvis.say('Aman Saxena')
                elif user_input == 'H':
                        jarvis.say('Indore')
                elif user_input == 'M':
                        jarvis.say('No Strings Attached')
                elif user_input == 'S':
                        jarvis.say('P.V.Sindhu')
                elif user_input == 'P':
                        myprog()
                else:
                        jarvis.say('Invalid options')