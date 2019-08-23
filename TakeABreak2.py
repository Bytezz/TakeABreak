import ctypes
import time
import winsound
import random

'''
Program to encourage me to take breaks and suggest an excercise when I do.
edit 'actions' to change excercises
edit 'sleepTime' to change interval between breaks, in seconds
edit 'repeats' to change number of breaks per run
'''

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0,text, title, style)

sleepTime = 1200
repeats = 10
actions = ["Wrist stretches", "10 Push-ups", "10 squats", "Neck stretches", "Get a snack", "1 minute plank", "Take a stroll", "Eye Excersizes"]
tempactions = list(actions)


n=0
while (n < repeats):

    time.sleep(sleepTime)

    winsound.Beep(1200,500)
    length = len(tempactions)-1
    num = random.randint(0, length)
    message = tempactions[num]
    tempactions.pop(num)
    if len(tempactions) == 0:
        tempactions = list(actions)

    Mbox('Breaktime!', message, 0 | 0x40000)
    n = n + 1

time.sleep(sleepTime)
winsound.Beep(1200,500)
Mbox('Breaktime!', 'Last Break, Stop working or restart', 0 | 0x40000)
    
