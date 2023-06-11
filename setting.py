import tkinter as tk
from tkinter import ttk

import home
import task
import help
import RPi.GPIO as GPIO

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)


# settings page window
class settingsPage(tk.Frame):
     
    def __init__(self, parent, controller):
         # of times taps have occurred
        self.iterations = 0

        # define GPIO mode
        GPIORED = 11  # red
        GPIOGREEN = 13  # green
        GPIOBLUE = 15  # blue
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIORED, GPIO.OUT)
        GPIO.setup(GPIOGREEN, GPIO.OUT)
        GPIO.setup(GPIOBLUE, GPIO.OUT)

        # helpful functions
        def changeLightColor(self):
            if (self.iterations == 0):
                GPIO.output(GPIORED, 1)
                GPIO.output(GPIOGREEN, 0)
                GPIO.output(GPIOBLUE, 0)
                self.iterations += 1
                print(self.iterations)
                print("red")
            elif (self.iterations == 1):
                GPIO.output(GPIORED, 0)
                GPIO.output(GPIOGREEN, 1)
                GPIO.output(GPIOBLUE, 0)
                print("green")
                self.iterations += 1
            else:
                GPIO.output(GPIORED, 0)
                GPIO.output(GPIOGREEN, 0)
                GPIO.output(GPIOBLUE, 1)
                print("blue")
                self.iterations = 0

        def changeMusic():
            # TODO @ANNA
            print("change music here")

        def changeVolumeLevel():
            # TODO @ANNA
            print("change volume level here")
        
        
        # running program starts here
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = LARGEFONT)
        label.grid(row = 1, column = 5, padx = 10, pady = 10)
  
        # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton',
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton',
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton',
                             command = lambda : controller.show_frame(help.helpPage))
        # helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10, sticky=tk.SE) 


        # lay out 3 settings button
        lightBtn = ttk.Button(self, text = "Light Color", style = 'btn.TButton', command = lambda:changeLightColor(self))
        musicBtn = ttk.Button(self, text = "Music", style = 'btn.TButton', command = changeMusic)
        volumeBtn = ttk.Button(self, text = "Volume Level", style = 'btn.TButton', command = changeVolumeLevel)
        lightBtn.grid(row = 3, column = 1, padx = 10, pady = 10)
        musicBtn.grid(row = 5, column = 1, padx = 10, pady = 10)
        volumeBtn.grid(row = 7, column = 1, padx = 10, pady = 10)
  
  