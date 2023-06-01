import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess

import setting
import task
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)
SMALLFONT =("IBM Plex Sans Thai", 15)

# first window frame startpage
class homePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # styles
        labelStyle = ttk.Style()
        labelStyle.theme_use('classic')
        labelStyle.configure('header.TLabel', foreground = "black", background="white",
                             height = 30, width = 30, font = MEDIUMFONT)
        
        btnStyle = ttk.Style()
        btnStyle.configure('btn.TButton', foreground = "black", background = "white", borderwidth=0,
                           height = 30, width = 8, font = SMALLFONT)
        # btnStyle.map("btn.TButton",
        #              foreground=[('pressed', 'red'), ('active', 'blue')])

        imgStyle = ttk.Style()
        imgStyle.configure('img.TLabel', background = "#77A752")
        #77A752

     
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton',
                             command = lambda : controller.show_frame(homePage))
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton',
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton',
                             command = lambda : controller.show_frame(help.helpPage))
        # helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10, sticky=tk.SE) 
        
        # label of header
        label = ttk.Label(self, text ="Hi I'm Cactcobot,\nyour personal reminder robot",
                          style = 'header.TLabel', font = LARGEFONT)
        label.grid(row = 1, column = 5, padx = 10, pady = 10)
        # label of main text
        label = ttk.Label(self, text ="Let's take a look at today's tasks!", font = MEDIUMFONT)
        label.grid(row = 2, column = 5, padx = 10, pady = 10)

        # add Catcobot image

        image_path = "images/Cactobot_big.png"
        image = tk.PhotoImage(file=image_path)
        # image = image.resize((100, 100))
        # Create a label widget and set the image
        imageLabel = ttk.Label(self, image=image, style = 'img.TLabel', width = 100)
        imageLabel.image = image  # Keep a reference to the image
        imageLabel.grid(row = 10, column = 0, sticky = tk.SW, padx = 10, pady = 0)

        # task button to link to task page
        taskBtn = ttk.Button(self, text ="TASKS", style = 'btn.TButton',
                             command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.grid(row = 5, column = 5, padx = 10, pady = 10)
        