# apreca
# a basic python3 web server
# Written by Aaron Duce 2018
# github.com/aaronduce
# Additions by Sam Brashaw 2018
# github.com/sambrashaw
from socket import socket

from tkinter import *
import socket
from datetime import datetime

# general tkinter gui setup

hostStartMenuWindow = Tk()
hostStartMenuWindow.geometry("250x400")
hostStartMenuWindow.configure(background='#383838')
logname = "apreca-log.txt"
enteredport = StringVar()
enteredhostfile = StringVar()
status = StringVar()

# socket definition and setup
comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def limit(*args):
    value = enteredport.get()
    if len(value) > 5:
        enteredport.set(value[0:5])

def appendLog(tolog):
    log = open(logname, 'w')
    log.append("\n [" + str(datetime.now()) + "]" + tolog)
    log.close()

def setstatus(text, code):
    if code == 0:
        hostStartMenuWindowStatusLabel.configure(foreground="#0F0") # Green
    elif code == 1:
        hostStartMenuWindowStatusLabel.configure(foreground="#FFA500") # Orange
    elif code == 2:
        hostStartMenuWindowStatusLabel.configure(foreground="#F00") # Red
    else:
        hostStartMenuWindowStatusLabel.configure(foreground="#FFF") # White
    status.set(text)

def hoststart():
    host, port = enteredhostfile.get(), enteredport.get()
    if host == "" or port == 0 or host is None:
        setstatus("Host or Port not defined.\nAppended to log: apreca-log.txt", 2)
        appendLog("Host or Port not defined. Appended to log: apreca-log.txt")
    else:
        comm_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        comm_socket.bind((host, int(port)))
        comm_socket.listen(1)
        setstatus("Running.", 0)

enteredport.trace("w", limit)  # when the variable changes run limit()

# more gui setup
hostStartMenuWindowAprecaTitle = Label(hostStartMenuWindow, text="apreca", fg="#FFFFFF", font=("Trebuchet MS", 32))
hostStartMenuWindowAprecaTitle.configure(background='#383838')

hostStartMenuWindowAprecaSubTitle = Label(hostStartMenuWindow, text="a basic python3 web server", fg="#FFFFFF", font=("Trebuchet MS", 14))
hostStartMenuWindowAprecaSubTitle.configure(background='#383838')

hostStartMenuWindowAprecaSubSubTitle = Label(hostStartMenuWindow, text="github.com/aaronduce/apreca", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowAprecaSubSubTitle.configure(background='#383838')

hostStartMenuWindowPortLabel = Label(hostStartMenuWindow, text="Enter a port number to host \n the server on (max 5 chars)", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowPortLabel.configure(background='#383838')
hostStartMenuWindowPortEntry = Entry(hostStartMenuWindow, textvariable=enteredport)

hostStartMenuWindowFileLabel = Label(hostStartMenuWindow, text="Enter a file name to host that \n is in Apreca's directory", fg="#FFFFFF", font=("Trebuchet MS", 10))
hostStartMenuWindowFileLabel.configure(background='#383838')
hostStartMenuWindowFileEntry = Entry(hostStartMenuWindow, textvariable=enteredhostfile)

hostStartMenuWindowStartButton = Button(hostStartMenuWindow, text="Start Host", command=hoststart, bg="#000", fg="#fff", font=("Trebuchet MS", 8))

hostStartMenuWindowStatusLabel = Label(hostStartMenuWindow, text="", textvariable=status, fg="#fff", bg="#383838", font=("Trebuchet MS", 10))

hostStartMenuWindowAprecaTitle.pack()
hostStartMenuWindowAprecaSubTitle.pack()
hostStartMenuWindowAprecaSubSubTitle.pack()
hostStartMenuWindowPortLabel.pack()
hostStartMenuWindowPortEntry.pack()
hostStartMenuWindowFileLabel.pack()
hostStartMenuWindowFileEntry.pack()
hostStartMenuWindowStartButton.pack()
hostStartMenuWindowStatusLabel.pack()

hostStartMenuWindow.mainloop() # EOP
