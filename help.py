import tkinter as tk
from tkinter import ttk

import setting
import task
import home

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

# first window frame startpage
class helpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
     
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME",
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 1, padx = 10, pady = 10)

        settingBtn = ttk.Button(self, text ="SETTINGS",
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10)
  
        # label of header
        label = ttk.Label(self, text ="Here's how to use your Catcobot", font = LARGEFONT)
        # putting the grid in its place by using grid
        label.grid(row = 1, column = 4, padx = 10, pady = 10)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP",
                             command = lambda : controller.show_frame(helpPage))
        helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)