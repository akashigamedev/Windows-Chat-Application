import tkinter as tk
from tkinter import *
import os

root = tk.Tk()
root.title("CodeShare")

window_width = 600
window_height = 400

# get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

root.attributes('-alpha', 0.9)

root.attributes('-topmost', 1)


#--------------------------------------
# design layout

users_frame = tk.Frame(root, bg="red")
users_frame.place(relwidth=0.3, relheight=1)

scrollbar = tk.Scrollbar(users_frame)
scrollbar.pack(side= RIGHT, fill = Y)

mylist = Listbox(users_frame, yscrollcommand= scrollbar.set)
for line in range(100):
    mylist.insert(END, "The is line number" + str(line))

mylist.pack( side = LEFT, fill = BOTH)
scrollbar.config( command = mylist.yview)

chat_frame = tk.Frame(root, bg="blue")
chat_frame.place(relwidth=0.7, relheight=1, relx = 0.3)


root.mainloop()