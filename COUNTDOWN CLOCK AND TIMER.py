from tkinter import *
from tkinter import messagebox
import time
#setting the window
window=Tk()
window.title("Countdown clock and Timer")
window.geometry("600x400")
window.config(bg="black")
#Adding a caption to the window
lbl=Label(window,text="Countdown clock and Timer",fg="white",bg="red",font=("Helvetica",25,"bold"))
lbl.place(x=100,y=30)
lbl=Label(window, font =("Helvetica",20,"bold"), text = 'Current Time:', bg = 'green',fg="black")
lbl.place(x = 120 ,y = 90)
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(window, font =("Helvetica",20,"bold"), text = ' ', bg = 'green',fg="black")
curr_time.place(x = 320 , y = 90)
clock()
#Declaration of variables and setting the default value to 0
hrs=StringVar()
mins=StringVar()
sec=StringVar()
hrs.set("00")
mins.set("00")
sec.set("00")
#Taking input from the user
hrsEntry=Entry(window,textvariable=hrs,width=3,fg="white",bg="blue",font=("Garamound",24,"bold"))
hrsEntry.place(x=210,y=160)
minEntry=Entry(window,textvariable=mins,width=3,fg="white",bg="blue",font=("Garamound",24,"bold"))
minEntry.place(x=280,y=160)
secEntry=Entry(window,textvariable=sec,width=3,fg="white", bg="blue",font=("Garamound",24,"bold"))
secEntry.place(x=350,y=160)
#Countdown function
def countdownTimer():
    times=int(hrs.get())*3600+int(mins.get())*60+int(sec.get())
    while times>-1:
        minute,second=divmod(times,60)
        hour=0
        if minute>60:
            hour,minute=divmod(minute,60)
        hrs.set("{0:2d}".format(hour))
        mins.set("{0:2d}".format(minute))
        sec.set("{0:2d}".format(second))
#Updating the the tk window everytime after decrementing the time value every time
        window.update()
        time.sleep(1)
#When the time value=0,a message box will pop up with a sound
        if (times==0):
            messagebox.showinfo("Time up!")
        times-=1
        
btn=Button(window,text="Set the timer",bd=5,command=countdownTimer)
btn.place(x=270,y=240)
window.mainloop()
