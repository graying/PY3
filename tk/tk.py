from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("AppWindow")

v_count = 1


def on_btn_add():
    global v_name, v_lastname, v_location, gender, listview, v_count
    print(v_name.get() + ' ', end='')
    print(v_lastname.get() + ' is in ', end='')
    print(v_location.get() + ' ', end='')
    print(' Gender is ' + gender.get())
    listview.insert(END, str(v_count) + ' - '
                    + v_name.get() + ' '
                    + v_lastname.get() + ' '
                    + 'is in ' + v_location.get() + ' '
                    + 'gender is: ' + gender.get()
                    )
    v_count += 1


def on_btn_clear():
    # empty the view
    global listview, v_count
    listview.delete(0, END)
    v_count = 0


def on_quit():
    if messagebox.askokcancel("Quiting", "please comfirm your action"):
        root.destroy()


def on_key(event):
    on_btn_add()


# create a menu bar
mainmenu = Menu(root)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Add', command=on_btn_add)
filemenu.add_command(label='Clear', command=on_btn_clear)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=on_quit)
mainmenu.add_cascade(label="File", menu=filemenu)
root.config(menu=mainmenu)

# create labels
label_name = ttk.Label(root, text="First Name:")
label_name.grid(row=0, column=0, sticky=NW)
label_location = ttk.Label(root, text="Location:")
label_location.grid(row=1, column=0, sticky=NW)

label_lastname = ttk.Label(root, text="Last Name:")
label_lastname.grid(row=0, column=2, sticky=NW)
label_gender = ttk.Label(root, text="Gender:")
label_gender.grid(row=1, column=2, sticky=NW)

# create entries to input
v_name = StringVar()
v_lastname = StringVar()
v_location = StringVar()
ttk.Entry(root, width=20, textvariable=v_name).grid(row=0, column=1, sticky=NW)
ttk.Entry(root, width=20, textvariable=v_lastname).grid(row=0, column=3, sticky=NW)
ttk.Entry(root, width=20, textvariable=v_location).grid(row=1, column=1, sticky=NW)

# create drop down input frame to select gender
gender_set = ["Male", "Female", "Unknown"]
gender = StringVar()
om_gender = ttk.OptionMenu(root, gender, gender_set[0], *gender_set)
om_gender.grid(row=1, column=3, sticky=NW)

# create the scrollbar for list view
scrollbar = Scrollbar(root)
scrollbar.grid(row=2, column=4, rowspan=6, sticky=NS)

# create the view for data inputted
listview = Listbox(root, width=58, height=6, yscrollcommand=scrollbar.set)
listview.grid(row=2, column=0, columnspan=4, rowspan=6, sticky=NS)
scrollbar.config(command=listview.yview)

# Create the buttons
btn_add = Button(root, text="Add", command=on_btn_add, width=8)
btn_add.grid(row=2, column=5, sticky=NE)
btn_clear = Button(root, text="Clear", command=on_btn_clear, width=8)
btn_clear.grid(row=3, column=5, sticky=NE)

# bind shortcut return to button Add
root.bind('<Return>', on_key)
root.mainloop()
