#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the registration screen                          #
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
from tkinter import *
import tkinter as tk
import Login_Screen
import Notifiy_Window


class New_User_Window:
    def __init__(self, master, list_of_users):
        #frame definition
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.list_of_users = list_of_users
        self.master = master

        # buttons and text defintions
        self.background_image = tk.PhotoImage(file="backgroundpacing.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        self.entry_username = Entry(self.frame_root)
        self.entry_username.place(x=200, y=300)
        self.label_username = Label(self.frame_root, text="UserID:")
        self.label_username.place(x=155, y=300)

        self.entry_password = Entry(self.frame_root)
        self.entry_password.config(show="*")
        self.entry_password.place(x=200, y=330)
        self.label_password = Label(self.frame_root, text="Password:")
        self.label_password.place(x=140, y=330)

        self.entry_password_confirmation = Entry(self.frame_root)
        self.entry_password_confirmation.place(x=200, y=360)
        self.entry_password_confirmation.config(show="*")
        self.label_password_confirmation = Label(self.frame_root, text="Confirm Password:")
        self.label_password_confirmation.place(x=95, y=360)

        self.button_username = Button(self.frame_root, text="Create")
        self.button_username.place(x=200, y=390)
        self.button_username.config(command=self.create_user)
        self.button_cancel = Button(self.frame_root, text="Cancel")
        self.button_cancel.config(command=self.from_new_user)
        self.button_cancel.place(x=250, y=390)

    def from_new_user(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        self.LoginScreen = Login_Screen.Login_Window(self.master)

    def create_user(self):  # We take the collected username and password and save them
        username = self.entry_username.get()
        password = self.entry_password.get()
        password_confirm = self.entry_password_confirmation.get()
        isnumber_username = False
        isnumber_password = False

        if len(username) > 5:
            for i in username:
                if i.isdigit():
                    isnumber_username = True
            if len(password) > 5:
                for i in username:
                    if i.isdigit():
                        isnumber_password = True

        if isnumber_username and isnumber_password:
            if password == password_confirm:
                self.list_of_users = Login_Screen.add_user(self.list_of_users, username, password)
                list_of_users = Login_Screen.save_users(self.list_of_users)
                print(list_of_users)
                self.from_new_user()  ##goes back to login screen
            else:
                error = Notifiy_Window.Notify_window(4)
        else:
             Notifiy_Window.Notify_window(3)
