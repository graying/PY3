'''ListBox is a layout container,
just like Box or Grid'''
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ListBox Demo")
        self.set_border_width(10)

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Date Format", xalign=0)
        hbox.pack_start(label, True, True, 0)

        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "24-hours")
        combo.insert(1, "1", "AM/PM")
        hbox.pack_start(combo, True, True, 0)
        listbox.add(row)

        row2 = Gtk.ListBoxRow()
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row2.add(hbox2)
        label2 = Gtk.Label("Using DateTime")
        check2 = Gtk.CheckButton()
        hbox2.pack_start(label2, True, True, 0)
        hbox2.pack_start(check2, True, True, 0)
        listbox.add(row2)


window = MyWindow()
window.connect('delete_event', Gtk.main_quit)
window.show_all()
Gtk.main()
