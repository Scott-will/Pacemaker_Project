#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the Login Screen and its required functions       #
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
import pickle
import New_User_Screen
import Menu_Window
import Notifiy_Window



def save_users(list_of_users):  ##writing users to file
    f = open("Users.txt", 'wb')  # opens file then dumps users into file
    pickle.dump(list_of_users, f)
    f.close()
    list_of_users = read_users()
    print(list_of_users)
    print("su")
    return list_of_users


def read_users():  # reading saved users from txt file
    list_of_users = []
    try:
        f = open("Users.txt", 'rb')  # opens file
        while True:
            try:
                list_of_users = pickle.load(f)  ##reading data from file if not end of file
            except EOFError:
                break
        f.close()
    except IOError:
        f = open("Users.txt", 'w+')
        f.close()
    return list_of_users


def read_last_login():  ##reading last user saved if remember me is checked
    last_login = []
    try:
        f2 = open("Remembered.txt", 'rb')  ##opens file
        while True:
            try:
                last_login = pickle.load(f2)  ##reads file while not end of file
            except EOFError:
                break
        f2.close()
    except IOError:
        f2 = open("Remembered.txt", 'w+')
        f2.close()

    return last_login


def add_user(list_of_users, username, password):  ##adding a user
    try:
        if len(list_of_users) < 20:  ##check if not max number of users
            not_found = True
            for i in range(0, len(list_of_users) - 1, 2):
                if username == list_of_users[i]:
                    not_found = False
                    Notifiy_Window.Notify_window(1)
                    break
            if not_found == True:  ##ERRROR IS SOMEWHERE HERE
                list_of_users.append(username)
                list_of_users.append(password)  # append login info
        else:
            Notifiy_Window.Notify_window(7)  ##error window
    except TypeError:
        list_of_users = []
        list_of_users.append(username)
        list_of_users.append(password)
        print(list_of_users)
        print("au")
    return list_of_users

list_of_users = read_users()
last_login = read_last_login()

class Login_Window:  # Class for the create of the main login window
    def __init__(self, master):  ##initializes the class, root is the master

        # We will be using the same root window and placing and removing frames different frames, every class will
        # have its own frame
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.master = master

        # Here we are setting the background image for the window. line 46 creates a reference to the image as python
        # will garbage collect the image if there is no reference made
        self.background_image = tk.PhotoImage(file='newbackground.png')
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        # Block for the creation of text labels for the login frame
        self.label_user = Label(self.frame_root, text="UserID:")
        self.label_user.place(x=125, y=350)
        self.label_pass = Label(self.frame_root, text="Password:")
        self.label_pass.place(x=110, y=380)
        self.label_remember = Label(self.frame_root, text="Remember me")
        self.label_remember.place(x=190, y=401)

        # Block for the creation of the entry boxes for the login frame
        self.entry_user = Entry(self.frame_root)
        self.entry_user.place(x=170, y=350)
        self.entry_pass = Entry(self.frame_root)
        self.entry_pass.config(show="*")
        self.entry_pass.place(x=170, y=380)

        # Block for the creation of the checkboxes for the login frame
        self.check_state_var = IntVar()  ##variable to check the state of the checkbox
        self.checkbutton_remember = Checkbutton(self.frame_root,
                                                variable=self.check_state_var)  ##, command=self.remember_me())
        self.checkbutton_remember.config(command=self.remember_me)
        self.checkbutton_remember.place(x=165, y=400)
        self.get_old_users()  ##gets old user login info if remember me is checked,

        # Block for the creation of the buttons for the login frame
        self.button_login = Button(self.frame_root, text="Login",
                                   command=self.menu_screen)  # command = self.check_user(self.entry_user.get(), self.entry_pass.get()))
        self.button_login.place(x=170, y=425)
        # self.button_login.config(command=self.check_user(self.entry_user.get(), self.entry_pass.get()))
        self.button_create = Button(self.frame_root, text="New User", command=self.new_user_window)
        self.button_create.place(x=235, y=425)

    def remember_me(self):  ##function called when remember me box ix checked, saves user to a file
        if self.check_state_var.get() == 1:  ##checks if remember me is checked adds info to dump to file
            to_dump = [self.entry_user.get(), self.entry_pass.get(), self.check_state_var.get()]
            f = open("Remembered.txt", 'wb')
            pickle.dump(to_dump, f)  ##dumps info
            f.close()
        if self.check_state_var.get() == 0:
            to_dump = []
            f = open("Remembered.txt", 'wb')
            pickle.dump(to_dump, f)  ##dumps info
            f.close()

    def menu_screen(self):  ##calls menu screen
        password = self.entry_pass.get()
        username = self.entry_user.get()
        list_of_users = read_users()
        success = 0  ##variable to check if need to call error window
        try:
            for i in range(0, len(list_of_users) - 1, 2):  # checks if user exists and password is correct
                if list_of_users[i] == username:
                    if password == list_of_users[i + 1]:
                        self.frame_root.pack_forget()
                        self.menuscreen = Menu_Window.menu(self.master, username)
                        success = 1
        except TypeError:
            pass
        if success == 0:
            Error = Notifiy_Window.Notify_window(6)  ##user does not exist

    def new_user_window(self):  # calls new user screen
        self.frame_root.pack_forget()
        self.NewUserWindow = New_User_Screen.New_User_Window(self.master, list_of_users)

    def get_old_users(self):
        try:
            old_user = []
            f2 = open("Remembered.txt", "rb")
            while True:
                try:
                    old_user = (pickle.load(f2))  # reads old user login info while not end of file
                except EOFError:
                    break
            f2.close()
            try:
                if old_user[2] == 1:  ##checks if remembered me is checked
                    self.entry_user.insert(10, old_user[0])  # inserts into user and password entry spot
                    self.entry_pass.insert(10, old_user[1])
                    self.check_state_var.set(1)
            except IndexError:
                pass
            except TypeError:
                old_user = []  ##does nothing
        except IOError:
            f2 = open("Remembered.txt", 'w+')
            old_user = []
            f2.close()