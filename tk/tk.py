from tkinter import *
from tkinter import ttk

root = Tk()
root.title("AppWindow")

label_txt = ttk.Label(root, text="ttk label")
label_txt.pack()

root.mainloop()