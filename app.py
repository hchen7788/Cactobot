import tkinter as tk
from tkinter import ttk
from home import homePage
from setting import settingsPage
from task import tasksPage
from help import helpPage
 
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)

  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (homePage, settingsPage, tasksPage, helpPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(homePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Driver Code
app = tkinterApp()
app.title("Cactobot")
# app.geometry("1200x400")
# # app['background'] = 'green'
# # app.configure(bg="green")

# app.configure(background='green')
# # style configuration
# style = ttk.Style(app)
# style.configure(bg="green")
# style.configure('TLabel', background='black', foreground='black')
# style.configure('TFrame', background='black')

new_task = tk.StringVar()

app.mainloop()


# ## functions to use

# # test function
# def sayhi():
#     label = tk.Label(root, text="hi")
#     label.pack()

# # test function
# def donothing():
#    filewin = tk.Toplevel(root)
#    button = tk.Button(filewin, text="Do nothing button")
#    button.pack()

# def openSettings():
#     label = tk.Label(root, text="open the settings page")
#     label.pack()

# def openTasks():
#     label = tk.Label(root, text="open the tasks page")
#     label.pack()

# def addTasks():
#     label = tk.Label(root, text="open the add tasks page")
#     label.pack()

# def checkItem():
#     # if want to get the text of the item
#     # task=checkbutton.cget("text")
#     label = tk.Label(root, text="one task completed!")
#     label.pack()
#     # make message disapper after 1 second
#     root.after(1000, label.destroy)

#     # TODO: send signal to feedback (light/audio)






# ## actual program starts below

# # variable to store status of item checked
# checked = False

# # variables to store signal to lights and audio controller
# lightOn = False
# audioOn = False

# # list to store daily tasks
# tasks = ["brush your teeth", "make your bed", "take a shower"]
# checkButtons = []

# # Create the main window
# root = tk.Tk()
# root.title("Cactobot")

# # Create header
# label = tk.Label(root, text="Welcome to Cactobot")
# label.pack()

# # Create menu buttons
# setting_btn = tk.Button(root, text="Settings", command=openSettings)
# task_btn = tk.Button(root, text="Tasks", command=openTasks)
# add_btn = tk.Button(root, text="Add Tasks", command=addTasks)

# setting_btn.pack(padx=5, pady=5)
# task_btn.pack(padx=5, pady=5)
# add_btn.pack(padx=5, pady=5)
# # canvas = tk.Canvas(root, bg='white', width=50, height=50)

# # create task list
# for item in tasks:
#     checkbutton = tk.Checkbutton(root, text=item, command=checkItem)
#     checkbutton.pack(padx=5, pady=5)


# # entry = tk.Entry(root, text="Entry", width=10)
# # frame = tk.Frame(root)
# # labelframe = tk.LabelFrame(root, text="LabelFrame", padx=5, pady=5)
# # listbox = tk.Listbox(root, height=3)

# # # create menu
# # menubar = tk.Menu(root)
# # root.config(menu=menubar)



# # entry.pack(padx=5, pady=5)
# # frame.pack(padx=5, pady=10)
# # labelframe.pack(padx=5, pady=5)
# # listbox.pack(padx=5, pady=5)

# # Run forever!
# root.mainloop()

