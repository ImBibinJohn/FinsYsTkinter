from math import prod
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
import mysql.connector as mysql
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import datetime as dt

root = tk.Tk()

root.title("finsYs")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")
wrappen=ttk.LabelFrame(root)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=1345,height=2500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=2400,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="EDIT PAY SLIP", font=('times new roman', 28, 'bold'),padx=525, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=30, pady=30, bd=0, fg="Black", bg="#243e55")
F.place(x=30, y=30, width=1270, height=1950)

label1=Label(F, text="MAP Creations", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=500,y=1)

label2=Label(F, text="Employee Name", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=100,y=90)
label2=Entry(F,bg='#2f516a',fg='#fff')
label2.place(x=100,y=130,height=40,width=300)

label3=Label(F, text="Employee Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=90)
label3=Entry(F,bg='#2f516a',fg='#fff')
label3.place(x=450,y=130,height=40,width=300)

label4=Label(F, text="Designation", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label4=Entry(F,bg='#2f516a',fg='#fff')
label4.place(x=800,y=130,height=40,width=300)

label2=Label(F, text="Pay Peried - From", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=100,y=190)
label2 = DateEntry(F, width= 28, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable='idat1')
label2.place(x=100,y=230)

label3=Label(F, text="To", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=190)
label3 = DateEntry(F, width= 28, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable='dat1')
label3.place(x=450,y=230)

label4=Label(F, text="Date of Payment", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=190)
label4 = DateEntry(F, width= 28, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable='idat1')
label4.place(x=800,y=230)

label1=Label(F, text="Salary Details", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=500,y=400)

label1=Label(F, text="Earnings", font=('times new roman', 17, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=200,y=500)

label1=Label(F, text="Basic Salary", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=40,y=580)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=580,height=40,width=230)

label1=Label(F, text="Dearance Allowance", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=40,y=640)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=640,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=40,y=700,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=700,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=40,y=760,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=760,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=40,y=820,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=820,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=40,y=880,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=880,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=40,y=940,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=940,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=40,y=1000,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=280,y=1000,height=40,width=230)




label1=Label(F, text="Deduction", font=('times new roman', 17, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=850,y=500)

label1=Label(F, text="Provident Fund", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=580)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=940,y=580,height=40,width=230)

label1=Label(F, text="Profession Tax", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=640)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=940,y=640,height=40,width=230)

label1=Label(F, text="ESI", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=640)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=940,y=700,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=700,y=760,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=940,y=760,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=700,y=820,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=940,y=820,height=40,width=230)


label1=Label(F, text="Gross Pay", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1080)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=900,y=1080,height=40,width=270)

label1=Label(F, text="Total Deduction", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1140)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=900,y=1140,height=40,width=270)

label1=Label(F, text="Net Salary", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1200)
label1=Entry(F,bg='#2f516a',fg='#fff')
label1.place(x=900,y=1200,height=40,width=270)

butn1=Button(F, text="Update Payslip", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=500,y=1350)



wrappen.pack(fill='both',expand='yes',)




root.mainloop()

