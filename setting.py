import tkinter as tk
from tkinter import ttk

import home
import task
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

# settings page window
class settingsPage(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME",
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 1, padx = 10, pady = 10)

        settingBtn = ttk.Button(self, text ="SETTINGS",
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        taskBtn = ttk.Button(self, text ="Tasks",
                            command = lambda : controller.show_frame(task.tasksPage))
     
        # putting the button in its place by
        # using grid
        taskBtn.grid(row = 9, column = 5, padx = 10, pady = 10)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP",
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)
  
  