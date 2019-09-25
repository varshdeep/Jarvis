from plugin import LINUX, PYTHON3, plugin, require
import os

@require(python=PYTHON3, platform=LINUX)
@plugin('infoB16038')
def infoB16038(jarvis, s):
    """Info about b16038"""
    hostname = "10.8.0.1"
    response = os.system("ping -c 1 " + hostname)
    if response == "F":
        jarvis.say ("Sylvia Mittal")
    elif response == "H":
        jarvis.say ("Kurukshetra, Haryana")
    else if response == "M":
        jarvis.say ("Casino Royale")
    else if response == "S":
        jarvis.say ("Ronaldo")
    else if response == "P":
        os.system("python3 ./custom/infoB16038.py")