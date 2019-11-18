#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the mode selection screen                        #
#                                                                   #
#####################################################################

#################################
# Import classes as needed      #
# Class list:                   #
# import winsound               #
# from tkinter import *         #
# import tkinter as tk          #
# import pickle                 #
# import Login_Screen           #
# import New_User_Screen        #
# import Menu_Window            #
# import Parameter_Window       #
# import Pacing_Screen          #
# import EGram_Window           #
# import Notify_Window          #
#################################
from tkinter import *
import tkinter as tk
import Login_Screen
import Menu_Window
import Paramter_Window
import Excel_Handling as ex
import pandas as pd






class Pacing_Window:
    def __init__(self, master, user, df):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.text = Label(self.frame_root, text="Please select a Pacing mode")
        self.text.config(font=("Courier", 15))
        self.text.place(x=95, y=150)
        self.user = user
        self.master = master
        self.df = df

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.from_Pacing_Window)
        self.button_signout.place(x=400, y=90)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root, image=self.Back_image)
        self.button_back.config(command=self.To_Menu)
        self.button_back.place(x=400, y=50)

        self.AOO_image = tk.PhotoImage(file="AOO.png")
        self.AOO_button = Button(self.frame_root, image=self.AOO_image)
        self.AOO_button.config(command=self.To_Parameters1)
        self.AOO_button.place(x=100, y=200)

        self.VOO_image = tk.PhotoImage(file="VOO.png")
        self.VOO_button = Button(self.frame_root, image=self.VOO_image)
        self.VOO_button.config(command=self.To_Parameters2)
        self.VOO_button.place(x=100, y=300)

        self.AAI_image = tk.PhotoImage(file="AAI.png")
        self.AAI_button = Button(self.frame_root, image=self.AAI_image)
        self.AAI_button.config(command=self.To_Parameters3)
        self.AAI_button.place(x=300, y=200)

        self.VVI_image = tk.PhotoImage(file="VVI.png")
        self.VVI_button = Button(self.frame_root, image=self.VVI_image)
        self.VVI_button.config(command=self.To_Parameters4)
        self.VVI_button.place(x=300, y=300)



    def from_Pacing_Window(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        self.LoginScreen = Login_Screen.Login_Window(self.master)

    # These 4 methods will display the appropriate texts depending on which mode was pressed on the pacing screen
    def To_Parameters1(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Paramter_Window.Parameter_Window(self.master, 1, self.user)

    def To_Parameters2(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Paramter_Window.Parameter_Window(self.master, 2, self.user)

    def To_Parameters3(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Paramter_Window.Parameter_Window(self.master, 3, self.user)

    def To_Parameters4(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Paramter_Window.Parameter_Window(self.master, 4, self.user)

    def To_Menu(self):
        self.frame_root.pack_forget()
        self.menu = Menu_Window.menu(self.master,self.user)
