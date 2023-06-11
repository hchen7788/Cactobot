import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess

import setting
import task
import help

HEADERFONT = ("Verdana", 45)
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

# first window frame startpage
class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # styles
        labelStyle = ttk.Style()
        labelStyle.theme_use('classic')
        labelStyle.configure('header.TLabel', foreground = "black", background="#77A752",
                             height = 30, width = 30, font = LARGEFONT, anchor = "center")
        
        btnStyle = ttk.Style()
        btnStyle.configure('btn.TButton', foreground = "black", background = "white",
                           highlightthickness=0, height = 30, font = SMALLFONT)
        # btnStyle.map("btn.TButton",
        #              foreground=[('pressed', 'red'), ('active', 'blue')])

        imgStyle = ttk.Style()
        imgStyle.configure('img.TLabel', background = "#77A752")
        #77A752

     
        # putting the home and settings button
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda : controller.show_frame(homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.image = help_icon
        helpBtn.grid(row = 2, column = 2, padx = 10, pady = 10, sticky=tk.SE)
        
        # # label of header
        # label = ttk.Label(self, text ="Hi I'm Cactcobot,\nyour personal reminder robot",
        #                   style = 'header.TLabel', font = LARGEFONT)
        # label.grid(row = 1, column = 5, padx = 10, pady = 10)
        # # label of main text
        # label = ttk.Label(self, text ="Let's take a look at\ntoday's tasks!",
        #                   style = 'dialog.TLabel')
        # label.grid(row = 2, column = 5, padx = 10, pady = 10)

        # add dialog bubble
        dialog_path = "images/dialog_bubble.png"
        dialog_img = tk.PhotoImage(file=dialog_path)
        # image = image.resize((100, 100))
        # Create a label widget and set the image
        dialogLabel = ttk.Label(self, image=dialog_img, style = 'img.TLabel', width = 100)
        dialogLabel.image = dialog_img  # Keep a reference to the image
        dialogLabel.grid(row = 1, column = 1, padx = 10, pady = 0)

        # add Catcobot image
        image_path = "images/Cactobot.png"
        image = tk.PhotoImage(file=image_path)
        # image = image.resize((100, 100))
        # Create a label widget and set the image
        imageLabel = ttk.Label(self, image=image, style = 'img.TLabel', width = 100)
        imageLabel.image = image  # Keep a reference to the image
        imageLabel.grid(row = 1, column = 0, sticky = tk.SW, padx = 10, pady = 0)

        # dummy_label = ttk.Label(self, text = "make it longgggg", background="black", width = 100)
        # dummy_label.grid(row =1, column = 2)
        # dummy_label2 = ttk.Label(self, text = "make it longgggg", background="black", width = 100)
        # dummy_label2.grid(row =2, column = 2)
        # dummy_label3 = ttk.Label(self, text = "make it longgggg", font=LARGEFONT,
        #                          background="black", foreground="white", width = 10)
        # dummy_label3.grid(row =3, column = 2)

        # dummy_c = ttk.Label(self, text = "make it short", background="white")
        # dummy_c.grid(row =1, column = 1)
        # dummy_c2 = ttk.Label(self, text = "make it short", background="white")
        # dummy_c2.grid(row =1, column = 2)
        # dummy_c3 = ttk.Label(self, text = "make it short", background="white")
        # dummy_c3.grid(row =1, column = 3)


        # task button to link to task page
        task_icon_path = "images/task_icon_big.png"
        task_icon = tk.PhotoImage(file = task_icon_path)
        taskBtn = ttk.Button(self, image = task_icon, style = 'btn.TButton',
                             command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.image = task_icon
        taskBtn.grid(row = 2, column = 1, padx = 10, pady = 10)