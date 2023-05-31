import tkinter as tk
from tkinter import ttk

import home
import setting
import help

LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

taskList = ["Brush your teeth", "Wash your face", "Take medication", "Eat and hydrate"]
deleteList = ["Brush your teeth", "Wash your face", "Take medication", "Eat and hydrate"]
checkCount = 0
listCount = len(taskList)


# tasks page window
class tasksPage(tk.Frame):

    def __init__(self, parent, controller):
        # variables
        input = tk.StringVar()

        # helpful functions
        def find_widget(x,y):
            for child in self.children.values():
                x1 = child.winfo_rootx()-self.winfo_rootx()
                y1 = child.winfo_rooty()-self.winfo_rooty()
                x2 = x1+ child.winfo_width()
                y2 = y1+ child.winfo_height()
                if x1 <= x <= x2 and y1 <= y <= y2:
                    return child
            return None
        
        def checkItem():
            global checkCount
            checkCount += 1
            print("item checked")
            if(checkCount == listCount):
                # TODO: @TANIA @ANNA send signal to output
                print("Congrats!")
        
        def deleteItem(text):
            # print("item deleted")
            # print(self.grid_info()['row'])
            # print(self.grid_info()['column'])
            print(text, " is going to be deleted")
            
        
        def displayList():
            c = 2
            for item in taskList:
                label = ttk.Label(self, text = item, font = MEDIUMFONT)
                label.grid(row = c, column = 5, padx = 10, pady = 10)

                # add done button to the left
                doneBtn = ttk.Button(self, text = "DONE", command = checkItem)
                doneBtn.grid(row = c, column = 4, padx = 10, pady = 10)

                # add delete button to the right
                deleteBtn = ttk.Button(self, text = "DELETE",
                                       command = lambda: deleteItem(label.cget("text")))
                deleteBtn.grid(row = c, column = 6, padx = 10, pady = 10)
                c += 1
        
        def addTasks():
            entryText = input.get()
            if(entryText == ""):
                return
            taskList.append(entryText)
            input.set("")
            global listCount
            listCount += 1
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