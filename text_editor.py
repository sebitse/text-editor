import tkinter as tk
from menu_bar import MenuBar


class TextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Notepad")
        self.root.geometry("860x600")

        menu_object = MenuBar(self.root)
        menu_object.filemenu_generate()

        self.menu = menu_object.get_menu()
        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(expand=True, fill="both")

        self.root.config(menu=self.menu)
        self.root.mainloop()
