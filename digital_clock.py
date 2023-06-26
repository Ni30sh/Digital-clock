from tkinter import *
import datetime


def date_time():
    time = datetime.datetime.now()
    hours = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    ampm = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    date_lab.config(text=date)
    month_lab.config(text=month)
    year_lab.config(text=year)
    day_lab.config(text=day)
    clock_hr.config(text=hours)
    clock_min.config(text=min)
    clock_sec.config(text=sec)
    ampm_clock.config(text=ampm)

    clock_hr.after(200, date_time)



root = Tk()
root.geometry("820x550+400+80")
root.title("Digital Clock")
root.config(bg="yellow")
########################################################################################################

frame_ln = Label(root,text="CLOCK",font=("chillers",23,"bold"),bg="yellow")
frame_ln.place(x=320,y=0,height=50,width=200)

freme_lab1 = Frame(root,width=820,height=30,bg="black")
freme_lab1.place(x=0,y=90)
freme_lab2 = Frame(root,width=820,height=30,bg="black")
freme_lab2.place(x=0,y=130)
freme_lab3 = Frame(root,width=820,height=30,bg="black")
freme_lab3.place(x=0,y=170)
freme_lab4 = Frame(root,width=820,height=30,bg="black")
freme_lab4.place(x=0,y=210)
freme_lab5 = Frame(root,width=820,height=30,bg="black")
freme_lab5.place(x=0,y=250)
freme_lab6 = Frame(root,width=820,height=30,bg="black")
freme_lab6.place(x=0,y=290)
freme_lab7 = Frame(root,width=820,height=30,bg="black")
freme_lab7.place(x=0,y=330)
freme_lab8 = Frame(root,width=820,height=30,bg="black")
freme_lab8.place(x=0,y=370)
freme_lab9 = Frame(root,width=820,height=30,bg="black")
freme_lab9.place(x=0,y=410)

freme_lab = Frame(root,width=720,height=450,bg="black")
freme_lab.place(x=45,y=45)

clock_hr = Label(freme_lab, text="00", font=("times", 70,"bold"),anchor="center",background="black",foreground="red")
clock_hr.place(x=100, y=70, height=100, width=120)
Frame(freme_lab,width=13,height=13,bg="red").place(x=237,y=135)
Frame(freme_lab,width=13,height=13,bg="red").place(x=237,y=103)
Label(freme_lab,width=11,height=1,bg="black",text="HOUR",fg="white",font=("chiller",12,"bold")).place(x=100,y=187)

clock_min = Label(freme_lab, text="00", font=("times", 70, "bold"),anchor="center",background="black", foreground="red")
clock_min.place(x=270, y=70, height=100, width=120)
Frame(freme_lab,width=13,height=13,bg="red").place(x=405,y=135)
Frame(freme_lab,width=13,height=13,bg="red").place(x=405,y=103)
Label(freme_lab,width=11,height=1,bg="black",text="MINUTES",fg="white",font=("chiller",12,"bold")).place(x=270,y=187)

clock_sec = Label(freme_lab, text="00", font=("times", 70, "bold"),anchor="center",background="black", foreground="red")
clock_sec.place(x=440, y=70, height=100, width=120)
Label(freme_lab,width=11,height=1,bg="black",text="SECOND",fg="white",font=("chiller",12,"bold")).place(x=440,y=187)

ampm_clock = Label(freme_lab, text="AM", font=("times", 19, "bold"),anchor="center",background="black", foreground="red")
ampm_clock.place(x=570, y=135, height=34, width=45)
Label(freme_lab,width=5,height=1,bg="black",text="AM/PM",fg="white",font=("chiller",12,"bold")).place(x=570,y=187)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


date_lab = Label(freme_lab, text="00", font=("times", 70,"bold"), anchor="center", background="black", foreground="red")
date_lab.place(x=80, y=240, height=100, width=120)
Frame(freme_lab, width=20, height=10, bg="red").place(x=220, y=290)
Label(freme_lab,width=11,height=1,bg="black",text="DATE",fg="white",font=("chiller",12,"bold")).place(x=80,y=350)


month_lab = Label(freme_lab, text="00", font=("times", 70, "bold"),anchor="center", background="black", foreground="red")
month_lab.place(x=260, y=240, height=100, width=120)
Frame(freme_lab, width=20, height=10, bg="red").place(x=397,y=290)
Label(freme_lab,width=11,height=1,bg="black",text="MONTH",fg="white",font=("chiller",12,"bold")).place(x=260,y=350)

year_lab = Label(freme_lab, text="00", font=("times", 70, "bold"),anchor="center", background="black", foreground="red")
year_lab.place(x=430, y=240, height=100, width=120)
Label(freme_lab,width=11,height=1,bg="black",text="YEAR",fg="white",font=("chiller",12,"bold")).place(x=430,y=350)



day_lab = Label(freme_lab, text="00", font=("times", 30, "bold"), anchor="center", background="black", foreground="red")
day_lab.place(x=570, y=300, height=40, width=90)
Label(freme_lab,width=8,height=1,bg="black",text="DAY",fg="white",font=("chiller",12,"bold")).place(x=570,y=350)

date_time()

root.mainloop()
