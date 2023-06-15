import tkinter as tk
from tkinter import ttk

import home
import task
import help

import pygame as py
from pygame import mixer

HEADERFONT = ("Verdana", 42)
LARGEFONT =("Verdana", 33)
MEDIUMFONT =("Verdana", 23)
SMALLFONT =("Verdana", 15)
BTNFONT =("Verdana", 35)

selectedMusicPath = "audio/Complete.mp3" # default audio is Complete.mp3
selectedVolumeLevel = 0.2 # default volume level is 0.2
selectedColor = "white" # default light color 

# Settings Page -- where the user can customize the different features of the Cactobot
class settingsPage(tk.Frame):
     
    def __init__(self, parent, controller):
        # Function that places the color buttons that the user selects to change light color
        def colorButtonsAppear():
            introLabel['text'] = "Change the color of your Cactobot!"
            musicMenu.grid_remove() 
            volumeMenu.grid_remove()
            print("Color buttons appearing")
            colors_menu.grid(row=2, column=1, sticky=tk.W, rowspan = 2)

        # Function that updates the selected light color based on user selection
        def changeLightColor(color):
            print("change light color here")

            global selectedColor
            if (color == "red"):
                selectedColor = "red"
                print("red")
            elif (color == "green"):
                selectedColor = "green"
                print("green")
            else:
                selectedColor = "blue"
                print("blue")

            # Hide music + volume menu
            musicMenu.grid_remove() 
            volumeMenu.grid_remove()

        # Function that makes visible the music menu where user can select task complete audio
        def changeMusic():
            print("change music here")
            introLabel['text'] = "Pick a sound to celebrate\ncompleting a task!"

            # Hide volume + colors menu
            volumeMenu.grid_remove()
            colors_menu.grid_remove()

            if not musicMenu.winfo_ismapped():
                musicMenu.grid(row=2, column=1, sticky=tk.W)
            else:
                musicMenu.grid_remove()
                introLabel['text'] = "Customize your Cactobot here!\nPress a button on the left to begin"

        # Function that updates the selected audio file based on user selection when user presses 'Select' button
        def selectMusic():
            selectedIndices = musicListbox.curselection()
            print(selectedIndices)
            print(len(selectedIndices) == 0)

            if not len(selectedIndices) == 0:
                index = int(list(selectedIndices)[0])
                selectedMusic = musicOptions[index]

                global selectedMusicPath
                selectedMusicPath = musicPaths[index]

                mixer.music.load(selectedMusicPath)
                mixer.music.set_volume(selectedVolumeLevel)
                mixer.music.play()

        # Function that makes visible the volume adjustment buttons that the user can use to adjust volume
        def changeVolumeLevel():
            # TODO @ANNA
            print("change volume level here")
            introLabel['text'] = "Set the volume of your Cactobot!"

            # Hide music + colors menu
            musicMenu.grid_remove()
            colors_menu.grid_remove()

            if not volumeMenu.winfo_ismapped():
                volumeMenu.grid(row=2, column=1, sticky=tk.W)
            else:
                volumeMenu.grid_remove()
                introLabel['text'] = "Customize your Cactobot here!\nPress a button on the left to begin"

        # Function that increases the volume if user clicks increase volume button
        def incrementVolume():
            global selectedVolumeLevel
            selectedVolumeLevel = min(1, selectedVolumeLevel + 0.1)
            updateVolumeLabel()

        # Function that decreases the volume if user clicks decrease volume button
        def decrementVolume():
            global selectedVolumeLevel
            selectedVolumeLevel = max(0, selectedVolumeLevel - 0.1)
            updateVolumeLabel()

        # Function that updates UI on volume menu to accurately reflect current volume level to the user
        def updateVolumeLabel():
            volumeLabel.config(text=f"Volume: {selectedVolumeLevel:.1f}")
            introLabel['text'] = "Set the volume of your Cactobot!"

        # Function that removes any of the customization menus when navigating to a different page
        def handleButtonClick(page):
            colors_menu.grid_remove()
            musicMenu.grid_remove()
            volumeMenu.grid_remove()
            controller.show_frame(page)
        
        # running program starts here
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="SETTINGS", font = HEADERFONT,
                          width = 13, background = "#77A752", anchor="center")
        label.grid(row = 0, column = 1)

        padding_right = ttk.Label(self, text ="", font = LARGEFONT,
                          width = 3, background = "#77A752", anchor="center")
        padding_right.grid(row = 0, column = 2, padx = 10, pady = 10)
  
        # Placing home button to link to home page
        home_icon_path = "images/home_icon.png"
        home_icon = tk.PhotoImage(file = home_icon_path)
        homeBtn = ttk.Button(self, text="HOME", style = 'btn.TButton', image = home_icon,
                             command = lambda: handleButtonClick(home.homePage))
        homeBtn.image = home_icon
        homeBtn.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NW)

        # Placing setting button to link to setting page
        setting_icon_path = "images/setting_icon.png"
        setting_icon = tk.PhotoImage(file = setting_icon_path)
        settingBtn = ttk.Button(self, text ="SETTINGS", style = 'btn.TButton', image = setting_icon,
                                command = lambda : controller.show_frame(settingsPage))
        settingBtn.image = setting_icon
        settingBtn.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = tk.NE)

        # Placing task button to link to task page
        task_icon_path = "images/task_icon.png"
        task_icon = tk.PhotoImage(file = task_icon_path)
        taskBtn = ttk.Button(self, text ="TASK", style = 'btn.TButton', image = task_icon,
                                command = lambda : controller.show_frame(task.tasksPage))
        taskBtn.image = task_icon
        taskBtn.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tk.SW)
        
        # Placing help button to link to help page
        help_icon_path = "images/help_icon.png"
        help_icon = tk.PhotoImage(file = help_icon_path)
        helpBtn = ttk.Button(self, text = "HELP", style = 'btn.TButton', image = help_icon, 
                             command = lambda: handleButtonClick(help.helpPage))
        helpBtn.image = help_icon

        helpBtn.grid(row = 5, column = 2, padx = 10, pady = 10, sticky=tk.SE)

        # Set style of customization buttons in Setting
        settingBtnStyle = ttk.Style()
        settingBtnStyle.theme_use('classic')
        settingBtnStyle.configure('settingBtn.TButton', foreground = "black", background = "#D9E9CD",
                           highlightthickness = 0, width = 13, borderwidth = 0, font = MEDIUMFONT)

        # Configure and place the three customization setting buttons
        lightBtn = ttk.Button(self, text = "Light Color", style = 'settingBtn.TButton', command = colorButtonsAppear)
        musicBtn = ttk.Button(self, text = "Music", style = 'settingBtn.TButton', command = changeMusic)
        volumeBtn = ttk.Button(self, text = "Volume Level", style = 'settingBtn.TButton', command = changeVolumeLevel)

        lightBtn.grid(row = 1, column = 0, padx = 10, pady = 10)
        musicBtn.grid(row = 2, column = 0, padx = 10, pady = 10)
        volumeBtn.grid(row = 3, column = 0, padx = 10, pady = 10)

        ################################################

        # Style for music and volume frame
        frameStyle = ttk.Style()
        frameStyle.configure('audioMenu.TFrame', background='#96BF76')

        audioBtnStyle = ttk.Style()
        audioBtnStyle.configure('audioBtn.TButton', background='#D9E9CD',
                              highlightthickness = 0, borderwidth = 0, font = MEDIUMFONT)

        # Intro message label display
        introStyle = ttk.Style()
        introStyle.configure('introLabel.TLabel', background = "#77A752",
                             font = MEDIUMFONT)
        introLabel = ttk.Label(self, text = "Customize your Cactobot here!\nPress a button on the left to begin!",
                               style = "introLabel.TLabel", anchor="center")
        introLabel.grid(row = 1, column = 1, padx = 10, pady = 10)

        # Music button clicked UI
        musicMenu = ttk.Frame(self, style = 'audioMenu.TFrame')

        # Currently available music option on Cactobot
        musicOptions = ["Air", "Bell Ringing", "Bright Jingle", "Complete", "Deep Bell", "Motion", "Rising Choir", 
                        "Short Success", "Song", "Soothing", "Trumpets", "Twinkle", "Whoosh"]

        # Paired list with corresponding paths to audio files for musicOptions list
        musicPaths = ["audio/Air.mp3", "audio/Bell_Ringing.mp3", "audio/Bright_Jingle.mp3", "audio/Complete.mp3",
                      "audio/Deep_Bell.mp3", "audio/Motion.mp3", "audio/Rising_Choir.mp3", "audio/Short_Success.mp3",
                      "audio/Song.mp3", "audio/Soothing.mp3", "audio/Success_Trumpets.mp3","audio/Twinkle.mp3", "audio/Whoosh.mp3"]

        # UI music displayed in scrollable listbox
        musicListbox = tk.Listbox(musicMenu, width=28, height = 6, selectmode=tk.SINGLE,
                                  background='#D9E9CD', font = MEDIUMFONT)
        scrollbar = tk.Scrollbar(musicMenu, orient=tk.VERTICAL, command=musicListbox.yview)
        musicListbox.config(yscrollcommand=scrollbar.set)
        
        # Add music options to listbox so user can choose from them
        for option in musicOptions:
            musicListbox.insert(tk.END, option)
        
        musicListbox.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Place select button that locks in the user's music selection
        selectButton = ttk.Button(musicMenu, text="Select", command=selectMusic,
                                  style = "audioBtn.TButton")
        selectButton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Place location of musicMenu grid when Music button pressed
        musicMenu.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W, rowspan = 3)
        musicMenu.grid_remove()

        ################################################
        # Volume menu UI
        volumeMenu = ttk.Frame(self, style = 'audioMenu.TFrame')

        # Place volume menu label
        volumeLabel = ttk.Label(volumeMenu, text=f"Volume: {selectedVolumeLevel:.1f}",
                                font=LARGEFONT, background = "#96BF76",
                                width = 18, anchor = "center")
        volumeLabel.grid(row=0, column=0, padx=10, pady=10)

        # Place increase volume button
        incrementButton = ttk.Button(volumeMenu, text="Increase",
                                     style = "audioBtn.TButton", command=incrementVolume)
        incrementButton.grid(row=1, column=0, padx=10, pady=10)

        # Place decrease volume button
        decrementButton = ttk.Button(volumeMenu, text="Decrease",
                                     style = "audioBtn.TButton", command=decrementVolume)
        decrementButton.grid(row=2, column=0, padx=10, pady=10)

        # Place location of volumeMenu when Volume Level button pressed
        volumeMenu.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W, rowspan = 3)
        volumeMenu.grid_remove()

        ################################################
        # Colors customization UI

        # Placing the colors buttons
        colors_menu = ttk.Frame(self, style = 'audioMenu.TFrame')

        # Red button in menu when Color button selected
        red_button_path = "images/red_circle.png"
        red_button_img = tk.PhotoImage(file=red_button_path)
        red_button_img = red_button_img.subsample(20)  # Adjust the subsample factor to resize the image 
        redButton = ttk.Button(colors_menu, text="RED", style='btn.TButton', image=red_button_img, compound=tk.CENTER,
                                   command = lambda: changeLightColor("red"))
        redButton.image = red_button_img
        redButton.grid(row = 0, column = 0)
        
        # Green button in menu when Color button selected
        green_button_path = "images/green_circle.png"
        green_button_img = tk.PhotoImage(file=green_button_path)
        green_button_img = green_button_img.subsample(5)  # Adjust the subsample factor to resize the image 
        greenButton = ttk.Button(colors_menu, text="GREEN", style='btn.TButton', image=green_button_img, compound=tk.CENTER,
                                 command = lambda: changeLightColor("green"))
        greenButton.image = green_button_img
        greenButton.grid(row = 0, column = 1)

        # Blue button in menu when Color button selected
        blue_button_path = "images/blue_circle.png"
        blue_button_img = tk.PhotoImage(file=blue_button_path)
        blue_button_img = blue_button_img.subsample(5)  # Adjust the subsample factor to resize the image 

        blueButton = ttk.Button(colors_menu, text="BLUE", style='btn.TButton', image=blue_button_img, compound=tk.CENTER,
                                command = lambda: changeLightColor("blue"))
        blueButton.image = blue_button_img
        blueButton.grid(row = 1, column = 0)

        # Teal button in menu when Color button selected
        teal_button_path = "images/teal_circle.png"
        teal_button_img = tk.PhotoImage(file=teal_button_path)
        teal_button_img = teal_button_img.subsample(5)  # Adjust the subsample factor to resize the image

        tealButton = ttk.Button(colors_menu, text="TEAL", style='btn.TButton', image=teal_button_img, compound=tk.CENTER,
                                command = lambda: changeLightColor("blue"))
        tealButton.image = teal_button_img
        tealButton.grid(row = 1, column = 1)

# Getter to return user selected color
def getSelectedColor():
    return selectedColor

# Getter to return path to user selected music
def getSelectedMusicPath():
    return selectedMusicPath

# Getter to return user selected volume level
def getSelectedVolumeLevel():
    return selectedVolumeLevel