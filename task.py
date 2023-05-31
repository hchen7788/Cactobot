import tkinter as tk
from tkinter import ttk

import home
import setting

# third window frame page2
class tasksPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Tasks", font = 15)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Settings",
                            command = lambda : controller.show_frame(setting.settingsPage))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(home.homePage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)