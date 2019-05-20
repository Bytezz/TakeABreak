import ctypes
import time
import winsound

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0,text, title, style)

n=0
while (n < 10):

    time.sleep(1200)
    if n == 9:
        winsound.Beep(1200,500)
        Mbox('Breaktime!', 'Last Break, Stop working or restart', 0 | 0x40000)
    else:
        winsound.Beep(1200,500)
        Mbox('Breaktime!', 'Hey! Take a break. Make sure to stretch.', 0 | 0x40000)
    n = n + 1
    
