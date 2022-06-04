import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from turtle import clear
from wsgiref.validate import validator
import matplotlib.figure
import matplotlib.patches
from tkcalendar import DateEntry
from datetime import datetime, date, timedelta
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import xcorr, yscale
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cursor=mydata.cursor()
#cc
def profitloss():
    prlframe=tk.Tk()
    prlframe.title('Profit Loss')
    prlframe.geometry('1500x1000')
    cid=2
    #dash['bg'] = '#2f516f'
    mycanvas=tk.Canvas(prlframe,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(prlframe,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    profitlossframe=tk.Frame(mycanvas)
    profitlossframe['bg']='#2f516f'
    mycanvas.create_window((0,0),window=profitlossframe,anchor='nw',width=1500,height=2200)

    pframe=tk.Frame(profitlossframe,bg='#243e54')
    tk.Label(pframe,text='PROFIT AND LOSS',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')

    def menu(e):
        global dte,dtee
        toda = date.today()
        tod = toda.strftime("%Y-%m-%d")
        dropp=drop.get()
        if dropp=='Custom':            
            tk.Label(form_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.45,rely=0.1)
            dte=StringVar()
            DateEntry(form_frame,textvariable=dte).place(relx=0.45,rely=0.23,relwidth=0.2,relheight=0.15)
            tk.Label(form_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.70,rely=0.1)
            dtee=StringVar()
            DateEntry(form_frame,textvariable=dtee).place(relx=0.70,rely=0.23,relwidth=0.2,relheight=0.15)
        elif dropp=='Today':
            fromdate = tod
            todate = tod 
        elif dropp=='This month':
            fromdate = toda.strftime("%Y-%m-01")
            todate = toda.strftime("%Y-%m-31")
        elif dropp=='This financial year':
            if int(toda.strftime("%m")) >= 1 and int(toda.strftime("%m")) <= 3:
                pyear = int(toda.strftime("%Y")) - 1
                fromdate = f'{pyear}-03-01'
                todate = f'{toda.strftime("%Y")}-03-31'
            else:
                pyear = int(toda.strftime("%Y")) + 1
                fromdate = f'{toda.strftime("%Y")}-03-01'
                todate = f'{pyear}-03-31'    

    def cleartree():#to clear treeview
        for item in set.get_children():
            set.delete(item) 
    def accrecifetch():
        period=drop.get()
        if period=='All dates':
            cleartree()
            alldates() 
        elif period=='Today':
            cleartree()
            betweendates() 
        elif period=='Custom':
            global fromdate,todate
            fromdate=dte.get()
            todate=dtee.get()
            cleartree()
            betweendates()  
        elif period=='This month':
            cleartree()
            betweendates()  
        elif period=='This financial year':
            cleartree()
            betweendates()    
    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= ttk.Combobox(form_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menu)
    drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
     #buttons
    tk.Button(form_frame,text = "Run Report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=accrecifetch).place(relx=0.55,rely=0.5,relwidth=0.15)
    tk.Button(form_frame,text = "Back",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold')).place(relx=0.75,rely=0.5,relwidth=0.15)
    form_frame.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.1)

    tableframe=tk.Frame(profitlossframe,bg='#243e54')
    #image
    imageframe=tk.Frame(tableframe,bg='#add8e6')
    size=(200,200)
    cv=Image.open('timeact.png').resize(size)
    ax=ImageTk.PhotoImage(cv,master=prlframe)
    ay=tk.Label(imageframe,image=ax,bg='#243e54')
    ay.place(relx=0.02,rely=0.08,relheight=0.8,relwidth=0.2)

    cursor.execute("SELECT cname FROM company WHERE id =%s",([cid]))
    h=cursor.fetchone()
    tk.Label(imageframe,text=h[0], font=('times new roman', 25, 'bold'),bg="#add8e6").place(relx=0.25,rely=0.4,relwidth=0.2)
    imageframe.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.15)
    #contents
    conttframe=tk.Frame(tableframe,bg='white')
    conttframe.place(relx=0.05,rely=0.17,relwidth=0.9,relheight=0.7)
    mycanvass=tk.Canvas(conttframe,width=1200,height=1200)
    mycanvass.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(conttframe,orient='vertical',command=mycanvass.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvass.configure(yscrollcommand=yscrollbar.set)
    mycanvass.bind('<Configure>',lambda e:mycanvass.configure(scrollregion=mycanvass.bbox('all')))
    contframe=tk.Frame(mycanvass)
    contframe['bg']='white'
    mycanvass.create_window((0,0),window=contframe,anchor='nw',width=1100,height=1200)
    set = ttk.Treeview(contframe,height=0)
    set.place(relx=0,rely=0,relwidth=1)
    set = ttk.Treeview(contframe,height=0)
    set.place(relx=0,rely=0,relwidth=1)
    

    set['columns']= ('CUSTOMER NAME','TOTAL')
    set.column("#0", width=0,  stretch=NO)
    set.column("CUSTOMER NAME",width=820,anchor=CENTER )
    set.column("TOTAL",width=198,anchor=CENTER)


    #set.heading("#0",text="",anchor=CENTER)
    set.heading("CUSTOMER NAME",text="",anchor=CENTER )
    set.heading("TOTAL",text="TOTAL",anchor=CENTER)
    tk.Label(contframe,text = "Income",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
    def alldates():
        def incomevalues():
            global x,totin
            x=0.08
            totin=0.0
            nme='Income'
            try:
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([nme,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                    x=x+0.04
                    totin=totin+i[1]
            except:  
                pass
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nme,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                    x=x+0.04
                    totin=totin+i[1]
            except:  
                pass
            tk.Label(contframe,text = " Total Income",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=x)
            tk.Label(contframe,text = totin,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x)
        incomevalues() 
        tk.Label(contframe,text = " Cost of Goods Sold ",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=x+0.04)
        def costofgoodsvalue():
            nmee='Cost of Goods Sold'
            global y,gros
            tot1=0.0
            y=x+0.08
            try:
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                
                print(val)
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=y)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                    y=y+0.04
                    tot1=tot1+i[1]
            except:  
                pass
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=y)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                    y=y+0.04
                    tot1=tot1+i[1]
            except:  
                pass
            gros=totin-tot1
            tk.Label(contframe,text = " Gross Profit ",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=y)
            tk.Label(contframe,text = gros,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y)
        costofgoodsvalue()
        def otherincome():
            nmee='Other Income'
            global z,tot2
            tot2=0.0
            z=y+0.04
            try:
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=z)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=z)
                    z=z+0.04
                    tot2=tot2+i[1]
            except:  
                pass
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=z)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=z)
                    z=z+0.04
                    tot2=tot2+i[1]
            except:  
                pass
            
            tk.Label(contframe,text = "Other Income",bg='grey',font=('times new roman', 14)).place(relx=0.06,rely=z)
            tk.Label(contframe,text = tot2,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=z)
        otherincome()    
        tk.Label(contframe,text = "Expenses",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=z+0.04)
        def expenses():
            nmee='Expenses'
            global w,tot3
            w=z+0.08
            tot3=0.0
            try:
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=w)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=w)
                    w=w+0.04
                    tot3=tot3+i[1]
            except:  
                pass
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=w)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=w)
                    w=w+0.04
                    tot3=tot3+i[1]
            except:  
                pass
        expenses()    
        tk.Label(contframe,text = "Other Expenses",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.03,rely=w)
        def otherexpenses():
            nmee='Other Expenses'
            global v,tot4
            v=w+0.04
            tot4=0.0
            try:
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=v)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=v)
                    v=v+0.04
                    tot4=tot4+i[1]
            except:  
                pass
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nmee,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=v)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=v)
                    v=v+0.04
                    tot4=tot4+i[1]
            except:  
                pass
        otherexpenses() 
        expp=tot3+tot4 
        tk.Label(contframe,text = "TOTAL EXPENSE",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=v)
        tk.Label(contframe,text = expp,bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=v) 
        incc=gros+tot2
        vml=incc-expp  
        tk.Label(contframe,text = "PROFIT OR LOSS",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=v+0.04)
        tk.Label(contframe,text = vml,bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=v+0.04)   
    alldates()
    def betweendates():
        totalama = 0.0
        cursor.execute("SELECT grandtotal,payornot FROM bills where paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
        bill=cursor.fetchall()
        print(bill)
    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
   
    prlframe.mainloop()
profitloss()    