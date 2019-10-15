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
        self.PaceingScren = Pacing_Window(root)

    def new_user_window(self):  # calls new user screen
        self.frame_root.pack_forget()
        self.NewUserWindow = New_User_Window(root)

    def read_input(self):
        print('')


class New_User_Window:
    def __init__(self, master):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()

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
        self.entry_password.config(show="*")
        self.entry_password.place(x=200, y=330)
        self.label_password = Label(self.frame_root, text="Password:")
        self.label_password.place(x=140, y=330)

        self.entry_password_confirmation = Entry(self.frame_root)
        self.entry_password_confirmation.place(x=200, y=360)
        self.entry_password_confirmation.config(show="*")
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
        self.LoginScreen = Login_Window(root)

    def create_user(self, username, password):
        Users.add_user(username, password)
        Users.save_users()

    def read_input(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        password_confirm = self.entry_password_confirmation.get()

        # Block for error handling in user creation
        if username:
            if not password:
                Notify_window(2)
            elif not password_confirm:
                Notify_window(3)
            elif password != password_confirm:
                Notify_window(4)
            elif password == password_confirm:
                self.create_user(username, password)
        else:
            Notify_window(1)

        if username and password and password_confirm and password == password_confirm:
            # Create window to notify users that registration has been completed
            # and bring users back to login window
            Notify_window(5)
            self.from_new_user()


class Notify_window():  # Class to warn users of errors various errors or to notify them of a conformation
    # If you want to add more errors or conformations, start a new block of if and elif cases
    # Use this class for any notifications that require a separate window
    def __init__(self, error):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Basic windows error sound to notify users
        box = Tk()  # Creating a separate tk window for the errors
        box.geometry('300x100')
        box.resizable(0, 0)
        # Button for closing the error window
        Ok_button = Button(box, text="        OK        ", command=box.destroy)
        Ok_button.place(x=110, y=50)

        # Add more statements if you have more errors to throw, please label the errors
        if error == 1:  # For no username entered in register
            error1_label = Label(box, text="Please enter a username")
            error1_label.place(x=80, y=20)

        elif error == 2:  # For no password entered in register
            error2_label = Label(box, text="Please enter a password")
            error2_label.place(x=80, y=20)

        elif error == 3:  # For no confirm password in register
            error3_label = Label(box, text="Please confirm your password")
            error3_label.place(x=80, y=20)

        elif error == 4:  # For non matching passwords entered in register
            error4_label = Label(box, text="Passwords do not match")
            error4_label.place(x=80, y=20)

        elif error == 5:  # For successful creation of new user
            created_label = Label(box, text="Registration confrimed!")
            created_label.place(x=80, y=20)


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

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.from_Pacing_Window)
        self.button_signout.place(x=400, y=50)

        self.AOO_image = tk.PhotoImage(file="AOO.png")
        self.AOO_button = Button(self.frame_root, image=self.AOO_image)
        self.AOO_button.config(command=self.To_Parameters)
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
        self.LoginScreen = Login_Window(root)

    def To_Parameters(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Parameter_Window(root,1)


class Parameter_Window:
    def __init__(self, master,mode):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()

        self.background_image = tk.PhotoImage(file="backgroundpacing.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        self.entry_Upperlim = Entry(self.frame_root)
        self.entry_Upperlim.place(x=200, y=300)
        self.entry_Lowerlim = Entry(self.frame_root)
        self.entry_Lowerlim.place(x=200, y=350)
        self.entry_Delay = Entry(self.frame_root)
        self.entry_Delay.place(x=200, y=400)
        self.entry_Width = Entry(self.frame_root)
        self.entry_Width.place(x=200, y=250)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root,image = self.Back_image)
        self.button_back.config(command=self.from_Parameter_Window)
        self.button_back.place(x=400, y=50)
        self.label_lowlim = Label(self.frame_root, text="Lower limit:")
        self.label_lowlim.place(x=130, y=250)
        self.label_uplim = Label(self.frame_root, text="Upper limit:")
        self.label_uplim.place(x=130, y=300)
        self.label_delay = Label(self.frame_root, text="Delay:")
        self.label_delay.place(x=160, y=350)
        self.label_width = Label(self.frame_root, text="Pluse width:")
        self.label_width.place(x=130, y=400)



        self.button_ok = Button(self.frame_root, text="     Ok     ")
        self.button_ok.config(command=self.Ok)
        self.button_ok.place(x=190, y=430)

        self.button_apply = Button(self.frame_root, text="    Apply    ")
        self.button_apply.config(command=self.Apply)
        self.button_apply.place(x=260, y=430)

        if mode == 1:
            self.label_title1 = Label(self.frame_root, text="VVI Pacing Mode")
            self.label_title1.config(font=("Courier", 15))
            self.label_title1.place(x=160, y=150)

        elif mode == 2:
            self.label_title2 = Label(self.frame_root, text="AAO Pacing Mode")
            self.label_title1.config(font=("Courier", 15))
            self.label_title2.place(x=100, y=150)

        elif mode == 3:
            self.label_title2 = Label(self.frame_root, text="AAI Pacing Mode")
            self.label_title1.config(font=("Courier", 15))
            self.label_title2.place(x=100, y=150)

        elif mode == 4:
            self.label_title2 = Label(self.frame_root, text="VOO Pacing Mode")
            self.label_title1.config(font=("Courier", 15))
            self.label_title2.place(x=100, y=150)

    def from_Parameter_Window(self):
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Window(root)

    def Apply(self): # Apply will save the parameters in the entry fields and return to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Window(root)
        # Add code here to also save the parameters

    def Ok(self): # Ok will only save the parameters in the entry fields
        x = 1 # Just random code so pycharm doesnt freak out that there is nothing in the function
        # add code here to save the parameters


list_of_users = [User0, User1, User2, User3, User4, User5, User6, User7, User8, User9]
root = Tk()
root.resizable(0, 0)
LoginScreen = Login_Window(root)
Users = ListOfUsers(list_of_users)
root.mainloop()
