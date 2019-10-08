import winsound
from tkinter import *
from winsound import *
import tkinter as tk

User0 = {
    'Username':'NULL',
    'Password':'NULL'
}

User1 = {
    'Username':'NULL',
    'Password':'NULL'
}

User2 = {
    'Username':'NULL',
    'Password':'NULL'
}
User3 = {
    'Username':'NULL',
    'Password':'NULL'
}
User4 = {
    'Username':'NULL',
    'Password':'NULL'
}
User5 = {
    'Username':'NULL',
    'Password':'NULL'
}
User6 = {
    'Username':'NULL',
    'Password':'NULL'
}

User7 = {
    'Username':'NULL',
    'Password':'NULL'
}

User8 = {
    'Username':'NULL',
    'Password':'NULL'
}

User9 = {
    'Username':'NULL',
    'Password':'NULL'
}



class ListOfUsers:
    def __init__(self, users):
        self.numberofusers = 0
        self.users = users
    def save_users(self):
        f = open("fUsers.txt", 'w+')
        f.write('%d' % self.numberofusers)
        f.close()
    def add_user(self, username, password):
        self.numberofusers += 1
        list_of_users[self.numberofusers - 1]['Username'] = username
        print(list_of_users[self.numberofusers - 1]['Username'])


class Login_Window:
    def __init__(self, master): ##initializes the class, root is the master
        self.frame_root = Frame(master, width = 500, height = 500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file = 'newbackground.png')
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.label_user = Label(self.frame_root, text="UserID:")
        self.label_user.place(x=125, y=350)
        self.label_pass = Label(self.frame_root, text="Password:")
        self.label_pass.place(x=110, y=380)
        self.label_remember = Label(self.frame_root, text="Remember me")
        self.label_remember.place(x=190, y=401)

        self.entry_user = Entry(self.frame_root)
        self.entry_user.place(x=170, y=350)
        self.entry_pass = Entry(self.frame_root)
        self.entry_pass.config(show="*")
        self.entry_pass.place(x=170, y=380)

        self.checkbutton_remember = Checkbutton(self.frame_root)
        self.checkbutton_remember.place(x=165, y=400)

        self.button_login = Button(self.frame_root, text="Login", command=self.pacing_screen)
        self.button_login.place(x=170, y=425)
        self.button_create = Button(self.frame_root, text="New User", command=self.new_user_window)
        self.button_create.place(x=235, y=425)

    def pacing_screen(self): ##calls pacing screen
        self.frame_root.pack_forget()
        PacingScreen = Pacing_Window(root)

    def new_user_window(self): #caalls new user screen
        self.frame_root.pack_forget()
        NewUserWindow = New_User_Window(root)
    def read_input(self):
        print('')


class New_User_Window:
    def __init__(self, master):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        # button to create user

        self.background_image = tk.PhotoImage(file="backgroundpacing.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        # place to enter text
        self.entry_username = Entry(self.frame_root)
        self.entry_username.place(x=200, y=300)
        self.label_username = Label(self.frame_root, text="UserID:")
        self.label_username.place(x=155, y=300)
        self.entry_password = Entry(self.frame_root)
        self.entry_password.place(x=200, y=330)
        self.label_password = Label(self.frame_root, text="Password:")
        self.label_password.place(x=140, y=330)
        self.entry_password_confirmation = Entry(self.frame_root)
        self.entry_password_confirmation.place(x=200, y=360)
        self.label_password_confirmation = Label(self.frame_root, text="Confirm Password:")
        self.label_password_confirmation.place(x=95, y=360)

        # button to create user
        self.button_username = Button(self.frame_root, text="Create")
        self.button_username.place(x=200, y=390)
        self.button_username.config(command = self.read_input)
        self.button_cancel = Button(self.frame_root, text="Cancel") #need something here
        self.button_cancel.place(x=250, y=390)

    def create_user(self, username, password):
        Users.add_user(username, password)


    def read_input(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        password_confirm = self.entry_password_confirmation.get()
        if password == password_confirm:
            self.create_user(username, password)
        else:
            print(username)

class Pacing_Window:
    def __init__(self, master):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

class ErrorWindow:
    def __init__(self):
        self.errorwindow = Tk()
        sound()
        self.label_error = Label(errorwindow, text="Error: Wrong password and or userid entered")
        self.label_error.grid(row=1)
        self.button_ok = Button(errorwindow, text="   ok   ")
        self.button_ok.grid(columnspan=2)

list_of_users = [User0, User1, User2, User3, User4, User5, User6, User7, User8, User9]
root = Tk()
LoginScreen = Login_Window(root)
Users = ListOfUsers(list_of_users)
root.mainloop()
