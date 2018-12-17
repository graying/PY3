import Tkinter as tk
import sys

counter = 0 
conti = True

def counter_label(label):
  def count():
    global counter
    global conti
    if (conti):
      counter += 1
      label.config(text=str(counter))
    label.after(1000, count)
  count()

def set_continue():
  global conti
  global button
  conti = not conti
  if conti:
    button.config(text='Stop!')
  else:
    button.config(text='Continue...')

root = tk.Tk()
root.title("Counting Seconds")

label = tk.Label(root, fg="green")
label.grid(row=0, column=0, sticky=tk.E)
counter_label(label)

button = tk.Button(root, text='Stop!', width=15, command=set_continue)
button.grid(row=0, column=1, sticky=tk.E)

exit_button = tk.Button(root, text='Exit', command=sys.exit)
exit_button.grid(row=1, column=1, sticky=tk.E)

root.mainloop()
