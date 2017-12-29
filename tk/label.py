import Tkinter as tk

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
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop!', width=25, command=set_continue)
button.pack()
root.mainloop()
