import tkinter as tk
from tkinter import ttk
from functools import partial

import pygame as py
from pygame import mixer

# Uncomment the GPIO code and import statement when running on raspberry pi
# import RPi.GPIO as GPIO 

import home
import setting
import help
import time

HEADERFONT = ("Verdana", 40)
LARGEFONT =("Verdana", 30)
MEDIUMFONT =("Verdana", 25)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

taskList = [("Brush your teeth", "!disabled"), ("Wash your face", "!disabled"), ("Take medication", "!disabled"), ("Eat and hydrate", "!disabled")]
deleteList = []
labelList = []
doneList = []
editList = []
checkCount = 0
listCount = len(taskList)
color = "white"


# tasks page window
class tasksPage(tk.Frame):

    def __init__(self, parent, controller):
        # Uncomment GPIO code when running on pi

        # Set up GPIO pins for RGB LED ouput
        # Define GPIO mode
        # GPIORED = 17  # red
        # GPIOGREEN = 27  # green
        # GPIOBLUE = 22  # blue
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(GPIORED, GPIO.OUT)
        # GPIO.setup(GPIOGREEN, GPIO.OUT)
        # GPIO.setup(GPIOBLUE, GPIO.OUT)

        # variables
        input = tk.StringVar()
        editInput = tk.StringVar()

        # styles
        labelStyle = ttk.Style()
        labelStyle.theme_use('classic')
        labelStyle.configure('task.TLabel', foreground = "white", background="#B8906A",
                             height = 10, width = 20, font = LARGEFONT)
        
        btnStyle = ttk.Style()
        btnStyle.configure('btn.TButton', foreground = "black", background = "#77A752", borderwidth=0)

        entryStyle = ttk.Style()
        entryStyle.configure('entry.TEntry', font = LARGEFONT)

        imgStyle = ttk.Style()
        imgStyle.configure('img.TLabel', background = "#77A752")

        # Instantiate mixer to play audio files
        mixer.init()

        # Function called to play audio file when task completed
        def playSound():
            # Load audio file
            mixer.music.load(setting.getSelectedMusicPath())

            # Set preferred volume
            mixer.music.set_volume(setting.getSelectedVolumeLevel())

            # Play the music
            mixer.music.play()


        # helpful functions
        # Function that handles when a task is marked completed
        def checkItem(i):
            global checkCount
            checkCount += 1

            # Send signal to output for one item checked

            # Task complete sound
            playSound()

            # Output selected light color
            # Uncomment GPIO when running on pi
            if (setting.selectedColor == "red"):
                #GPIO.output(GPIORED, GPIO.HIGH)
                #GPIO.output(GPIOGREEN, GPIO.LOW)
                #GPIO.output(GPIOBLUE, GPIO.LOW)
                print("light is now red!")
            elif (setting.selectedColor == "green"):
                #GPIO.output(GPIORED, GPIO.LOW)
                #GPIO.output(GPIOGREEN, GPIO.HIGH)
                #GPIO.output(GPIOBLUE, GPIO.LOW)
                print("light is now green!")
            elif (setting.selectedColor == "blue"):
                #GPIO.output(GPIORED, GPIO.LOW)
                #GPIO.output(GPIOGREEN, GPIO.LOW)
                #GPIO.output(GPIOBLUE, GPIO.HIGH)
                print("light is now blue!")
            elif (setting.selectedColor == "teal"):
                #GPIO.output(GPIORED, GPIO.LOW)
                #GPIO.output(GPIOGREEN, GPIO.HIGH)
                #GPIO.output(GPIOBLUE, GPIO.HIGH)
                print("light is now teal!")
            else:
                #GPIO.output(GPIORED, GPIO.HIGH)
                #GPIO.output(GPIOGREEN, GPIO.HIGH)
                #GPIO.output(GPIOBLUE, GPIO.HIGH)
                print("light is not set up yet.")

            taskList[i] = (taskList[i][0], "disabled")
            doneList[i].state(["disabled"])
            editList[i].state(["disabled"])

            print("task ", taskList[i][0], " completed")

            clearScreen()
            displayList()

            # Dim lights after 5 seconds
            self.after(5000, dimLights)

        # Function that dims the lights after certain amount of time
        def dimLights():
            # Uncomment GPIO when run on pi
            #GPIO.output(GPIORED, GPIO.LOW)
            #GPIO.output(GPIOGREEN, GPIO.LOW)
            #GPIO.output(GPIOBLUE, GPIO.LOW)
            print("Lights are now dimmed")

        # Function that is used to confirm edit made to task by user
        def confirmEdit(i, entry):
            taskList[i] = (editInput.get(), taskList[i][1])
            entry.destroy()
            clearScreen()
            displayList()
        
        # Function that handles when user edits a task
        def editItem(i):
            editList[i]['text'] = "CONFIRM"
            editInput.set(labelList[i].cget('text'))
            labelList[i].destroy()
            entry = ttk.Entry(self, textvariable = editInput, style = 'entry.TEntry', width = 20, font = MEDIUMFONT)
            entry.grid(row = i + 2, column = 1, padx = 10, pady = 10)
            # TODO: screenkeyboard when clicked on entry
            editList[i]['command'] = partial(confirmEdit, i, entry)

        # Function that handles when user deletes a task
        def deleteItem(i):
            global listCount
            listCount -= 1
            global checkCount
            # check if this task is checked
            state = doneList[i]['state']
            if (state == 'disabled'):
                checkCount -= 1

            print("task ", taskList[i][0], " is going to be deleted")

            del taskList[i]
            labelList[i].destroy()
            deleteList[i].destroy()
            doneList[i].destroy()
            editList[i].destroy()
            del labelList[i]
            del deleteList[i]
            del doneList[i]
            del editList[i]
            clearScreen()
            displayList()
        
        # Clear screen -- helper method called in other functions
        def clearScreen():
            for label in labelList:
                label.destroy()
            for deleteBtn in deleteList:
                deleteBtn.destroy()
            for doneBtn in doneList:
                doneBtn.destroy()
            for editBtn in editList:
                editBtn.destroy()
            
        # Display current task list on screen
        def displayList():
            # clear fields
            labelList.clear()
            deleteList.clear()
            doneList.clear()
            editList.clear()

            r = 2
            # For each task in list of tasks
            for item in taskList:

                label = ttk.Label(self, text = item[0], style = 'task.TLabel', anchor = "center")
                label.grid(row = r, column = 1, padx = 10, pady = 10)
                labelList.append(label)
                
                # add done button to the left of task
                done_icon_path = "images/check_icon.png"
                done_icon = tk.PhotoImage(file = done_icon_path)
                doneBtn = ttk.Button(self, text = "DONE", state = item[1], image = done_icon, 
                                     style = "btn.TButton", command = partial(checkItem, r - 2))
                doneBtn.image = done_icon
                doneBtn.grid(row = r, column = 0, padx = 10, pady = 10)
                doneList.append(doneBtn)

                # add edit button with icon to the right of task
                edit_icon_path = "images/edit_icon.png"
                edit_icon = tk.PhotoImage(file = edit_icon_path)
                editBtn = ttk.Button(self, text = "EDIT", state = item[1], style = "btn.TButton",
                                     image = edit_icon, command = partial(editItem, r - 2))
                editBtn.image = edit_icon
                editBtn.grid(row = r, column = 2, padx = 10, pady = 10)
                editList.append(editBtn)

                # add delete button to the right of task
                delete_icon_path = "images/trash_icon.png"
                delete_icon = tk.PhotoImage(file = delete_icon_path)
                deleteBtn = ttk.Button(self, text = "-", image = delete_icon,
                                       style = "btn.TButton", command = partial(deleteItem, r - 2))
                deleteBtn.image = delete_icon
                deleteBtn.grid(row = r, column = 3)
                deleteList.append(deleteBtn)

                r += 1
            
            # display everything lower than the list
            entry.grid(row = listCount + 2, column = 1, padx = 10, pady = 10)
            addBtn.grid(row = listCount + 2, column = 2)
            imageLabel.grid(row = listCount + 2, column = 0, sticky = tk.SW, padx = 10, pady = 0)
            helpBtn.grid(row = listCount + 2, column = 4, sticky=tk.SE)

            # When all tasks have been completed
            if(checkCount == listCount):
                # All tasks completed sound
                playSound()

                print("All tasks completed. Congrats!")
        
        # Function that handles the user adding tasks to the list
        def addTasks():
            entryText = input.get()
            if(entryText == ""):
                return
            taskList.append((entryText, 0))
            input.set("")
            global listCount
            listCount += 1
            clearScreen()
            displayList()


        # running program starts here
        tk.Frame.__init__(self, parent)

        # things to reuse
        image_path = "images/Cactobot_small.png"
        image = tk.PhotoImage(file=image_path)

        # Create a label widget and set the image
        imageLabel = ttk.Label(self, image=image, style = 'img.TLabel', width = 100)
        imageLabel.image = image  # Keep a reference to the image

        entry = ttk.Entry(self, textvariable = input, width=10)

        # add button with image
        add_icon_path = "images/add_icon.png"
        add_icon = tk.PhotoImage(file = add_icon_path)
        addBtn = ttk.Button(self, style = "btn.TButton",
                        image = add_icon, command = addTasks)
        addBtn.image = add_icon

        # Placing the home button to link to home page
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        # Placing the setting button to link to setting page
        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 4, sticky = tk.NE)

        # Placing the help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.image = help_icon

        # put header text
        label = ttk.Label(self, text ="TODAY'S TASKS", font = HEADERFONT,
                          width = 20, anchor="center", background = "#77A752")
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        # lay out default checklist items
        displayList()
        