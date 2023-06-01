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
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton',
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton',
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton',
                             command = lambda : controller.show_frame(helpPage))
        # helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10, sticky=tk.SE) 
  
        # label of header
        label = ttk.Label(self, text ="Here's how to use your Catcobot", font = LARGEFONT)
        # putting the grid in its place by using grid
        label.grid(row = 1, column = 4, padx = 10, pady = 10)