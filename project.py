import threading
from continuous_threading import PeriodicThread

from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk,StringVar

import serial
import time
ser = serial.Serial("COM2",9600)
if not(ser.is_open):
        ser.open()    
time.sleep(1)

import line_api
mytoken = '25DlrgHR5MEVMYbDtEuYSDAsh8l41DhEV1Q8hD1kay0'
import ST
notify = ["9:25-12:05","13:00-15:40","15:45-18:25"]
notify_tt = ["20:40:00","20:41:00","20:42:00"]
t={}
sub=[]
n,s,d=False,False,False
print("Running")

def set_line():
        global n
        n=not(n)
        if(n==True):
                ser.write(str.encode('N1'))
                print('Line ON')
        else:
                ser.write(str.encode('N0'))
                print('Line OFF')
def set_sound():
        global s
        s=not(s)
        if(s==True):
                ser.write(str.encode('S1'))
                print('Sound ON')
        else:
                ser.write(str.encode('S0'))
                print('Sound OFF')
def set_lcd():
        global d
        d=not(d)
        if(d==True):
                ser.write(str.encode('D1'))
                print('LCD ON')
        else:
                ser.write(str.encode('D0'))
                print('LCD OFF')
def save():
        print('save')
        global t
        t={'Mon':[en0.get(),en1.get(),en2.get()],
        'Tue':[en3.get(),en4.get(),en5.get()],
        'Wed':[en6.get(),en7.get(),en8.get()],
        'Thu':[en9.get(),en10.get(),en11.get()],
        'Fri':[en12.get(),en13.get(),en14.get()]}
        print(t)
        dt = time.localtime()
        D = time.strftime('%a',dt)
        global sub
        sub=list(t.get(D))
        print(sub)
        
def clear():
        print('clear')
        global t
        t={}
        print(t)
        
def check_time():
        dt = time.localtime()    
        T = "{:02d}:{:02d}:{:02d}".format(dt[3],dt[4],dt[5])
        i=4
        try:
                if(notify_tt[0] == T)and(sub[0]!=''):
                        i=0
                if(notify_tt[1] == T)and(sub[1]!=''):
                        i=1
                if(notify_tt[2] == T)and(sub[2]!=''):
                        i=2
        except:
                i=4
        if(i<3):
                lcd(i)
                st(i)
                line(i)
         
def st(i):
        if(s==True):
                ST.tts('อีก10นาทีคุณมีเรียน '+str(sub[i])+' เวลา '+notify[i],'th')
def line(i):
        if(n==True):
                line_api.lineNotify('อีก10นาทีคุณมีเรียน '+str(sub[i])+' เวลา '+notify[i],mytoken)
                line_api.notifySticker(161,2,mytoken)
def lcd(i):
        dt = time.localtime()
        D = time.strftime('%a',dt)
        if(d==True):
                ser.write(str.encode('L1:'+D+'  '+notify[i]))
                time.sleep(3)
                ser.write(str.encode('L2:'+str(sub[i])))

style = Style(theme="superhero")
window = style.master
window.title("LabMicro")
window.geometry("630x600")

lb1 = ttk.Label(window,text="Notify",font=("Helvetica 30 bold"),foreground='#FA9F42')
lb1.place(x=40,y=30,width=120)
fm=ttk.Labelframe(window, text="Select Mode",padding=10)
fm.pack(padx=0,pady=(20,10),fill='y',expand='no')
style.configure("Roundtoggle.Toolbutton",font=("Helvetica 10"))
bt1 = ttk.Checkbutton(fm,text="Line",style="success.Roundtoggle.Toolbutton",command=set_line).pack(side='left')
bt2 = ttk.Checkbutton(fm,text="LCD",style="Roundtoggle.Toolbutton",command=set_lcd).pack(side='left')
bt3 = ttk.Checkbutton(fm,text="Sound",style="info.Roundtoggle.Toolbutton",command=set_sound).pack(side='left')

fs=ttk.Labelframe(window, text="Select Time & Enter Subject",padding=5)
fs.pack(padx=20,pady=0,fill='both')
lb2 = ttk.Label(fs,text="[Time]       9:25-12:05                    13:00-15:40                     15:45-18:25",font=("Helvetica 11"),foreground='#FA9F42')
lb2.pack(fill='x',padx=(20,0)) 
 
f1=ttk.Labelframe(fs, text="Mon",padding=10)
f1.pack(padx=20,pady=0,fill='both')
f2=ttk.Labelframe(fs, text="Tue",padding=10)
f2.pack(padx=20,pady=0,fill='both')
f3=ttk.Labelframe(fs, text="Wed",padding=10)
f3.pack(padx=20,pady=0,fill='both')
f4=ttk.Labelframe(fs, text="Thu",padding=10)
f4.pack(padx=20,pady=0,fill='both')
f5=ttk.Labelframe(fs, text="Fri",padding=10)
f5.pack(padx=20,pady=0,fill='both')

en0=ttk.Entry(f1,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en0.pack(side='left',padx=(20,0))
en1=ttk.Entry(f1,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en1.pack(side='left',padx=(15,0),pady=5)
en2=ttk.Entry(f1,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en2.pack(side='left',padx=(15,0),pady=5)

en3=ttk.Entry(f2,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en3.pack(side='left',padx=(20,0))
en4=ttk.Entry(f2,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en4.pack(side='left',padx=(15,0),pady=5)
en5=ttk.Entry(f2,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en5.pack(side='left',padx=(15,0),pady=5)

en6=ttk.Entry(f3,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en6.pack(side='left',padx=(20,0))
en7=ttk.Entry(f3,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en7.pack(side='left',padx=(15,0),pady=5)
en8=ttk.Entry(f3,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en8.pack(side='left',padx=(15,0),pady=5)

en9=ttk.Entry(f4,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en9.pack(side='left',padx=(20,0))
en10=ttk.Entry(f4,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en10.pack(side='left',padx=(15,0),pady=5)
en11=ttk.Entry(f4,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en11.pack(side='left',padx=(15,0),pady=5)

en12=ttk.Entry(f5,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en12.pack(side='left',padx=(20,0))
en13=ttk.Entry(f5,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en13.pack(side='left',padx=(15,0),pady=5)
en14=ttk.Entry(f5,font=("Helvetica 11"),foreground='black',textvariable=StringVar(),width=17)
en14.pack(side='left',padx=(15,0),pady=5)

style.configure("Outline.TButton",font=("Helvetica 15"))
bt1 = ttk.Button(window,text="Clear",cursor="hand2",style="danger.Outline.TButton",command=clear)
bt1.place(x=420,y=530,width=80)

style.configure("Outline.TButton",font=("Helvetica 15"))
bt1 = ttk.Button(window,text="save",cursor="hand2",style="success.Outline.TButton",command=save)
bt1.place(x=520,y=530,width=80)

PeriodicThread(0.5,check_time).start()

window.mainloop()
