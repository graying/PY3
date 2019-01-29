# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import sys

win=tk.Tk()
win.title("calculate 24")
win.geometry("800x600")


def on_quit():
#    if tk.messagebox.askokcancel("Quiting", "please comfirm your action"):
    win.destroy()
    sys.exit()
        
mainmenu = tk.Menu(win)
filemenu = tk.Menu(mainmenu, tearoff=0)

#filemenu.add_command(label='Add', command=on_btn_add)
#filemenu.add_command(label='Clear', command=on_btn_clear)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=on_quit)
mainmenu.add_cascade(label="File", menu=filemenu)
win.config(menu=mainmenu)


win.mainloop()