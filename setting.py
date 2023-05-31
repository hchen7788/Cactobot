import tkinter as tk
from tkinter import ttk

import home
import task

# second window frame page1
class settingsPage(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = 15)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(home.homePage))
     
        # putting the button in its place
        # by using grid
        homeBtn.grid(row = 9, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        taskBtn = ttk.Button(self, text ="Tasks",
                            command = lambda : controller.show_frame(task.tasksPage))
     
        # putting the button in its place by
        # using grid
        taskBtn.grid(row = 9, column = 5, padx = 10, pady = 10)
  
  