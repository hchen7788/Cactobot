import tkinter as tk
from tkinter import ttk
from functools import partial

import home
import setting
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

taskList = [("Brush your teeth", "!disabled"), ("Wash your face", "!disabled"), ("Take medication", "!disabled"), ("Eat and hydrate", "!disabled")]
deleteList = []
labelList = []
doneList = []
checkCount = 0
listCount = len(taskList)


# tasks page window
class tasksPage(tk.Frame):

    def __init__(self, parent, controller):
        # variables
        input = tk.StringVar()

        # helpful functions
        def checkItem(r):
            global checkCount
            checkCount += 1
            # TODO: @TANIA @ ANNA send signal to output for one item checked
            # taskList[r][1] = 1
            taskList[r] = (taskList[r][0], "disabled")
            doneList[r].state(["disabled"])

            print("task ", taskList[r][0], " completed")

            clearScreen()
            displayList()
        

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
            del labelList[i]
            del deleteList[i]
            del doneList[i]
            clearScreen()
            displayList()
        
        def clearScreen():
            for label in labelList:
                label.destroy()
            for deleteBtn in deleteList:
                deleteBtn.destroy()
            for doneBtn in doneList:
                doneBtn.destroy()
            
        def displayList():
            # clear fields
            labelList.clear()
            deleteList.clear()
            doneList.clear()

            r = 2
            for item in taskList:
                # if(item == ""):
                #     continue
                
                label = ttk.Label(self, text = item[0], font = MEDIUMFONT)
                label.grid(row = r, column = 5, padx = 10, pady = 10)
                labelList.append(label)

                # add done button to the left
                doneBtn = ttk.Button(self, text = "DONE", state = item[1], command = partial(checkItem, r - 2))
                doneBtn.grid(row = r, column = 4, padx = 10, pady = 10)
                doneList.append(doneBtn)

                # add delete button to the right
                deleteBtn = ttk.Button(self, text = "DELETE", command = partial(deleteItem, r - 2))
                deleteBtn.grid(row = r, column = 6, padx = 10, pady = 10)
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
        homeBtn = ttk.Button(self, text="HOME",
                             command = lambda : controller.show_frame(home.homePage))
        homeBtn.grid(row = 0, column = 1, padx = 10, pady = 10)

        settingBtn = ttk.Button(self, text ="SETTINGS",
                                command = lambda : controller.show_frame(setting.settingsPage))
        settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10)

        # put header text
        label = ttk.Label(self, text ="Here are today's tasks", font = LARGEFONT)
        label.grid(row = 1, column = 5, padx = 10, pady = 10)

        # lay out default checklist items
        displayList()

        # putting help button to link to help page
        helpBtn = ttk.Button(self, text = "HELP",
                             command = lambda : controller.show_frame(help.helpPage))
        helpBtn.grid(row = 10, column = 10, padx = 10, pady = 10)

        entry = ttk.Entry(self, textvariable = input, width=10)
        entry.grid(row =9, column = 5, padx = 10, pady = 10)

        addBtn = ttk.Button(self, text = "Add Task", command = addTasks)
        addBtn.grid(row = 8, column = 5, padx = 10, pady = 10)

        # s = ttk.Style()                                                                 
        # s.configure('Red.TCheckbutton', indicatorforeground="green", font = ('calibri', 10, 'bold', 'underline'),
        #         foreground = 'red')         
        # cb = ttk.Checkbutton(master=self, style='Red.TCheckbutton', text='Test')         
        # cb.grid(row =11, column = 5, padx = 10, pady = 10) 