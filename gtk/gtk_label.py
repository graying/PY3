import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_title("WinTitle")

label = Gtk.Label()
label.set_label("Oh this labek")
label.set_angle(30)
window.add(label)

window.connect('delete_event', Gtk.main_quit)
window.show_all()
Gtk.main()