import DCM_Def
from tkinter import*

#list_of_users = DCMV18.read_users()  ##get our list of users


#last_login = DCMV18.read_last_login()
root = Tk()  # Created the window where the entire program is run

# This make it so the users cannot adjust the side of the window, we do this because expanding
# the window will ruin the background and layout fo the widgets
root.resizable(0, 0)

# Here we take the window we just created and we place the first frame onto it which is the login frame
LoginScreen = DCM_Def.Login_Window(root)

# Creates a infinite loop that keeps the program from closing
root.mainloop()