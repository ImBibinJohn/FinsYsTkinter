import tkinter as tk
from tkinter import ttk
from tkinter import *
import zlib
import matplotlib.figure
import matplotlib.patches
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from tkcalendar import DateEntry
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cursor=mydata.cursor()
#cc
def balancesheet():
    prlframe=tk.Tk()
    prlframe.title('Balance Sheet')
    prlframe.geometry('1500x1000')
    #dash['bg'] = '#2f516f'
    cid=2
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
    tk.Label(pframe,text='BALANCE SHEET',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')

    def menu1(e):
        dropp=drop.get()
        def datedate1():
            fdate=dte.get()
            ldate=dtee.get()   
        if dropp=='Custom':            
            tk.Label(form_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.45,rely=0.1)
            dte=StringVar()
            DateEntry(form_frame,textvariable=dte).place(relx=0.45,rely=0.23,relwidth=0.2,relheight=0.15)
            tk.Label(form_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.70,rely=0.1)
            dtee=StringVar()
            DateEntry(form_frame,textvariable=dtee).place(relx=0.70,rely=0.23,relwidth=0.2,relheight=0.15)
            datedate1()

    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= ttk.Combobox(form_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menu1)
    drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
     #buttons
    tk.Button(form_frame,text = "Run Report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold')).place(relx=0.55,rely=0.5,relwidth=0.15)
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
    tk.Label(imageframe,text="INFOX", font=('times new roman', 25, 'bold'),bg="#add8e6").place(relx=0.25,rely=0.4,relwidth=0.2)
    imageframe.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.15)
    #contents
    contframe=tk.Frame(tableframe,bg='white')
    contframe.place(relx=0.05,rely=0.17,relwidth=0.9,relheight=0.7)
    set = ttk.Treeview(contframe,height=0)
    set.place(relx=0,rely=0,relwidth=1)

    set['columns']= ('CUSTOMER NAME','TOTAL')
    set.column("#0", width=0,  stretch=NO)
    set.column("CUSTOMER NAME",width=750,anchor=CENTER )
    set.column("TOTAL",width=198,anchor=CENTER)


    #set.heading("#0",text="",anchor=CENTER)
    set.heading("CUSTOMER NAME",text="",anchor=CENTER )
    set.heading("TOTAL",text="TOTAL",anchor=CENTER)

    tk.Label(contframe,text = "Assets",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
    tk.Label(contframe,text = " Current Assets",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.08)
    #current assets database values
    def currentassets():
        global x,tott1,tott2
        current='Current Assets'
        x=0.12   
        try:
            tott1=0.0
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                x=x+0.04
                tott1=tott1+i[1]
        except:  
            pass
        try:
            tott2=0.0
            cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                x=x+0.04
                tott2=tott2+i[1]
        except:  
            pass
        tk.Label(contframe,text = "Bank",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
    currentassets()    
    tk.Label(contframe,text = " Account Receivable(Debtors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x+0.04)
    def AccountReceivable():
        global y
        current='Account Receivable(Debtors)'
        y=x+0.08  
        try:
            tott3=0.0
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                y=y+0.04
                tott3=tott3+i[1]
        except:  
            pass
        try:
            tott4=0.0
            cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                y=y+0.04
                tott4=tott4+i[1]
        except:  
            pass
        taccountsreceivable = tott3 + tott4
        tcurrentassets = tott1 + tott2 + taccountsreceivable
        tk.Label(contframe,text = " Total Account Receivable(Debtors)",bg="grey",font=('times new roman', 14)).place(relx=0.08,rely=y)
        tk.Label(contframe,text = taccountsreceivable,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y)
        tk.Label(contframe,text = " Total Current Assets",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=y+0.04)
        tk.Label(contframe,text = tcurrentassets,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.04)
        tk.Label(contframe,text = " Total Assets",bg="grey",font=('times new roman', 14)).place(relx=0.04,rely=y+0.08)
        tk.Label(contframe,text = tcurrentassets,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.08)
    AccountReceivable() 
    tk.Label(contframe,text = " Liabilities and Equity",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=y+0.12) 
    tk.Label(contframe,text = " Current Liabilities",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=y+0.16)    
    def currentLiabilities():
        global z,tliabilities
        current='Current Liabilities'
        z=y+0.20  
        try:
            tott5=0.0
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=z)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=z)
                z=z+0.04
                tott5=tott5+i[1]
        except:  
            pass
        try:
            tott6=0.0
            cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=z)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=z)
                z=z+0.04
                tott6=tott6+i[1]
        except:  
            pass
        tliabilities=tott5+tott6

    currentLiabilities()
    tk.Label(contframe,text = " Accounts Payable(Creditors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=z)
    def Accounts_Payable_creditors():
        global v,taccountspayable
        current='Accounts Payable(Creditors)'
        v=z+0.04 
        try:
            tott7=0.0
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=v)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=v)
                v=v+0.04
                tott7=tott7+i[1]
        except:  
            pass
        try:
            tott8=0.0
            cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=v)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=v)
                v=v+0.04
                tott8=tott8+i[1]
        except:  
            pass
        taccountspayable =  tott8 +  tott7
    Accounts_Payable_creditors()
    tcurrentliabilties =  tliabilities + taccountspayable
    tk.Label(contframe,text = " Total Accounts Payable(Creditors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=v)
    tk.Label(contframe,text = taccountspayable,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=v)
    tk.Label(contframe,text = " Total Current Liabilities",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=v+0.04)
    tk.Label(contframe,text = tcurrentliabilties,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=v+0.04)
    tk.Label(contframe,text = " Equity",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=v+0.08)
    def equity():
        global equityy
        w=v+0.12
        current='Equity'
        try:
            tott9=0.0
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=w)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=w)
                w=w+0.04
                tott9=tott9+i[1]
        except:  
            pass
        try:
            tott10=0.0
            cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
            val=cursor.fetchall()
            for i in val:
                tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=w)
                tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=w)
                w=w+0.04
                tott10=tott10+i[1]
        except:  
            pass
        equityy=tott9+tott10
        def getothervalues():
            global proandloss
            totincome=0.0
            nme='Income'
            try:
                cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([nme,cid]))
                val=cursor.fetchall()
                for i in val:
                    totincome=totincome+i[0]
            except:  
                pass
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nme,cid]))
                val=cursor.fetchall()
                for i in val:
                    totincome=totincome+i[0]
            except:  
                pass
            namee='Cost of Goods Sold'
            costsold=0.0
            try:
                cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([namee,cid]))
                val=cursor.fetchall()
                for i in val:
                    costsold=costsold+i[0]
            except:  
                pass
            try:
                cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([namee,cid]))
                val=cursor.fetchall()
                for i in val:
                    costsold=costsold+i[0]
            except:  
                pass
            nameee='Other Income'
            otherincome=0.0
            try:
                cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([nameee,cid]))
                val=cursor.fetchall()
                for i in val:
                    otherincome=otherincome+i[0]
            except:  
                pass
            try:
                cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([nameee,cid]))
                val=cursor.fetchall()
                for i in val:
                    otherincome=otherincome+i[0]
            except:  
                pass
            nameee1='Expenses'
            expenses=0.0
            try:
                cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([nameee1,cid]))
                val=cursor.fetchall()
                for i in val:
                    expenses=expenses+i[0]
            except:  
                pass
            try:
                cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([nameee1,cid]))
                val=cursor.fetchall()
                for i in val:
                    expenses=expenses+i[0]
            except:  
                pass
            name1='Other Expenses'
            otherexpenses=0.0
            try:
                cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([name1,cid]))
                val=cursor.fetchall()
                for i in val:
                    otherexpenses=otherexpenses+i[0]
            except:  
                pass
            try:
                cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([name1,cid]))
                val=cursor.fetchall()
                for i in val:
                    otherexpenses=otherexpenses+i[0]
            except:  
                pass
            proandloss = ((totincome - costsold) + otherincome) - (expenses + otherexpenses)
            tk.Label(contframe,text = " Profit for the Year",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=w)  
            tk.Label(contframe,text =proandloss,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=w)
        getothervalues()           
        tk.Label(contframe,text = " Total Equity",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=w+0.04)
        totequity = equityy + proandloss
        tk.Label(contframe,text =totequity,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=w+0.04)
        tk.Label(contframe,text = " Total Liabilities and Equity",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=w+0.08)
        tlande = tcurrentliabilties + totequity
        tk.Label(contframe,text =tlande,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=w+0.08)       
    equity() 



    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
   
    prlframe.mainloop()
balancesheet()   