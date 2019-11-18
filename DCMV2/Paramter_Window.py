#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the parameter window                             #
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
# import Notify_Window
#
#################################
from tkinter import *
import tkinter as tk
import pickle
import Login_Screen
import Pacing_Screen
import Notifiy_Window
import Excel_Handling as ex
import pandas as pd





class Parameter_Window:
    def __init__(self, master, mode, user, df):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root.pack()
        self.mode = mode
        self.user = user
        self.master = master
        self.parameters = self.old_parameters()
        self.df = df



        # The following 4 modes will display the correct set of titles depending on which pacing mode the user wants to
        # edit
        if self.mode == 1:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()
            # command's parameters are the x and y coordinates for the various widgets it creates
            self.common(125, 172, 125, 222, 30, 220, 30, 170, 300, 50, 300, 350, 300, 300, 300, 90)

            self.label_title1 = Label(self.frame_root, text="AOO Pacing Mode")
            self.label_title1.config(font=("Courier", 11))
            self.label_title1.place(x=130, y=145)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=30, y=270)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=24, y=320)
            self.label_Atr_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Atr_Sens.place(x=30, y=370)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=93, y=420)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=80, y=470)

            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=125, y=270)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=125, y=320)
            self.entry_Atr_Sens = Entry(self.frame_root)
            self.entry_Atr_Sens.place(x=125, y=370)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=125, y=420)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=125, y=470)

            self.write_parameters()

        elif self.mode == 2:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 240, 60, 190, 300, 50, 300, 310, 300, 260, 300, 90)

            self.label_title2 = Label(self.frame_root, text="VOO Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=100, y=150)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=40, y=292)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=33, y=342)

            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=155, y=292)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=155, y=342)
            self.write_parameters()


        elif self.mode == 3:

            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 240, 60, 190, 430, 60, 400, 420, 400, 370, 430, 100)

            self.label_title3 = Label(self.frame_root, text="AAI Pacing Mode")
            self.label_title3.config(font=("Courier", 15))
            self.label_title3.place(x=200, y=150)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=57, y=342)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=50, y=292)
            self.label_Atr_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Atr_Sens.place(x=62, y=392)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=125, y=442)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=365, y=192)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=345, y=242)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=315, y=292)

            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=155, y=292)
            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=155, y=342)
            self.entry_Atr_Sens = Entry(self.frame_root)
            self.entry_Atr_Sens.place(x=155, y=392)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=155, y=442)

            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=410, y=192)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=410, y=242)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=410, y=292)

            self.write_parameters()


        elif self.mode == 4:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(180, 182, 180, 232, 85, 182, 85, 232, 430, 60, 400, 350, 400, 300, 430, 100)

            self.label_title4 = Label(self.frame_root, text="VII Pacing Mode")
            self.label_title4.config(font=("Courier", 12))
            self.label_title4.place(x=210, y=150)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=66, y=272)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=60, y=322)
            self.label_Vent_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Vent_Sens.place(x=70, y=372)
            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=150, y=422)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=335, y=172)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=317, y=222)

            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=180, y=272)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=180, y=322)
            self.entry_Vent_Sens = Entry(self.frame_root)
            self.entry_Vent_Sens.place(x=180, y=372)
            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=180, y=422)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=410, y=182)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=410, y=232)
            self.write_parameters()



    # All widgets are created in common() are common between all 4 pacing mode. Because the layout for the window of
    # each mode is different we will just pass the x and y coord as parameters when the method is called
    def common(self, upperlimx, upperlimy, lowerlimx, lowerlimy, upperlimx2, upperlimy2, lowerlimx2, lowerlimy2, backx,
               backy, okx, oky, applyx, applyy, signoutx, signouty):
        self.entry_Upperlim = Entry(self.frame_root)
        self.entry_Upperlim.place(x=upperlimx, y=upperlimy)
        self.entry_Lowerlim = Entry(self.frame_root)
        self.entry_Lowerlim.place(x=lowerlimx, y=lowerlimy)

        self.label_lowlim = Label(self.frame_root, text="Lower Rate limit:")
        self.label_lowlim.place(x=lowerlimx2, y=lowerlimy2)
        self.label_uplim = Label(self.frame_root, text="Upper Rate limit:")
        self.label_uplim.place(x=upperlimx2, y=upperlimy2)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root, image=self.Back_image)
        self.button_back.config(command=self.from_Parameter_Window)
        self.button_back.place(x=backx, y=backy)

        self.button_ok = Button(self.frame_root, text="     Ok     ")
        self.button_ok.config(command=self.Ok)
        self.button_apply = Button(self.frame_root, text="    Apply    ")
        self.button_apply.config(command=self.Apply)
        self.button_apply.place(x=applyx, y=applyy)
        self.button_ok.place(x=okx, y=oky)

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.To_login)
        self.button_signout.place(x=signoutx, y=signouty)

    def from_Parameter_Window(self):  # Returns to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)

    def To_login(self):
        self.frame_root.pack_forget()
        self.login = Login_Screen.Login_Window(self.master, self.df)


    def Apply(self):  # Apply will save the #parameters in the entry fields and return to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)
        # Add code here to also save the parameters

        self.save_parameters()

    def Ok(self):  # Ok will only save the parameters in the entry fields
        self.save_parameters()  # Just random code so pycharm doesnt freak out that there is nothing in the function
        # add code here to save the parameters

    def save_parametersV2(self):

                ##check if correct bounds
                ##change correct paramters in the excel file

    def save_VOO(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]: ##find user
                    if int(self.entry_Lowerlim.get()) >= 60 and int(self.entry_Lowerlim.get()) < int(self.entry_Upperlim.get()):
                        self.df[self.df['Users'].iloc[i], 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                    if int(self.entry_Upperlim.get()) <= 120 and int(self.entry_Upperlim.get()) > int(self.entry_Lowerlim.get)
                        self.df[self.df['Users'].iloc[i], 'VOO Upper Rate Limit'] = int(self.entry_UpperLim.get())
                    if int(self.entry_Vent_Pulse) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'VOO Pulse Width'] = int(self.entry_)
                    if int(self.entry_Vent_Amp) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'VOO Ventrical Amplitude'] = int()
            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window(8)

    def save_AOO(self):
        for i in range(0, 20, 2):
            if self.user == self.df['Users'].iloc[i]: ##find user
                self.df[self.df['Users'].iloc[i], 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                self.df[self.df['Users'].iloc[i], 'VOO Upper Rate Limit'] = int(self.entry_UpperLim.get())
                self.df[self.df['Users'].iloc[i], 'VOO Pulse Width'] = int(self.entry_)
                self.df[self.df['Users'].iloc[i], 'VOO Ventrical Amplitude'] = int()
        ##LowerRateLimit, upper rate limit, pulse width, atrial amplitude
        ##save parameter
    def save_VVI(self):
        for i in range(0, 20, 2):
            if self.user == self.df['Users'].iloc[i]: ##find user
                self.df[self.df['Users'].iloc[i], 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                self.df[self.df['Users'].iloc[i], 'VOO Upper Rate Limit'] = int(self.entry_UpperLim.get())
                self.df[self.df['Users'].iloc[i], 'VOO Pulse Width'] = int(self.entry_)
                self.df[self.df['Users'].iloc[i], 'VOO Ventrical Amplitude'] = int()
        ##lower rate limit, upper rate limit, pulse width, ventricular amplitude,
        ##ventricular sensitiivity, vrp, rate smoothing
    def save_AAI(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]: ##find user
                    self.df[self.df['Users'].iloc[i], 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                    self.df[self.df['Users'].iloc[i], 'VOO Upper Rate Limit'] = int(self.entry_UpperLim.get())
                    self.df[self.df['Users'].iloc[i], 'VOO Pulse Width'] = int(self.entry_)
                    self.df[self.df['Users'].iloc[i], 'VOO Ventrical Amplitude'] = int()
        except ValueError:
            Notifiy_Window(8)
    def save_DOO(self):
        #save parameters
    def save_AOOR(self):
        ##save parameters
    def save_AAIR(self):
        ##save parameters
    def save_VOOR(self):
        ##save parameters
    def save_VVIR(self):
        ##save parameters
    def save_DOOR(self):
        ##save parameters
    def save_DDDR(self):
        ##save parameters


    def save_parameters(self):  ##saves parameters

        ##check if file is empty,
        ##order is user, ul, ll, d, w, mode
        ##so search file to see if user exists (icrement by 6 6)
        ##if yes change data
        ##if no add user and data
        i = 0
        while True:
            try:
                if self.user == self.parameters[i]:  ##if user already has parameters, change them
                    self.parameters[i + 1] = self.entry_Upperlim.get()
                    self.parameters[i + 2] = self.entry_Lowerlim.get()
                    self.parameters[i + 3] = self.entry_Sensor_Rate.get()
                    self.parameters[i + 4] = self.entry_AV_Delay.get()
                    self.parameters[i + 5] = self.entry_Dyn_AV_Delay.get()
                    self.parameters[i + 6] = self.entry_AV_Delay_Off1.get()
                    self.parameters[i + 7] = self.entry_Atr_Amp.get()
                    self.parameters[i + 8] = self.entry_Vent_Amp.get()
                    self.parameters[i + 9] = self.entry_Atr_Pulse.get()
                    self.parameters[i + 10] = self.entry_Vent_Pulse.get()
                    self.parameters[i + 11] = self.entry_Vent_Sens.get()
                    self.parameters[i + 12] = self.entry_Atr_Sens.get()
                    self.parameters[i + 13] = self.entry_VRP.get()
                    self.parameters[i + 14] = self.entry_ARP.get()
                    self.parameters[i + 15] = self.entry_PVARP.get()
                    self.parameters[i + 16] = self.entry_PVARP_Ext.get()
                    self.parameters[i + 17] = self.entry_Hyst.get()
                    self.parameters[i + 18] = self.entry_Rate_Smooth.get()
                    self.parameters[i + 19] = self.entry_ATR_Dur.get()
                    self.parameters[i + 20] = self.entry_ATR_Fallback_Mode.get()
                    self.parameters[i + 21] = self.entry_Act_Thres.get()
                    self.parameters[i + 22] = self.entry_React_Time.get()
                    self.parameters[i + 23] = self.entry_Resp_Fact.get()
                    self.parameters[i + 24] = self.entry_Recv_Time.get()
                    self.parameters[i + 25] = self.mode
                    break
                else:
                    i = i + 26
            except EOFError or IndexError:  ##if user not found add them and their data
                self.parameters.append(self.user)
                self.parameters.append(self.entry_Upperlim.get())
                self.parameters.append(self.entry_Lowerlim.get())
                self.parameters.append(self.entry_Sensor_Rate.get())
                self.parameters.append(self.entry_AV_Delay.get())
                self.parameters.append(self.entry_Dyn_AV_Delay.get())
                self.parameters.append(self.entry_AV_Delay_Off1.get())
                self.parameters.append(self.entry_Atr_Amp.get())
                self.parameters.append(self.entry_Vent_Amp.get())
                self.parameters.append(self.entry_Atr_Pulse.get())
                self.parameters.append(self.entry_Vent_Pulse.get())
                self.parameters.append(self.entry_Vent_Sens.get())
                self.parameters.append(self.entry_Atr_Sens.get())
                self.parameters.append(self.entry_VRP.get())
                self.parameters.append(self.entry_ARP.get())
                self.parameters.append(self.entry_PVARP.get())
                self.parameters.append(self.entry_PVARP_Ext.get())
                self.parameters.append(self.entry_Hyst.get())
                self.parameters.append(self.entry_Rate_Smooth.get())
                self.parameters.append(self.entry_ATR_Dur.get())
                self.parameters.append(self.entry_ATR_Fallback_Mode.get())
                self.parameters.append(self.entry_Act_Thres.get())
                self.parameters.append(self.entry_React_Time.get())
                self.parameters.append(self.entry_Resp_Fact.get())
                self.parameters.append(self.entry_Recv_Time.get())
                self.parameters.append(self.mode)
                break
            except IndexError:  ##here we have the parameters and there bounds, just copy the if statement into the proper location,
                ## make sure each screen only shows the ones it needs for the desired mode
                self.parameters.append(self.user)
                if int(self.entry_Upperlim.get()) < 100 and int(self.entry_Upperlim.get()) > int(
                        self.entry_Lowerlim.get()):
                    self.parameters.append(self.entry_Upperlim.get())
                if int(self.entry_Lowerlim.get()) < int(self.entry_Upperlim.get()) and int(
                        self.entry_Lowerlim.get()) >= 60:
                    self.parameters.append(self.entry_Lowerlim.get())
                # if int(self.entry_Sensor_Rate.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Sensor_Rate.get()) ##sensor rate range between TBD
                if int(self.entry_AV_Delay.get()) <= 300 and int(self.entry_AV_Delay.get()) >= 150:
                    self.parameters.append(self.entry_AV_Delay.get())  ## between 150 - 300 ms
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Dyn_AV_Delay.get()) ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_AV_Delay_Off1.get()) ## TBD
                if int(self.entry_Atr_Amp.get()) <= 80 and int(self.entry_Atr_Amp.get()) >= 30:
                    self.parameters.append(self.entry_Atr_Amp.get())  ## between 30 - 80
                if int(self.entry_Vent_Amp.get()) <= 80 and int(self.entry_Vent_Amp.get()) >= 30:
                    self.parameters.append(self.entry_Vent_Amp.get())  ## same as atr
                if int(self.entry_Atr_Pulse.get()) <= 10 and int(self.entry_Atr_Pulse.get()) >= 1:
                    self.parameters.append(self.entry_Atr_Pulse.get())  ## 1 - 10
                if int(self.entry_Vent_Pulse.get()) <= 10 and int(self.entry_Vent_Pulse.get()) >= 1:
                    self.parameters.append(self.entry_Vent_Pulse.get())  ## 1 - 10
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #    self.parameters.append(self.entry_Vent_Sens.get()) ## between TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Atr_Sens.get()) ## between TBD
                if int(self.entry_VRP.get()) <= 300 and int(self.entry_VRP.get()) >= 150:
                    self.parameters.append(self.entry_VRP.get())  ## between 150 - 300ms
                if int(self.entry_ARP.get()) <= 300 and int(self.entry_ARP.get()) >= 150:
                    self.parameters.append(self.entry_ARP.get())  ## 150  - 300
                if int(self.entry_PVARP.get()) <= 300 and int(self.entry_PVARP.get()) >= 150:
                    self.parameters.append(self.entry_PVARP.get())  ## 150 - 300
                if int(self.entry_PVARP_Ext.get()) <= 300 and int(self.entry_PVARP_Ext.get()) >= 150:
                    self.parameters.append(self.entry_PVARP_Ext.get())  ## 150 - 300 (TBD)
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Hyst.get()) ## baked into the board, not needed
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #    self.parameters.append(self.entry_Rate_Smooth.get()) ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_ATR_Dur.get())    ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_ATR_Fallback_Mode.get())  ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Act_Thres.get()) ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_React_Time.get()) ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Resp_Fact.get()) ## TBD
                # if int(self.entry_Upperlim.get()) < 120 and int(self.entry_Upperlim.get()) >= 60:
                #   self.parameters.append(self.entry_Recv_Time.get()) ## TBD
                self.parameters.append(self.mode)
                break
        all_numbers = True
        for i in range(0, len(self.parameters) - 1):
            if self.parameters[i].isdigit() == False:
                all_numbers = False
        if all_numbers:
            pickle.dump(self.parameters, f)
        else:
            Notifiy_Window.Notify_window(8)
        f.close()

    def old_parameters(self):  ##gets the old parameters
        old_parameters = []
        try:
            f2 = open("Parameters.txt", 'rb')
            while True:
                try:
                    old_parameters = pickle.load(f2)
                except EOFError:
                    break
            f2.close()
        except IOError:
            f2 = open("Parameters.txt", 'w+')
            old_parameters = []
            f2.close()
        return old_parameters

    def write_parameters(self):
        i = 0
        while True:
            try:
                if self.user == self.parameters[i]:
                    if self.mode == self.parameters[i + 25]:
                        self.entry_Upperlim.insert(10, self.parameters[i + 1])
                        self.entry_Lowerlim.insert(10, self.parameters[i + 2])
                        self.entry_Sensor_Rate.insert(10, self.parameters[i + 3])
                        self.entry_AV_Delay.insert(10, self.parameters[i + 4])
                        self.entry_Dyn_AV_Delay.insert(10, self.parameters[i + 5])
                        self.entry_AV_Delay_Off1.insert(10, self.parameters[i + 6])
                        self.entry_Atr_Amp.insert(10, self.parameters[i + 7])
                        self.entry_Vent_Amp.insert(10, self.parameters[i + 8])
                        self.entry_Atr_Pulse.insert(10, self.parameters[i + 9])
                        self.entry_Vent_Pulse.insert(10, self.parameters[i + 10])
                        self.entry_Vent_Sens.insert(10, self.parameters[i + 11])
                        self.entry_Atr_Sens.insert(10, self.parameters[i + 12])
                        self.entry_VRP.insert(10, self.parameters[i + 13])
                        self.entry_ARP.insert(10, self.parameters[i + 14])
                        self.entry_PVARP.insert(10, self.parameters[i + 15])
                        self.entry_PVARP_Ext.insert(10, self.parameters[i + 16])
                        self.entry_Hyst.insert(10, self.parameters[i + 17])
                        self.entry_Rate_Smooth.insert(10, self.parameters[i + 18])
                        self.entry_ATR_Dur.insert(10, self.parameters[i + 19])
                        self.entry_ATR_Fallback_Mode.insert(10, self.parameters[i + 20])
                        self.entry_Act_Thres.insert(10, self.parameters[i + 21])
                        self.entry_React_Time.insert(10, self.parameters[i + 22])
                        self.entry_Resp_Fact.insert(10, self.parameters[i + 23])
                        self.entry_Recv_Time.insert(10, self.parameters[i + 24])

                        break
                    else:
                        break
                else:
                    i = i + 26
            except IndexError:
                break
            except TypeError:
                break