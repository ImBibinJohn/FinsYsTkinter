import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
from datetime import datetime, date, timedelta
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def salespayments():  
    estwin=tk.Tk()
    estwin.title('Sales Records')
    estwin.geometry('1500x1000')
    estwin['bg'] = '#2f516f'
    cid=2
    mycanvas=tk.Canvas(estwin,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(estwin,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1500)
    hf1=tk.Frame(frame,bg='#243e54')
    tk.Label(hf1,text='Receive Payments',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    hf1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.05)
    hf2=tk.Frame(frame,bg='#243e54')
            #customer
    tk.Label(hf2,text='Fin sYs',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.02)     
    def salespaymentscusinput():
        try:
                cur.execute("SELECT firstname,lastname FROM customer")
                val=cur.fetchall()         
                for row in val:
                    tm.append(row[0]+row[1])   
        except:
            pass              
    tm=['Select Customer']
    salespaymentscusinput()      
    tk.Label(hf2,text='Customer',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.11) 
    estcus=ttk.Combobox(hf2,font=('times new roman', 12),values=tm)
    def get_mail(event):
        def des():
            label44tabdescription.delete(0,END)
            email.delete(0,END)
            label44tabduedate.delete(0,END)
            label44taboriginalamount.delete(0,END)
            label44tabopenbalance.delete(0,END)
        des()
        option=estcus.get()
        x = option.split(" ", 1)
        print("boy",option)
        # mycursor.execute("SELECT * FROM app1_customer where firstname=%s and lastname=%s",(x[0],x[1]))
        # table1=mycursor.fetchone()
        # email.set(table1[9])
            # billto.set(i[12:17])
        
        cur.execute("SELECT descrip,email,duedate,orgamt,openbal FROM payment where customer=%s ",([option]))
        table2=cur.fetchone() 
        email.insert(0,table2[1])
        label44tabduedate.insert(0,table2[2])
        label44tabdescription.insert(0,table2[0])
        label44taboriginalamount.insert(0,table2[3])
        label44tabopenbalance.insert(0,table2[4])
    estcus.bind('<<ComboboxSelected>>',get_mail)
    estcus.place(relx=0.05,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Button(hf2,text='+',font=(14)).place(relx=0.26,rely=0.15,relwidth=0.025,relheight=0.03)
    tk.Label(hf2,text='Email',font=('times new roman', 14),bg='#2f516f').place(relx=0.30,rely=0.11)
    email=tk.Entry(hf2)
    email.place(relx=0.3,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Label(hf2,text='Find by invoice number',font=('times new roman', 14),bg='#2f516f').place(relx=0.55,rely=0.11)
    invno=tk.Entry(hf2)
    invno.place(relx=0.55,rely=0.15,relwidth=0.2,relheight=0.03)
    toda = date.today()
    to = toda.strftime("%Y-%m-%d")
    tk.Label(hf2,text='Payment Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.2)
    estdate=tk.Entry(hf2)
    estdate.insert(0,to)
    estdate.place(relx=0.05,rely=0.24,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text='Payment Method',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.29)

    def pmethod(event):
        global add,label44add
        p = paymet.get()
        print(p)
        
        if p == 'Add New':
            def wer(n):
                cc=label44add.get()
                paymet.delete(0,END)
                paymet.insert(0,label44add.get())
            add=StringVar()    
            label44add=Entry(hf2,bg='#2f516a',fg='#fff',textvariable=add, font=('times new roman', 11, 'bold'))
            label44add.place(relx=0.05,rely=0.37,relwidth=0.2,relheight=0.03)
            label44add.bind("<KeyRelease>",wer)
        if p!='Add New':
            label44add['state']='disabled'   
    met=['Cash','Cheque','Credit Card','Add New']
    paymet=ttk.Combobox(hf2,values=met)
    paymet.current(0)
    paymet.bind('<<ComboboxSelected>>',pmethod)
    paymet.place(relx=0.05,rely=0.33,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text="Deposit To",font=('times new roman', 14),bg='#2f516f').place(relx=0.55,rely=0.2)
    drop1accounttype=ttk.Combobox(hf2,textvariable='accounttype')
    drop1accounttype['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund")
    drop1accounttype.place(relx=0.55,rely=0.24,relwidth=0.2,relheight=0.03) 
    Label(hf2, text="Amount Recieved", font=('times new roman', 14),bg='#2f516f').place(relx=0.72,rely=0.32) 
    label44amountrec=Entry(hf2,font=('times new roman', 11))
    label44amountrec.place(relx=0.72,rely=0.35,relwidth=0.2,relheight=0.03) 
    #label44amountrec.bind('<KeyRelease>')

    Label(hf2, text="AMOUNT RECIEVED", font=('times new roman', 12), bd=12,bg='#2f516f').place(relx=0.72,rely=0.40) 
    label4amount=Entry(hf2, font=('times new roman',11))
    label4amount.place(relx=0.72,rely=0.45,relwidth=0.2,relheight=0.03) 

    label4=Label(hf2, text="#", font=('times new roman', 12,'bold'), bd=12, bg='#2f516f')
    label4.place(relx=0.05,rely=0.55)
    label44=Entry(hf2,textvariable='desig', font=('times new roman', 11))
    label44.place(relx=0.05,rely=0.62,relwidth=0.05,relheight=0.03)

    label4=Label(hf2, text="DESCRIPTION", font=('times new roman', 12,'bold'), bd=12, bg='#2f516f')
    label4.place(relx=0.12,rely=0.55)
    label44tabdescription=Entry(hf2,font=('times new roman', 11))
    label44tabdescription.place(relx=0.12,rely=0.62,relwidth=0.15,relheight=0.03)

    label4=Label(hf2, text="DUE DATE", font=('times new roman', 12, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.29,rely=0.55)
    label44tabduedate=Entry(hf2,font=('times new roman', 11, 'bold'))
    label44tabduedate.place(relx=0.29,rely=0.62,relwidth=0.15,relheight=0.03)

    label4=Label(hf2, text="ORIGINAL AMOUNT", font=('times new roman', 12,'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.46,rely=0.55)
    label44taboriginalamount=Entry(hf2, font=('times new roman', 11))
    label44taboriginalamount.place(relx=0.46,rely=0.62,relwidth=0.15,relheight=0.03)

    label4=Label(hf2, text="OPEN BALANCE", font=('times new roman', 12, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.64,rely=0.55)
    label44tabopenbalance=Entry(hf2,font=('times new roman', 11))
    label44tabopenbalance.place(relx=0.64,rely=0.62,relwidth=0.12,relheight=0.03)

    label4=Label(hf2, text="PAYMENT", font=('times new roman', 12, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.80,rely=0.55)
    label44tabpayment=Entry(hf2, font=('times new roman', 11, 'bold'))
    label44tabpayment.place(relx=0.80,rely=0.62,relwidth=0.12,relheight=0.03)

    label4=Label(hf2, text="Amount to Apply", font=('times new roman', 14, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.60,rely=0.70)
    label44amountapply=Entry(hf2, font=('times new roman', 11, 'bold'))
    label44amountapply.place(relx=0.75,rely=0.70,relwidth=0.15,relheight=0.04)

    label4=Label(hf2, text="Amount to Credit", font=('times new roman', 14, 'bold'), bd=12,bg="#2f516f" )
    label4.place(relx=0.60,rely=0.77)
    label44=Entry(hf2,font=('times new roman', 11, 'bold'))
    label44.place(relx=0.75,rely=0.77,relwidth=0.15,relheight=0.04)

    tk.Button(hf2,text='Save',bg="#2f516f",font=('times new roman', 14, 'bold')).place(relx=0.65,rely=0.9,relwidth=0.1,relheight=0.05)

    hf2.place(relx=0.1,rely=0.12,relwidth=0.8,relheight=0.7)
    estwin.mainloop()   
salespayments()    