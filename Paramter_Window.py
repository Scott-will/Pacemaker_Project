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
# import Notify_Window          #
# import serial                 #
# import Serial_com             #
# import time                   #
#################################
from tkinter import *
import tkinter as tk
import pickle
import Login_Screen
import Pacing_Screen
import Notifiy_Window

class Parameter_Window:
    def __init__(self, master, mode, user):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root.pack()
        self.mode = mode
        self.user = user
        self.master = master
        self.parameters = self.old_parameters()



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

        elif self.mode == 5:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DOO Pacing Mode")
            self.label_title2.config(font=("Courier", 13))
            self.label_title2.place(x=120, y=145)

            self.common(140, 172, 140, 222, 50, 220, 50, 170, 300, 50, 300, 350, 300, 300, 300, 90)

            self.label.AV_del = Label(self.frame_root,text="Fixed Av Delay:")
            self.label.AV_del.place(x=57, y=272)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=45, y=322)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=27, y=372)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=40, y=422)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventrical Pulse Width:")
            self.label_Vent_Pulse.place(x=21, y=472)

            self.entry_AV_del = Entry(self.frame_root)
            self.entry_AV_del.place(x=140, y=272)
            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=140, y=322)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=140, y=372)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=140, y=422)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=140, y=472)

        elif self.mode == 6:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=180, y=145)

            self.common(145, 172, 145, 222, 50, 172, 50, 222, 430, 60, 230, 450, 300, 450, 430, 100)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=50, y=270)
            self.label_AV_Delay = Label(self.frame_root, text="Fixed AV Delay:")
            self.label_AV_Delay.place(x=58, y=320)

            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=300, y=170)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=283, y=220)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=292, y=270)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=278, y=320)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=58, y=370)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=50, y=420)
            self.label_Act_Thres = Label(self.frame_root, text="Acticity Threshold:")
            self.label_Act_Thres.place(x=295, y=372)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=315, y=422)

            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=145, y=272)
            self.entry_AV_Delay = Entry(self.frame_root)
            self.entry_AV_Delay.place(x=145, y=322)

            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=400, y=172)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=400, y=222)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=400, y=272)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=400, y=322)

            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=400, y=372)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=400, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=145, y=370)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=145, y=420)



        elif self.mode == 7:
            self.background_image = tk.PhotoImage(file="backgroundpacing2.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DDDR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=650, y=130)

            self.Back_image = tk.PhotoImage(file="Back.png")
            self.button_back = Button(self.frame_root, image=self.Back_image)
            self.button_back.config(command=self.from_Parameter_Window)
            self.button_back.place(x=1400, y=35)

            self.button_ok = Button(self.frame_root, text="     Ok     ")
            self.button_ok.config(command=self.Ok)
            self.button_apply = Button(self.frame_root, text="    Apply    ")
            self.button_apply.config(command=self.Apply)
            self.button_apply.place(x=1100, y=250)
            self.button_ok.place(x=1100, y=300)

            self.signout_image = tk.PhotoImage(file="signout.png")
            self.button_signout = Button(self.frame_root, image=self.signout_image)
            self.button_signout.config(command=self.To_login)
            self.button_signout.place(x=1400, y=75)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=125, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=125, y=222)
            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=125, y=272)
            self.entry_AV_Delay = Entry(self.frame_root)
            self.entry_AV_Delay.place(x=125, y=322)
            self.entry_Dyn_AV_Delay = Entry(self.frame_root)
            self.entry_Dyn_AV_Delay.place(x=125, y=372)
            self.entry_AV_Delay_Off1 = Entry(self.frame_root)
            self.entry_AV_Delay_Off1.place(x=125, y=422)

            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=400, y=172)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=400, y=222)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=400, y=272)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=400, y=322)
            self.entry_Vent_Sens = Entry(self.frame_root)
            self.entry_Vent_Sens.place(x=400, y=372)
            self.entry_Atr_Sens = Entry(self.frame_root)
            self.entry_Atr_Sens.place(x=400, y=422)

            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=650, y=172)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=650, y=222)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=650, y=272)
            self.entry_PVARP_Ext = Entry(self.frame_root)
            self.entry_PVARP_Ext.place(x=650, y=322)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=650, y=372)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=650, y=422)

            self.entry_ATR_Dur = Entry(self.frame_root)
            self.entry_ATR_Dur.place(x=920, y=172)
            self.entry_ATR_Fallback_Mode = Entry(self.frame_root)
            self.entry_ATR_Fallback_Mode.place(x=920, y=222)
            self.entry_ATR_Fallback_time = Entry(self.frame_root)
            self.entry_ATR_Fallback_time.place(x=920, y=272)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=920, y=322)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=920, y=372)

            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=30, y=170)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=30, y=220)
            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=30, y=270)
            self.label_AV_Delay = Label(self.frame_root, text="Fixed AV Delay:")
            self.label_AV_Delay.place(x=30, y=320)
            self.label_Dyn_AV_Delay = Label(self.frame_root, text="Dynamic Av Delay:")
            self.label_Dyn_AV_Delay.config(font=("Times", 8))
            self.label_Dyn_AV_Delay.place(x=25, y=370)
            self.label_Sen_AV_Delay_Off1 = Label(self.frame_root, text="Sensed AV:")
            self.label_Sen_AV_Delay_Off2 = Label(self.frame_root, text="Delay Offset")
            self.label_Sen_AV_Delay_Off1.place(x=55, y=420)
            self.label_Sen_AV_Delay_Off2.place(x=50, y=440)

            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=300, y=170)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=283, y=220)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=292, y=270)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=276, y=320)
            self.label_Vent_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Vent_Sens.place(x=288, y=370)
            self.label_Atr_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Atr_Sens.place(x=303, y=420)

            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=610, y=170)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=610, y=220)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=600, y=270)
            self.label_PVARP_Ext = Label(self.frame_root, text="PVARP Extension:")
            self.label_PVARP_Ext.place(x=550, y=320)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=585, y=370)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=552, y=420)

            self.label_ATR_Dur = Label(self.frame_root, text="ATR Duration:")
            self.label_ATR_Dur.place(x=833, y=170)
            self.label_ATR_Fallback_Mode = Label(self.frame_root, text="ATR Fallback Mode:")
            self.label_ATR_Fallback_Mode.place(x=805, y=220)
            self.label_ATR_Fallback_time = Label(self.frame_root, text="ATR Fallback Time:")
            self.label_ATR_Fallback_time.place(x=810, y=270)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=810, y=320)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=830, y=370)

        elif self.mode == 8:
            self.background_image = tk.PhotoImage(file="backgroundpacing3.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="AAIR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=320, y=120)

            self.common(145, 172, 145, 222, 50, 172, 50, 222, 750, 30, 330, 460, 400, 460, 750, 70)

            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=145, y=272)
            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=145, y=322)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=145, y=372)
            self.entry_Atr_Sens = Entry(self.frame_root)
            self.entry_Atr_Sens.place(x=145, y=422)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=50, y=272)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=50, y=322)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=45, y=372)
            self.label_Atr_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Atr_Sens.place(x=50, y=422)

            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=450, y=172)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=450, y=222)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=450, y=272)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=450, y=322)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=450, y=372)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=450, y=422)

            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=413, y=172)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=400, y=222)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=385, y=272)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=355, y=322)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=347, y=372)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=365, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=710, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=710,y=222)

            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=621, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=615, y=222)

        elif self.mode == 9:
            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="AOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=160, y=145)

            self.common(125, 172, 125, 222, 30, 220, 30, 170, 400, 50, 350, 370, 350, 320, 400, 90)

            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=125, y=272)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=125, y=322)
            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=125, y=372)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=125, y=422)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=25, y=272)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=25, y=322)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=20, y=372)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=20, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=360, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=360, y=222)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=360, y=272)


            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=270, y=272)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=270, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=265, y=222)

        elif self.mode == 10:
            self.background_image = tk.PhotoImage(file="backgroundpacing3.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="VVIR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=300, y=120)

            self.common(150, 172, 150, 222, 55, 220, 55, 170, 700, 30, 700, 370, 700, 320, 700, 70)

            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=150, y=272)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=150, y=322)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=150, y=372)
            self.entry_Vent_Sens = Entry(self.frame_root)
            self.entry_Vent_Sens.place(x=150, y=422)


            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=55, y=272)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=35, y=323)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=27, y=372)
            self.label_Vent_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Vent_Sens.place(x=38, y=422)

            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=390, y=172)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=390, y=220)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=390, y=272)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=390, y=322)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=390, y=372)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=390, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=700, y=172)

            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=360, y=172)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=327, y=222)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=295, y=272)
            self.label_Act_Thres = Label(self.frame_root, text="Acticity Threshold:")
            self.label_Act_Thres.place(x=285, y=322)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=305, y=372)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=295, y=422)

            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=620, y=172)

        elif self.mode == 11:
            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="VOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=160, y=145)

            self.common(125, 172, 125, 222, 30, 220, 30, 170, 400, 50, 350, 370, 350, 320, 400, 90)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=30, y=272)
            self.label_Vent_Amp = Label(self.frame_root, text="Vent Amplitude:")
            self.label_Vent_Amp.place(x=30, y=323)
            self.label_Vent_Pulse = Label(self.frame_root, text="VentrPulse Width:")
            self.label_Vent_Pulse.place(x=27, y=372)
            self.label_Act_Thres = Label(self.frame_root, text="Acticity Threshold:")
            self.label_Act_Thres.place(x=20, y=422)


            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=125, y=272)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=125, y=322)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=125, y=372)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=125, y=422)


            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=260, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=257, y=222)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=260, y=272)

            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=350, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=350, y=222)
            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=350, y=272)

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
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user)

    def To_login(self):
        self.frame_root.pack_forget()
        self.login = Login_Screen.Login_Window(self.master)


    def Apply(self):  # Apply will save the #parameters in the entry fields and return to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user)
        # Add code here to also save the parameters

        self.save_parameters()

    def Ok(self):  # Ok will only save the parameters in the entry fields
        self.save_parameters()  # Just random code so pycharm doesnt freak out that there is nothing in the function
        # add code here to save the parameters

    def save_parameters(self):  ##saves parameters
        f = open("Parameters.txt", 'wb')
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