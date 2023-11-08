import tkinter as tk
from socket import *


def click():
    client.send(bytes("\00", 'ascii'))


def finish():
    win.destroy()


win = tk.Tk()

win.title('dog')
win.geometry("300x300+300+300")
win.config(bg='#FFCA86')
btn = tk.Button(win, text='lie', font="Arial 40", width=5, height=2, command=click)
btn.place(relx=0.5, rely=0.5, anchor='center')
client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.1.55", 5001))
win.mainloop()
client.close()
