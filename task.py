import tkinter as tk
from tkinter import ttk
from functools import partial

import home
import setting
import help
import RPi.GPIO as GPIO

LARGEFONT =("IBM Plex Sans Thai", 35)
MEDIUMFONT =("IBM Plex Sans Thai", 25)
SMALLFONT =("IBM Plex Sans Thai", 15)

taskList = [("Brush your teeth", "!disabled"), ("Wash your face", "!disabled"), ("Take medication", "!disabled"), ("Eat and hydrate", "!disabled")]
deleteList = []
labelList = []
doneList = []
editList = []
checkCount = 0
listCount = len(taskList)


# tasks page window
class tasksPage(tk.Frame):

    def __init__(self, parent, controller):
        # define GPIO mode
        GPIORED = 11  # red
        GPIOGREEN = 13  # green
        GPIOBLUE = 15  # blue
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIORED, GPIO.OUT)
        GPIO.setup(GPIOGREEN, GPIO.OUT)
        GPIO.setup(GPIOBLUE, GPIO.OUT)

        # variables
        input = tk.StringVar()
        editInput = tk.StringVar()

        # styles
        labelStyle = ttk.Style()
        labelStyle.theme_use('classic')
        labelStyle.configure('task.TLabel', foreground = "white", background="#B8906A",
                             height = 15, width = 20, font = MEDIUMFONT)
        
        btnStyle = ttk.Style()
        btnStyle.configure('btn.TButton', foreground = "black", background = "white", borderwidth=0,
                           height = 15, width = 8, font = SMALLFONT)
        # btnStyle.map("btn.TButton",
        #              foreground=[('pressed', 'red'), ('active', 'blue')])

        entryStyle = ttk.Style()
        entryStyle.configure('entry.TEntry', font = MEDIUMFONT)


        # helpful functions
        def checkItem(i):
            global checkCount
            checkCount += 1

            # TODO: @TANIA @ ANNA send signal to output for one item checked
            GPIO.output(GPIORED, 1)
            GPIO.output(GPIOGREEN, 1)
            GPIO.output(GPIOBLUE, 0)

            taskList[i] = (taskList[i][0], "disabled")
            doneList[i].state(["disabled"])
            editList[i].state(["disabled"])

            print("Task ", taskList[i][0], " has been completed.")

            clearScreen()
            displayList()

        
        def confirmEdit(i, entry):
            taskList[i] = (editInput.get(), taskList[i][1])
            entry.destroy()
            clearScreen()
            displayList()
        
        
        def editItem(i):
            editList[i]['text'] = "CONFIRM"
            editInput.set(labelList[i].cget('text'))
            labelList[i].destroy()
            entry = ttk.Entry(self, textvariable = editInput, style = 'entry.TEntry', width = 20, font = MEDIUMFONT)
            entry.grid(row = i + 2, column = 5, padx = 10, pady = 10)
            editList[i]['command'] = partial(confirmEdit, i, entry)


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
        
        def clearScreen():
            for label in labelList:
                label.destroy()
            for deleteBtn in deleteList:
                deleteBtn.destroy()
            for doneBtn in doneList:
                doneBtn.destroy()
            for editBtn in editList:
                editBtn.destroy()
            
        def displayList():
            # clear fields
            labelList.clear()
            deleteList.clear()
            doneList.clear()
            editList.clear()

            r = 2
            for item in taskList:

                label = ttk.Label(self, text = item[0], style = 'task.TLabel', anchor = "center")
                label.grid(row = r, column = 5, padx = 10, pady = 10)
                labelList.append(label)

                
                # add done button to the left
                doneBtn = ttk.Button(self, text = "DONE", state = item[1],
                                     style = "btn.TButton", command = partial(checkItem, r - 2))
                doneBtn.grid(row = r, column = 4, padx = 10, pady = 10)
                doneList.append(doneBtn)

                # add edit button to the right
                editBtn = ttk.Button(self, text = "EDIT", state = item[1],
                                     style = "btn.TButton", command = partial(editItem, r - 2))
                editBtn.grid(row = r, column = 6, padx = 10, pady = 10)
                editList.append(editBtn)

                # add delete button to the right
                deleteBtn = ttk.Button(self, text = "DELETE",
                                       style = "btn.TButton", command = partial(deleteItem, r - 2))
                deleteBtn.grid(row = r, column = 7, padx = 10, pady = 10)
                deleteList.append(deleteBtn)

                r += 1

            if(checkCount == listCount):
                # TODO: @TANIA @ANNA send signal to output for all items checked
                print("All tasks completed. Congrats!")
        
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
         # putting the home and settings button
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton',
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton',
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10, sticky = tk.NE)

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton',
                             command = lambda : controller.show_frame(help.helpPage))
        # helpBtn.grid(row = 9, column = 10, padx = 10, pady = 10)
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10, sticky=tk.SE) 

        # put header text
        label = ttk.Label(self, text ="Here are today's tasks", font = LARGEFONT, background = "#77A752")
        label.grid(row = 1, column = 5, padx = 10, pady = 10)

        # lay out default checklist items
        displayList()

        entry = ttk.Entry(self, textvariable = input, width=10)
        entry.grid(row =9, column = 5, padx = 10, pady = 10)

        addBtn = ttk.Button(self, text = "Add Task", style = "btn.TButton", command = addTasks)
        addBtn.grid(row = 8, column = 5, padx = 10, pady = 10)

        