import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    mycount = 0
    def __init__(self):
        Gtk.Window.__init__(self, title="My Window")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

        self.button1 = Gtk.Button(label='hello')
        self.button1.connect('clicked', self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label='World')
        self.button2.connect('clicked', self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print('button1 clicked' + str(self.mycount))
        self.mycount += 1

    def on_button2_clicked(self, widget):
        print('button2 world clicked  ' + str(self.mycount))
        self.mycount += 1

win = MyWindow()
win.connect('delete_event', Gtk.main_quit)
win.show_all()
Gtk.main()
