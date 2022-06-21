from msilib import Table
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import datetime as dt
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql


def fun():#db connection
    global mydb2,mycursor
    mydb2=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsYs_tkinter'
        )
    mycursor = mydb2.cursor()
    

# def add_invoice():


        



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


fun()
mycursor.execute('select * from app1_customer ')
customers=mycursor.fetchall()
customers_data=[]
for cus in customers:
    customers_data.append(cus)


mycursor.execute('select * from app1_accounts ')
account=mycursor.fetchall()
account_data=[]
for acc in account:
    account_data.append(acc)

#set today date 
date = dt.datetime.now()
format_date = f"{date:%Y - %d - %m }"
today_date = Label(form_frame, text=format_date, fg="white", bg="black", font=("helvetica", 40))

#company details
user_id=[4]
mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
cmp1=mycursor.fetchone()

# cmp1=[1]

mycursor.execute("SELECT cname,cemail,state FROM app1_company WHERE id_id=%s",(user_id))
cmp_data=mycursor.fetchone()


global select_customer,email,invno,paydate,paymethod,deposit,amount
select_customer = StringVar(form_frame)
email = StringVar(form_frame)
invno = StringVar(form_frame)
paydate = StringVar(form_frame)
paymethod = StringVar(form_frame)
deposit = StringVar(form_frame)
amount = StringVar(form_frame)
drp = StringVar()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=30, pady=30, bd=0, fg="Black", bg="#243e55")
F.place(x=35, y=30, width=1270, height=1950)

label4=Label(F, text="Fin sYs", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=530,y=5)


def get_mail(event):
    # mycursor.execute('select * from app1_customer ')
    # customers=mycursor.fetchall()
    # name=[]
    option=drop12.get()
    x = option.split(" ", 1)
    
    # name.append(option)
    print("wel",x)
    print("wel",option)
    # for custm in customers_data:
    #     print(customers_data)
    #     full_name=custm[2] + custm[3]
    #     if full_name==name[0]:
            # first_name=custm[2]
            # last_name=custm[3]
    mycursor.execute("SELECT * FROM app1_customer where firstname=%s and lastname=%s",(x[0],x[1]))
    table2=mycursor.fetchall()
    for i in table2:
        email.set(i[9])
        # billto.set(i[12:17])

print(cmp1)
select_customer_lab=tk.Label(F,text="Customer",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop12=ttk.Combobox(F,textvariable=drp,font=('times new roman', 11, 'bold'))
# sql = "select firstname from app1_customer"
# mycursor.execute(sql)
# cusna = mycursor.fetchall()
# # value=[]
# # for cuser in cusna:
# #     value.append(cuser[0])

# sql = "select lastname from app1_customer"
# mycursor.execute(sql)
# cusnan = mycursor.fetchall()
# values=[]
# print("json",cusnan)
# for cuser in cusnan:
#     values.append(cuser[0])
# wer = value + values
# print("vis",wer)
# drop1['values']=wer
# print("hhh",values)


value=[]
for cust in  customers_data:
    customer_values=cust[-1]
    
    if customer_values==cmp1[0]:
        value.append((cust[2]+' '+cust[3]))
        drop12['values']=value
    else:
        pass

drop12.bind("<<ComboboxSelected>>",get_mail)
select_customer_lab.place(x=100,y=90)
drop12.place(x=100,y=130,height=40,width=270)



add_custom=Button(F,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command='add_custom')
add_custom.place(x=375,y=130)


label3=Label(F, text="Email", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=90)
label33=Entry(F,bg='#2f516a',fg='#fff',textvariable=email, font=('times new roman', 11, 'bold'))
label33.place(x=450,y=130,height=40,width=300)

label4=Label(F, text="Find by invoice number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=800,y=130,height=40,width=300)


label3=Label(F, text="Payment Date", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=100,y=170)
label33=Entry(F,bg='#2f516a',fg='#fff',textvariable='mployeenumber', font=('times new roman', 11, 'bold'))
label33.place(x=100,y=210,height=40,width=300)



sanitizer1_lbl=tk.Label(F,text="Payment Method",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop1=ttk.Combobox(F,textvariable='accounttype')
drop1['values']=("Cash","Check","Credit Card","Add New")
sanitizer1_lbl.place(x=100,y=250)
drop1.place(x=100,y=290,height=40,width=300)

sanitizer1_lbl=tk.Label(F,text="Deposit To",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop1=ttk.Combobox(F,textvariable='accounttype')
drop1['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund")
sanitizer1_lbl.place(x=800,y=250)
drop1.place(x=800,y=290,height=40,width=270)

add_custom=Button(F,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command='add_custom')
add_custom.place(x=1075,y=290)


label4=Label(F, text="Amount Recieved", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=340)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=800,y=380,height=40,width=300)


label4=Label(F, text="AMOUNT RECIEVED", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=430)
label4=Label(F, text="00", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=470)





# Table

#
label4=Label(F, text="#", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=10,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=10,y=580,height=40,width=50)

label4=Label(F, text="DESCRIPTION", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=75,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=75,y=580,height=40,width=210)

label4=Label(F, text="DUE DATE", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=295,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=295,y=580,height=40,width=210)

label4=Label(F, text="ORIGINAL AMOUNT", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=515,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=515,y=580,height=40,width=210)

label4=Label(F, text="OPEN BALANCE", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=735,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=735,y=580,height=40,width=210)

label4=Label(F, text="PAYMENT", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=955,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=955,y=580,height=40,width=210)







label4=Label(F, text="Amount to Apply", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=750,y=670)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=955,y=670,height=40,width=210)


label4=Label(F, text="Amount to Credit", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=750,y=730)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=955,y=730,height=40,width=210)


root.mainloop()