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
        # helpful functions
        def changeLightColor():
            # TODO @TANIA
            print("change light color here")

        def changeMusic():
            # TODO @ANNA
            print("change music here")

        def changeVolumeLevel():
            # TODO @ANNA
            print("change volume level here")
        
        
        # running program starts here
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = LARGEFONT, background = "#77A752")
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        # putting the home and settings button
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 4, column = 2, padx = 10, pady = 10, sticky=tk.SE)


        # lay out 3 settings button
        lightBtn = ttk.Button(self, text = "Light Color", style = 'btn.TButton', command = changeLightColor)
        musicBtn = ttk.Button(self, text = "Music", style = 'btn.TButton', command = changeMusic)
        volumeBtn = ttk.Button(self, text = "Volume Level", style = 'btn.TButton', command = changeVolumeLevel)
        lightBtn.grid(row = 1, column = 0, padx = 10, pady = 10)
        musicBtn.grid(row = 2, column = 0, padx = 10, pady = 10)
        volumeBtn.grid(row = 3, column = 0, padx = 10, pady = 10)
  
  