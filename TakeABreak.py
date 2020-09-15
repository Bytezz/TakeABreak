#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,time,random
if os.name=="nt":
	import ctypes,winsound
else:
	import pymsgbox
	from playsound import playsound
'''
Program to encourage me to take breaks and suggest an excercise when I do.
edit 'actions' to change excercises
edit 'sleepTime' to change interval between breaks, in seconds
edit 'repeats' to change number of breaks per run (0 for infinite)
'''
sleepTime=1200
repeats=10
actions=[
	"Wrist stretches",
	"10 Push-ups",
	"10 squats",
	"Neck stretches",
	"Get a snack",
	"1 minute plank",
	"Take a stroll",
	"Eye Excersizes"
]
tempactions=list(actions)

def Mbox(title, text):
	if os.name=="nt":
		return ctypes.windll.user32.MessageBoxW(0,text, title, style)
	else:
		return pymsgbox.alert(text, title)

def wait(sleepTime):
	while sleepTime>0:
		if os.name=="nt":
			print(">%s\r"%sleepTime)
		else:
			sys.stdout.write(">%s\r"%sleepTime)
			sys.stdout.flush()
		time.sleep(1)
		sleepTime-=1
	if os.name=="nt":
		winsound.Beep(1200,500)
	else:
		playsound('beeps.wav')

for i in range(0,repeats-1):

	wait(sleepTime)

	if len(tempactions)==0:
		tempactions=list(actions)
	num=random.randint(0,len(tempactions)-1)
	message = tempactions[num]
	tempactions.pop(num)

	Mbox('Breaktime!', message)

wait(sleepTime)
Mbox('Breaktime!', 'Last Break, Stop working or restart')