import tkinter as tk
from tkinter import ttk

import setting
import task
import home

HEADERFONT = ("Verdana", 45)
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)
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
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tk.NE)

        task_icon_path = "images/task_icon.png"
        task_icon = tk.PhotoImage(file = task_icon_path)
        taskBtn = ttk.Button(self, text ="TASK", style = 'btn.TButton', image = task_icon,
                                command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.image = task_icon
        taskBtn.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tk.SW)

        # putting help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda : controller.show_frame(helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 2, column = 2, padx = 10, pady = 10, sticky=tk.SE)

        # label of header
        label = ttk.Label(self, text ="Here's how to use your Catcobot",
                          font = LARGEFONT, background = "#77A752",
                          width = 37, anchor="center")
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        # instructions content
        instructions = ttk.Label(self, text = "1. Press the HOME button in the top left corner \n to go back to the home page. \n"
                                              "2. Press the SETTINGS button in the top right corner \n to open the settings page. \n"
                                              "     a. Use the buttons in the settings page \n to change the light color, music, and volume level. \n"
                                              "3. Press the TASK button in the bottom left corner \n to return to the tasks page. \n"
                                              "     a. Add tasks via the text bar at the bottom of the page. \n"
                                              "     b. Edit tasks via the pencil icon to the right of each task. \n"
                                              "     c. Delete tasks via the trash icon to the right of each task. \n"
                                              "4. When you complete a task, the top of your Cactobot \n will light up and a celebratory sound will play. \n"
                                              "     a. Customize light color and music in Settings. \n"
                                              "5. Press the HELP button in the bottom right corner to return here.",
                                              background='#D9E9CD', font = MEDIUMFONT, anchor = "center")
        instructions.grid(row = 1, column = 1, padx = 5, pady = 5)