from tkinter import *
from tkinter import ttk

root = Tk()
root.title("AppWindow")

label_name = ttk.Label(root, text="First Name:")
label_name.grid(row=0, column=0, sticky=NW)
label_location = ttk.Label(root, text="Location:")
label_location.grid(row=1, column=0, sticky=NW)

label_lastname = ttk.Label(root, text="Last Name:")
label_lastname.grid(row=0, column=2, sticky=NW)
label_gender = ttk.Label(root, text="Gender:")
label_gender.grid(row=1, column=2, sticky=NW)

v_name = StringVar()
v_lastname = StringVar()
v_location = StringVar()
ttk.Entry(root, width=20, textvariable=v_name).grid(row=0, column=1, sticky=NW)
ttk.Entry(root, width=20, textvariable=v_lastname).grid(row=0, column=3, sticky=NW)
ttk.Entry(root, width=20, textvariable=v_location).grid(row=1, column=1, sticky=NW)
listbox_gender = Listbox(root, height=2)
listbox_gender.grid(row=1, column=3, sticky=NW)
listbox_gender.insert(0, 'Male')
listbox_gender.insert(1, 'Female')

listview = Listbox(root, width=60, height=6)
listview.grid(row=2, column=0, rowspan=6, columnspan=4, sticky=SW)


def on_btn_add():
    global v_name, v_lastname, v_location
    print(v_name.get() + ' ', end='')
    print(v_lastname.get() + ' is in ', end='')
    print(v_location.get())


btn_add = Button(root, text="Add", command=on_btn_add)
btn_add.grid(row=2, column=5, sticky=NE)
btn_clear = Button(root, text="Clear", command=on_btn_add)
btn_clear.grid(row=3, column=5, sticky=NE)

root.mainloop()
