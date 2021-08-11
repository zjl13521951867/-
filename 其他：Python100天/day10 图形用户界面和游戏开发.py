import tkinter
import tkinter.messagebox
top = tkinter.Tk()
import time
from time import sleep

while False:
    sleep(2) 
    if tkinter.messagebox.askokcancel('温馨提示', '10分钟到了'):
        top.quit()
