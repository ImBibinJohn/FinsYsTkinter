from lib2to3.pgen2.token import PERCENT
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
from tkcalendar import DateEntry
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def viewmaterials():
    global treevv
    viewmatwin=tk.Tk()
    viewmatwin.title('View Materials')
    viewmatwin.geometry('1500x900')
    viewmatwin['bg'] = '#2f516f'
    f1=tk.Frame(viewmatwin,bg='#243e54')
    tk.Label(f1,text='VIEW MATERIAL DETAILS',bg='#243e54',font=('Times New Roman',24)).place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    f1.place(relx=0.1,rely=0.05,relheight=0.1,relwidth=0.8)
    f2=tk.Frame(viewmatwin,bg='#243e54')
    def searched():
        searchs=serch.get()
        for item in treevv.get_children():
            treevv.delete(item) 
        if searchs!='':  
            cur.execute("SELECT productionid,productname,sku,hsn,quantity,manufacturing_date,expiry_date FROM production WHERE productname LIKE %s ",(searchs,))    
            xx=cur.fetchall()
            if xx:
                for x in xx:
                    treevv.insert('', 'end',values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        else:
            cur.execute("SELECT productionid,productname,sku,hsn,quantity,manufacturing_date,expiry_date FROM production")
            val=cur.fetchall()
            if val:
                for x in val:
                    treevv.insert('', 'end',values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))         
    serch=tk.Entry(f2)
    serch.place(relx=0,rely=0,relwidth=0.2,relheight=0.07)
    search=tk.Button(f2,text='Search',bg='#243e54',font=('Times New Roman',14),command=searched)
    search.place(relx=0.25,rely=0,relwidth=0.15,relheight=0.07)
    #tree
        #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='black',fieldbackground='#243e54')
    style.map('Treeview',background=[('selected','green')])
    treevv = ttk.Treeview(f2, height=20, columns=(1,2,3,4,5,6,7), show='headings') 
    treevv.heading(1, text='ID')
    treevv.heading(2, text='PRODUCT NAME')#headings
    treevv.heading(3, text='SKU')
    treevv.heading(4, text='HSN')
    treevv.heading(5, text='QUANTITY')
    treevv.heading(6, text='MANUFACTURING DATE')
    treevv.heading(7, text='EXPIRY DATE')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=10, width=20,anchor=CENTER)#coloumns
    treevv.column(2, minwidth=30, width=160,anchor=CENTER)
    treevv.column(3, minwidth=30, width=60,anchor=CENTER)
    treevv.column(4, minwidth=30, width=60,anchor=CENTER)
    treevv.column(5, minwidth=30, width=160,anchor=CENTER)
    treevv.column(6, minwidth=30, width=160,anchor=CENTER)
    treevv.column(7, minwidth=30, width=160,anchor=CENTER)
    cur.execute("SELECT productionid,productname,sku,hsn,quantity,manufacturing_date,expiry_date FROM production")
    val=cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end',values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
    treevv.place(relx=0,rely=0.1,relwidth=1,relheight=0.7)
    def productionedit():
        estwin=tk.Tk()
        estwin.title('Materials')
        estwin.geometry('1500x1000')
        estwin['bg'] = '#2f516f'
        cid=2
        str = treevv.focus()
        values=treevv.item(str,'values')
        b=[values[0]]
        cur.execute("SELECT * FROM production WHERE productionid=%s",(b))
        s=cur.fetchone()
        mycanvas=tk.Canvas(estwin,width=1800,height=1200)
        mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(estwin,orient='vertical',command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT,fill=Y)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        frame=tk.Frame(mycanvas)
        frame['bg']='#2f516f'
        mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=2000)
        hf1=tk.Frame(frame,bg='#243e54')
        tk.Label(hf1,text='MATERIAL MASTER',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
        hf1.place(relx=0.1,rely=0.03,relwidth=0.8,relheight=0.04)
        hf2=tk.Frame(frame,bg='#243e54')
        mycanvass=tk.Canvas(hf2,width=1800,height=1200)
        mycanvass.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbarr =ttk.Scrollbar(hf2,orient='vertical',command=mycanvass.yview)
        yscrollbarr.pack(side=RIGHT,fill=Y)
        mycanvass.configure(yscrollcommand=yscrollbarr.set)
        mycanvass.bind('<Configure>',lambda e:mycanvass.configure(scrollregion=mycanvass.bbox('all')))
        frame1=tk.Frame(mycanvass)
        frame1['bg']='#243e54'
        mycanvass.create_window((0,0),window=frame1,anchor='nw',width=1500,height=2500)
                #PRODUCT     
        tk.Label(frame1,text='PRODUCT NAME',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.01)
        product=tk.Entry(frame1)
        try:
            product.insert(0,s[2])
        except:
            pass    
        product.place(relx=0.15,rely=0.025,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.01)
        sku=tk.Entry(frame1)
        try:
            sku.insert(0,s[3])
        except:
            pass
        sku.place(relx=0.45,rely=0.025,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='HSN',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.045)
        hsn=tk.Entry(frame1)
        try:
            hsn.insert(0,s[4])
        except:
            pass
        hsn.place(relx=0.15,rely=0.06,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='QUANTITY',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.045)
        quanty=tk.Entry(frame1)
        try:
            quanty.insert(0,s[5])
        except:
                pass
        quanty.place(relx=0.45,rely=0.06,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='Manufacturing Date',bg='#2f516f',font=('times new roman', 14)).place(relx=0.15,rely=0.08)
        mandate=StringVar()
        DateEntry(frame1,textvariable=mandate,date_pattern='y-mm-dd').place(relx=0.15,rely=0.10,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='Expiry Date',bg='#2f516f',font=('times new roman', 14)).place(relx=0.45,rely=0.08)
        expdate=StringVar()
        DateEntry(frame1,textvariable=expdate,date_pattern='y-mm-dd').place(relx=0.45,rely=0.10,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='Manufacture',bg='#243e54',font=('Times New Roman',30)).place(relx=0.31,rely=0.125)
        #components
        tk.Label(frame1,text='Components',bg='#243e54',font=('Times New Roman',24)).place(relx=0.15,rely=0.140)
        tk.Label(frame1,text='Max:30',bg='#243e54',font=('Times New Roman',12)).place(relx=0.05,rely=0.143)
        tk.Label(frame1,text='Product Name',font=('times new roman', 14),bg='#2f516f').place(relx=0.01,rely=0.17)
        tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.105,rely=0.17)
        tk.Label(frame1,text='Quantity',font=('times new roman', 14),bg='#2f516f').place(relx=0.18,rely=0.17)
        tk.Label(frame1,text='Price',font=('times new roman', 14),bg='#2f516f').place(relx=0.245,rely=0.17)
        tk.Label(frame1,text='Amount',font=('times new roman', 14),bg='#2f516f').place(relx=0.31,rely=0.17)
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
        #row1
        global aldatas,qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
        q,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        qtytotal,subtot=0,0.0
        tot,tot1,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
        abcd='Components'
        cur.execute("SELECT * FROM rawmaterials WHERE productionid =%s and Type =%s",[b[0],abcd])
        aldatas=cur.fetchone()
        def getproductcomp(s):
            def clearskucomp():
                sku.delete(0,END)
                rate.delete(0,END)
            clearskucomp()    
            prodd=prod.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                sku.insert(0,fet[0])
                rate.insert(0,fet[2])
                tod=float(fet[1])
            elif fetch:
                sku.insert(0,fetch[0])
                rate.insert(0,fetch[2])
                tod=float(fetch[1])
        def calculatetotal(x):  
            global clearcomptotamount,clearcomptotquan,qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
            def clear_text():
                total.delete(0, END) 
            def clearcomptotquan():  
                totalquantity.delete(0,END)
            def clearcomptotamount():  
                totalamount.delete(0,END) 
                costofcomp.delete(0,END)    
            q=float(qty.get())
            r=float(rate.get())  
            tot=(q*r)
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
            clearcomptotquan()
            totalquantity.insert(0,qtytotal)
            totalquantity.insert(14,'Nos')
            clear_text()
            total.insert(0,tot)
            clearcomptotamount()
            totalamount.insert(0,subtot)
            costofcomp.insert(0,subtot)
        prod=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prod.insert(0,aldatas[4])
        except:
            pass    
        prod.bind('<<ComboboxSelected>>',getproductcomp)
        prod.place(relx=0.01,rely=0.19,relheight=0.015,relwidth=0.08)
        sku=tk.Entry(frame1,font=(4))
        try:
            sku.insert(0,aldatas[5])
        except:
            pass    
        sku.place(relx=0.105,rely=0.19,relheight=0.015,relwidth=0.06)
        qty=tk.Spinbox(frame1,from_=0,to=2000,font=(4))
        try:
            qty.delete(0,END)
            qty.insert(0,aldatas[6])
        except:
            pass
        qty.bind('<FocusIn>',calculatetotal)
        qty.place(relx=0.18,rely=0.19,relheight=0.015,relwidth=0.05)
        rate=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:  
            rate.delete(0,END)          
            rate.insert(0,aldatas[7])
        except:
            pass
        rate.bind('<FocusIn>',calculatetotal)
        rate.place(relx=0.245,rely=0.19,relheight=0.015,relwidth=0.05)
        total=tk.Entry(frame1,font=(4))
        try:          
            total.insert(0,aldatas[8])
        except:
            pass
        total.place(relx=0.31,rely=0.19,relheight=0.015,relwidth=0.05)
        #row2
        def getproductcomp1(s):
            def clearskucomp1():
                sku1.delete(0,END)
                rate1.delete(0,END)
            clearskucomp1()    
            prodd=prod1.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                sku1.insert(0,fet[0])
                rate1.insert(0,fet[2])
            elif fetch:
                sku1.insert(0,fetch[0])
                rate1.insert(0,fetch[2])
        def calculatetotal1(x):
            global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
            def clear_text1():
                total1.delete(0, END) 
            q1=float(qty1.get())
            r1=float(rate1.get())
            tot1=(q1*r1)
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
            clear_text1()
            total1.insert(0,tot1)
            clearcomptotquan()
            totalquantity.insert(0,qtytotal)
            totalquantity.insert(14,'Nos')
            clearcomptotamount()
            totalamount.insert(0,subtot)
            costofcomp.insert(0,subtot)
        prod1=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prod1.insert(0,aldatas[9])
        except:
            pass    
        prod1.bind('<<ComboboxSelected>>',getproductcomp1)
        prod1.place(relx=0.01,rely=0.21,relheight=0.015,relwidth=0.08)
        sku1=tk.Entry(frame1,font=(4))
        try:
            sku1.insert(0,aldatas[10])
        except:
            pass   
        sku1.place(relx=0.105,rely=0.21,relheight=0.015,relwidth=0.06)
        qty1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qty1.delete(0,END)
            qty1.insert(0,aldatas[11])
        except:
            pass
        qty1.bind('<FocusIn>',calculatetotal1)
        qty1.place(relx=0.18,rely=0.21,relheight=0.015,relwidth=0.05)
        rate1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:  
            rate1.delete(0,END)          
            rate1.insert(0,aldatas[12])
        except:
            pass
        rate1.bind('<FocusIn>',calculatetotal1)
        rate1.place(relx=0.245,rely=0.21,relheight=0.015,relwidth=0.05)
        total1=tk.Entry(frame1,font=(4))
        try:          
            total1.insert(0,aldatas[13])
        except:
            pass
        total1.place(relx=0.31,rely=0.21,relheight=0.015,relwidth=0.05)
        #row3
        def getproductcomp2(s):
            def clearskucomp2():
                sku2.delete(0,END)
                rate2.delete(0,END)
            clearskucomp2()    
            prodd=prod2.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                sku2.insert(0,fet[0])
                rate2.insert(0,fet[2])
            elif fetch:
                sku2.insert(0,fetch[0])
                rate2.insert(0,fetch[2])
        def calculatetotal2(x):
            global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
            def clear_text2():
                total2.delete(0, END) 
            q2=float(qty2.get())
            r2=float(rate2.get())
            tot2=(q2*r2)
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
            clear_text2()
            total2.insert(0,tot2)
            clearcomptotquan()
            totalquantity.insert(0,qtytotal)
            totalquantity.insert(14,'Nos')
            clearcomptotamount()
            totalamount.insert(0,subtot)
            costofcomp.insert(0,subtot)
        prod2=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prod2.insert(0,aldatas[14])
        except:
            pass    
        prod2.bind('<<ComboboxSelected>>',getproductcomp2)
        prod2.place(relx=0.01,rely=0.23,relheight=0.015,relwidth=0.08)
        sku2=tk.Entry(frame1,font=(4))
        try:
            sku2.insert(0,aldatas[15])
        except:
            pass    
        sku2.place(relx=0.105,rely=0.23,relheight=0.015,relwidth=0.06)
        qty2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qty2.delete(0,END)
            qty2.insert(0,aldatas[16])
        except:
            pass
        qty2.bind('<FocusIn>',calculatetotal2)
        qty2.place(relx=0.18,rely=0.23,relheight=0.015,relwidth=0.05)
        rate2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:  
            rate2.delete(0,END)          
            rate2.insert(0,aldatas[17])
        except:
            pass        
        rate2.bind('<FocusIn>',calculatetotal2)
        rate2.place(relx=0.245,rely=0.23,relheight=0.015,relwidth=0.05)
        total2=tk.Entry(frame1,font=(4))
        try:          
            total2.insert(0,aldatas[18])
        except:
            pass        
        total2.place(relx=0.31,rely=0.23,relheight=0.015,relwidth=0.05)
        #row4
        def getproductcomp3(s):
            def clearskucomp3():
                sku3.delete(0,END)
                rate3.delete(0,END)
            clearskucomp3()    
            prodd=prod3.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                sku3.insert(0,fet[0])
                rate3.insert(0,fet[2])
            elif fetch:
                sku3.insert(0,fetch[0])
                rate3.insert(0,fetch[2])
        def calculatetotal3(x):
            global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
            def clear_text3():
                total3.delete(0, END) 
            q3=float(qty3.get())
            r3=float(rate3.get())
            tot3=(q3*r3)
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
            clear_text3()
            total3.insert(0,tot3)
            clearcomptotquan()
            totalquantity.insert(0,qtytotal)
            totalquantity.insert(14,'Nos')
            clearcomptotamount()
            totalamount.insert(0,subtot)
            costofcomp.insert(0,subtot)
        prod3=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prod3.insert(0,aldatas[19])
        except:
            pass   
        prod3.bind('<<ComboboxSelected>>',getproductcomp3)
        prod3.place(relx=0.01,rely=0.25,relheight=0.015,relwidth=0.08)
        sku3=tk.Entry(frame1,font=(4))
        try:
            sku3.insert(0,aldatas[20])
        except:
            pass           
        sku3.place(relx=0.105,rely=0.25,relheight=0.015,relwidth=0.06)
        qty3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qty3.delete(0,END)
            qty3.insert(0,aldatas[21])
        except:
            pass        
        qty3.bind('<FocusIn>',calculatetotal3)
        qty3.place(relx=0.18,rely=0.25,relheight=0.015,relwidth=0.05)
        rate3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:  
            rate3.delete(0,END)          
            rate3.insert(0,aldatas[22])
        except:
            pass           
        rate3.bind('<FocusIn>',calculatetotal3)
        rate3.place(relx=0.245,rely=0.25,relheight=0.015,relwidth=0.05)
        total3=tk.Entry(frame1,font=(4))
        try:          
            total3.insert(0,aldatas[23])
        except:
            pass            
        total3.place(relx=0.31,rely=0.25,relheight=0.015,relwidth=0.05)
        #row5
        def getproductcomp4(s):
            def clearskucomp4():
                sku4.delete(0,END)
                rate4.delete(0,END)
            clearskucomp4()    
            prodd=prod4.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                sku4.insert(0,fet[0])
                rate4.insert(0,fet[2])
            elif fetch:
                sku4.insert(0,fetch[0])
                rate4.insert(0,fetch[2])
        def calculatetotal4(x):
            global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
            def clear_text4():
                total4.delete(0, END) 
            q4=float(qty4.get())
            r4=float(rate4.get())
            tot4=(q4*r4)
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
            clear_text4()
            total4.insert(0,tot4)
            clearcomptotquan()
            totalquantity.insert(0,qtytotal)
            totalquantity.insert(14,'Nos')
            clearcomptotamount()
            totalamount.insert(0,subtot)
            costofcomp.insert(0,subtot)
        prod4=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prod4.insert(0,aldatas[24])
        except:
            pass           
        prod4.bind('<<ComboboxSelected>>',getproductcomp4)
        prod4.place(relx=0.01,rely=0.27,relheight=0.015,relwidth=0.08)
        sku4=tk.Entry(frame1,font=(4))
        try:
            sku4.insert(0,aldatas[25])
        except:
            pass             
        sku4.place(relx=0.105,rely=0.27,relheight=0.015,relwidth=0.06)
        qty4=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        try:
            qty4.delete(0,END)
            qty4.insert(0,aldatas[26])
        except:
            pass         
        qty4.bind('<FocusIn>',calculatetotal4)
        qty4.place(relx=0.18,rely=0.27,relheight=0.015,relwidth=0.05)
        rate4=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        try:  
            rate4.delete(0,END)          
            rate4.insert(0,aldatas[27])
        except:
            pass          
        rate4.bind('<FocusIn>',calculatetotal4)
        rate4.place(relx=0.245,rely=0.27,relheight=0.015,relwidth=0.05)
        total4=tk.Entry(frame1,font=(4))
        try:          
            total4.insert(0,aldatas[28])
        except:
            pass           
        total4.place(relx=0.31,rely=0.27,relheight=0.015,relwidth=0.05)
        #row6
        def getproductcomp5(s):
            def clearskucomp5():
                sku5.delete(0,END)
                rate5.delete(0,END)
            clearskucomp5()    
            prodd=prod5.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                sku5.insert(0,fet[0])
                rate5.insert(0,fet[2])
            elif fetch:
                sku5.insert(0,fetch[0])
                rate5.insert(0,fetch[2])
        def calculatetotal5(x):
            global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
            def clear_text5():
                total5.delete(0, END) 
            q5=float(qty5.get())
            r5=float(rate5.get())
            tot5=(q5*r5)
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
            clear_text5()
            total5.insert(0,tot5)
            clearcomptotquan()
            totalquantity.insert(0,qtytotal)
            totalquantity.insert(14,'Nos')
            clearcomptotamount()
            totalamount.insert(0,subtot)
            costofcomp.insert(0,subtot)
        prod5=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prod5.insert(0,aldatas[29])
        except:
            pass            
        prod5.bind('<<ComboboxSelected>>',getproductcomp5)
        prod5.place(relx=0.01,rely=0.29,relheight=0.015,relwidth=0.08)
        sku5=tk.Entry(frame1,font=(4))
        try:
            sku5.insert(0,aldatas[30])
        except:
            pass           
        sku5.place(relx=0.105,rely=0.29,relheight=0.015,relwidth=0.06)
        qty5=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        try:
            qty5.delete(0,END)
            qty5.insert(0,aldatas[31])
        except:
            pass             
        qty5.bind('<FocusIn>',calculatetotal5)
        qty5.place(relx=0.18,rely=0.29,relheight=0.015,relwidth=0.05)
        rate5=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        try:  
            rate5.delete(0,END)          
            rate5.insert(0,aldatas[32])
        except:
            pass          
        rate5.bind('<FocusIn>',calculatetotal5)
        rate5.place(relx=0.245,rely=0.29,relheight=0.015,relwidth=0.05)
        total5=tk.Entry(frame1,font=(4))
        try:          
            total5.insert(0,aldatas[33])
        except:
            pass           
        total5.place(relx=0.31,rely=0.29,relheight=0.015,relwidth=0.05)
        #row1
        global x
        x=0.31
        if aldatas[34]!='':
            def getproductcomp6(s):
                def clearskucomp6():
                    sku6.delete(0,END)
                    rate6.delete(0,END)
                clearskucomp6()    
                prodd=prod6.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku6.insert(0,fet[0])
                    rate6.insert(0,fet[2])
                elif fetch:
                    sku6.insert(0,fetch[0])
                    rate6.insert(0,fetch[2])   
            def calculatetotal6(xx):  
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29  
                    def clear_text6():
                        total6.delete(0, END) 
                    q6=float(qty6.get())
                    r6=float(rate6.get())
                    tot6=(q6*r6)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text6()
                    total6.insert(0,tot6)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
            prod6=ttk.Combobox(frame1,values=pro,font=(4)) 
            prod6.bind('<<ComboboxSelected>>',getproductcomp6)
            prod6.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku6=tk.Entry(frame1,font=(4))
            sku6.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty6=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty6.bind('<FocusIn>',calculatetotal6)
            qty6.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate6=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate6.bind('<FocusIn>',calculatetotal6)
            rate6.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total6=tk.Entry(frame1,font=(4))
            total6.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            try:
                prod6.insert(0,aldatas[34])
                sku6.insert(0,aldatas[35])
                qty6.insert(0,aldatas[36])
                rate6.insert(0,aldatas[37])
                total6.insert(0,aldatas[38])
            except:
                pass    
            x=x+0.02
        if aldatas[39]:   
            def getproductcomp7(s):
                def clearskucomp7():
                    sku7.delete(0,END)
                    rate7.delete(0,END)
                clearskucomp7()    
                prodd=prod7.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku7.insert(0,fet[0])
                    rate7.insert(0,fet[2])
                elif fetch:
                    sku7.insert(0,fetch[0])
                    rate7.insert(0,fetch[2])
            def calculatetotal7(xx):  
                global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29  
                def clear_text7():
                    total7.delete(0, END) 
                q7=float(qty7.get())
                r7=float(rate7.get())
                tot7=(q7*r7)
                subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                clear_text7()
                total7.insert(0,tot7)
                clearcomptotquan()
                totalquantity.insert(0,qtytotal)
                totalquantity.insert(14,'Nos')
                clearcomptotamount()
                totalamount.insert(0,subtot)
                costofcomp.insert(0,subtot)
            prod7=ttk.Combobox(frame1,values=pro,font=(4))
            prod7.bind('<<ComboboxSelected>>',getproductcomp7)
            prod7.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku7=tk.Entry(frame1,font=(4))
            sku7.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)     
            qty7=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty7.bind('<FocusIn>',calculatetotal7)
            qty7.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate7=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate7.bind('<FocusIn>',calculatetotal7)
            rate7.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total7=tk.Entry(frame1,font=(4))
            total7.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            try:
                prod7.insert(0,aldatas[39])
                sku7.insert(0,aldatas[40])
                qty7.insert(0,aldatas[41])
                rate7.insert(0,aldatas[42])
                total7.insert(0,aldatas[43])
            except:
                pass
        if aldatas[44]!='':    
            def getproductcomp8(s):
                def clearskucomp8():
                    sku8.delete(0,END)
                    rate8.delete(0,END)
                clearskucomp8()    
                prodd=prod8.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku8.insert(0,fet[0])
                    rate8.insert(0,fet[2])
                elif fetch:
                    sku8.insert(0,fetch[0])
                    rate8.insert(0,fetch[2])
            def calculatetotal8(xx):   
                global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                def clear_text8():
                    total8.delete(0, END) 
                q8=float(qty8.get())
                r8=float(rate8.get())
                tot8=(q8*r8)
                subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                clear_text8()
                total8.insert(0,tot8)
                clearcomptotquan()
                totalquantity.insert(0,qtytotal)
                totalquantity.insert(14,'Nos')
                clearcomptotamount()
                totalamount.insert(0,subtot)
                costofcomp.insert(0,subtot)
            prod8=ttk.Combobox(frame1,values=pro)
            prod8.bind('<<ComboboxSelected>>',getproductcomp8)
            prod8.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku8=tk.Entry(frame1)
            sku8.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty8=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty8.bind('<FocusIn>',calculatetotal8)
            qty8.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate8=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate8.bind('<FocusIn>',calculatetotal8)
            rate8.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total8=tk.Entry(frame1,font=(4))
            total8.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            try:
                prod8.insert(0,aldatas[44])
                sku8.insert(0,aldatas[45])
                qty8.insert(0,aldatas[46])
                rate8.insert(0,aldatas[47])
                total8.insert(0,aldatas[48])
            except:
                pass
        if aldatas[49]!='':       
            def getproductcomp9(s):
                def clearskucomp9():
                    sku9.delete(0,END)
                    rate9.delete(0,END)
                clearskucomp9()    
                prodd=prod9.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku9.insert(0,fet[0])
                    rate9.insert(0,fet[2])
                elif fetch:
                    sku9.insert(0,fetch[0])
                    rate9.insert(0,fetch[2])          
            def calculatetotal9(xx): 
                global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                def clear_text9():
                    total9.delete(0, END) 
                q9=float(qty9.get())
                r9=float(rate9.get())
                tot9=(q9*r9)
                subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                clear_text9()
                total9.insert(0,tot9)
                clearcomptotquan()
                totalquantity.insert(0,qtytotal)
                totalquantity.insert(14,'Nos')
                clearcomptotamount()
                totalamount.insert(0,subtot)
                costofcomp.insert(0,subtot)
            prod9=ttk.Combobox(frame1,values=pro)
            prod9.bind('<<ComboboxSelected>>',getproductcomp9)
            prod9.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku9=tk.Entry(frame1)
            sku9.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan9=IntVar()  
            qty9=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty9.bind('<FocusIn>',calculatetotal9)
            qty9.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price9=IntVar()
            rate9=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate9.bind('<FocusIn>',calculatetotal9)
            rate9.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total9=tk.Entry(frame1,font=(4))
            total9.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            try:
                prod9.insert(0,aldatas[49])
                sku9.insert(0,aldatas[50])
                qty9.insert(0,aldatas[51])
                rate9.insert(0,aldatas[52])
                total9.insert(0,aldatas[53])
            except:
                pass
        if aldatas[54]!='':       
            def getproductcomp10(s):
                def clearskucomp10():
                    sku10.delete(0,END)
                    rate10.delete(0,END)
                clearskucomp10()    
                prodd=prod10.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku10.insert(0,fet[0])
                    rate10.insert(0,fet[2])
                elif fetch:
                    sku10.insert(0,fetch[0])
                    rate10.insert(0,fetch[2])          
            def calculatetotal10(xx): 
                global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                def clear_text10():
                    total10.delete(0, END) 
                q10=float(qty10.get())
                r10=float(rate10.get())
                tot10=(q10*r10)
                subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                clear_text10()
                total10.insert(0,tot10)
                clearcomptotquan()
                totalquantity.insert(0,qtytotal)
                totalquantity.insert(14,'Nos')
                clearcomptotamount()
                totalamount.insert(0,subtot)
                costofcomp.insert(0,subtot)
            prod10=ttk.Combobox(frame1,values=pro)
            prod10.bind('<<ComboboxSelected>>',getproductcomp10)
            prod10.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku10=tk.Entry(frame1)
            sku10.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty10=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty10.bind('<FocusIn>',calculatetotal10)
            qty10.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate10=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate10.bind('<FocusIn>',calculatetotal10)
            rate10.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total10=tk.Entry(frame1,font=(4))
            total10.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            try:
                prod10.insert(0,aldatas[54])
                sku10.insert(0,aldatas[55])
                qty10.insert(0,aldatas[56])
                rate10.insert(0,aldatas[57])
                total10.insert(0,aldatas[58])
            except:
                pass
        if aldatas[59]!='':       
            def getproductcomp11(s):
                def clearskucomp11():
                    sku11.delete(0,END)
                    rate11.delete(0,END)
                clearskucomp11()    
                prodd=prod11.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku11.insert(0,fet[0])
                    rate11.insert(0,fet[2])
                elif fetch:
                    sku11.insert(0,fetch[0])
                    rate11.insert(0,fetch[2])          
            def calculatetotal11(xx): 
                global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                def clear_text11():
                    total11.delete(0, END) 
                q11=float(qty11.get())
                r11=float(rate11.get())
                tot11=(q11*r11)
                subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                clear_text11()
                total11.insert(0,tot11)
                clearcomptotquan()
                totalquantity.insert(0,qtytotal)
                totalquantity.insert(14,'Nos')
                clearcomptotamount()
                totalamount.insert(0,subtot)
                costofcomp.insert(0,subtot)
            prod11=ttk.Combobox(frame1,values=pro)
            prod11.bind('<<ComboboxSelected>>',getproductcomp11)
            prod11.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku11=tk.Entry(frame1)
            sku11.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty11=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty11.bind('<FocusIn>',calculatetotal11)
            qty11.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate11=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate11.bind('<FocusIn>',calculatetotal11)
            rate11.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total11=tk.Entry(frame1,font=(4))
            total11.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            try:
                prod11.insert(0,aldatas[59])
                sku11.insert(0,aldatas[60])
                qty11.insert(0,aldatas[61])
                rate11.insert(0,aldatas[62])
                total11.insert(0,aldatas[63])
            except:
                pass
        if aldatas[64]!='':       
            def getproductcomp12(s):
                def clearskucomp12():
                    sku12.delete(0,END)
                    rate12.delete(0,END)
                clearskucomp12()    
                prodd=prod12.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    sku12.insert(0,fet[0])
                    rate12.insert(0,fet[2])
                elif fetch:
                    sku12.insert(0,fetch[0])
                    rate12.insert(0,fetch[2])          
            def calculatetotal12(xx): 
                global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                def clear_text12():
                    total12.delete(0, END) 
                q12=float(qty12.get())
                r12=float(rate12.get())
                tot12=(q12*r12)
                subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                clear_text12()
                total12.insert(0,tot12)
                clearcomptotquan()
                totalquantity.insert(0,qtytotal)
                totalquantity.insert(14,'Nos')
                clearcomptotamount()
                totalamount.insert(0,subtot)
                costofcomp.insert(0,subtot)
            prod12=ttk.Combobox(frame1,values=pro)
            prod12.bind('<<ComboboxSelected>>',getproductcomp12)
            prod12.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku12=tk.Entry(frame1)
            sku12.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty12=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty12.bind('<FocusIn>',calculatetotal12)
            qty12.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate12=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate12.bind('<FocusIn>',calculatetotal12)
            rate12.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total12=tk.Entry(frame1,font=(4))
            total12.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            try:
                prod12.insert(0,aldatas[59])
                sku12.insert(0,aldatas[60])
                qty12.insert(0,aldatas[61])
                rate12.insert(0,aldatas[62])
                total12.insert(0,aldatas[63])
            except:
                pass                 
        ##adding new row                                                                                                                                                                                                                                                                    
        #coproducts/scrap
        #
        ##
        ######
        tk.Label(frame1,text='Coproducts/Scrap',bg='#243e54',font=('Times New Roman',24)).place(relx=0.51,rely=0.140)
        tk.Label(frame1,text='Max :20',bg='#243e54',font=('Times New Roman',12)).place(relx=0.43,rely=0.143)
        tk.Label(frame1,text='Product Name',font=('times new roman', 14),bg='#2f516f').place(relx=0.41,rely=0.17)
        tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.505,rely=0.17)
        tk.Label(frame1,text='Quantity',font=('times new roman', 14),bg='#2f516f').place(relx=0.585,rely=0.17)
        tk.Label(frame1,text='Price',font=('times new roman', 14),bg='#2f516f').place(relx=0.65,rely=0.17)
        tk.Label(frame1,text='Amount',font=('times new roman', 14),bg='#2f516f').place(relx=0.72,rely=0.17)
        #row11
        global aldatass,qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
        qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
        qtytotalt1,subtott1=0,0.0
        abcde='Coproducts/Scrap'
        cur.execute("SELECT * FROM rawmaterials WHERE productionid =%s and Type =%s",[b[0],abcde])
        aldatass=cur.fetchone()
        def getproductscrap(s):
            def clearskuscrap():
                skuu1.delete(0,END)
                ratee1.delete(0,END)
            clearskuscrap()    
            prodd=prodd1.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                skuu1.insert(0,fet[0])
                ratee1.insert(0,fet[2])
            elif fetch:
                skuu1.insert(0,fetch[0])
                ratee1.insert(0,fet[2])
        def calculatescraptotal(x):
            global clearscraptotamount,qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
            def clear_scraptext():
                totall1.delete(0, END) 
            def clearscraptotamount():
                totalscrapamount.delete(0,END) 
            qq1=float(qtyy1.get())
            rr1=float(ratee1.get())
            tott1=(qq1*rr1)
            clear_scraptext()
            totall1.insert(0,tott1)
            subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
            clearscraptotamount()
            totalscrapamount.insert(0,subtott1)
        prodd1=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prodd1.insert(0,aldatass[4])
        except:
            pass
        prodd1.bind('<<ComboboxSelected>>',getproductscrap)
        prodd1.place(relx=0.41,rely=0.19,relheight=0.015,relwidth=0.08)
        skuu1=tk.Entry(frame1,font=(4))
        try:
            skuu1.insert(0,aldatass[5])
        except:
            pass
        skuu1.place(relx=0.505,rely=0.19,relheight=0.015,relwidth=0.06)
        qtyy1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qtyy1.delete(0,END)
            qtyy1.insert(0,aldatass[6])
        except:
            pass
        qtyy1.bind('<FocusIn>',calculatescraptotal)
        qtyy1.place(relx=0.585,rely=0.19,relheight=0.015,relwidth=0.05)
        ratee1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            ratee1.delete(0,END)
            ratee1.insert(0,aldatass[7])
        except:
            pass
        ratee1.bind('<FocusIn>',calculatescraptotal)
        ratee1.place(relx=0.65,rely=0.19,relheight=0.015,relwidth=0.05)
        totall1=tk.Entry(frame1,font=(4))
        try:
            totall1.insert(0,aldatass[8])
        except:
            pass        
        totall1.place(relx=0.72,rely=0.19,relheight=0.015,relwidth=0.05)
        #row22
        def getproductscrap2(s):
            def clearskuscrap2():
                skuu2.delete(0,END)
                ratee2.delete(0,END)
            clearskuscrap2()    
            prodd=prodd2.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                skuu2.insert(0,fet[0])
                ratee2.insert(0,fet[2])
            elif fetch:
                skuu2.insert(0,fetch[0])
                ratee2.insert(0,fetch[2])
        def calculatescraptotal2(x):
            global qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
            def clear_scraptext2():
                totall2.delete(0, END) 
            qq2=float(qtyy2.get())
            rr2=float(ratee2.get())
            tott2=(qq2*rr2)
            clear_scraptext2()
            totall2.insert(0,tott2)
            subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
            clearscraptotamount()
            totalscrapamount.insert(0,subtott1)
        prodd2=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prodd2.insert(0,aldatass[9])
        except:
            pass
        prodd2.bind('<<ComboboxSelected>>',getproductscrap2)
        prodd2.place(relx=0.41,rely=0.21,relheight=0.015,relwidth=0.08)
        skuu2=tk.Entry(frame1,font=(4))
        try:
            skuu2.insert(0,aldatass[10])
        except:
            pass
        skuu2.place(relx=0.505,rely=0.21,relheight=0.015,relwidth=0.06)
        qtyy2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qtyy2.delete(0,END)
            qtyy2.insert(0,aldatass[11])
        except:
            pass
        qtyy2.bind('<FocusIn>',calculatescraptotal2)
        qtyy2.place(relx=0.585,rely=0.21,relheight=0.015,relwidth=0.05)
        ratee2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            ratee2.delete(0,END)
            ratee2.insert(0,aldatass[12])
        except:
            pass
        ratee2.bind('<FocusIn>',calculatescraptotal2)
        ratee2.place(relx=0.65,rely=0.21,relheight=0.015,relwidth=0.05)
        totall2=tk.Entry(frame1,font=(4))
        try:
            totall2.insert(0,aldatass[13])
        except:
            pass     
        totall2.place(relx=0.72,rely=0.21,relheight=0.015,relwidth=0.05)
            #row33
        def getproductscrap3(s):
            global qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
            def clearskuscrap3():
                skuu3.delete(0,END)
                ratee3.delete(0,END)
            clearskuscrap3()    
            prodd=prodd3.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                skuu3.insert(0,fet[0])
                ratee3.insert(0,fet[2])
            elif fetch:
                skuu3.insert(0,fetch[0]) 
                ratee3.insert(0,fetch[2])   
        def calculatescraptotal3(x):
            global qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
            def clear_scraptext3():
                totall3.delete(0, END) 
            qq3=float(qtyy3.get())
            rr3=float(ratee3.get())
            tott3=(qq3*rr3)
            subtott3=tott3
            clear_scraptext3()
            totall3.insert(0,tott3)
            subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
            clearscraptotamount()
            totalscrapamount.insert(0,subtott1)
        prodd3=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prodd3.insert(0,aldatass[14])
        except:
            pass
        prodd3.bind('<<ComboboxSelected>>',getproductscrap3)
        prodd3.place(relx=0.41,rely=0.23,relheight=0.015,relwidth=0.08)
        skuu3=tk.Entry(frame1,font=(4))
        try:
            skuu3.insert(0,aldatass[15])
        except:
            pass
        skuu3.place(relx=0.505,rely=0.23,relheight=0.015,relwidth=0.06)
        qtyy3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qtyy3.delete(0,END)
            qtyy3.insert(0,aldatass[16])
        except:
            pass
        qtyy3.bind('<FocusIn>',calculatescraptotal3)
        qtyy3.place(relx=0.585,rely=0.23,relheight=0.015,relwidth=0.05)
        ratee3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            ratee3.delete(0,END)
            ratee3.insert(0,aldatass[17])
        except:
            pass
        ratee3.bind('<FocusIn>',calculatescraptotal3)
        ratee3.place(relx=0.65,rely=0.23,relheight=0.015,relwidth=0.05)
        totall3=tk.Entry(frame1,font=(4))
        try:
            totall3.insert(0,aldatass[18])
        except:
            pass     
        totall3.place(relx=0.72,rely=0.23,relheight=0.015,relwidth=0.05)
                #row44
        def getproductscrap4(s):
            
            def clearskuscrap4():
                skuu4.delete(0,END)
                ratee4.delete(0,END)
            clearskuscrap4()    
            prodd=prodd4.get()
            cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            if fet:
                skuu4.insert(0,fet[0])
                ratee4.insert(0,fet[2])
            elif fetch:
                skuu4.insert(0,fetch[0])  
                ratee4.insert(0,fetch[2]) 
        def calculatescraptotal4(x):
            global qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
            def clear_scraptext4():
                totall4.delete(0, END) 
            qq4=float(qtyy4.get())
            rr4=float(ratee4.get())
            tott4=(qq4*rr4)
            clear_scraptext4()
            totall4.insert(0,tott4)
            subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
            clearscraptotamount()
            totalscrapamount.insert(0,subtott1)
        prodd4=ttk.Combobox(frame1,values=pro,font=(4))
        try:
            prodd4.insert(0,aldatass[19])
        except:
            pass
        prodd4.bind('<<ComboboxSelected>>',getproductscrap4)
        prodd4.place(relx=0.41,rely=0.25,relheight=0.015,relwidth=0.08)
        skuu4=tk.Entry(frame1,font=(4))
        try:
            skuu4.insert(0,aldatass[20])
        except:
            pass
        skuu4.place(relx=0.505,rely=0.25,relheight=0.015,relwidth=0.06)
        qtyy4=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            qtyy4.delete(0,END)
            qtyy4.insert(0,aldatass[21])
        except:
            pass
        qtyy4.bind('<FocusIn>',calculatescraptotal4)
        qtyy4.place(relx=0.585,rely=0.25,relheight=0.015,relwidth=0.05)
        ratee4=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        try:
            ratee4.delete(0,END)
            ratee4.insert(0,aldatass[22])
        except:
            pass
        ratee4.bind('<FocusIn>',calculatescraptotal4)
        ratee4.place(relx=0.65,rely=0.25,relheight=0.015,relwidth=0.05)
        totall4=tk.Entry(frame1,font=(4))
        try:
            totall4.insert(0,aldatass[23])
        except:
            pass     
        totall4.place(relx=0.72,rely=0.25,relheight=0.015,relwidth=0.05)                                                                                  
        tk.Label(frame,text='Total Quantity',font=('times new roman', 16),bg='#2f516f').place(relx=0.25,rely=0.40,relwidth=0.1,relheight=0.03)
        totalquantity=tk.Entry(frame,font=(8))
        try:
            totalquantity.insert(0,aldatas[160])
        except:
            pass         
        totalquantity.place(relx=0.26,rely=0.43,relwidth=0.08,relheight=0.02)
        tk.Label(frame,text='Total Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.38,rely=0.40,relwidth=0.1,relheight=0.03)
        totalamount=tk.Entry(frame,font=(8))
        try:
            totalamount.insert(0,aldatas[161])
        except:
            pass 
        totalamount.place(relx=0.39,rely=0.43,relwidth=0.08,relheight=0.02)
        tk.Label(frame,text='Total Scrap Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=0.41,relwidth=0.15,relheight=0.03)
        totalscrapamount=tk.Entry(frame,font=(6))
        try:
            totalscrapamount.insert(0,aldatass[161])
        except:
                pass
        totalscrapamount.place(relx=0.79,rely=0.41,relwidth=0.1,relheight=0.02)
        tk.Label(frame,text='Cost of components',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=0.44,relwidth=0.15,relheight=0.03)
        costofcomp=tk.Entry(frame,font=(6))
        try:
            costofcomp.insert(0,aldatas[161])
        except:
            pass    
        costofcomp.place(relx=0.79,rely=0.44,relwidth=0.1,relheight=0.02)
        tk.Label(frame,text='Type of Additional Cost',font=('times new roman', 16),bg='#2f516f').place(relx=0.53,rely=0.47,relwidth=0.15,relheight=0.03)
        additional1=tk.Entry(frame,font=(6))
        try:
            additional1.insert(0,aldatas[154])
        except:
            pass
        additional1.place(relx=0.55,rely=0.50,relwidth=0.12,relheight=0.02)
        tk.Label(frame,text='Percentage',font=('times new roman', 16),bg='#2f516f').place(relx=0.67,rely=0.47,relwidth=0.1,relheight=0.03)
        global v,addbtn,ded,ded1,ded2,ded3,totaddlcost
        v=0.56
        ded,ded1,ded2,ded3=0.0,0.0,0.0,0.0
        def labels():
            global v,addlcost,totaddlcost,ded,ded2,ded3,ded1,subtot,effccost,effcost
            effccost=0.0
            tk.Label(frame1,text='QTY',bg='#243e54',font=('Times New Roman',14)).place(relx=0.67,rely=0.140)
            def quantityy(x):
                qq=int(quantity.get())
                efrate=(effccost/qq)
                effcost.delete(0,END)
                effcost.insert(0,effccost)
                effrate.delete(0,END)
                effrate.insert(0,efrate)
            quantity=tk.Spinbox(frame1,font=(6),from_=0,to=50)
            quantity.bind('<FocusIn>',quantityy)
            quantity.place(relx=0.70,rely=0.140,relwidth=0.03,relheight=0.015)
            tk.Label(frame,text='Total Addl. Cost:',font=('times new roman', 16),bg='#2f516f').place(relx=0.53,rely=v,relwidth=0.15,relheight=0.03)
            addlcost=tk.Entry(frame,font=(6))
            totaddlcost=float(round(ded+ded1+ded2+ded3))   
            addlcost.insert(0,totaddlcost) 
            addlcost.place(relx=0.79,rely=v,relwidth=0.1,relheight=0.02) 
            tk.Label(frame,text='Effective Cost:',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=v+0.03,relwidth=0.25,relheight=0.03) 
            effcost=tk.Entry(frame,font=(6))  
            effccost=round(subtot-totaddlcost) 
            effcost.delete(0,END)
            effcost.insert(0,effccost)     
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            effccost=round(subtot-totaddlcost) 
            effcost.place(relx=0.79,rely=v+0.03,relwidth=0.1,relheight=0.02) 
            tk.Label(frame,text='Effective rate of Primary Item:',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=v+0.06,relwidth=0.2,relheight=0.03)
            effrate=tk.Entry(frame,font=(6))   
            effrate.place(relx=0.79,rely=v+0.06,relwidth=0.1,relheight=0.02) 
        def percen1(q):
            global ded,ded2,ded3,ded1,totaddlcost,clearaddtotcost,subtot
            add1=additional1.get()
            print(subtot)
            percen=int(percentage1.get())
            if add1:              
                ded=float((percen/100)*subtot)
                def clear_ded1():
                    addtotal1.delete(0,END) 
                clear_ded1()    
                addtotal1.insert(0,ded)
                def clearaddtotcost():
                    addlcost.delete(0,END)  
                clearaddtotcost()
                totaddlcost=float(round(ded+ded1+ded2+ded3)) 
                addlcost.insert(0,totaddlcost)  
                effcost.delete(0,END)
                effccost=round(subtot-totaddlcost) 
                effcost.insert(0,effccost)
                labels()             
        percentage1=tk.Entry(frame,font=(6))
        try:
            percentage1.insert(0,aldatas[155])
        except:
                pass
        percentage1.bind('<KeyRelease>',percen1)
        percentage1.place(relx=0.697,rely=0.50,relwidth=0.04,relheight=0.02)    
        tk.Label(frame,font=(6),text='%').place(relx=0.72,rely=0.50,relwidth=0.01,relheight=0.02)   
        addtotal1=tk.Entry(frame,font=(6))
        try:
            addtotal1.insert(0,aldatas[156])
        except:
                pass
        addtotal1.place(relx=0.79,rely=0.50,relwidth=0.1,relheight=0.02)  
        labels()
        #additional2
        additional2=tk.Entry(frame,font=(6))
        try:
            additional2.insert(0,aldatas[157])
        except:
                pass
        additional2.place(relx=0.55,rely=0.53,relwidth=0.12,relheight=0.02)
        def percen2(q):
            global ded,ded2,ded3,ded1,totaddlcost
            add2=additional2.get()
            if add2:
                percen=float(percentage2.get())
                ded1=float((percen/100)*subtot)
                def clear_ded2():
                        addtotal2.delete(0,END)   
                clear_ded2()   
                addtotal2.insert(0,ded1) 
                clearaddtotcost()
                totaddlcost=float(round(ded+ded1+ded2+ded3))  
                addlcost.insert(0,totaddlcost)     
                labels()                
        percentage2=tk.Entry(frame,font=(6))
        try:
            percentage2.insert(0,aldatas[158])
        except:
                pass
        percentage2.bind('<KeyRelease>',percen2)
        percentage2.place(relx=0.697,rely=0.53,relwidth=0.04,relheight=0.02)    
        tk.Label(frame,font=(6),text='%').place(relx=0.72,rely=0.53,relwidth=0.01,relheight=0.02)
        addtotal2=tk.Entry(frame,font=(6))
        try:
            addtotal2.insert(0,aldatas[159])
        except:
                pass
        addtotal2.place(relx=0.79,rely=0.53,relwidth=0.1,relheight=0.02)
        labels()
        #additional3
        def newadditional():
            global addbtn1,v,ded,ded2,ded3,ded1,totaddlcost
            def desaddbtn():
                addbtn.destroy()   
            def percen3(q):
                add3=additional3.get()
                if add3:
                    percen=float(percentage3.get())
                    ded2=float((percen/100)*subtot)
                    def clear_ded3():
                            addtotal3.delete(0,END)  
                    clear_ded3()   
                    addtotal3.insert(0,ded2)
                    clearaddtotcost()
                    totaddlcost=float(round(ded+ded1+ded2+ded3))    
                    addlcost.insert(0,totaddlcost)              
            additional3=tk.Entry(frame,font=(6))
            additional3.place(relx=0.55,rely=v,relwidth=0.12,relheight=0.02)
            percentage3=tk.Entry(frame,font=(6))
            percentage3.bind('<KeyRelease>',percen3)
            percentage3.place(relx=0.697,rely=v,relwidth=0.04,relheight=0.02)
            tk.Label(frame,font=(6),text='%').place(relx=0.72,rely=v,relwidth=0.01,relheight=0.02)   
            addtotal3=tk.Entry(frame,font=(6))
            addtotal3.place(relx=0.79,rely=v,relwidth=0.1,relheight=0.02)  
            addbtn1=tk.Button(frame,text='+',font=(12),command=newadditional2)
            addbtn1.place(relx=0.75,rely=v,relwidth=0.03,relheight=0.02) 
            v=v+0.03
            desaddbtn()  
            labels()
        #additinal4
        def newadditional2():
            global v,ded,ded3,ded1,totaddlcost,ded2
            def desaddbtn1():
                addbtn1.destroy()   
            def percen4(q):
                add4=additional4.get()
                if add4:
                    percen=float(percentage4.get())
                    ded3=float((percen/100)*subtot)
                    def clear_ded4():
                            addtotal4.delete(0,END)  
                    clear_ded4()   
                    addtotal4.insert(0,ded3)
                    clearaddtotcost()
                    totaddlcost=float(round(ded+ded1+ded3+ded2))
                    addlcost.insert(0,totaddlcost)                          
            additional4=tk.Entry(frame,font=(6))
            additional4.place(relx=0.55,rely=v,relwidth=0.12,relheight=0.02)
            percentage4=tk.Entry(frame,font=(6))
            percentage4.bind('<KeyRelease>',percen4)
            percentage4.place(relx=0.697,rely=v,relwidth=0.04,relheight=0.02)
            tk.Label(frame,font=(6),text='%').place(relx=0.72,rely=v,relwidth=0.01,relheight=0.02)   
            addtotal4=tk.Entry(frame,font=(6))
            addtotal4.place(relx=0.79,rely=v,relwidth=0.1,relheight=0.02)  
            v=v+0.03
            labels()
            desaddbtn1()  
        labels()    
        addbtn=tk.Button(frame,text='+',font=(12),command=newadditional)
        addbtn.place(relx=0.75,rely=0.53,relwidth=0.03,relheight=0.02) 
        def editgetproductiondetails():
            p=product.get()
            sk=sku.get()
            hs=hsn.get()
            qt=quanty.get()
            md=mandate.get()
            ed=expdate.get()
            cid=2
            cur.execute("UPDATE  production set productname =%s,sku =%s,hsn =%s,quantity =%s,manufacturing_date =%s,expiry_date =%s WHERE productionid =%s and cid =%s",(p,sk,hs,qt,md,ed,b[0],cid))
            mydata.commit()
            #components
            #1st row
            p1,p2,p3,p4,p5,p6=prod.get(),prod1.get(),prod2.get(),prod3.get(),prod4.get(),prod5.get()
            sk1,sk2,sk3,sk4,sk5,sk6=sku.get(),sku1.get(),sku2.get(),sku3.get(),sku4.get(),sku5.get()
            qt1,qt2,qt3,qt4,qt5,qt6=qty.get(),qty1.get(),qty2.get(),qty3.get(),qty4.get(),qty5.get()
            pr1,pr2,pr3,pr4,pr5,pr6=rate.get(),rate1.get(),rate2.get(),rate3.get(),rate4.get(),rate5.get()
            tt1,tt2,tt3,tt4,tt5,tt6=total.get(),total1.get(),total2.get(),total3.get(),total4.get(),total5.get()    
            cur.execute("""UPDATE rawmaterials set prod =%s,sku =%s,qty =%s,price =%s,total =%s,prod1 =%s,prod2 =%s,prod3 =%s,prod4 =%s,prod5 =%s,qty1 =%s,qty2=%s,qty3=%s,qty4=%s,qty5=%s,sku1=%s,sku2=%s,sku3=%s,sku4=%s,sku5=%s,price1=%s,price2=%s,price3=%s,price4=%s,price5=%s,total1=%s,total2=%s,total3=%s,total4=%s,total5=%s,totalquantity=%s,subtotal=%s WHERE productionid =%s and cid =%s""",
            (p1,sk1,qt1,pr1,tt1,p2,p3,p4,p5,p6,qt2,qt3,qt4,qt5,qt6,sk2,sk3,sk4,sk5,sk6,pr2,pr3,pr4,pr5,pr6,tt2,tt3,tt4,tt5,tt6,qtytotal,subtot,b[0],cid))
            mydata.commit()
            if prod6.get():
                p7=prod6.get()
                sk7=sku6.get()
                qt7=qty6.get()
                pr7=rate6.get()
                tt7=total6.get()
                cur.execute("UPDATE rawmaterials set prod6=%s,sku6=%s,qty6=%s,price6=%s,total =%s WHERE productionid =%s and cid =%s",(p7,sk7,qt7,pr7,tt7,b[0],cid))
                mydata.commit()
            if prod7.get():
                p8=prod7.get()
                sk8=sku7.get()
                qt8=qty7.get()
                pr8=rate7.get()
                tt8=total7.get()
                cur.execute("UPDATE rawmaterials set prod7=%s,sku7=%s,qty7=%s,price7=%s,total =%s WHERE productionid =%s and cid =%s",(p8,sk8,qt8,pr8,tt8,b[0],cid))
                mydata.commit() 
            if prod8.get():
                p9=prod8.get()
                sk9=sku8.get()
                qt9=qty8.get()
                pr9=rate8.get()
                tt9=total8.get()
                cur.execute("UPDATE rawmaterials set prod8=%s,sku8=%s,qty8=%s,price8=%s,total8 =%s WHERE productionid =%s and cid =%s",(p9,sk9,qt9,pr9,tt9,b[0],cid))
                mydata.commit()
            if prod9.get():
                p10=prod9.get()
                sk10=sku9.get()
                qt10=qty9.get()
                pr10=rate9.get()
                tt10=total9.get()
                cur.execute("UPDATE rawmaterials set prod9=%s,sku9=%s,qty9=%s,price9=%s,total9 =%s WHERE productionid =%s and cid =%s",(p10,sk10,qt10,pr10,tt10,b[0],cid))
                mydata.commit()               
            pp1,pp2,pp3,pp4=prodd1.get(),prodd2.get(),prodd3.get(),prodd4.get()
            skk1,skk2,skk3,skk4=skuu1.get(),skuu2.get(),skuu3.get(),skuu4.get()
            qtt1,qtt2,qtt3,qtt4=qtyy1.get(),qtyy2.get(),qtyy3.get(),qtyy4.get()
            prr1,prr2,prr3,prr4=ratee1.get(),ratee2.get(),ratee3.get(),ratee4.get()
            ttt1,ttt2,ttt3,ttt4=totall1.get(),totall2.get(),totall3.get(),totall4.get()
            type1='Coproducts/scrap'

            estwin.destroy()
        hf2.place(relx=0.1,rely=0.10,relwidth=0.8,relheight=0.3)
        tk.Button(frame,text='CREATE',bg='#243e54',font=('Times New Roman',20),command=editgetproductiondetails).place(relx=0.45,rely=0.73,relwidth=0.1,relheight=0.03)
        estwin.mainloop()
    edit_btn = Button(f2, text="Edit",command=productionedit)
    edit_btn.place(relx=0.35,rely=0.85,relheight=0.1,relwidth=0.1)
    def productiondelete():
        # Get selected item to Delete
        str=treevv.focus() 
        values=treevv.item(str,'values')
        b=[values[0]]
        cur.execute("DELETE FROM production WHERE productionid=%s",(b))
        mydata.commit()
        treevv.delete(str)
    del_btn = Button(f2, text="Delete",command=productiondelete)
    del_btn.place(relx=0.5,rely=0.85,relheight=0.1,relwidth=0.1)  
    f2.place(relx=0.1,rely=0.2,relheight=0.7,relwidth=0.8)
    viewmatwin.mainloop()
    
viewmaterials()    