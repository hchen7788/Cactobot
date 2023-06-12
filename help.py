import tkinter as tk
from tkinter import ttk

import setting
import task
import home

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 20)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# first window frame startpage
class helpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # putting the home and settings button
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, sticky = tk.NW)

        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 2, sticky = tk.NE)

        task_icon_path = "images/task_icon.png"
        task_icon = tk.PhotoImage(file = task_icon_path)
        taskBtn = ttk.Button(self, text ="TASK", style = 'btn.TButton', image = task_icon,
                                command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.image = task_icon
        taskBtn.grid(row = 2, column = 0, sticky = tk.SW)

        # putting help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda : controller.show_frame(helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 2, column = 2, sticky=tk.SE)

        # label of header
        label = ttk.Label(self, text ="HOW TO USE YOUR CACTOBOT",
                          font = LARGEFONT, background = "#77A752",
                          width = 33, anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 1)

        # instructions content
        instructions = ttk.Label(self, text = "1. Press HOME button in the top left \n to go to home page. \n"
                                              "2. Press SETTINGS button in the top right \n to open settings page. \n"
                                              "     a. Buttons in the settings page \n change light color, music, and volume. \n"
                                              "3. Press TASK button in the bottom left \n to return to tasks page. \n"
                                              "     a. Add tasks via text bar at bottom of page. \n"
                                              "     b. Edit task via pencil icon to right of task. \n"
                                              "     c. Delete task via trash icon to right of task. \n"
                                              "4. Completing tasks causes Cactobot \n to light up and play music. \n"
                                              "     a. Customize light color and music in Settings. \n"
                                              "5. Press HELP button in the bottom right corner to return here.",
                                              background='#D9E9CD', font = MEDIUMFONT, anchor = "center")
        instructions.grid(row = 1, column = 0, columnspan = 3, rowspan = 2)