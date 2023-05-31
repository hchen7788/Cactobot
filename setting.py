import tkinter as tk
from tkinter import ttk

import home
import task
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

# def changeLightColor():
#     # TODO
#     print("change light color here")

# def changeMusic():
#     # TODO
#     print("change music here")

# def changeVolumeLevel():
#     # TODO
#     print("change volume level here")

# settings page window
class settingsPage(tk.Frame):
     
    def __init__(self, parent, controller):
        # helpful functions
        def changeLightColor():
            # TODO
            print("change light color here")

        def changeMusic():
            # TODO
            print("change music here")

        def changeVolumeLevel():
            # TODO
            print("change volume level here")
        
        
        # running program starts here
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = LARGEFONT)
        label.grid(row = 1, column = 5, padx = 10, pady = 10)
  
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME",
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 1, padx = 10, pady = 10)

        settingBtn = ttk.Button(self, text ="SETTINGS",
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP",
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)


        # lay out 3 settings button
        lightBtn = ttk.Button(self, text = "Light Color", command = changeLightColor)
        musicBtn = ttk.Button(self, text = "Music", command = changeMusic)
        volumeBtn = ttk.Button(self, text = "Volume Level", command = changeVolumeLevel)
        lightBtn.grid(row = 3, column = 1, padx = 10, pady = 10)
        musicBtn.grid(row = 5, column = 1, padx = 10, pady = 10)
        volumeBtn.grid(row = 7, column = 1, padx = 10, pady = 10)
  
  