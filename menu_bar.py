import tkinter as tk
from tkinter import filedialog
import os
FILE_TYPES = [("Text files", "*.txt"), ("All files", "*.*")]


def save_as():
    # Prompt the user to specify the name and location for the new file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=FILE_TYPES)


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Opening file:", file_path)
    else:
        print("Something wrong with the path: ", file_path)


class MenuBar:
    def __init__(self, root):
        self.root = root
        self.menu = tk.Menu(root)
        self.filemenu = tk.Menu(self.menu)
        self.helpmenu = tk.Menu(self.menu)
        self.helpmenu.add_command(label="About")

        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)

    def filemenu_generate(self):
        self.filemenu.add_command(label="Save As", command=save_as)
        self.filemenu.add_command(label="Open", command=open_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)

    def get_menu(self):
        return self.menu
