# gtk application to change river options (main_ratio, main_count, etc.)

# First screen is a bunch of buttons to open menus for each option

# toggle_gaps, switch_layout, cycle_layouts, list_layouts, main_count, main_ratio, toggle_prefer_horizontal, toggle_prefer_right, toggle_reverse, gaps, location

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

options = [ "gaps", "main_count", "main_ratio", "toggle_prefer_horizontal", "toggle_prefer_right", "toggle_reverse", "location" ]
        
# main window is a grid with 3 columns with all the buttons
# when a button is clicked, it may change the window to a new grid with the options for that button or just execute the command
class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="River Options")
        self.set_border_width(10)
        self.set_default_size(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(10)
        self.grid.set_row_spacing(10)
        self.add(self.grid)

        self.buttons = []
        for i in range(len(options)):
            self.buttons.append(Gtk.Button.new_with_label(options[i]))
            self.buttons[i].connect("clicked", self.button_clicked)
            self.grid.attach(self.buttons[i], i % 3, i // 3, 1, 1)

    def button_clicked(self, widget):
        #print(widget.get_label())
        if widget.get_label() == "gaps":
            # place two buttons in the grid: outer and inner
            self.gaps_clicked(widget)
            # force the focus to the dialog
            self.gaps_dialog.grab_focus()


        elif widget.get_label() == "main_count":
            self.grid.destroy()
            self.grid = Gtk.Grid()
            self.grid.set_column_spacing(10)
            self.grid.set_row_spacing(10)
            self.add(self.grid)

            self.main_count = Gtk.Entry()
            self.main_count.set_text("1")
            self.grid.attach(self.main_count, 0, 0, 1, 1)

            self.main_count_button = Gtk.Button.new_with_label("Set Main Count")
            self.main_count_button.connect("clicked", self.main_count_clicked)
            self.grid.attach(self.main_count_button, 1, 0, 1, 1)

        elif widget.get_label() == "main_ratio":
            self.grid.destroy()
            self.grid = Gtk.Grid()
            self.grid.set_column_spacing(10)
            self.grid.set_row_spacing(10)
            self.add(self.grid)

            self.main_ratio = Gtk.Entry()
            self.main_ratio.set_text("0.5")
            self.grid.attach(self.main_ratio, 0, 0, 1, 1)

            self.main_ratio_button = Gtk.Button.new_with_label("Set Main Ratio")
            self.main_ratio_button.connect("clicked", self.main_ratio_clicked)
            self.grid.attach(self.main_ratio_button, 1, 0, 1, 1)

        elif widget.get_label() == "toggle_prefer_horizontal":
            self.toggle_prefer_horizontal_clicked()

        elif widget.get_label() == "toggle_prefer_right":
            self.toggle_prefer_right_clicked()

        elif widget.get_label() == "toggle_reverse":
            self.toggle_reverse_clicked()
            
        elif widget.get_label() == "location":
            self.location_clicked()

    def gaps_clicked(self, widget):
    # two options: outer and inner. when one is clicked, open a dialog to set the gaps
        print("gaps clicked")
        self.gaps_dialog = Gtk.Dialog("Set Gaps", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.gaps_dialog.set_default_size(150, 100)
        self.gaps_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.gaps_dialog.set_modal(True)
        self.gaps_dialog.set_border_width(10)

        self.gaps_dialog_grid = Gtk.Grid()
        self.gaps_dialog_grid.set_column_spacing(10)
        self.gaps_dialog_grid.set_row_spacing(10)
        self.gaps_dialog.get_content_area().add(self.gaps_dialog_grid)
        
        self.gaps_dialog_label = Gtk.Label("Outer or Inner Gaps?")
        self.gaps_dialog_grid.attach(self.gaps_dialog_label, 0, 0, 1, 1)

        self.gaps_dialog_outer = Gtk.Button.new_with_label("Outer")
        self.gaps_dialog_outer.connect("clicked", self.gaps_dialog_outer_clicked)
        self.gaps_dialog_grid.attach(self.gaps_dialog_outer, 0, 1, 1, 1)

        self.gaps_dialog_inner = Gtk.Button.new_with_label("Inner")
        self.gaps_dialog_inner.connect("clicked", self.gaps_dialog_inner_clicked)
        self.gaps_dialog_grid.attach(self.gaps_dialog_inner, 1, 1, 1, 1)

        self.gaps_dialog.show_all()

    def gaps_dialog_outer_clicked(self, widget):
        #print("outer clicked")
        self.gaps_dialog.destroy()
        self.gaps_dialog = Gtk.Dialog("Set Outer Gaps", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.gaps_dialog.set_default_size(150, 100)
        self.gaps_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.gaps_dialog.set_modal(True)
        self.gaps_dialog.set_border_width(10)

        self.gaps_dialog_grid = Gtk.Grid()
        self.gaps_dialog_grid.set_column_spacing(10)
        self.gaps_dialog_grid.set_row_spacing(10)
        self.gaps_dialog.get_content_area().add(self.gaps_dialog_grid)
        
        self.gaps_dialog_label = Gtk.Label("Enter Gaps")
        self.gaps_dialog_grid.attach(self.gaps_dialog_label, 0, 0, 1, 1)

        self.gaps_dialog_entry = Gtk.Entry()
        self.gaps_dialog_entry.set_text("0")
        self.gaps_dialog_grid.attach(self.gaps_dialog_entry, 0, 1, 1, 1)

        self.gaps_dialog.show_all()

    def gaps_dialog_inner_clicked(self, widget):
        #print("inner clicked")
        self.gaps_dialog.destroy()
        self.gaps_dialog = Gtk.Dialog("Set Inner Gaps", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.gaps_dialog.set_default_size(150, 100)
        self.gaps_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.gaps_dialog.set_modal(True)
        self.gaps_dialog.set_border_width(10)

        self.gaps_dialog_grid = Gtk.Grid()
        self.gaps_dialog_grid.set_column_spacing(10)
        self.gaps_dialog_grid.set_row_spacing(10)
        self.gaps_dialog.get_content_area().add(self.gaps_dialog_grid)
        
        self.gaps_dialog_label = Gtk.Label("Enter Gaps")
        self.gaps_dialog_grid.attach(self.gaps_dialog_label, 0, 0, 1, 1)

        self.gaps_dialog_entry = Gtk.Entry()
        self.gaps_dialog_entry.set_text("0")
        self.gaps_dialog_grid.attach(self.gaps_dialog_entry, 0, 1, 1, 1)

        self.gaps_dialog.show_all()

    def main_count_clicked(self, widget):
        #print("main count clicked")
        self.main_count_dialog = Gtk.Dialog("Set Main Count", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.main_count_dialog.set_default_size(150, 100)
        self.main_count_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.main_count_dialog.set_modal(True)
        self.main_count_dialog.set_border_width(10)

        self.main_count_dialog_grid = Gtk.Grid()
        self.main_count_dialog_grid.set_column_spacing(10)
        self.main_count_dialog_grid.set_row_spacing(10)
        self.main_count_dialog.get_content_area().add(self.main_count_dialog_grid)
        
        self.main_count_dialog_label = Gtk.Label("Enter Main Count")
        self.main_count_dialog_grid.attach(self.main_count_dialog_label, 0, 0, 1, 1)

        self.main_count_dialog_entry = Gtk.Entry()
        self.main_count_dialog_entry.set_text("0")
        self.main_count_dialog_grid.attach(self.main_count_dialog_entry, 0, 1, 1, 1)

        self.main_count_dialog.show_all()

    def main_ratio_clicked(self, widget):
        #print("main ratio clicked")
        self.main_ratio_dialog = Gtk.Dialog("Set Main Ratio", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.main_ratio_dialog.set_default_size(150, 100)
        self.main_ratio_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.main_ratio_dialog.set_modal(True)
        self.main_ratio_dialog.set_border_width(10)

        self.main_ratio_dialog_grid = Gtk.Grid()
        self.main_ratio_dialog_grid.set_column_spacing(10)
        self.main_ratio_dialog_grid.set_row_spacing(10)
        self.main_ratio_dialog.get_content_area().add(self.main_ratio_dialog_grid)
        
        self.main_ratio_dialog_label = Gtk.Label("Enter Main Ratio")
        self.main_ratio_dialog_grid.attach(self.main_ratio_dialog_label, 0, 0, 1, 1)

        self.main_ratio_dialog_entry = Gtk.Entry()
        self.main_ratio_dialog_entry.set_text("0")
        self.main_ratio_dialog_grid.attach(self.main_ratio_dialog_entry, 0, 1, 1, 1)

        self.main_ratio_dialog.show_all()

    def toggle_gaps_clicked(self, widget):
        # print("toggle gaps clicked")
        self.toggle_gaps_dialog = Gtk.Dialog("Toggle Gaps", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.toggle_gaps_dialog.set_default_size(150, 100)
        self.toggle_gaps_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.toggle_gaps_dialog.set_modal(True)
        self.toggle_gaps_dialog.set_border_width(10)

        self.toggle_gaps_dialog_grid = Gtk.Grid()
        self.toggle_gaps_dialog_grid.set_column_spacing(10)
        self.toggle_gaps_dialog_grid.set_row_spacing(10)
        self.toggle_gaps_dialog.get_content_area().add(self.toggle_gaps_dialog_grid)
        
        self.toggle_gaps_dialog_label = Gtk.Label("Toggle Gaps")
        self.toggle_gaps_dialog_grid.attach(self.toggle_gaps_dialog_label, 0, 0, 1, 1)

        self.toggle_gaps_dialog.show_all()

    def toggle_main_clicked(self, widget):
        #print("toggle main clicked")
        self.toggle_main_dialog = Gtk.Dialog("Toggle Main", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.toggle_main_dialog.set_default_size(150, 100)
        self.toggle_main_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.toggle_main_dialog.set_modal(True)
        self.toggle_main_dialog.set_border_width(10)

        self.toggle_main_dialog_grid = Gtk.Grid()
        self.toggle_main_dialog_grid.set_column_spacing(10)
        self.toggle_main_dialog_grid.set_row_spacing(10)
        self.toggle_main_dialog.get_content_area().add(self.toggle_main_dialog_grid)
        
        self.toggle_main_dialog_label = Gtk.Label("Toggle Main")
        self.toggle_main_dialog_grid.attach(self.toggle_main_dialog_label, 0, 0, 1, 1)

        self.toggle_main_dialog.show_all()

    def toggle_main_count_clicked(self, widget):
        #print("toggle main count clicked")
        self.toggle_main_count_dialog = Gtk.Dialog("Toggle Main Count", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.toggle_main_count_dialog.set_default_size(150, 100)
        self.toggle_main_count_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.toggle_main_count_dialog.set_modal(True)
        self.toggle_main_count_dialog.set_border_width(10)

        self.toggle_main_count_dialog_grid = Gtk.Grid()
        self.toggle_main_count_dialog_grid.set_column_spacing(10)
        self.toggle_main_count_dialog_grid.set_row_spacing(10)
        self.toggle_main_count_dialog.get_content_area().add(self.toggle_main_count_dialog_grid)
        
        self.toggle_main_count_dialog_label = Gtk.Label("Toggle Main Count")
        self.toggle_main_count_dialog_grid.attach(self.toggle_main_count_dialog_label, 0, 0, 1, 1)

        self.toggle_main_count_dialog.show_all()

    def toggle_main_ratio_clicked(self, widget):
        #print("toggle main ratio clicked")
        self.toggle_main_ratio_dialog = Gtk.Dialog("Toggle Main Ratio", self, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
        self.toggle_main_ratio_dialog.set_default_size(150, 100)
        self.toggle_main_ratio_dialog.set_position(Gtk.WindowPosition.CENTER)
        self.toggle_main_ratio_dialog.set_modal(True)
        self.toggle_main_ratio_dialog.set_border_width(10)

        self.toggle_main_ratio_dialog_grid = Gtk.Grid()
        self.toggle_main_ratio_dialog_grid.set_column_spacing(10)
        self.toggle_main_ratio_dialog_grid.set_row_spacing(10)
        self.toggle_main_ratio_dialog.get_content_area().add(self.toggle_main_ratio_dialog_grid)
        
        self.toggle_main_ratio_dialog_label = Gtk.Label("Toggle Main Ratio")
        self.toggle_main_ratio_dialog_grid.attach(self.toggle_main_ratio_dialog_label, 0, 0, 1, 1)

        self.toggle_main_ratio_dialog.show_all()



if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

