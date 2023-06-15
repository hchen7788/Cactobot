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
        frame.configure(bg="#77A752")


# Driver Code
app = tkinterApp()
app.geometry("1024x600")
app.title("Cactobot")

app.mainloop()