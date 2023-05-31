import tkinter as tk
from tkinter import ttk

import home
import setting
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

TASKLIST = ["Brush your teeth", "Wash your face", "Take medication", "Eat and hydrate"]
CHECKCOUNT = 0
LISTCOUNT = len(TASKLIST)

def addTasks():
    # global LISTCOUNT
    # LISTCOUNT += 1
    entryText = tasksPage.entry.get()
    print("hi")
    print(entryText)

# tasks page window
class tasksPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME",
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 1, padx = 10, pady = 10)

        settingBtn = ttk.Button(self, text ="SETTINGS",
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10)

        # put header text
        label = ttk.Label(self, text ="Here are today's tasks", font = LARGEFONT)
        label.grid(row = 1, column = 5, padx = 10, pady = 10)

        # lay out default checklist items
        c = 2
        for item in TASKLIST:
            label = ttk.Label(self, text = item, font = MEDIUMFONT)
            label.grid(row = c, column = 5, padx = 10, pady = 10)
            c += 1

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP",
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10)

        entry = ttk.Entry(self, text="add your new task here", width=10)
        entry.grid(row =9, column = 5, padx = 10, pady = 10)

        addBtn = ttk.Button(self, text = "Add Task", command = addTasks)
        addBtn.grid(row = 8, column = 5, padx = 10, pady = 10)