import tkinter as tk
from tkinter import ttk

import setting
import task

def addTasks():
    label = ttk.Label(text="open the add tasks page")
    label.pack()


# first window frame startpage
class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # label of header
        label = ttk.Label(self, text ="Hi I'm Cactcobot, your personal reminder robot", font = 15)
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # label of frame Layout 2
        label = ttk.Label(self, text ="To get started click the add task button", font = 10)
        # putting the grid in its place by using
        label.grid(row = 1, column = 4, padx = 10, pady = 10)


        addBtn = ttk.Button(self, text="Add Tasks", command=addTasks)
        addBtn.grid(row = 2, column = 4, padx = 10, pady = 10)
  
        settingBtn = ttk.Button(self, text ="Settings",
        command = lambda : controller.show_frame(setting.settingsPage))
     
        # putting the button in its place by
        # using grid
        settingBtn.grid(row = 9, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        taskBtn = ttk.Button(self, text ="Tasks",
        command = lambda : controller.show_frame(task.tasksPage))
     
        # putting the button in its place by
        # using grid
        taskBtn.grid(row = 9, column = 5, padx = 10, pady = 10)