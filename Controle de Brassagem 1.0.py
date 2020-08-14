
# -*- coding: utf-8 -*-
"""

This Software is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation.
  
Created on Fri OCT 11 10:41:02 2019

@author: Igor Arantes
e-mail igor.l.arantes@gmail.com

"""


from tkinter import *
from tkinter import ttk
from datetime import date
import matplotlib.pyplot as plt
import csv


  
#variable Declaration
timem = 0
mm ="00"
ss ="00"

brew =False
timestamp = mm+":"+ss
graphx=[]
graphy=[]
Window_Program = Tk()
Window_Program.geometry("400x600")
Window_Program.title("Controle de Brassagem")
Serial_Command = "800"

fontePadrao = ("Arial", "10")

tempstep1lb= Label(Window_Program,text="Temp da Rampa 1:")
tempstep1lb["font"]=fontePadrao
tempstep1lb.place(height=25, relx=0.01, rely=0.3)
tempstep1en=Entry(Window_Program)
tempstep1en["font"] = fontePadrao
tempstep1en.place(height=25, relx=0.3, rely=0.3,width=40)
               
tempstep2lb= Label(Window_Program,text="Temp da Rampa 2:")
tempstep2lb["font"]=fontePadrao
tempstep2lb.place(height=25, relx=0.01, rely=0.35)
tempstep2en=Entry(Window_Program)
tempstep2en["font"] = fontePadrao
tempstep2en.place(height=25, relx=0.3, rely=0.35,width=40)

timestep2lb= Label(Window_Program,text="Tempo 2:")
timestep2lb["font"]=fontePadrao
timestep2lb.place(height=25, relx=0.4, rely=0.35)
timestep2en=Entry(Window_Program)
timestep2en["font"] = fontePadrao
timestep2en.place(height=25, relx=0.55, rely=0.35,width=40) 

tempstep3lb= Label(Window_Program,text="Temp da Rampa 3:")
tempstep3lb["font"]=fontePadrao
tempstep3lb.place(height=25, relx=0.01, rely=0.4)
tempstep3en=Entry(Window_Program)
tempstep3en["font"] = fontePadrao
tempstep3en.place(height=25, relx=0.3, rely=0.4,width=40)

timestep3lb= Label(Window_Program,text="Tempo 3:")
timestep3lb["font"]=fontePadrao
timestep3lb.place(height=25, relx=0.4, rely=0.4)
timestep3en=Entry(Window_Program)
timestep3en["font"] = fontePadrao
timestep3en.place(height=25, relx=0.55, rely=0.4,width=40) 

tempstep4lb= Label(Window_Program,text="Temp da Rampa 4:")
tempstep4lb["font"]=fontePadrao
tempstep4lb.place(height=25, relx=0.01, rely=0.45)
tempstep4en=Entry(Window_Program)
tempstep4en["font"] = fontePadrao
tempstep4en.place(height=25, relx=0.3, rely=0.45,width=40)

timestep4lb= Label(Window_Program,text="Tempo 4:")
timestep4lb["font"]=fontePadrao
timestep4lb.place(height=25, relx=0.4, rely=0.45)
timestep4en=Entry(Window_Program)
timestep4en["font"] = fontePadrao
timestep4en.place(height=25, relx=0.55, rely=0.45,width=40) 

def StartBoiler():
    boiler="ON"
    mixer="OFF"
    s=open('sets.temp', 'w')
    s.write(boiler+"\n"+mixer)
    s.close()   
    
def StopBoiler():
    boiler="OFF"
    mixer="OFF"
    s=open('sets.temp', 'w')
    s.write(boiler+"\n"+mixer)
    s.close()       

     
