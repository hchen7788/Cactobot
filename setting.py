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

            # Hide music menu
            musicMenu.grid_remove() 

        def changeMusic():
            # TODO @ANNA
            print("change music here")

            if not musicMenu.winfo_ismapped():
                musicMenu.grid(row=5, column=2, padx=10, pady=10, sticky=tk.W)
            else:
                musicMenu.grid_remove()

        def changeVolumeLevel():
            # TODO @ANNA
            print("change volume level here")

            # Hide music menu
            musicMenu.grid_remove()

        def handleButtonClick(page):
             musicMenu.grid_remove()
             controller.show_frame(page)
        
        # running program starts here
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = LARGEFONT, background = "#77A752")
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        # putting the home and settings button
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda: handleButtonClick(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda: handleButtonClick(help.helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10, sticky=tk.SE)


        # lay out 3 settings button
        lightBtn = ttk.Button(self, text = "Light Color", style = 'btn.TButton', command = changeLightColor)
        musicBtn = ttk.Button(self, text = "Music", style = 'btn.TButton', command = changeMusic)
        volumeBtn = ttk.Button(self, text = "Volume Level", style = 'btn.TButton', command = changeVolumeLevel)
        lightBtn.grid(row = 3, column = 1, padx = 10, pady = 10)
        musicBtn.grid(row = 5, column = 1, padx = 10, pady = 10)
        volumeBtn.grid(row = 7, column = 1, padx = 10, pady = 10)

        ################################################
        # change music button clicked UI
        musicMenu = ttk.Frame(self)
        musicOptions = ["Deep Bell", "Short Success", "Success Trumpets"]
        musicPaths = 
        musicListbox = tk.Listbox(musicMenu, width=40)
        scrollbar = tk.Scrollbar(musicMenu, orient=tk.VERTICAL, command=musicListbox.yview)
        musicListbox.config(yscrollcommand=scrollbar.set)
        for option in musicOptions:
            musicListbox.insert(tk.END, option)
        musicListbox.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        musicMenu.grid(row=5, column=2, padx=10, pady=10, sticky=tk.W)
        musicMenu.grid_remove()