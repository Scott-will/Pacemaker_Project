#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for serial communication                             #
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
# import serial                 #
# import Serial_com             #
# import time                   #
#################################

import tkinter as tk
from tkinter import *
import serial
import Login_Screen
import Menu_Window
import time
from serial import Serial


################################################
#           Serial configuration               #
#                                              #
################################################



class Scom:
    def __init__(self):
        self.s = Serial()
        self.s.port = 'COM7'
        self.s.baudrate = 9600
        self.s.timeout = 0.5
        self.s.dtr = 0

    def startcom(self):

        self.s = Serial()
        self.s.port = 'COM7'
        self.s.baudrate = 9600
        self.s.timeout = 0.5
        self.s.dtr = 0
        self.s.open()
        self.state = self.s.isOpen()
        return self.state

    def stopcom(self):
        self.ser.close()
        self.state = self.s.isOpen()
        return self.state








class Serial_Window:
    def __init__(self, master,user):
        self.master = master
        self.user = user
        self.frame_root = Frame(self.master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.from_Serial_Window)
        self.button_signout.place(x=400, y=90)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root, image=self.Back_image)
        self.button_back.config(command=self.To_Menu)
        self.button_back.place(x=400, y=50)

        self.start_image = tk.PhotoImage(file="start.png")
        self.button_start = Button(self.frame_root, image=self.start_image)
        self.button_start.config(command=self.startpress)
        self.button_start.place(x=50, y=170)

        self.stop_image = tk.PhotoImage(file="stop.png")
        self.button_stop = Button(self.frame_root, image=self.stop_image)
        self.button_start.config(command=self.stoppress)
        self.button_stop.place(x=50, y=310)

        self.serialclosed_image = tk.PhotoImage(file="serialclosed.png")
        self.label_serialclosed = Label(self.frame_root, image=self.serialclosed_image)
        self.label_serialclosed.place(x=350, y=250)

    def startpress(self):
            if Scom.startcom(self):
                self.serialopen_image = tk.PhotoImage(file="serialopen.png")
                self.label_serialopen = Label(self.frame_root, image=self.serialopen_image)
                self.label_serialopen.place(x=350, y=250)
            else:
                self.serialclosed_image = tk.PhotoImage(file="serialclosed.png")
                self.label_serialclosed = Label(self.frame_root, image=self.serialclosed_image)
                self.label_serialclosed.place(x=350, y=250)

    def stoppress(self):
            if Scom.startcom(self):
                self.serialopen_image = tk.PhotoImage(file="serialopen.png")
                self.label_serialopen = Label(self.frame_root, image=self.serialopen_image)
                self.label_serialopen.place(x=350, y=250)
            else:
                self.serialclosed_image = tk.PhotoImage(file="serialclosed.png")
                self.label_serialclosed = Label(self.frame_root, image=self.serialclosed_image)
                self.label_serialclosed.place(x=350, y=250)

    def from_Serial_Window(self):
        self.frame_root.pack_forget()
        self.LoginScreen = Login_Screen.Login_Window(self.master)

    def To_Menu(self):
        self.frame_root.pack_forget()
        self.menu = Menu_Window.menu(self.master, self.user)
