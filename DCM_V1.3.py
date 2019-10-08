import winsound
from tkinter import *
from winsound import *
import tkinter as tk
import pickle

User0 = {
    'Username': 'NULL',
    'Password': 'NULL'
}

User1 = {
    'Username': 'NULL',
    'Password': 'NULL'
}

User2 = {
    'Username': 'NULL',
    'Password': 'NULL'
}
User3 = {
    'Username': 'NULL',
    'Password': 'NULL'
}
User4 = {
    'Username': 'NULL',
    'Password': 'NULL'
}
User5 = {
    'Username': 'NULL',
    'Password': 'NULL'
}
User6 = {
    'Username': 'NULL',
    'Password': 'NULL'
}

User7 = {
    'Username': 'NULL',
    'Password': 'NULL'
}

User8 = {
    'Username': 'NULL',
    'Password': 'NULL'
}

User9 = {
    'Username': 'NULL',
    'Password': 'NULL'
}


class ListOfUsers:
    def __init__(self, users):
        self.numberofusers = 0
        self.users = users
        self.data = 0

    def save_users(self):
        f = open("Users.txt", 'wb')
        pickle.dump(self.users, f)
        f.close()

    def read_users(self):  # reading saved users
        f = open("Users.txt", rb)
        self.data = pickle.load("Users.txt")

    def add_user(self, username, password):
        self.numberofusers += 1
        list_of_users[self.numberofusers - 1]['Username'] = username
        list_of_users[self.numberofusers - 1]['Password'] = password
        print(list_of_users[self.numberofusers - 1]['Username'])


class Login_Window:
    def __init__(self, master):  ##initializes the class, root is the master
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file='newbackground.png')
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

    def pacing_screen(self):  ##calls pacing screen
        self.frame_root.pack_forget()
        PaceingScren = Pacing_Window(root)
        self.AOO_image = tk.PhotoImage(file="AOO.png")
        self.AOObutton = Button(self.frame_root, image="AOO_image.png")
        self.AOObutton.place(x=100, y=100)

    def new_user_window(self):  # caalls new user screen
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
        self.button_username.config(command=self.read_input)
        self.button_cancel = Button(self.frame_root, text="Cancel")
        self.button_cancel.config(command=self.from_new_user)
        self.button_cancel.place(x=250, y=390)

    def from_new_user(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        LoginScreen = Login_Window(root)

    def create_user(self, username, password):
        Users.add_user(username, password)
        Users.save_users()

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
        self.text = Label(self.frame_root, text="Please select a Pacing mode")
        self.text.config(font=("Courier", 15))
        self.text.place(x=95, y=150)

        self.cancel_image = tk.PhotoImage(file="cancel.png")
        self.button_cancel = Button(self.frame_root, image=self.cancel_image)
        self.button_cancel.config(command=self.from_Pacing_Window)
        self.button_cancel.place(x=400, y=50)

        self.AOO_image = tk.PhotoImage(file="AOO.png")
        self.AOO_button = Button(self.frame_root, image=self.AOO_image)
        self.AOO_button.place(x=100, y=200)

        self.VOO_image = tk.PhotoImage(file="VOO.png")
        self.VOO_button = Button(self.frame_root, image=self.VOO_image)
        self.VOO_button.place(x=100, y=300)

        self.AAI_image = tk.PhotoImage(file="AAI.png")
        self.AAI_button = Button(self.frame_root, image=self.AAI_image)
        self.AAI_button.place(x=300, y=200)

        self.VVI_image = tk.PhotoImage(file="VVI.png")
        self.VVI_button = Button(self.frame_root, image=self.VVI_image)
        self.VVI_button.place(x=300, y=300)

    def from_Pacing_Window(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        LoginScreen = Login_Window(root)


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