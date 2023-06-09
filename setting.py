import tkinter as tk
from tkinter import ttk

import home
import task
import help

HEADERFONT = ("Verdana", 45)
LARGEFONT =("Verdana", 35)
MEDIUMFONT =("Verdana", 25)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

selectedMusicPath = "audio/Short_Success_Glockenspiel.mp3" # default is Short_Success_Glockenspiel.mp3
selectedVolumeLevel = 0.2 # default is 0.2

# settings page window
class settingsPage(tk.Frame):
     
    def __init__(self, parent, controller):
        # helpful functions
        def changeLightColor():
            # TODO @TANIA
            print("change light color here")

            # Hide music + volume menu
            musicMenu.grid_remove() 
            volumeMenu.grid_remove()

        def changeMusic():
            # TODO @ANNA
            print("change music here")

            # Hide volume menu
            volumeMenu.grid_remove()

            if not musicMenu.winfo_ismapped():
                musicMenu.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
            else:
                musicMenu.grid_remove()

        def selectMusic():
            selectedIndices = musicListbox.curselection()
            print(selectedIndices)
            print(len(selectedIndices) == 0)

            if not len(selectedIndices) == 0:
                index = int(list(selectedIndices)[0])
                selectedMusic = musicOptions[index]

                global selectedMusicPath
                selectedMusicPath = musicPaths[index]

        def changeVolumeLevel():
            # TODO @ANNA
            print("change volume level here")

            # Hide music menu
            musicMenu.grid_remove()

            if not volumeMenu.winfo_ismapped():
                volumeMenu.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)
            else:
                volumeMenu.grid_remove()

        def incrementVolume():
            global selectedVolumeLevel
            selectedVolumeLevel = min(1, selectedVolumeLevel + 0.1)
            updateVolumeLabel()

        def decrementVolume():
            global selectedVolumeLevel
            selectedVolumeLevel = max(0, selectedVolumeLevel - 0.1)
            updateVolumeLabel()

        def updateVolumeLabel():
            volumeLabel.config(text=f"Volume: {selectedVolumeLevel:.1f}")

        def handleButtonClick(page):
             musicMenu.grid_remove()
             volumeMenu.grid_remove()
             controller.show_frame(page)
        
        # running program starts here
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Settings", font = HEADERFONT,
                          width = 16, background = "#77A752", anchor="center")
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        padding_right = ttk.Label(self, text ="", font = LARGEFONT,
                          width = 7, background = "#77A752", anchor="center")
        padding_right.grid(row = 0, column = 2, padx = 10, pady = 10)
  
        # putting the home and settings button
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda: handleButtonClick(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.image = setting_icon
        # settingBtn.grid(row = 0, column = 10, padx = 10, pady = 10, sticky = tk.NE)
        settingBtn.grid(row = 0, column = 3, padx = 10, pady = 10, sticky = tk.NE)

        task_icon_path = "images/task_icon.png"
        task_icon = tk.PhotoImage(file = task_icon_path)
        taskBtn = ttk.Button(self, text ="TASK", style = 'btn.TButton', image = task_icon,
                                command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.image = task_icon
        taskBtn.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tk.SW)
        
        # putting help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda: handleButtonClick(help.helpPage))
        helpBtn.image = help_icon

        helpBtn.grid(row = 5, column = 3, padx = 10, pady = 10, sticky=tk.SE)

        settingBtnStyle = ttk.Style()
        settingBtnStyle.theme_use('classic')
        settingBtnStyle.configure('settingBtn.TButton', foreground = "black", background = "#D9E9CD",
                           highlightthickness = 0, width = 15, borderwidth = 0, font = MEDIUMFONT)
        # #96BF76

        # lay out 3 settings button
        lightBtn = ttk.Button(self, text = "Light Color", style = 'settingBtn.TButton', command = changeLightColor)
        musicBtn = ttk.Button(self, text = "Music", style = 'settingBtn.TButton', command = changeMusic)
        volumeBtn = ttk.Button(self, text = "Volume Level", style = 'settingBtn.TButton', command = changeVolumeLevel)
        
        # paddingBtnStyle = ttk.Style()
        # paddingBtnStyle.configure('paddingBtn.TButton', foreground = "black", background = "#D9E9CD",
        #                    highlightthickness = 0, width = 15, borderwidth = 0, font = MEDIUMFONT)

        # paddingBtn1 = ttk.Button(self, text = "", style = 'paddingBtn.TButton')
        # paddingBtn2 = ttk.Button(self, text = "", style = 'paddingBtn.TButton')

        lightBtn.grid(row = 1, column = 0, padx = 10, pady = 10)
        musicBtn.grid(row = 2, column = 0, padx = 10, pady = 10)
        # paddingBtn2.grid(row = 4, column = 0, padx = 10, pady = 10)
        volumeBtn.grid(row = 3, column = 0, padx = 10, pady = 10)
        # paddingBtn1.grid(row = 4, column = 0, padx = 10, pady = 10, rowspan = 2)

        ################################################

        # style for music and volume frame
        frameStyle = ttk.Style()
        frameStyle.configure('audioMenu.TFrame', background='#96BF76')

        audioBtnStyle = ttk.Style()
        audioBtnStyle.configure('audioBtn.TButton', background='#D9E9CD',
                              highlightthickness = 0, borderwidth = 0, font = MEDIUMFONT)

        # intro message label display
        introStyle = ttk.Style()
        introStyle.configure('introLabel.TLabel', background = "#77A752",
                             font = MEDIUMFONT)
        introLabel = ttk.Label(self, text = "Customize your Cactobot here!\nPress one of the buttons to begin",
                               style = "introLabel.TLabel")
        introLabel.grid(row = 1, column = 1, padx = 10, pady = 10, rowspan = 2)

        # dummy padding bottom
        dummyStyle = ttk.Style()
        dummyStyle.configure('dummyLabel.TLabel', background = "#77A752", foreground = "#77A752")
        dummyLabel1 = ttk.Label(self, text = "x\nx\nx\nx\nx\nx\nx\n",
                               style = "dummyLabel.TLabel")
        dummyLabel1.grid(row = 1, column = 2, padx = 10, pady = 10, sticky=tk.E)
        dummyLabel2 = ttk.Label(self, text = "x\nx\nx\nx\nx\nx\nx\nx",
                               style = "dummyLabel.TLabel")
        dummyLabel2.grid(row = 2, column = 2, padx = 10, pady = 10, sticky=tk.E)
        dummyLabel3 = ttk.Label(self, text = "x\nx\nx\nx\nx\nx\nx\nx",
                               style = "dummyLabel.TLabel")
        dummyLabel3.grid(row = 3, column = 2, padx = 10, pady = 10, sticky=tk.E)
        # dummyLabel4 = ttk.Label(self, text = "x",
        #                        style = "dummyLabel.TLabel")
        # dummyLabel4.grid(row = 4, column = 2, padx = 10, pady = 10, sticky=tk.E)

        # music button clicked UI
        musicMenu = ttk.Frame(self, style = 'audioMenu.TFrame')

        musicOptions = ["Deep Bell", "Short Success", "Success Trumpets"]
        musicPaths = ["audio/Deep_Bell.mp3", "audio/Short_Success_Glockenspiel.mp3", "audio/Success_Trumpets.mp3"]

        musicListbox = tk.Listbox(musicMenu, width=25, selectmode=tk.SINGLE,
                                  background='#D9E9CD', font = MEDIUMFONT)
        scrollbar = tk.Scrollbar(musicMenu, orient=tk.VERTICAL, command=musicListbox.yview)
        musicListbox.config(yscrollcommand=scrollbar.set)
        
        for option in musicOptions:
            musicListbox.insert(tk.END, option)
        
        musicListbox.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        selectButton = ttk.Button(musicMenu, text="Select", command=selectMusic,
                                  style = "audioBtn.TButton")
        selectButton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        musicMenu.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W, rowspan = 3)
        musicMenu.grid_remove()

        ################################################
        # volume menu UI
        volumeMenu = ttk.Frame(self, style = 'audioMenu.TFrame')

        volumeLabel = ttk.Label(volumeMenu, text=f"Volume: {selectedVolumeLevel:.1f}",
                                font=LARGEFONT, background = "#96BF76")
        volumeLabel.grid(row=0, column=0, padx=10, pady=10)

        incrementButton = ttk.Button(volumeMenu, text="Increase",
                                     style = "audioBtn.TButton", command=incrementVolume)
        incrementButton.grid(row=1, column=0, padx=10, pady=10)

        decrementButton = ttk.Button(volumeMenu, text="Decrease",
                                     style = "audioBtn.TButton", command=decrementVolume)
        decrementButton.grid(row=2, column=0, padx=10, pady=10)

        volumeMenu.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W, rowspan = 3)
        volumeMenu.grid_remove()


def getSelectedMusicPath():
    return selectedMusicPath

def getSelectedVolumeLevel():
    return selectedVolumeLevel

  
  

