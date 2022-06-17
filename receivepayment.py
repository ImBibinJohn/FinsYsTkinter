import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
# import mysql.connector as mysql


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

full_frame=Frame(mycanvas,width=1345,height=2550,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas,bg="white")
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=2550,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

wrappen.pack(fill='both',expand='yes',)

tit = Label(heading_frame, text="RECIEVE PAYMENT", font=('times new roman', 25, 'bold'),padx=500, pady=2, bd=5, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=30, pady=30, bd=0, fg="Black", bg="#243e55")
F.place(x=35, y=30, width=1270, height=1950)

select_customer_lab=tk.Label(F,text="Select Customer",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop1=ttk.Combobox(F,textvariable = 'select_customer')

value=[]
# for cust in  customers_data:
#     customer_values=cust[-1]
    
#     if customer_values==cmp1[0]:
#         value.append((cust[2]+cust[3]))
#         drop1['values']=value
        
#     else:
#         messagebox.showerror('error', 'invalid data')

# drop1.bind("<<ComboboxSelected>>",get_email)
select_customer_lab.place(x=100,y=90)
drop1.place(x=100,y=130,height=40,width=270)

add_custom=Button(F,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command='add_custom')
add_custom.place(x=375,y=130)


label3=Label(F, text="Employee Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=90)
label33=Entry(F,bg='#2f516a',fg='#fff',textvariable='mployeenumber', font=('times new roman', 11, 'bold'))
label33.place(x=450,y=130,height=40,width=300)

label4=Label(F, text="Designation", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=800,y=130,height=40,width=300)


label3=Label(F, text="Employee Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=90)
label33=Entry(F,bg='#2f516a',fg='#fff',textvariable='mployeenumber', font=('times new roman', 11, 'bold'))
label33.place(x=450,y=130,height=40,width=300)

label4=Label(F, text="Designation", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=800,y=130,height=40,width=300)

label4=Label(F, text="Designation", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=800,y=130,height=40,width=300)









root.mainloop()