def StartBrew(brew = False,sec = None):
    if brew == False:
        sec = int(timefield.get())*60
        timestamp['text'] = '00:00'
        tempstamp['text'] = "--ºC"
    if sec == 0:
        timestamp['text'] = '00:00'
        tempstamp['text'] = "--ºC"
        boiler="OFF"
        mixer="OFF"
        s=open('sets.temp', 'w')
        s.write(boiler+"\n"+mixer)
        s.close()
        
        plt.rcParams['figure.figsize'] = (50,10)
        plt.title(nome_receita.get())
        plt.xlabel("Tempo mm:ss")
        plt.ylabel("Temperatura ºC")
        plt.plot(graphx, graphy)
        date_now = date.today()
        plt.savefig(str(nome_receita.get())+str(date_now)+".png")
        plt.figure(1)
        with open((str(nome_receita.get())+str(date_now)+".csv"), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=';')
            for i in range(len(graphx)):
                csvwriter.writerow([graphx[i]]+[graphy[i]])
                
    else:
        
        
        #temp Reading
        f=open('temp.temp', 'r')
        temperature=f.readline()
        f.close()
        
        
        graphy.append(round(float(temperature)))
        
        temp2label = temperature.split(".")
        tempstamp['text'] = temp2label[0]+"ºC"
        
        
        #Time Loop
        mm=sec//60
        ss=int(round(((sec/60-sec//60)*60),2))
        sec = sec - 1
        timestamp['text'] = str(mm)+":"+str(ss)
        
        
        graphx.append(str(mm)+":"+str(ss))
        


        
        #Reading and setting conditional operations running
        tempindex = tempsteps.current()
        tempstep1= int(tempstep1en.get())
        
        try:
            timestep2= int(timestep2en.get())
        except:
            timestep2 = 0
            
        try:            
            tempstep2= int(tempstep2en.get())
        except:
            tempstep2=0
        
        try:             
            timestep3= int(timestep3en.get())
        except:
            timestep3=0
        try:
            tempstep3= int(tempstep3en.get())            
        except:
            tempstep3=0
            
        try:   
            tempstep3= int(tempstep3en.get())            
        except:
            tempstep3=0
            
        try:     
            timestep4= int(timestep4en.get())
        except:
            timestep4=0
        
        try:
            tempstep4= int(tempstep4en.get())
        except:
            tempstep4=0
        
        if int(tempindex) ==0:
            if float(temperature)<= int(tempstep1):
                boiler="ON"
                mixer="ON"
                s=open('sets.temp', 'w')
                s.write(boiler+"\n"+mixer)
                s.close()
            else:
                boiler="OFF"
                mixer="OFF"
                s=open('sets.temp', 'w')
                s.write(boiler+"\n"+mixer)
                s.close()
                
        if int(tempindex) ==1:
            
            timestep2sec=timestep2*60
            
            if sec >= timestep2sec:
                if float(temperature)<= int(tempstep1):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
            else:
                if float(temperature)<= int(tempstep2):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF" 
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()

        if int(tempindex) ==2:             
            
            timestep2sec=timestep2*60
            timestep3sec=timestep3*60
            
            if sec >= timestep2sec:
                if float(temperature)<= int(tempstep1):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()

            if sec >timestep3sec and sec < timestep2sec:
                if float(temperature)<= int(tempstep2):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
            else:
                if float(temperature)<= int(tempstep3):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                    
        if int(tempindex) ==3:         
             
            
            timestep2sec=timestep2*60
            timestep3sec=timestep3*60
            timestep4sec=timestep4*60
            
            if sec > timestep2sec:
                if float(temperature)<= int(tempstep1):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()           
            if sec >timestep3sec and sec < timestep2sec:
                if float(temperature)<= int(tempstep2):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"   
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
            if sec >timestep4sec and sec < timestep3sec:
                if float(temperature)<= int(tempstep3):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                    
            else:
                if float(temperature)<= int(tempstep4):
                    boiler="ON"
                    mixer="ON"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()
                else:
                    boiler="OFF"
                    mixer="OFF"
                    s=open('sets.temp', 'w')
                    s.write(boiler+"\n"+mixer)
                    s.close()

        
        
        timestamp.after(1000, lambda : StartBrew(True,sec))          
        

  
#Recipe name container
titulo = Label(Window_Program, text="Nome da Receita")
titulo["font"] = ("Arial", "10", "bold")
titulo.place(height=25, relx=0.01, rely=0.01)
 
nome_receita = Entry(Window_Program)
nome_receita["font"] = fontePadrao
nome_receita.place(height=20, relx=0.01, rely=0.05, width=200)

  
  
#Timer Config
timelabel = Label(Window_Program, text="Tempo de Brassagem:")
timelabel["font"] = ("Arial", "10")
timelabel.place(height=20, relx=0.01, rely=0.1)
  
timefield = Entry(Window_Program)
timefield["font"] = fontePadrao
timefield.place(height=20, relx=0.012,rely=0.135,width=45)
timeun = Label(Window_Program, text="Minutos")
timeun["font"] = ("Arial", "10")
timeun.place(height=20, relx=0.06,rely=0.135)
  
 
#Temp Config
templb = Label(Window_Program, text="Rampas de Temperatura:")
templb["font"] = fontePadrao
templb.place(height=25, relx=0.01, rely=0.2)

tempsteps = ttk.Combobox(Window_Program,values=["Rampa Unica","2 Rampas","3 Rampas","4 Rampas"])
tempsteps.place(height=25, relx=0.01, rely=0.25)
tempsteps.current(0)
 
 #Timer Panel
timestamp = Label(Window_Program, fg="blue")
timestamp["font"] =("Arial Narrow", "35",)
timestamp.place(height=60, relx=0.4, rely=0.78)

 #Temp Panel
tempstamp = Label(Window_Program, fg="blue")
tempstamp["font"] =("Arial Narrow", "35",)
tempstamp.place(height=60, relx=0.4, rely=0.68)
    
   
#Start Button   
startbrew = Button(Window_Program, text="Iniciar Brassagem",command=StartBrew)
startbrew["font"] = ("Arial", "10","bold")
startbrew["foreground"] = ("blue")
startbrew["width"] = 20
startbrew.place(height=25, relx=0.3, rely=0.9)

#Start Boiler Button 

startbrew = Button(Window_Program, text="Ligar Aquecedor",command=StartBoiler)
startbrew["font"] = ("Arial", "10","bold")
startbrew["foreground"] = ("red")
startbrew["width"] = 16
startbrew.place(height=20, relx=0.05, rely=0.52)

#Stop Boiler Button 

startbrew = Button(Window_Program, text="Desligar Aquecedor",command=StopBoiler)
startbrew["font"] = ("Arial", "10","bold")
startbrew["foreground"] = ("red")
startbrew["width"] = 16
startbrew.place(height=20 ,relx=0.05, rely=0.57)





def OpenConfig():
    New_window = Window_Program.Toplevel(root)
       
        



    



#Application(Window_Program)
Window_Program.mainloop()