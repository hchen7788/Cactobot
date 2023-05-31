import tkinter as tk
from tkinter import ttk

import setting
import task
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)


# first window frame startpage
class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
     
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME",
                             command = lambda : controller.show_frame(homePage))
        homeBtn.grid(row = 0, column = 1, padx = 10, pady = 10)

        settingBtn = ttk.Button(self, text ="SETTINGS",
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10)
  
        
        # label of header
        label = ttk.Label(self, text ="Hi I'm Cactcobot, your personal reminder robot", font = LARGEFONT)
        label.grid(row = 1, column = 5, padx = 10, pady = 10)
        # label of main text
        label = ttk.Label(self, text ="Let's take a look at today's tasks!", font = MEDIUMFONT)
        label.grid(row = 2, column = 5, padx = 10, pady = 10)

        # TODO: add image

        # task button to link to task page
        taskBtn = ttk.Button(self, text ="TASKS",
                             command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.grid(row = 5, column = 5, padx = 10, pady = 10)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP",
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)
        