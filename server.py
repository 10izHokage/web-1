from socket import *
import tkinter as tk
import threading
from PIL import ImageTk, Image

Hostname = gethostname()
Host_IP = gethostbyname(Hostname)
print(Host_IP)

def change_image(im):
    global image_index, lab
    image_index = im
    image = images[image_index]
    lab.configure(image=image)
    lab.image = image

def start_server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((Host_IP, 5001))
    server.listen()

    user, addr = server.accept()

    while True:
        data = user.recv(1)
        data_decode = str(data, 'ascii')
        if not data:
            break
        change_image(int(data_decode))

def finish():
    win.destroy()

new_thread = threading.Thread(target=start_server)
new_thread.start()

win = tk.Tk()
win.title('FrogMood')
win.geometry("256x256+150+80")
win.config(bg='#C45B90')
win.minsize(256, 256)
img = ImageTk.PhotoImage(Image.open("images/first.jpg"))
lab = tk.Label(win, image=img)
lab.pack()

images = [
    ImageTk.PhotoImage(Image.open("images/first.jpg")),
    ImageTk.PhotoImage(Image.open("images/frog1.jpg")),
    ImageTk.PhotoImage(Image.open("images/frog2.jpg")),
]

win.protocol("WM_DELETE_WINDOW", finish)
win.mainloop()
