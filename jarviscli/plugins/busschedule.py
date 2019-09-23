from plugin import LINUX, PYTHON3, plugin, require
import time as t
@require(python=PYTHON3, platform=LINUX)
@plugin('busschedule')
def busschedule(jarvis, s):
     """
     Provides latest bus available
     """
     ar=t.ctime().split(' ')
     systime=ar[3].split(':')
     x=int(float(systime[1])/15)
     if int(systime[0])>=22 or int(systime[0])<7 :
        print("next bus "+"07:15")
     else :
        if(x==0):
          print("next bus "+systime[0]+":15")
        elif x==1:
          print("next bus "+systime[0]+":30")
        elif x==2:
          print("next bus "+systime[0]+":45")
        else :
          print("next bus "+str(int(systime[0])+1)+":15")
