#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the Egram plot, currently has no function        #
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
import Excel_Handling as ex
import pandas as pd


class Electrogram: # Still need to impletment
    def __init__(self, master, df):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.master = master
        self.df = df
