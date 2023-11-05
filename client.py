import tkinter as tk
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("10.23.23.197", 5001))

def click(num):
    client.send(bytes(num, 'ascii'))

def finish():
    win.destroy()


win = tk.Tk()
win.title('ChooseMood')
win.geometry("400x260")
win.config(bg='#00FF7F')
btn3 = tk.Button(win, text='Choose your mood',font="Arial 25", fg='#008800', width=15, height=1)
btn3.place(relx=0.5, rely=0.1, anchor='n')
btn3.bind('<Button-1>', lambda event: click("0"))
btn1 = tk.Button(win, text='GOOD)', font="Arial 25", fg='#008800', width=6, height=1)
btn1.place(relx=0.45, rely=0.65, anchor='e')
btn1.bind('<Button-1>', lambda event: click("1"))
btn2 = tk.Button(win, text='BAD(', font="Arial 25", fg='#008800', width=6, height=1)
btn2.place(relx=0.56, rely=0.65, anchor='w')
btn2.bind('<Button-1>', lambda event: click("2"))

win.mainloop()
client.close()
