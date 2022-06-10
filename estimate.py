import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def salesestimate():  
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
    tk.Label(hf1,text='ESTIMATE',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    hf1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
    hf2=tk.Frame(frame,bg='#243e54')
            #customer
    tk.Label(hf2,text='Fin sYs',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.02)      
    tk.Label(hf2,text='Customer',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.11) 
    def estimatecusinput():
        try:
                cur.execute("SELECT firstname,lastname FROM customer")
                val=cur.fetchall()         
                for row in val:
                    tm.append(row[0]+row[1])   
        except:
            pass              
    tm=['Select Customer']
    estimatecusinput()     
    estcus=ttk.Combobox(hf2,values=tm)
    estcus.current(0)  
    estcus.place(relx=0.05,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Button(hf2,text='+',font=(14)).place(relx=0.26,rely=0.15,relwidth=0.025,relheight=0.03)
    tk.Label(hf2,text='Email',font=('times new roman', 14),bg='#2f516f').place(relx=0.30,rely=0.11)
    email=tk.Entry(hf2)
    email.place(relx=0.3,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Label(hf2,text='Billing Address',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.2) 
    bill=tk.Entry(hf2)
    bill.place(relx=0.05,rely=0.24,relwidth=0.2,relheight=0.12)
    tk.Label(hf2,text='Estimate Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.2)
    estdate=tk.Entry(hf2)
    estdate.place(relx=0.3,rely=0.24,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text='Expiration Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.55,rely=0.2) 
    expdate=DateEntry(hf2)
    expdate.place(relx=0.55,rely=0.24,relwidth=0.2,relheight=0.03)
    tk.Label(hf2,text='Place of Supply',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.29)
    estplace=tk.Entry(hf2)
    estplace.place(relx=0.3,rely=0.33,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text='#',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.38)
    tk.Label(hf2,text='PRODUCT/SERVICES',font=('times new roman', 14),bg='#2f516f').place(relx=0.1,rely=0.38)
    tk.Label(hf2,text='DESCRIPTION',font=('times new roman', 14),bg='#2f516f').place(relx=0.28,rely=0.38)
    tk.Label(hf2,text='QTY',font=('times new roman', 14),bg='#2f516f').place(relx=0.41,rely=0.38,relwidth=0.1)
    tk.Label(hf2,text='RATE',font=('times new roman', 14),bg='#2f516f').place(relx=0.53,rely=0.38,relwidth=0.1)
    tk.Label(hf2,text='TOTAL',font=('times new roman', 14),bg='#2f516f').place(relx=0.66,rely=0.38,relwidth=0.1)
    tk.Label(hf2,text='TAX',font=('times new roman', 14),bg='#2f516f').place(relx=0.78,rely=0.38,relwidth=0.1)
    global subtot,amount,taxamt,taxamt2,taxamt3,taxamt4,tot,tot2,tot3,tot4
    estsubtot=0.0
    amount=0.0
    taxamt=0.0
    taxamt2=0.0
    taxamt3=0.0
    taxamt4=0.0
    tot=0.0
    tot2=0.0
    tot3=0.0
    tot4=0.0
   #row1
    pro=['Select Product']
    try:
                cur.execute("SELECT name FROM inventory WHERE cid =%s",([cid]))
                vall=cur.fetchall()         
                for row in vall:
                        pro.append(row[0])     
                cur.execute("SELECT name FROM noninventory WHERE cid =%s",([cid]))
                valll=cur.fetchall()         
                for row in valll:
                    pro.append(row[0])   
                cur.execute("SELECT name FROM bundle WHERE cid =%s",([cid]))
                vall1=cur.fetchall()         
                for row in vall1:
                    pro.append(row[0])         
    except:
                pass
    tk.Label(hf2,text='1',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.43)     
    prod=ttk.Combobox(hf2,values=pro)
    prod.bind('<<ComboboxSelected>>',)
    prod.place(relx=0.1,rely=0.43,relwidth=0.16,relheight=0.03)
    desc=tk.Entry(hf2)
    desc.place(relx=0.28,rely=0.43,relwidth=0.11,relheight=0.03)
    def salesestimatetotal(t):      
        global subtot,clear_total,tot,tot2,tot3
        def clear_text():
            total.delete(0, END) 
        def clear_total():
            sub.delete(0,END)    
        q=float(quan1.get())
        r=float(rate11.get())
        tot=(q*r)
        subtot=tot+tot2+tot3+tot4
        clear_text()
        total.insert(0,tot)
        clear_total()
        sub.insert(0,subtot) 
    quan1=IntVar()  
    qty=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan1,font=(8))
    qty.bind('<FocusIn>',salesestimatetotal)
    qty.place(relx=0.41,rely=0.43,relwidth=0.1,relheight=0.03)
    rate11=IntVar()
    rate=tk.Spinbox(hf2,textvariable=rate11,from_=0,to=2147483647,font=(8))
    rate.bind('<FocusIn>',salesestimatetotal)
    rate.place(relx=0.53,rely=0.43,relwidth=0.1,relheight=0.03)
    total=tk.Entry(hf2,font=(8))
    total.place(relx=0.66,rely=0.43,relwidth=0.1,relheight=0.03)
    def salesestimatetax1(y):
        global taxamt,clear_totalamount,taxamt2,taxamt4,taxamt3,amount
        tx=0.0
        def clear_tax():
            taxamount.delete(0,END)   
        def clear_totalamount():
            totalamount.delete(0,END)                 
        taxvalue=tax.get()
        if taxvalue=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue=='0.0% GST(0%)':
            tval=0.00
        elif taxvalue=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue=='Out of Scope(0%)':
            tval=0.00                                      
        tx=tot*tval
        taxtot=0.0
        if taxamt==0:
                taxtot=round(taxtot+tx,2)
        else:
                taxtot=round(tx,2)
        taxamt=taxtot    
        clear_tax()
        taxamount.insert(0,taxamt+taxamt2+taxamt3+taxamt4)
        clear_totalamount()
        amount=subtot-taxamt-taxamt2-taxamt3-taxamt4
        totalamount.insert(0,amount)
    taxval=['28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)','05.0% GST(05%)','03.0% GST(03%)',
                                                    '0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','Out of Scope(0%)']                                           
    tax=ttk.Combobox(hf2,values=taxval)
    tax.bind('<<ComboboxSelected>>',salesestimatetax1)
    tax.place(relx=0.78,rely=0.43,relwidth=0.1,relheight=0.03)

    #row22
    tk.Label(hf2,text='2',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.48)   
    prod1=ttk.Combobox(hf2,values=pro)
    prod1.bind('<<ComboboxSelected>>',)
    prod1.place(relx=0.1,rely=0.48,relwidth=0.16,relheight=0.03)
    desc1=tk.Entry(hf2)
    desc1.place(relx=0.28,rely=0.48,relwidth=0.11,relheight=0.03)
    def salesestimatetotal1(tt):
            global tot2,subtot,tot,tot4,tot3
            def clear_text1():
                total2.delete(0, END) 
            q2=float(quan2.get())
            r2=float(rate22.get())
            tot2=(q2*r2)
            subtot=tot+tot2+tot3+tot4
            clear_text1()
            total2.insert(0,tot2) 
            clear_total()
            sub.insert(0,subtot) 
    quan2=IntVar()  
    qty1=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan2,font=(8))
    qty1.bind('<FocusIn>',salesestimatetotal1)
    qty1.place(relx=0.41,rely=0.48,relwidth=0.1,relheight=0.03)
    rate22=IntVar()
    rate1=tk.Spinbox(hf2,textvariable=rate22,from_=0,to=2147483647,font=(8))
    rate1.bind('<FocusIn>',salesestimatetotal1)
    rate1.place(relx=0.53,rely=0.48,relwidth=0.1,relheight=0.03)
    total2=tk.Entry(hf2,font=(8))
    total2.place(relx=0.66,rely=0.48,relwidth=0.1,relheight=0.03)
    def salesestimatetax1(y):
        global taxamt,taxamt2,taxamt3,taxamt4,amount
        tx1=0.0
        print(tot2)
        def clear_tax():
            taxamount.delete(0,END)  
              
        taxvalue1=tax1.get()
        if taxvalue1=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue1=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue1=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue1=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue1=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue1=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue1=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue1=='0.0% GST(0%)':    
            tval=0.00   
        elif taxvalue1=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue1=='Out of Scope(0%)':
            tval=0.00                                   
        tx1=tot2*tval
        taxtot1=0.0
        if taxamt2==0:
                taxtot1=round(taxtot1+tx1,2)
        else:
                taxtot1=round(tx1,2)       
        clear_tax()
        taxamt2=taxtot1
        taxamount.insert(0,taxamt4+taxamt3+taxamt2+taxamt)
        clear_totalamount()
        amount=subtot-taxamt-taxamt2-taxamt3-taxamt4
        totalamount.insert(0,amount)
    tax1=ttk.Combobox(hf2,values=taxval)
    tax1.bind('<<ComboboxSelected>>',salesestimatetax1)
    tax1.place(relx=0.78,rely=0.48,relwidth=0.1,relheight=0.03)
    #third row
    tk.Label(hf2,text='3',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.53)   
    prod2=ttk.Combobox(hf2,values=pro)
    prod2.bind('<<ComboboxSelected>>',)
    prod2.place(relx=0.1,rely=0.53,relwidth=0.16,relheight=0.03)
    desc2=tk.Entry(hf2)
    desc2.place(relx=0.28,rely=0.53,relwidth=0.11,relheight=0.03)
    def salesestimatetotal2(tt):
            global tot3,subtot,tot,tot2,tot4
            def clear_text3():
                total3.delete(0, END)
            q3=float(quan3.get())
            r3=float(rate33.get())
            tot3=(q3*r3)
            subtot=tot+tot2+tot3+tot4
            clear_text3()
            total3.insert(0,tot3) 
            clear_total()
            sub.insert(0,subtot) 
    quan3=IntVar()  
    qty2=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan3,font=(8))
    qty2.bind('<FocusIn>',salesestimatetotal2)
    qty2.place(relx=0.41,rely=0.53,relwidth=0.1,relheight=0.03)
    rate33=IntVar()
    rate2=tk.Spinbox(hf2,textvariable=rate33,from_=0,to=2147483647,font=(8))
    rate2.bind('<FocusIn>',salesestimatetotal2)
    rate2.place(relx=0.53,rely=0.53,relwidth=0.1,relheight=0.03)
    total3=tk.Entry(hf2,font=(8))
    total3.place(relx=0.66,rely=0.53,relwidth=0.1,relheight=0.03)
    def salesestimatetax2(y):
        global taxamt,taxamt2,taxamt3,taxamt4,amount
        tx2=0.0
        def clear_tax():
            taxamount.delete(0,END)  
              
        taxvalue2=tax2.get()
        if taxvalue2=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue2=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue2=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue2=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue2=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue2=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue2=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue2=='0.0% GST(0%)':    
            tval=0.00   
        elif taxvalue2=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue2=='Out of Scope(0%)':
            tval=0.00                                   
        tx2=tot3*tval
        taxtot2=0.0
        if taxamt3==0:
                taxtot2=round(taxtot2+tx2,2)
        else:
                taxtot2=round(tx2,2)       
        clear_tax()
        taxamt3=taxtot2
        taxamount.insert(0,taxamt4+taxamt3+taxamt2+taxamt)
        clear_totalamount()
        amount=subtot-taxamt-taxamt2-taxamt3-taxamt4
        totalamount.insert(0,amount)
    tax2=ttk.Combobox(hf2,values=taxval)
    tax2.bind('<<ComboboxSelected>>',salesestimatetax2)
    tax2.place(relx=0.78,rely=0.53,relwidth=0.1,relheight=0.03)
    #forth row
    tk.Label(hf2,text='4',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.58)   
    prod3=ttk.Combobox(hf2,values=pro)
    prod3.bind('<<ComboboxSelected>>',)
    prod3.place(relx=0.1,rely=0.58,relwidth=0.16,relheight=0.03)
    desc3=tk.Entry(hf2)
    desc3.place(relx=0.28,rely=0.58,relwidth=0.11,relheight=0.03)
    def salesestimatetotal3(tt):
            global tot4,subtot,tot,tot2,tot3
            def clear_text4():
                total4.delete(0, END)
            q4=float(quan4.get())
            r4=float(rate55.get())
            tot4=(q4*r4)
            subtot=tot+tot2+tot3+tot4
            clear_text4()
            total4.insert(0,tot4) 
            clear_total()
            sub.insert(0,subtot) 
    quan4=IntVar()  
    qty3=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan4,font=(8))
    qty3.bind('<FocusIn>',salesestimatetotal3)
    qty3.place(relx=0.41,rely=0.58,relwidth=0.1,relheight=0.03)
    rate55=IntVar()
    rate3=tk.Spinbox(hf2,textvariable=rate55,from_=0,to=2147483647,font=(8))
    rate3.bind('<FocusIn>',salesestimatetotal3)
    rate3.place(relx=0.53,rely=0.58,relwidth=0.1,relheight=0.03)
    total4=tk.Entry(hf2,font=(8))
    total4.place(relx=0.66,rely=0.58,relwidth=0.1,relheight=0.03)
    def salesestimatetax3(y):
        global taxamt,taxamt2,taxamt3,taxamt4,amount
        tx3=0.0
        def clear_tax():
            taxamount.delete(0,END)    
        taxvalue3=tax3.get()
        if taxvalue3=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue3=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue3=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue3=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue3=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue3=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue3=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue3=='0.0% GST(0%)':    
            tval=0.00   
        elif taxvalue3=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue3=='Out of Scope(0%)':
            tval=0.00                                   
        tx3=tot4*tval
        taxtot3=0.0
        if taxamt4==0:
                taxtot3=round(taxtot3+tx3,2)
        else:
                taxtot3=round(tx3,2)       
        clear_tax()
        taxamt4=taxtot3
        taxamount.insert(0,taxamt4+taxamt3+taxamt2+taxamt)
        clear_totalamount()
        amount=subtot-taxamt-taxamt2-taxamt3-taxamt4
        totalamount.insert(0,amount)
    tax3=ttk.Combobox(hf2,values=taxval)
    tax3.bind('<<ComboboxSelected>>',salesestimatetax3)
    tax3.place(relx=0.78,rely=0.58,relwidth=0.1,relheight=0.03)

    #total
    tk.Label(hf2,text='Sub Total',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.65,relwidth=0.1,relheight=0.04)
    sub=tk.Entry(hf2,font=('times new roman', 16))
    sub.place(relx=0.82,rely=0.65,relheight=0.04,relwidth=0.12)
    tk.Label(hf2,text='Tax Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.71,relwidth=0.1,relheight=0.04)
    taxamount=tk.Entry(hf2,font=('times new roman', 16))
    taxamount.place(relx=0.82,rely=0.71,relheight=0.04,relwidth=0.12)
    tk.Label(hf2,text='Grand Total',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.77,relwidth=0.1,relheight=0.04)
    totalamount=tk.Entry(hf2,font=('times new roman', 16))
    totalamount.place(relx=0.82,rely=0.77,relheight=0.04,relwidth=0.12)
    tk.Button(hf2,text='Save',font=('times new roman', 16),bg='#2f516f').place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.04)
    hf2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.7)
    estwin.mainloop()   
salesestimate() 