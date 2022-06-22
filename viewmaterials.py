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
        print(s)
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
        product.insert(0,s[2])
        product.place(relx=0.15,rely=0.025,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.01)
        sku=tk.Entry(frame1)
        sku.insert(0,s[3])
        sku.place(relx=0.45,rely=0.025,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='HSN',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.045)
        hsn=tk.Entry(frame1)
        hsn.insert(0,s[4])
        hsn.place(relx=0.15,rely=0.06,relwidth=0.2,relheight=0.015)
        tk.Label(frame1,text='QUANTITY',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.045)
        quanty=tk.Entry(frame1)
        quanty.insert(0,s[5])
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
        global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
        q,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        qtytotal,subtot=0,0.0
        tot,tot1,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
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
        prod.bind('<<ComboboxSelected>>',getproductcomp)
        prod.place(relx=0.01,rely=0.19,relheight=0.015,relwidth=0.08)
        sku=tk.Entry(frame1,font=(4))
        sku.place(relx=0.105,rely=0.19,relheight=0.015,relwidth=0.06)
        qty=tk.Spinbox(frame1,from_=0,to=2000,font=(4))
        qty.bind('<FocusIn>',calculatetotal)
        qty.place(relx=0.18,rely=0.19,relheight=0.015,relwidth=0.05)
        rate=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        rate.bind('<FocusIn>',calculatetotal)
        rate.place(relx=0.245,rely=0.19,relheight=0.015,relwidth=0.05)
        total=tk.Entry(frame1,font=(4))
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
        prod1.bind('<<ComboboxSelected>>',getproductcomp1)
        prod1.place(relx=0.01,rely=0.21,relheight=0.015,relwidth=0.08)
        sku1=tk.Entry(frame1,font=(4))
        sku1.place(relx=0.105,rely=0.21,relheight=0.015,relwidth=0.06)
        qty1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qty1.bind('<FocusIn>',calculatetotal1)
        qty1.place(relx=0.18,rely=0.21,relheight=0.015,relwidth=0.05)
        rate1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        rate1.bind('<FocusIn>',calculatetotal1)
        rate1.place(relx=0.245,rely=0.21,relheight=0.015,relwidth=0.05)
        total1=tk.Entry(frame1,font=(4))
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
        prod2.bind('<<ComboboxSelected>>',getproductcomp2)
        prod2.place(relx=0.01,rely=0.23,relheight=0.015,relwidth=0.08)
        sku2=tk.Entry(frame1,font=(4))
        sku2.place(relx=0.105,rely=0.23,relheight=0.015,relwidth=0.06)
        qty2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qty2.bind('<FocusIn>',calculatetotal2)
        qty2.place(relx=0.18,rely=0.23,relheight=0.015,relwidth=0.05)
        rate2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        rate2.bind('<FocusIn>',calculatetotal2)
        rate2.place(relx=0.245,rely=0.23,relheight=0.015,relwidth=0.05)
        total2=tk.Entry(frame1,font=(4))
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
        prod3.bind('<<ComboboxSelected>>',getproductcomp3)
        prod3.place(relx=0.01,rely=0.25,relheight=0.015,relwidth=0.08)
        sku3=tk.Entry(frame1,font=(4))
        sku3.place(relx=0.105,rely=0.25,relheight=0.015,relwidth=0.06)
        qty3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qty3.bind('<FocusIn>',calculatetotal3)
        qty3.place(relx=0.18,rely=0.25,relheight=0.015,relwidth=0.05)
        rate3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        rate3.bind('<FocusIn>',calculatetotal3)
        rate3.place(relx=0.245,rely=0.25,relheight=0.015,relwidth=0.05)
        total3=tk.Entry(frame1,font=(4))
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
        prod4.bind('<<ComboboxSelected>>',getproductcomp4)
        prod4.place(relx=0.01,rely=0.27,relheight=0.015,relwidth=0.08)
        sku4=tk.Entry(frame1,font=(4))
        sku4.place(relx=0.105,rely=0.27,relheight=0.015,relwidth=0.06)
        qty4=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        qty4.bind('<FocusIn>',calculatetotal4)
        qty4.place(relx=0.18,rely=0.27,relheight=0.015,relwidth=0.05)
        rate4=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        rate4.bind('<FocusIn>',calculatetotal4)
        rate4.place(relx=0.245,rely=0.27,relheight=0.015,relwidth=0.05)
        total4=tk.Entry(frame1,font=(4))
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
        prod5.bind('<<ComboboxSelected>>',getproductcomp5)
        prod5.place(relx=0.01,rely=0.29,relheight=0.015,relwidth=0.08)
        sku5=tk.Entry(frame1,font=(4))
        sku5.place(relx=0.105,rely=0.29,relheight=0.015,relwidth=0.06)
        qty5=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        qty5.bind('<FocusIn>',calculatetotal5)
        qty5.place(relx=0.18,rely=0.29,relheight=0.015,relwidth=0.05)
        rate5=tk.Spinbox(frame1,from_=0,to=50,font=(4))
        rate5.bind('<FocusIn>',calculatetotal5)
        rate5.place(relx=0.245,rely=0.29,relheight=0.015,relwidth=0.05)
        total5=tk.Entry(frame1,font=(4))
        total5.place(relx=0.31,rely=0.29,relheight=0.015,relwidth=0.05)
        ##adding new row
        global x,btn,fetchrow1details,prod6
        x=0.31
        #row7
        def addnewrow1(): 
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
            global x,btn1,sku6,qty6,price6,total6,prod6        
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
            def clear1():
                btn.destroy()
            prod6=ttk.Combobox(frame1,values=pro,font=(4))
            prod6.bind('<<ComboboxSelected>>',getproductcomp6)
            prod6.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku6=tk.Entry(frame1,font=(4))
            sku6.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty6=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty6.bind('<FocusOut>',calculatetotal6)
            qty6.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate6=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate6.bind('<FocusOut>',calculatetotal6)
            rate6.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total6=tk.Entry(frame1,font=(4))
            total6.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear1()
            btn1=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow2)
            btn1.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01) 
            return prod6
            #row8
        def addnewrow2():
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
            global x,prod7,btn2,sku7,qty7,price7,total7
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
            def clear2():
                btn1.destroy()
            prod7=ttk.Combobox(frame1,values=pro)
            prod7.bind('<<ComboboxSelected>>',getproductcomp7)
            prod7.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku7=tk.Entry(frame1)
            sku7.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty7=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty7.bind('<FocusOut>',calculatetotal7)
            qty7.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate7=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate7.bind('<FocusOut>',calculatetotal7)
            rate7.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total7=tk.Entry(frame1,font=(4))
            total7.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear2()
            btn2=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow3)
            btn2.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01) 
            #row9  
        def addnewrow3():
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
            global x,btn3,prod8,sku8,qty8,price8,total8     
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
            def clear3():
                btn2.destroy()
            prod8=ttk.Combobox(frame1,values=pro)
            prod8.bind('<<ComboboxSelected>>',getproductcomp8)
            prod8.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku8=tk.Entry(frame1)
            sku8.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            qty8=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qty8.bind('<FocusOut>',calculatetotal8)
            qty8.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            rate8=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            rate8.bind('<FocusOut>',calculatetotal8)
            rate8.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total8=tk.Entry(frame1,font=(4))
            total8.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear3()
            btn3=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow4)
            btn3.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)  
            #row10
        def addnewrow4():
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
                global x,btn4,prod9,sku9,qty9,price9,total9              
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
                def clear4():
                    btn3.destroy()
                prod9=ttk.Combobox(frame1,values=pro)
                prod9.bind('<<ComboboxSelected>>',getproductcomp9)
                prod9.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku9=tk.Entry(frame1)
                sku9.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty9=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty9.bind('<FocusOut>',calculatetotal9)
                qty9.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate9=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate9.bind('<FocusOut>',calculatetotal9)
                rate9.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total9=tk.Entry(frame1,font=(4))
                total9.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear4()
                btn4=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow5)
                btn4.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                    #row11
        def addnewrow5():
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
                global x,btn5,prod10,sku10,qty10,price10,total10       
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
                def clear5():
                    btn4.destroy()
                prod10=ttk.Combobox(frame1,values=pro)
                prod10.bind('<<ComboboxSelected>>',getproductcomp10)
                prod10.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku10=tk.Entry(frame1)
                sku10.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty10=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty10.bind('<FocusOut>',calculatetotal10)
                qty10.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate10=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate10.bind('<FocusOut>',calculatetotal10)
                rate10.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total10=tk.Entry(frame1,font=(4))
                total10.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear5()
                btn5=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow6)
                btn5.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01) 
            #row12   
        def addnewrow6():
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
                global x,btn6,prod11,sku11,qty11,price11,total11 
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
                def clear6():
                    btn5.destroy()
                prod11=ttk.Combobox(frame1,values=pro)
                prod11.bind('<<ComboboxSelected>>',getproductcomp11)
                prod11.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku11=tk.Entry(frame1)
                sku11.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)     
                qty11=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty11.bind('<FocusOut>',calculatetotal11)
                qty11.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate11=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate11.bind('<FocusOut>',calculatetotal11)
                rate11.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total11=tk.Entry(frame1,font=(4))
                total11.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear6()
                btn6=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow7)
                btn6.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                #row13  
        def addnewrow7():
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
                global x,btn7,prod12,sku12,qty12,price12,total12
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
                def clear7():
                    btn6.destroy()
                prod12=ttk.Combobox(frame1,values=pro)
                prod12.bind('<<ComboboxSelected>>',getproductcomp12)
                prod12.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku12=tk.Entry(frame1)
                sku12.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty12=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty12.bind('<FocusOut>',calculatetotal12)
                qty12.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate12=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate12.bind('<FocusOut>',calculatetotal12)
                rate12.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total12=tk.Entry(frame1,font=(4))
                total12.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear7()
                btn7=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow8)
                btn7.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                    #row14 
        def addnewrow8():
                def getproductcomp13(s):
                    def clearskucomp13():
                        sku13.delete(0,END)
                        rate13.delete(0,END)
                    clearskucomp13()    
                    prodd=prod13.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku13.insert(0,fet[0])
                        rate13.insert(0,fet[2])
                    elif fetch:
                        sku13.insert(0,fetch[0])
                        rate13.insert(0,fetch[2])
                global x,btn8,prod13,sku13,qty13,price13,total13
                def calculatetotal13(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text13():
                        total13.delete(0, END) 
                    q13=float(qty13.get())
                    r13=float(rate13.get())
                    tot13=(q13*r13)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text13()
                    total13.insert(0,tot13)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear8():
                    btn7.destroy()
                prod13=ttk.Combobox(frame1,values=pro)
                prod13.bind('<<ComboboxSelected>>',getproductcomp13)
                prod13.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku13=tk.Entry(frame1)
                sku13.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty13=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty13.bind('<FocusOut>',calculatetotal13)
                qty13.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate13=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate13.bind('<FocusOut>',calculatetotal13)
                rate13.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total13=tk.Entry(frame1,font=(4))
                total13.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear8()
                btn8=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow9)
                btn8.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                        #row15 
        def addnewrow9():
                def getproductcomp14(s):
                    def clearskucomp14():
                        sku14.delete(0,END)
                        rate14.delete(0,END)
                    clearskucomp14()    
                    prodd=prod14.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku14.insert(0,fet[0])
                        rate14.insert(0,fet[2])
                    elif fetch:
                        sku14.insert(0,fetch[0])
                        rate14.insert(0,fetch[2])
                global x,btn9,prod14,sku14,qty14,price14,total14 
                def calculatetotal14(xx):  
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29  
                    def clear_text14():
                        total14.delete(0, END) 
                    q14=float(qty14.get())
                    r14=float(rate14.get())
                    tot14=(q14*r14)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text14()
                    total14.insert(0,tot14)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear9():
                    btn8.destroy()
                prod14=ttk.Combobox(frame1,values=pro)
                prod14.bind('<<ComboboxSelected>>',getproductcomp14)
                prod14.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku14=tk.Entry(frame1)
                sku14.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty14=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty14.bind('<FocusOut>',calculatetotal14)
                qty14.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate14=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate14.bind('<FocusOut>',calculatetotal14)
                rate14.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total14=tk.Entry(frame1,font=(4))
                total14.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear9()
                btn9=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow10)
                btn9.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                            #row16
        def addnewrow10():
                def getproductcomp15(s):
                    def clearskucomp15():
                        sku15.delete(0,END)
                        rate15.delete(0,END)
                    clearskucomp15()    
                    prodd=prod15.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku15.insert(0,fet[0])
                        rate15.insert(0,fet[2])
                    elif fetch:
                        sku15.insert(0,fetch[0])
                        rate15.insert(0,fetch[2])
                global x,btn10,prod15,sku15,qty15,price15,total15
                def calculatetotal15(xx):    
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
                    def clear_text15():
                        total15.delete(0, END) 
                    q15=float(qty15.get())
                    r15=float(rate15.get())
                    tot15=(q15*r15)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text15()
                    total15.insert(0,tot15)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear10():
                    btn9.destroy()
                prod15=ttk.Combobox(frame1,values=pro)
                prod15.bind('<<ComboboxSelected>>',getproductcomp15)
                prod15.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku15=tk.Entry(frame1)
                sku15.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty15=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty15.bind('<FocusOut>',calculatetotal15)
                qty15.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate15=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate15.bind('<FocusOut>',calculatetotal15)
                rate15.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total15=tk.Entry(frame1,font=(4))
                total15.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear10()
                btn10=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow11)
                btn10.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)   
                                #row17 
        def addnewrow11():
                def getproductcomp16(s):
                    def clearskucomp16():
                        sku16.delete(0,END)
                        rate16.delete(0,END)
                    clearskucomp16()    
                    prodd=prod16.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku16.insert(0,fet[0])
                        rate16.insert(0,fet[2])
                    elif fetch:
                        sku16.insert(0,fetch[0])
                        rate16.insert(0,fetch[2])
                global x,btn11,prod16,sku16,qty16,price16,total16 
                def calculatetotal16(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text16():
                        total16.delete(0, END) 
                    q16=float(qty16.get())
                    r16=float(rate16.get())
                    tot16=(q16*r16)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text16()
                    total16.insert(0,tot16)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear11():
                    btn10.destroy()
                prod16=ttk.Combobox(frame1,values=pro)
                prod16.bind('<<ComboboxSelected>>',getproductcomp16)
                prod16.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku16=tk.Entry(frame1)
                sku16.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty16=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty16.bind('<FocusOut>',calculatetotal16)
                qty16.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate16=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate16.bind('<FocusOut>',calculatetotal16)
                rate16.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total16=tk.Entry(frame1,font=(4))
                total16.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear11()
                btn11=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow12)
                btn11.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)                                                                     
        #row18
        def addnewrow12():
                def getproductcomp17(s):
                    def clearskucomp17():
                        sku17.delete(0,END)
                        rate17.delete(0,END)
                    clearskucomp17()    
                    prodd=prod17.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku17.insert(0,fet[0])
                        rate17.insert(0,fet[2])
                    elif fetch:
                        sku17.insert(0,fetch[0])
                        rate17.insert(0,fetch[2])
                global x,btn12,prod17,sku17,qty17,price17,total17 
                def calculatetotal17(xx): 
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                    def clear_text17():
                        total17.delete(0, END) 
                    q17=float(qty17.get())
                    r17=float(rate17.get())
                    tot17=(q17*r17)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text17()
                    total17.insert(0,tot17)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear12():
                    btn11.destroy()
                prod17=ttk.Combobox(frame1,values=pro)
                prod17.bind('<<ComboboxSelected>>',getproductcomp17)
                prod17.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku17=tk.Entry(frame1)
                sku17.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty17=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty17.bind('<FocusOut>',calculatetotal17)
                qty17.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate17=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate17.bind('<FocusOut>',calculatetotal17)
                rate17.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total17=tk.Entry(frame1,font=(4))
                total17.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear12()
                btn12=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow13)
                btn12.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
            #row19
        def addnewrow13():
                global x,btn13,prod18,sku18,qty18,price18,total18 
                def getproductcomp18(s):
                    def clearskucomp18():
                        sku18.delete(0,END)
                        rate18.delete(0,END)
                    clearskucomp18()    
                    prodd=prod18.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku18.insert(0,fet[0])
                        rate18.insert(0,fet[2])
                    elif fetch:
                        sku18.insert(0,fetch[0])
                        rate18.insert(0,fetch[2])
                def calculatetotal18(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text18():
                        total18.delete(0, END) 
                    q18=float(qty18.get())
                    r18=float(rate18.get())
                    tot18=(q18*r18)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text18()
                    total18.insert(0,tot18)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear13():
                    btn12.destroy()
                prod18=ttk.Combobox(frame1,values=pro)
                prod18.bind('<<ComboboxSelected>>',getproductcomp18)
                prod18.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku18=tk.Entry(frame1)
                sku18.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty18=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty18.bind('<FocusOut>',calculatetotal18)
                qty18.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate18=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate18.bind('<FocusOut>',calculatetotal18)
                rate18.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total18=tk.Entry(frame1,font=(4))
                total18.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear13()
                btn13=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow14)
                btn13.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                #row20
        def addnewrow14():
                def getproductcomp19(s):
                    def clearskucomp19():
                        sku19.delete(0,END)
                        rate19.delete(0,END)
                    clearskucomp19()    
                    prodd=prod19.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku19.insert(0,fet[0])
                        rate19.insert(0,fet[2])
                    elif fetch:
                        sku19.insert(0,fetch[0])
                        rate19.insert(0,fetch[2])
                global x,btn14,prod19,sku19,qty19,price19,total19 
                def calculatetotal19(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text19():
                        total19.delete(0, END) 
                    q19=float(qty19.get())
                    r19=float(rate19.get())
                    tot19=(q19*r19)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text19()
                    total19.insert(0,tot19)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear14():
                    btn13.destroy()
                prod19=ttk.Combobox(frame1,values=pro)
                prod19.bind('<<ComboboxSelected>>',getproductcomp19)
                prod19.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku19=tk.Entry(frame1)
                sku19.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty19=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty19.bind('<FocusOut>',calculatetotal19)
                qty19.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate19=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate19.bind('<FocusOut>',calculatetotal19)
                rate19.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total19=tk.Entry(frame1,font=(4))
                total19.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear14()
                btn14=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow15)
                btn14.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)  
                    #row21
        def addnewrow15():
                def getproductcomp20(s):
                    def clearskucomp20():
                        sku20.delete(0,END)
                        rate20.delete(0,END)
                    clearskucomp20()    
                    prodd=prod20.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku20.insert(0,fet[0])
                        rate20.insert(0,fet[2])
                    elif fetch:
                        sku20.insert(0,fetch[0])
                        rate20.insert(0,fetch[2])
                global x,btn15,prod20,sku20,qty20,price20,total20 
                def calculatetotal20(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text20():
                        total20.delete(0, END) 
                    q20=float(qty20.get())
                    r20=float(rate20.get())
                    tot20=(q20*r20)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text20()
                    total20.insert(0,tot20)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear15():
                    btn14.destroy()
                prod20=ttk.Combobox(frame1,values=pro)
                prod20.bind('<<ComboboxSelected>>',getproductcomp20)
                prod20.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku20=tk.Entry(frame1)
                sku20.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty20=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty20.bind('<FocusOut>',calculatetotal20)
                qty20.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate20=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate20.bind('<FocusOut>',calculatetotal20)
                rate20.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total20=tk.Entry(frame1,font=(4))
                total20.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear15()
                btn15=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow16)
                btn15.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                        #row22
        def addnewrow16():
                def getproductcomp21(s):
                    def clearskucomp21():
                        sku21.delete(0,END)
                        rate21.delete(0,END)
                    clearskucomp21()    
                    prodd=prod21.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku21.insert(0,fet[0])
                        rate21.insert(0,fet[2])
                    elif fetch:
                        sku21.insert(0,fetch[0])
                        rate21.insert(0,fetch[2])
                global x,btn16,prod21,sku21,qty21,price21,total21
                def calculatetotal21(xx):    
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
                    def clear_text21():
                        total21.delete(0, END) 
                    q21=float(qty21.get())
                    r21=float(rate21.get())
                    tot21=(q21*r21)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text21()
                    total21.insert(0,tot21)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear16():
                    btn15.destroy()
                prod21=ttk.Combobox(frame1,values=pro)
                prod21.bind('<<ComboboxSelected>>',getproductcomp21)
                prod21.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku21=tk.Entry(frame1)
                sku21.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty21=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty21.bind('<FocusOut>',calculatetotal21)
                qty21.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate21=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate21.bind('<FocusOut>',calculatetotal21)
                rate21.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total21=tk.Entry(frame1,font=(4))
                total21.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear16()
                btn16=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow17)
                btn16.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                            #row23
        def addnewrow17():
                def getproductcomp22(s):
                    def clearskucomp22():
                        sku22.delete(0,END)
                        rate22.delete(0,END)
                    clearskucomp22()    
                    prodd=prod22.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku22.insert(0,fet[0])
                        rate22.insert(0,fet[2])
                    elif fetch:
                        sku22.insert(0,fetch[0])
                        rate22.insert(0,fetch[2])
                global x,btn17,prod22,sku22,qty22,price22,total22 
                def calculatetotal22(xx): 
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                    def clear_text22():
                        total22.delete(0, END) 
                    q22=float(qty22.get())
                    r22=float(rate22.get())
                    tot22=(q22*r22)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text22()
                    total22.insert(0,tot22)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear17():
                    btn16.destroy()
                prod22=ttk.Combobox(frame1,values=pro)
                prod22.bind('<<ComboboxSelected>>',getproductcomp22)
                prod22.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku22=tk.Entry(frame1)
                sku22.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty22=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty22.bind('<FocusOut>',calculatetotal22)
                qty22.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate22=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate22.bind('<FocusOut>',calculatetotal22)
                rate22.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total22=tk.Entry(frame1,font=(4))
                total22.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear17()
                btn17=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow18)
                btn17.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
        #row24
        def addnewrow18():
                def getproductcomp23(s):
                    def clearskucomp23():
                        sku23.delete(0,END)
                        rate23.delete(0,END)
                    clearskucomp23()    
                    prodd=prod23.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku23.insert(0,fet[0])
                        rate23.insert(0,fet[2])
                    elif fetch:
                        sku23.insert(0,fetch[0])
                        rate23.insert(0,fetch[2])
                global x,btn18,prod23,sku23,qty23,price23,total23 
                def calculatetotal23(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text23():
                        total23.delete(0, END) 
                    q23=float(qty23.get())
                    r23=float(rate23.get())
                    tot23=(q23*r23)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text23()
                    total23.insert(0,tot23)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear18():
                    btn17.destroy()
                prod23=ttk.Combobox(frame1,values=pro)
                prod23.bind('<<ComboboxSelected>>',getproductcomp23)
                prod23.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku23=tk.Entry(frame1)
                sku23.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty23=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty23.bind('<FocusOut>',calculatetotal23)
                qty23.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate23=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate23.bind('<FocusOut>',calculatetotal23)
                rate23.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total23=tk.Entry(frame1,font=(4))
                total23.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear18()
                btn18=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow19)
                btn18.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
            #row25
        def addnewrow19():
                def getproductcomp24(s):
                    def clearskucomp24():
                        sku24.delete(0,END)
                        rate24.delete(0,END)
                    clearskucomp24()    
                    prodd=prod24.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku24.insert(0,fet[0])
                        rate24.insert(0,fet[2])
                    elif fetch:
                        sku24.insert(0,fetch[0])
                        rate24.insert(0,fetch[2])
                global x,btn19,prod24,sku24,qty24,price24,total24
                def calculatetotal24(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text24():
                        total24.delete(0, END) 
                    q24=float(qty24.get())
                    r24=float(rate24.get())
                    tot24=(q24*r24)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text24()
                    total24.insert(0,tot24)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear19():
                    btn18.destroy()
                prod24=ttk.Combobox(frame1,values=pro)
                prod24.bind('<<ComboboxSelected>>',getproductcomp24)
                prod24.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku24=tk.Entry(frame1)
                sku24.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty24=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty24.bind('<FocusOut>',calculatetotal24)
                qty24.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate24=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate24.bind('<FocusOut>',calculatetotal24)
                rate24.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total24=tk.Entry(frame1,font=(4))
                total24.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear19()
                btn19=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow20)
                btn19.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
        #row26       
        def addnewrow20():
                def getproductcomp25(s):
                    def clearskucomp25():
                        sku25.delete(0,END)
                        rate25.delete(0,END)
                    clearskucomp25()    
                    prodd=prod25.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku25.insert(0,fet[0])
                        rate25.insert(0,fet[2])
                    elif fetch:
                        sku25.insert(0,fetch[0])
                        rate25.insert(0,fetch[2])
                global x,btn20,prod25,sku25,qty25,price25,total25
                def calculatetotal25(xx):  
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29  
                    def clear_text25():
                        total25.delete(0, END) 
                    q25=float(qty25.get())
                    r25=float(rate25.get())
                    tot25=(q25*r25)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text25()
                    total25.insert(0,tot25)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear20():
                    btn19.destroy()
                prod25=ttk.Combobox(frame1,values=pro)
                prod25.bind('<<ComboboxSelected>>',getproductcomp25)
                prod25.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku25=tk.Entry(frame1)
                sku25.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty25=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty25.bind('<FocusOut>',calculatetotal25)
                qty25.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate25=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate25.bind('<FocusOut>',calculatetotal25)
                rate25.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total25=tk.Entry(frame1,font=(4))
                total25.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear20()
                btn20=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow21)
                btn20.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
            #row27      
        def addnewrow21():
                def getproductcomp26(s):
                    def clearskucomp26():
                        sku26.delete(0,END)
                        rate26.delete(0,END)
                    clearskucomp26()    
                    prodd=prod26.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku26.insert(0,fet[0])
                        rate26.insert(0,fet[2])
                    elif fetch:
                        sku26.insert(0,fetch[0])
                        rate26.insert(0,fetch[2])
                global x,btn21,prod26,sku26,qty26,price26,total26 
                def calculatetotal26(xx):  
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29  
                    def clear_text26():
                        total26.delete(0, END) 
                    q26=float(qty26.get())
                    r26=float(rate26.get())
                    tot26=(q26*r26)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text26()
                    total26.insert(0,tot26)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear21():
                    btn20.destroy()
                prod26=ttk.Combobox(frame1,values=pro)
                prod26.bind('<<ComboboxSelected>>',getproductcomp26)
                prod26.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku26=tk.Entry(frame1)
                sku26.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty26=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty26.bind('<FocusOut>',calculatetotal26)
                qty26.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate26=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate26.bind('<FocusOut>',calculatetotal26)
                rate26.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total26=tk.Entry(frame1,font=(4))
                total26.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear21()
                btn21=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow22)
                btn21.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)  
        #row28       
        def addnewrow22():
                def getproductcomp27(s):
                    def clearskucomp27():
                        sku27.delete(0,END)
                        rate27.delete(0,END)
                    clearskucomp27()    
                    prodd=prod27.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku27.insert(0,fet[0])
                        rate27.insert(0,fet[2])
                    elif fetch:
                        sku27.insert(0,fetch[0])
                        rate27.insert(0,fetch[2])
                global x,btn22,prod27,sku27,qty27,price27,total27 
                def calculatetotal27(xx): 
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29   
                    def clear_text27():
                        total27.delete(0, END) 
                    q27=float(qty27.get())
                    r27=float(rate27.get())
                    tot27=(q27*r27)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text27()
                    total27.insert(0,tot27)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear22():
                    btn21.destroy()
                prod27=ttk.Combobox(frame1,values=pro)
                prod27.bind('<<ComboboxSelected>>',getproductcomp27)
                prod27.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku27=tk.Entry(frame1)
                sku27.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                quan27=IntVar()  
                qty27=tk.Spinbox(frame1,from_=0,to=50,font=(4),textvariable=quan27)
                qty27.bind('<FocusOut>',calculatetotal27)
                qty27.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                price27=IntVar()
                rate27=tk.Spinbox(frame1,from_=0,to=50,font=(4),textvariable=price27)
                rate27.bind('<FocusOut>',calculatetotal27)
                rate27.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total27=tk.Entry(frame1,font=(4))
                total27.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear22()
                btn22=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow23)
                btn22.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
            #row29      
        def addnewrow23():
                def getproductcomp28(s):
                    def clearskucomp28():
                        sku28.delete(0,END)
                        rate28.delete(0,END)
                    clearskucomp28()    
                    prodd=prod28.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku28.insert(0,fet[0])
                        rate28.insert(0,fet[2])
                    elif fetch:
                        sku28.insert(0,fetch[0])
                        rate28.insert(0,fetch[2])
                global x,btn23,prod28,sku28,qty28,price28,total28
                def calculatetotal28(xx):    
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29
                    def clear_text28():
                        total28.delete(0, END) 
                    q28=float(qty28.get())
                    r28=float(rate28.get())
                    tot28=(q28*r28)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text28()
                    total28.insert(0,tot28)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear23():
                    btn22.destroy()
                prod28=ttk.Combobox(frame1,values=pro)
                prod28.bind('<<ComboboxSelected>>',getproductcomp28)
                prod28.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku28=tk.Entry(frame1)
                sku28.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty28=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty28.bind('<FocusOut>',calculatetotal28)
                qty28.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate28=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate28.bind('<FocusOut>',calculatetotal28)
                rate28.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total28=tk.Entry(frame1,font=(4))
                total28.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear23()
                btn23=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow24)
                btn23.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
    #30     
        def addnewrow24():
                def getproductcomp29(s):
                    def clearskucomp29():
                        sku29.delete(0,END)
                        rate29.delete(0,END)
                    clearskucomp29()    
                    prodd=prod29.get()
                    cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                    fet=cur.fetchone()
                    cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                    fetch=cur.fetchone()
                    if fet:
                        sku29.insert(0,fet[0])
                        rate29.insert(0,fet[2])
                    elif fetch:
                        sku29.insert(0,fetch[0])
                        rate29.insert(0,fetch[2])
                global x,prod29,sku29,qty29,price29,total29         
                def calculatetotal29(xx):   
                    global qtytotal,q,q1,tot,tot1,subtot,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,tot2,tot3,tot4,tot5,tot6,tot7,tot8,tot9,tot10,tot11,tot12,tot13,tot14,tot15,tot16,tot17,tot18,tot19,tot20,tot21,tot22,tot23,tot24,tot25,tot26,tot27,tot28,tot29 
                    def clear_text29():
                        total29.delete(0, END) 
                    q29=float(qty29.get())
                    r29=float(rate29.get())
                    tot29=(q29*r29)
                    subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
                    qtytotal=int(q+q1+q2+q3+q4+q5+q6+q7+q8+q9+q10+q11+q12+q13+q14+q15+q16+q17+q18+q19+q20+q21+q22+q23+q24+q25+q26+q27+q28+q29)
                    clear_text29()
                    total29.insert(0,tot29)
                    clearcomptotquan()
                    totalquantity.insert(0,qtytotal)
                    totalquantity.insert(14,'Nos')
                    clearcomptotamount()
                    totalamount.insert(0,subtot)
                    costofcomp.insert(0,subtot)
                def clear24():
                    btn23.destroy()
                prod29=ttk.Combobox(frame1,values=pro)
                prod29.bind('<<ComboboxSelected>>',getproductcomp29)
                prod29.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
                sku29=tk.Entry(frame1)
                sku29.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
                qty29=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                qty29.bind('<FocusOut>',calculatetotal29)
                qty29.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
                rate29=tk.Spinbox(frame1,from_=0,to=50,font=(4))
                rate29.bind('<FocusOut>',calculatetotal29)
                rate29.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
                total29=tk.Entry(frame1,font=(4))
                total29.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
                x=x+0.02
                clear24()                                                                                                                                                                                                                                                                          
        btn=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow1)
        btn.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
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
        global qtytotalt1,subtott1,qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20
        qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        tott1,tott2,tott3,tott4,tott5,tott6,tott7,tott8,tott9,tott10,tott11,tott12,tott13,tott14,tott15,tott16,tott17,tott18,tott19,tott20=0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
        qtytotalt1,subtott1=0,0.0
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
        prodd1.bind('<<ComboboxSelected>>',getproductscrap)
        prodd1.place(relx=0.41,rely=0.19,relheight=0.015,relwidth=0.08)
        skuu1=tk.Entry(frame1,font=(4))
        skuu1.place(relx=0.505,rely=0.19,relheight=0.015,relwidth=0.06)
        qtyy1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qtyy1.bind('<FocusIn>',calculatescraptotal)
        qtyy1.place(relx=0.585,rely=0.19,relheight=0.015,relwidth=0.05)
        ratee1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        ratee1.bind('<FocusIn>',calculatescraptotal)
        ratee1.place(relx=0.65,rely=0.19,relheight=0.015,relwidth=0.05)
        totall1=tk.Entry(frame1,font=(4))
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
        prodd2.bind('<<ComboboxSelected>>',getproductscrap2)
        prodd2.place(relx=0.41,rely=0.21,relheight=0.015,relwidth=0.08)
        skuu2=tk.Entry(frame1,font=(4))
        skuu2.place(relx=0.505,rely=0.21,relheight=0.015,relwidth=0.06)
        qtyy2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qtyy2.bind('<FocusIn>',calculatescraptotal2)
        qtyy2.place(relx=0.585,rely=0.21,relheight=0.015,relwidth=0.05)
        ratee2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        ratee2.bind('<FocusIn>',calculatescraptotal2)
        ratee2.place(relx=0.65,rely=0.21,relheight=0.015,relwidth=0.05)
        totall2=tk.Entry(frame1,font=(4))
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
        prodd3.bind('<<ComboboxSelected>>',getproductscrap3)
        prodd3.place(relx=0.41,rely=0.23,relheight=0.015,relwidth=0.08)
        skuu3=tk.Entry(frame1,font=(4))
        skuu3.place(relx=0.505,rely=0.23,relheight=0.015,relwidth=0.06)
        qtyy3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qtyy3.bind('<FocusIn>',calculatescraptotal3)
        qtyy3.place(relx=0.585,rely=0.23,relheight=0.015,relwidth=0.05)
        ratee3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        ratee3.bind('<FocusIn>',calculatescraptotal3)
        ratee3.place(relx=0.65,rely=0.23,relheight=0.015,relwidth=0.05)
        totall3=tk.Entry(frame1,font=(4))
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
        prodd4.bind('<<ComboboxSelected>>',getproductscrap4)
        prodd4.place(relx=0.41,rely=0.25,relheight=0.015,relwidth=0.08)
        skuu4=tk.Entry(frame1,font=(4))
        skuu4.place(relx=0.505,rely=0.25,relheight=0.015,relwidth=0.06)
        qtyy4=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        qtyy4.bind('<FocusIn>',calculatescraptotal4)
        qtyy4.place(relx=0.585,rely=0.25,relheight=0.015,relwidth=0.05)
        ratee4=tk.Spinbox(frame1,from_=0,to=2147483647,font=(4))
        ratee4.bind('<FocusIn>',calculatescraptotal4)
        ratee4.place(relx=0.65,rely=0.25,relheight=0.015,relwidth=0.05)
        totall4=tk.Entry(frame1,font=(4))
        totall4.place(relx=0.72,rely=0.25,relheight=0.015,relwidth=0.05)
                    #row55
        global y            
        y=0.27            
        def addnewscraprow():
            def getproductscrap5(s):
                def clearskuscrap5():
                    skuu5.delete(0,END)
                    ratee5.delete(0,END)
                clearskuscrap5()    
                prodd=prodd5.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu5.insert(0,fet[0])
                    ratee5.insert(0,fet[2])
                elif fetch:
                    skuu5.insert(0,fetch[0])  
                    ratee5.insert(0,fetch[2]) 
            global y,btnn1,prodd5,skuu5,quann5,pricee5,totall5
            def calculatescraptotal5(yy):
                def clear_scraptext5():
                    totall5.delete(0, END) 
                qq5=float(qtyy5.get())
                rr5=float(ratee5.get())
                tott5=(qq5*rr5)
                subtott5=tott5
                clear_scraptext5()
                totall5.insert(0,tott5)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear1():
                btnn.destroy()
            prodd5=ttk.Combobox(frame1,values=pro,font=(4))
            prodd5.bind('<<ComboboxSelected>>',getproductscrap5)
            prodd5.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.08)
            skuu5=tk.Entry(frame1,font=(4))
            skuu5.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)
            qtyy5=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy5.bind('<FocusIn>',calculatescraptotal5)
            qtyy5.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee5=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee5.bind('<FocusIn>',calculatescraptotal5)
            ratee5.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall5=tk.Entry(frame1,font=(4))
            totall5.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear1()
            btnn1=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow2)
            btnn1.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01) 
        #66
        def addnewscraprow2():
            def getproductscrap6(s):
                def clearskuscrap6():
                    skuu6.delete(0,END)
                    ratee6.delete(0,END)
                clearskuscrap6()    
                prodd=prodd6.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu6.insert(0,fet[0])
                    ratee6.insert(0,fet[2])
                elif fetch:
                    skuu6.insert(0,fetch[0])  
                    ratee6.insert(0,fetch[2]) 
            global y,btnn2,prodd6,skuu6,quann6,pricee6,totall6
            def calculatescraptotal6(x):
                def clear_scraptext6():
                    totall6.delete(0, END) 
                qq6=float(qtyy6.get())
                rr6=float(ratee6.get())
                tott6=(qq6*rr6)
                clear_scraptext6()
                totall6.insert(0,tott6)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear2():
                btnn1.destroy()    
            prodd6=ttk.Combobox(frame1,values=pro,font=(4))
            prodd6.bind('<<ComboboxSelected>>',getproductscrap6)
            prodd6.place(relx=0.41,rely=0.29,relheight=0.015,relwidth=0.08)
            skuu6=tk.Entry(frame1,font=(4))
            skuu6.place(relx=0.505,rely=0.29,relheight=0.015,relwidth=0.06)
            qtyy6=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy6.bind('<FocusIn>',calculatescraptotal6)
            qtyy6.place(relx=0.585,rely=0.29,relheight=0.015,relwidth=0.05)
            ratee6=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee6.bind('<FocusIn>',calculatescraptotal6)
            ratee6.place(relx=0.65,rely=0.29,relheight=0.015,relwidth=0.05)
            totall6=tk.Entry(frame1,font=(4))
            totall6.place(relx=0.72,rely=0.29,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear2()
            btnn2=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow3)
            btnn2.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01) 
            #row7
        def addnewscraprow3(): 
            def getproductscrap7(s):
                def clearskuscrap7():
                    skuu7.delete(0,END)
                    ratee7.delete(0,END)
                clearskuscrap7()    
                prodd=prodd7.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu7.insert(0,fet[0])
                    ratee7.insert(0,fet[2])
                elif fetch:
                    skuu7.insert(0,fetch[0])  
                    ratee7.insert(0,fetch[2])  
            global y,btnn3,prodd7,skuu7,quann7,pricee7,totall7
            def calculatescraptotal7(xx):    
                def clear_scraptext7():
                    totall7.delete(0, END) 
                qq7=float(qtyy7.get())
                rr7=float(ratee7.get())
                tott7=(qq7*rr7)
                subtott=tott7
                clear_scraptext7()
                totall7.insert(0,tott7)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear3():
                btnn2.destroy()
            prodd7=ttk.Combobox(frame1,values=pro,font=(4))
            prodd7.bind('<<ComboboxSelected>>',getproductscrap7)
            prodd7.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.08)
            skuu7=tk.Entry(frame1,font=(4))
            skuu7.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy7=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy7.bind('<FocusOut>',calculatescraptotal7)
            qtyy7.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee7=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee7.bind('<FocusOut>',calculatescraptotal7)
            ratee7.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall7=tk.Entry(frame1,font=(4))
            totall7.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear3()
            btnn3=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow4)
            btnn3.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
                #row8
        def addnewscraprow4():  
            def getproductscrap8(s):
                def clearskuscrap8():
                    skuu8.delete(0,END)
                    ratee8.delete(0,END)
                clearskuscrap8()    
                prodd=prodd8.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu8.insert(0,fet[0])
                    ratee8.insert(0,fet[2])
                elif fetch:
                    skuu8.insert(0,fetch[0])  
                    ratee8.insert(0,fetch[2])  
            global y,btnn4,prodd8,skuu8,quann8,pricee8,totall8
            def calculatescraptotal8(xx):    
                def clear_scraptext8():
                    totall8.delete(0, END) 
                qq8=float(qtyy8.get())
                rr8=float(ratee8.get())
                tott8=(qq8*rr8)
                subtott=tott8
                clear_scraptext8()
                totall8.insert(0,tott8)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear4():
                btnn3.destroy()
            prodd8=ttk.Combobox(frame1,values=pro,font=(4))
            prodd8.bind('<<ComboboxSelected>>',getproductscrap8)
            prodd8.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.08)
            skuu8=tk.Entry(frame1,font=(4))
            skuu8.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy8=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy8.bind('<FocusOut>',calculatescraptotal8)
            qtyy8.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee8=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee8.bind('<FocusOut>',calculatescraptotal8)
            ratee8.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall8=tk.Entry(frame1,font=(4))
            totall8.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear4()
            btnn4=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow5)
            btnn4.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
                    #row9
        def addnewscraprow5():  
            def getproductscrap9(s):
                def clearskuscrap9():
                    skuu9.delete(0,END)
                    ratee9.delete(0,END)
                clearskuscrap9()    
                prodd=prodd9.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu9.insert(0,fet[0])
                    ratee9.insert(0,fet[2])
                elif fetch:
                    skuu9.insert(0,fetch[0])  
                    ratee9.insert(0,fetch[2])  
            global y,btnn5,prodd9,skuu9,quann9,pricee9,totall9
            def calculatescraptotal9(xx):    
                def clear_scraptext9():
                    totall9.delete(0, END) 
                qq9=float(qtyy9.get())
                rr9=float(ratee9.get())
                tott9=(qq9*rr9)
                subtott=tott9
                clear_scraptext9()
                totall9.insert(0,tott9)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear5():
                btnn4.destroy()
            prodd9=ttk.Combobox(frame1,values=pro,font=(4))
            prodd9.bind('<<ComboboxSelected>>',getproductscrap9)
            prodd9.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu9=tk.Entry(frame1,font=(4))
            skuu9.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy9=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy9.bind('<FocusOut>',calculatescraptotal9)
            qtyy9.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee9=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee9.bind('<FocusOut>',calculatescraptotal9)
            ratee9.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall9=tk.Entry(frame1,font=(4))
            totall9.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear5()
            btnn5=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow6)
            btnn5.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
        #row10
        def addnewscraprow6():  
            def getproductscrap10(s):
                def clearskuscrap10():
                    skuu10.delete(0,END)
                    ratee10.delete(0,END)
                clearskuscrap10()    
                prodd=prodd10.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu10.insert(0,fet[0])
                    ratee10.insert(0,fet[2])
                elif fetch:
                    skuu10.insert(0,fetch[0])  
                    ratee10.insert(0,fetch[2])  
            global y,btnn6,prodd10,skuu10,quann10,pricee10,totall10
            def calculatescraptotal10(xx):    
                def clear_scraptext10():
                    totall10.delete(0, END) 
                qq10=float(qtyy10.get())
                rr10=float(ratee10.get())
                tott10=(qq10*rr10)
                subtott=tott10
                clear_scraptext10()
                totall10.insert(0,tott10)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear6():
                btnn5.destroy()
            prodd10=ttk.Combobox(frame1,values=pro,font=(4))
            prodd10.bind('<<ComboboxSelected>>',getproductscrap10)
            prodd10.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu10=tk.Entry(frame1,font=(4))
            skuu10.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy10=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy10.bind('<FocusOut>',calculatescraptotal10)
            qtyy10.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee10=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee10.bind('<FocusOut>',calculatescraptotal10)
            ratee10.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall10=tk.Entry(frame1,font=(4))
            totall10.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear6()
            btnn6=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow7)
            btnn6.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
            #row11
        def addnewscraprow7():  
            def getproductscrap11(s):
                def clearskuscrap11():
                    skuu11.delete(0,END)
                    ratee11.delete(0,END)
                clearskuscrap11()    
                prodd=prodd11.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu11.insert(0,fet[0])
                    ratee11.insert(0,fet[2])
                elif fetch:
                    skuu11.insert(0,fetch[0])  
                    ratee11.insert(0,fetch[2])  
            global y,btnn7,prodd11,skuu11,quann11,pricee11,totall11
            def calculatescraptotal11(xx):    
                def clear_scraptext11():
                    totall11.delete(0, END) 
                qq11=float(qtyy11.get())
                rr11=float(ratee11.get())
                tott11=(qq11*rr11)
                clear_scraptext11()
                totall11.insert(0,tott11)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear7():
                btnn6.destroy()
            prodd11=ttk.Combobox(frame1,values=pro,font=(4))
            prodd11.bind('<<ComboboxSelected>>',getproductscrap11)
            prodd11.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu11=tk.Entry(frame1,font=(4))
            skuu11.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy11=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy11.bind('<FocusOut>',calculatescraptotal11)
            qtyy11.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee11=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee11.bind('<FocusOut>',calculatescraptotal11)
            ratee11.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall11=tk.Entry(frame1,font=(4))
            totall11.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear7()
            btnn7=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow8)
            btnn7.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
                #row12
        def addnewscraprow8():  
            def getproductscrap12(s):
                def clearskuscrap12():
                    skuu12.delete(0,END)
                    ratee12.delete(0,END)
                clearskuscrap12()    
                prodd=prodd12.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu12.insert(0,fet[0])
                    ratee12.insert(0,fet[2])
                elif fetch:
                    skuu12.insert(0,fetch[0])  
                    ratee12.insert(0,fetch[2])  
            global y,btnn8,prodd12,skuu12,quann12,pricee12,totall12
            def calculatescraptotal12(xx):    
                def clear_scraptext12():
                    totall12.delete(0, END) 
                qq12=float(qtyy12.get())
                rr12=float(ratee12.get())
                tott12=(qq12*rr12)
                clear_scraptext12()
                totall12.insert(0,tott12)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear8():
                btnn7.destroy()
            prodd12=ttk.Combobox(frame1,values=pro,font=(4))
            prodd12.bind('<<ComboboxSelected>>',getproductscrap12)
            prodd12.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu12=tk.Entry(frame1,font=(4))
            skuu12.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy12=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy12.bind('<FocusOut>',calculatescraptotal12)
            qtyy12.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee12=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee12.bind('<FocusOut>',calculatescraptotal12)
            ratee12.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall12=tk.Entry(frame1,font=(4))
            totall12.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear8()
            btnn8=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow9)
            btnn8.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01) 
                    #row13
        def addnewscraprow9():  
            def getproductscrap13(s):
                def clearskuscrap13():
                    skuu13.delete(0,END)
                    ratee13.delete(0,END)
                clearskuscrap13()    
                prodd=prodd13.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu13.insert(0,fet[0])
                    ratee13.insert(0,fet[2])
                elif fetch:
                    skuu13.insert(0,fetch[0])  
                    ratee13.insert(0,fetch[2])  
            global y,btnn9,prodd13,skuu13,quann13,pricee13,totall13
            def calculatescraptotal13(xx):    
                def clear_scraptext13():
                    totall13.delete(0, END) 
                qq13=float(qtyy13.get())
                rr13=float(ratee13.get())
                tott13=(qq13*rr13)
                subtott=tott13
                clear_scraptext13()
                totall13.insert(0,tott13)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear9():
                btnn8.destroy()
            prodd13=ttk.Combobox(frame1,values=pro,font=(4))
            prodd13.bind('<<ComboboxSelected>>',getproductscrap13)
            prodd13.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu13=tk.Entry(frame1,font=(4))
            skuu13.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy13=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy13.bind('<FocusOut>',calculatescraptotal13)
            qtyy13.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee13=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee13.bind('<FocusOut>',calculatescraptotal13)
            ratee13.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall13=tk.Entry(frame1,font=(4))
            totall13.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear9()
            btnn9=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow10)
            btnn9.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
            #row14
        def addnewscraprow10():
            def getproductscrap14(s):
                def clearskuscrap14():
                    skuu14.delete(0,END)
                    ratee14.delete(0,END)
                clearskuscrap14()    
                prodd=prodd14.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu14.insert(0,fet[0])
                    ratee14.insert(0,fet[2])
                elif fetch:
                    skuu14.insert(0,fetch[0])  
                    ratee14.insert(0,fetch[2])   
            global y,prod6,btnn10,prodd14,skuu14,quann14,pricee14,totall14
            def calculatescraptotal14(xx):    
                def clear_scraptext14():
                    totall14.delete(0, END) 
                qq14=float(qtyy14.get())
                rr14=float(ratee14.get())
                tott14=(qq14*rr14)
                subtott=tott14
                clear_scraptext14()
                totall14.insert(0,tott14)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear10():
                btnn9.destroy()
            prodd14=ttk.Combobox(frame1,values=pro,font=(4))
            prodd14.bind('<<ComboboxSelected>>',getproductscrap14)
            prodd14.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu14=tk.Entry(frame1,font=(4))
            skuu14.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy14=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy14.bind('<FocusOut>',calculatescraptotal14)
            qtyy14.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee14=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee14.bind('<FocusOut>',calculatescraptotal14)
            ratee14.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall14=tk.Entry(frame1,font=(4))
            totall14.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear10()
            btnn10=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow11)
            btnn10.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01) 
        #row15
        def addnewscraprow11(): 
            def getproductscrap15(s):
                def clearskuscrap15():
                    skuu15.delete(0,END)
                    ratee15.delete(0,END)
                clearskuscrap15()    
                prodd=prodd15.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu15.insert(0,fet[0])
                    ratee15.insert(0,fet[2])
                elif fetch:
                    skuu15.insert(0,fetch[0])  
                    ratee15.insert(0,fetch[2])   
            global y,prod6,btnn11,prodd15,skuu15,quann15,pricee15,totall15
            def calculatescraptotal15(xx):    
                def clear_scraptext15():
                    totall15.delete(0, END) 
                qq15=float(qtyy15.get())
                rr15=float(ratee15.get())
                tott15=(qq15*rr15)
                clear_scraptext15()
                totall15.insert(0,tott15)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear11():
                btnn10.destroy()
            prodd15=ttk.Combobox(frame1,values=pro,font=(4))
            prodd15.bind('<<ComboboxSelected>>',getproductscrap15)
            prodd15.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu15=tk.Entry(frame1,font=(4))
            skuu15.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy15=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy15.bind('<FocusOut>',calculatescraptotal15)
            qtyy15.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee15=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee15.bind('<FocusOut>',calculatescraptotal15)
            ratee15.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall15=tk.Entry(frame1,font=(4))
            totall15.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear11()
            btnn11=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow12)
            btnn11.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
            #row16
        def addnewscraprow12(): 
            def getproductscrap16(s):
                def clearskuscrap16():
                    skuu16.delete(0,END)
                    ratee16.delete(0,END)
                clearskuscrap16()    
                prodd=prodd16.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu16.insert(0,fet[0])
                    ratee16.insert(0,fet[2])
                elif fetch:
                    skuu16.insert(0,fetch[0])  
                    ratee16.insert(0,fetch[2])   
            global y,prod6,btnn12,prodd16,skuu16,quann16,pricee16,totall16
            def calculatescraptotal16(xx):    
                def clear_scraptext16():
                    totall16.delete(0, END) 
                qq16=float(qtyy16.get())
                rr16=float(ratee16.get())
                tott16=(qq16*rr16)
                clear_scraptext16()
                totall16.insert(0,tott16)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear12():
                btnn11.destroy()
            prodd16=ttk.Combobox(frame1,values=pro,font=(4))
            prodd16.bind('<<ComboboxSelected>>',getproductscrap16)
            prodd16.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu16=tk.Entry(frame1,font=(4))
            skuu16.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy16=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy16.bind('<FocusOut>',calculatescraptotal16)
            qtyy16.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee16=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee16.bind('<FocusOut>',calculatescraptotal16)
            ratee16.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall16=tk.Entry(frame1,font=(4))
            totall16.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear12()
            btnn12=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow13)
            btnn12.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
                #row17
        def addnewscraprow13(): 
            def getproductscrap17(s):
                def clearskuscrap17():
                    skuu17.delete(0,END)
                    ratee17.delete(0,END)
                clearskuscrap17()    
                prodd=prodd17.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu17.insert(0,fet[0])
                    ratee17.insert(0,fet[2])
                elif fetch:
                    skuu17.insert(0,fetch[0])  
                    ratee17.insert(0,fetch[2])   
            global y,prod6,btnn13,prodd17,skuu17,quann17,pricee17,totall17
            def calculatescraptotal17(xx):    
                def clear_scraptext17():
                    totall17.delete(0, END) 
                qq17=float(qtyy17.get())
                rr17=float(ratee17.get())
                tott17=(qq17*rr17)
                subtott=tott17
                clear_scraptext17()
                totall17.insert(0,tott17)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear13():
                btnn12.destroy()
            prodd17=ttk.Combobox(frame1,values=pro,font=(4))
            prodd17.bind('<<ComboboxSelected>>',getproductscrap17)
            prodd17.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu17=tk.Entry(frame1,font=(4))
            skuu17.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy17=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy17.bind('<FocusOut>',calculatescraptotal17)
            qtyy17.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee17=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee17.bind('<FocusOut>',calculatescraptotal17)
            ratee17.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall17=tk.Entry(frame1,font=(4))
            totall17.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear13()
            btnn13=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow14)
            btnn13.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
                    #row18
        def addnewscraprow14():  
            def getproductscrap18(s):
                def clearskuscrap18():
                    skuu18.delete(0,END)
                    ratee18.delete(0,END)
                clearskuscrap18()    
                prodd=prodd18.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu18.insert(0,fet[0])
                    ratee18.insert(0,fet[2])
                elif fetch:
                    skuu18.insert(0,fetch[0])  
                    ratee18.insert(0,fetch[2])  
            global y,prod6,btnn14,prodd18,skuu18,quann18,pricee18,totall18
            def calculatescraptotal18(xx):    
                def clear_scraptext18():
                    totall18.delete(0, END) 
                qq18=float(qtyy18.get())
                rr18=float(ratee18.get())
                tott18=(qq18*rr18)
                subtott=tott18
                clear_scraptext18()
                totall18.insert(0,tott18)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear14():
                btnn13.destroy()
            prodd18=ttk.Combobox(frame1,values=pro,font=(4))
            prodd18.bind('<<ComboboxSelected>>',getproductscrap18)
            prodd18.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu18=tk.Entry(frame1,font=(4))
            skuu18.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy18=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy18.bind('<FocusOut>',calculatescraptotal18)
            qtyy18.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee18=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee18.bind('<FocusOut>',calculatescraptotal18)
            ratee18.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall18=tk.Entry(frame1,font=(4))
            totall18.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear14()
            btnn14=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow15)
            btnn14.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
                        #row19
        def addnewscraprow15():  
            def getproductscrap19(s):
                def clearskuscrap19():
                    skuu19.delete(0,END)
                    ratee19.delete(0,END)
                clearskuscrap19()    
                prodd=prodd19.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu19.insert(0,fet[0])
                    ratee19.insert(0,fet[2])
                elif fetch:
                    skuu19.insert(0,fetch[0])  
                    ratee19.insert(0,fetch[2])  
            global y,prod6,btnn15,prodd19,skuu19,quann19,pricee19,totall19
            def calculatescraptotal19(xx):    
                def clear_scraptext19():
                    totall19.delete(0, END) 
                qq19=float(qtyy19.get())
                rr19=float(ratee19.get())
                tott19=(qq19*rr19)
                subtott=tott19
                clear_scraptext19()
                totall19.insert(0,tott19)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear15():
                btnn14.destroy()
            prodd19=ttk.Combobox(frame1,values=pro,font=(4))
            prodd19.bind('<<ComboboxSelected>>',getproductscrap19)
            prodd19.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu19=tk.Entry(frame1,font=(4))
            skuu19.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy19=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy19.bind('<FocusOut>',calculatescraptotal19)
            qtyy19.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee19=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee19.bind('<FocusOut>',calculatescraptotal19)
            ratee19.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall19=tk.Entry(frame1,font=(4))
            totall19.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear15()
            btnn15=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow16)
            btnn15.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01) 
                            #row20
        def addnewscraprow16():  
            def getproductscrap20(s):
                def clearskuscrap20():
                    skuu20.delete(0,END)
                    ratee20.delete(0,END)
                clearskuscrap20()    
                prodd=prodd20.get()
                cur.execute("SELECT sku,initialqty,salesprice FROM inventory WHERE name =%s",([prodd]))
                fet=cur.fetchone()
                cur.execute("SELECT sku,initialqty,saleprice FROM noninventory WHERE name =%s",([prodd]))
                fetch=cur.fetchone()
                if fet:
                    skuu20.insert(0,fet[0])
                    ratee20.insert(0,fet[2])
                elif fetch:
                    skuu20.insert(0,fetch[0])  
                    ratee20.insert(0,fetch[2])  
            global y,prod6,prodd20,skuu20,quann20,pricee20,totall20
            def calculatescraptotal20(xx):    
                def clear_scraptext20():
                    totall20.delete(0, END) 
                qq20=float(qtyy20.get())
                rr20=float(ratee20.get())
                tott20=(qq20*rr20)
                subtott=tott20
                clear_scraptext20()
                totall20.insert(0,tott20)
                subtott1=tott1+tott2+tott3+tott4+tott5+tott6+tott7+tott8+tott9+tott10+tott11+tott12+tott13+tott14+tott15+tott16+tott17+tott18+tott19+tott20
                clearscraptotamount()
                totalscrapamount.insert(0,subtott1)
            def scrapclear16():
                btnn15.destroy()
            prodd20=ttk.Combobox(frame1,values=pro,font=(4))
            prodd20.bind('<<ComboboxSelected>>',getproductscrap20)
            prodd20.place(relx=0.41,rely=y,relheight=0.015,relwidth=0.09)
            skuu20=tk.Entry(frame1,font=(4))
            skuu20.place(relx=0.505,rely=y,relheight=0.015,relwidth=0.06)    
            qtyy20=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            qtyy20.bind('<FocusOut>',calculatescraptotal20)
            qtyy20.place(relx=0.585,rely=y,relheight=0.015,relwidth=0.05)
            ratee20=tk.Spinbox(frame1,from_=0,to=50,font=(4))
            ratee20.bind('<FocusOut>',calculatescraptotal20)
            ratee20.place(relx=0.65,rely=y,relheight=0.015,relwidth=0.05)
            totall20=tk.Entry(frame1,font=(4))
            totall20.place(relx=0.72,rely=y,relheight=0.015,relwidth=0.05)
            y=y+0.02
            scrapclear16()                                                                                   
    
        btnn=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewscraprow)
        btnn.place(relx=0.67,rely=y,relwidth=0.1,relheight=0.01)
        tk.Label(frame,text='Total Quantity',font=('times new roman', 16),bg='#2f516f').place(relx=0.25,rely=0.40,relwidth=0.1,relheight=0.03)
        totalquantity=tk.Entry(frame,font=(8))
        totalquantity.place(relx=0.26,rely=0.43,relwidth=0.08,relheight=0.02)
        tk.Label(frame,text='Total Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.38,rely=0.40,relwidth=0.1,relheight=0.03)
        totalamount=tk.Entry(frame,font=(8))
        totalamount.place(relx=0.39,rely=0.43,relwidth=0.08,relheight=0.02)
        tk.Label(frame,text='Total Scrap Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=0.41,relwidth=0.15,relheight=0.03)
        totalscrapamount=tk.Entry(frame,font=(6))
        totalscrapamount.place(relx=0.79,rely=0.41,relwidth=0.1,relheight=0.02)
        tk.Label(frame,text='Cost of components',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=0.44,relwidth=0.15,relheight=0.03)
        costofcomp=tk.Entry(frame,font=(6))
        costofcomp.place(relx=0.79,rely=0.44,relwidth=0.1,relheight=0.02)
        tk.Label(frame,text='Type of Additional Cost',font=('times new roman', 16),bg='#2f516f').place(relx=0.53,rely=0.47,relwidth=0.15,relheight=0.03)
        additional1=tk.Entry(frame,font=(6))
        additional1.place(relx=0.55,rely=0.50,relwidth=0.12,relheight=0.02)
        tk.Label(frame,text='Percentage',font=('times new roman', 16),bg='#2f516f').place(relx=0.67,rely=0.47,relwidth=0.1,relheight=0.03)
        global v,addbtn,ded,ded1,ded2,ded3,totaddlcost
        v=0.56
        ded,ded1,ded2,ded3,totaddlcost=0.0,0.0,0.0,0.0,0.0
        def labels():
            global v,addlcost,totaddlcost,ded,ded2,ded3,ded1,subtot,effccost
            effccost=0.0
            tk.Label(frame1,text='QTY',bg='#243e54',font=('Times New Roman',14)).place(relx=0.67,rely=0.140)
            def quantityy(x):
                qq=float(qqq.get())
                efrate=(effccost/qq)
                effrate.insert(0,efrate)
            qqq=IntVar()
            quantity=tk.Spinbox(frame1,font=(6),from_=0,to=50,textvariable=qqq)
            quantity.bind('<FocusIn>',quantityy)
            quantity.place(relx=0.70,rely=0.140,relwidth=0.03,relheight=0.015)
            tk.Label(frame,text='Total Addl. Cost:',font=('times new roman', 16),bg='#2f516f').place(relx=0.53,rely=v,relwidth=0.15,relheight=0.03)
            addlcost=tk.Entry(frame,font=(6))
            totaddlcost=float(round(ded+ded1+ded2+ded3)) 
            addlcost.insert(0,totaddlcost)
            addlcost.place(relx=0.79,rely=v,relwidth=0.1,relheight=0.02) 
            tk.Label(frame,text='Effective Cost:',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=v+0.03,relwidth=0.25,relheight=0.03) 
            effcost=tk.Entry(frame,font=(6))
            totaddlcost=float(round(ded+ded1+ded2+ded3)) 
            subtot=tot+tot1+tot2+tot3+tot4+tot5+tot6+tot7+tot8+tot9+tot10+tot11+tot12+tot13+tot14+tot15+tot16+tot17+tot18+tot19+tot20+tot21+tot22+tot23+tot24+tot25+tot26+tot27+tot28+tot29
            effccost=round(subtot-totaddlcost)
            effcost.insert(0,effccost)
            effcost.place(relx=0.79,rely=v+0.03,relwidth=0.1,relheight=0.02) 
            tk.Label(frame,text='Effective rate of Primary Item:',font=('times new roman', 16),bg='#2f516f').place(relx=0.50,rely=v+0.06,relwidth=0.2,relheight=0.03)
            effrate=tk.Entry(frame,font=(6))
            effrate.place(relx=0.79,rely=v+0.06,relwidth=0.1,relheight=0.02) 
        def percen1(q):
            global ded,ded2,ded3,ded1,totaddlcost,clearaddtotcost
            add1=additional1.get()
            percen=float(percentage1.get())
            if add1:
                ded=float((percen/100)*subtot)
                def clear_ded():
                    addtotal1.delete(0,END)
                clear_ded()   
                addtotal1.insert(0,ded)
                def clearaddtotcost():
                    addlcost.delete(0,END)  
                clearaddtotcost()
                totaddlcost=float(round(ded+ded1+ded2+ded3)) 
                addlcost.insert(0,totaddlcost)  
                labels()        
        percentage1=tk.Entry(frame,font=(6))
        percentage1.bind('<KeyRelease>',percen1)
        percentage1.place(relx=0.697,rely=0.50,relwidth=0.04,relheight=0.02)    
        tk.Label(frame,font=(6),text='%').place(relx=0.72,rely=0.50,relwidth=0.01,relheight=0.02)   
        addtotal1=tk.Entry(frame,font=(6))
        addtotal1.place(relx=0.79,rely=0.50,relwidth=0.1,relheight=0.02)  
        labels()
        #additional2
        additional2=tk.Entry(frame,font=(6))
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
        percentage2.bind('<KeyRelease>',percen2)
        percentage2.place(relx=0.697,rely=0.53,relwidth=0.04,relheight=0.02)    
        tk.Label(frame,font=(6),text='%').place(relx=0.72,rely=0.53,relwidth=0.01,relheight=0.02)
        addtotal2=tk.Entry(frame,font=(6))
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
        def getproductiondetails():
            p=product.get()
            sk=sku.get()
            hs=hsn.get()
            qt=quanty.get()
            md=mandate.get()
            ed=expdate.get()
            cid=2
            productiondet="INSERT INTO production (cid,productname,sku,hsn,quantity,manufacturing_date,expiry_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(productiondet,[(cid),(p),(sk),(hs),(qt),(md),(ed)])
            mydata.commit()
            cur.execute("SELECT productionid FROM production WHERE productname= %s",([p]))
            v=cur.fetchone()
            #components
            #1st row
            p1,p2,p3,p4,p5,p6=prod.get(),prod1.get(),prod2.get(),prod3.get(),prod4.get(),prod5.get()
            sk1,sk2,sk3,sk4,sk5,sk6=sku.get(),sku1.get(),sku2.get(),sku3.get(),sku4.get(),sku5.get()
            qt1,qt2,qt3,qt4,qt5,qt6=quan.get(),quan1.get(),quan2.get(),quan3.get(),quan4.get(),quan5.get()
            pr1,pr2,pr3,pr4,pr5,pr6=price.get(),price1.get(),price2.get(),price3.get(),price4.get(),price5.get()
            tt1,tt2,tt3,tt4,tt5,tt6=total.get(),total1.get(),total2.get(),total3.get(),total4.get(),total5.get()
            type='Components'
            raw='''INSERT INTO rawmaterials (productionid,cid,Type,prod,sku,qty,price,total,prod1,sku1,qty1,price1,total1,prod2,sku2,qty2,price2,total2,prod3,sku3,qty3,price3,total3,prod4,sku4,qty4,price4,total4,
                prod5,sku5,qty5,price5,total5) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cur.execute(raw,[(v[0]),(cid),(type),(p1),(sk1),(qt1),(pr1),(tt1),(p2),(sk2),(qt2),(pr2),(tt2),(p3),(sk3),(qt3),(pr3),(tt3),(p4),(sk4),(qt4),(pr4),(tt4),(p5),(sk5),(qt5),(pr5),(tt5),(p6),(sk6),(qt6),(pr6),(tt6)])    
            try:
                p7,p8,p9,p10,pp10=prod6.get(),prod7.get(),prod8.get(),prod9.get(),prod10.get()
                p11,p12,p13,p14,p15,p16,p17,p18,p19,p20=prod11.get(),prod12.get(),prod13.get(),prod14.get(),prod15.get(),prod16.get(),prod17.get(),prod18.get(),prod19.get(),prod20.get()
                p21,p22,p23,p24,p25,p26,p27,p28,p29=prod21.get(),prod22.get(),prod23.get(),prod24.get(),prod25.get(),prod26.get(),prod27.get(),prod28.get(),prod29.get()
                sk7,sk8,sk9,sk10,sk11,sk12=sku6.get(),sku7.get(),sku8.get(),sku9.get(),sku10.get(),sku11.get()
                sk13,sk14,sk15,sk16,sk17,sk18,sk19,sk20,sk21=sku12.get(),sku13.get(),sku14.get(),sku15.get(),sku16.get(),sku17.get(),sku18.get(),sku19.get(),sku20.get()
                sk22,sk23,sk24,sk25,sk26,sk27,sk28,sk29,sk30=sku21.get(),sku22.get(),sku23.get(),sku24.get(),sku25.get(),sku26.get(),sku27.get(),sku28.get(),sku29.get()
                qt7,qt8,qt9,qt10,qqtt10=quan6.get(),quan7.get(),quan8.get(),quan9.get(),quan10.get()
                qt11,qt12,qt13,qt14,qt15,qt16,qt17,qt18,qt19,qt20=quan11.get(),quan12.get(),quan13.get(),quan14.get(),quan15.get(),quan16.get(),quan17.get(),quan18.get(),quan19.get(),quan20()
                qt21,qt22,qt23,qt24,qt25,qt26,qt27,qt28,qt29=quan21.get(),quan22.get(),quan23.get(),quan24.get(),quan25.get(),quan26.get(),quan27.get(),quan28.get(),quan29.get()
                pr7,pr8,pr9,pr10=price6.get(),price7.get(),price8.get(),price9.get()
                pr11,pr12,pr13,pr14,pr15,pr16,pr17,pr18,pr19,pr20=price10.get(),price11.get(),price12.get(),price13.get(),price14.get(),price15.get(),price16.get(),price17.get(),price18.get(),price19.get()
                pr21,pr22,pr23,pr24,pr25,pr26,pr27,pr28,pr29,pr30=price20.get(),price21.get(),price22.get(),price23.get(),price24.get(),price25.get(),price26.get(),price27.get(),price28.get(),price29.get()
                tt7,tt8,tt9,tt10=total6.get(),total7.get(),total8.get(),total9.get()
                tt11,tt12,tt13,tt14,tt15,tt16,tt17,tt18,tt19,tt20=total10.get(),total11.get(),total12.get(),total13.get(),total14.get(),total15.get(),total16.get(),total17.get(),total18.get(),total19.get()
                tt21,tt22,tt23,tt24,tt25,tt26,tt27,tt28,tt29,tt30=total20.get(),total21.get(),total22.get(),total23.get(),total24.get(),total25.get(),total26.get(),total27.get(),total28.get(),total29.get()
                raw1='''INSERT INTO rawmaterials (prod6,sku6,qty6,price6,total6,prod7,sku7,qty7,price7,total7,prod8,sku8,qty8,price8,total8,prod9,sku9,qty9,price9,total9,prod10,sku10,qty10,price10,total10,
                prod11,sku11,qty11,price11,total11,prod12,sku12,qty12,price12,total12,prod13,sku13,qty13,price13,total13,prod14,sku14,qty14,price14,total14,prod15,sku15,qty15,price15,total15,
                prod16,sku16,qty16,price16,total16,prod17,sku17,qty17,price17,total17,prod18,sku18,qty18,price18,total18,prod19,sku19,qty19,price19,total19,prod20,sku20,qty20,price20,total20,prod21,sku21,qty21,price21,total21,
                prod22,sku22,qty22,price22,total22,prod23,sku23,qty23,price23,total23,prod24,sku24,qty24,price24,total24,prod25,sku25,qty25,price25,total26,prod26,sku26,qty26,price26,total26,prod27,sku27,qty27,price27,total27,
                prod28,sku28,qty28,price28,total28,prod29,sku29,qty29,price29,total29) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,,%s,%s,%s,%s,%s,,%s,%s,%s,%s,%s,)'''
                cur.execute(raw1,[(p7),(sk7),(qt7),(pr7),(tt7),(p8),(sk8),(qt8),(pr8),(tt8),(p9),(sk9),(qt9),(pr9),(tt9),(p10),(sk10),(qt10),(pr10),(tt10),(pp10),(sk11),(qqtt10),(pr11),(tt11),(p11),(sk12),(qt11),(pr12),(tt12),(p12),(sk13),(qt12),(pr13),(tt13),(p13),(sk14),(qt13),(pr14),(tt14),(p14),(sk15),(qt14),(pr15),(tt15),
                (p15),(sk16),(qt15),(pr16),(tt16),(p16),(sk17),(qt16),(pr17),(tt17),(p17),(sk18),(qt17),(pr18),(tt18),(p18),(sk19),(qt18),(pr19),(tt19),(p19),(sk20),(qt19),(pr20),(tt20),(p20),(sk21),(qt20),(pr21),(tt21),(p21),(sk22),(qt21),(pr22),(tt22),(p22),(sk23),(qt22),(pr23),(tt23),
                (p23),(sk24),(qt23),(pr24),(tt24),(p24),(sk25),(qt24),(pr25),(tt25),(p25),(sk26),(qt25),(pr26),(tt26),(p26),(sk27),(qt26),(pr27),(tt27),(p27),(sk28),(qt27),(pr28),(tt28),(p28),(sk29),(qt28),(pr29),(tt29),(p29),(sk30),(qt29),(pr30),(tt30)])
                mydata.commit()
            except:
                pass
                #scrap row1 
            pp1,pp2,pp3,pp4=prodd1.get(),prodd2.get(),prodd3.get(),prodd4.get()
            skk1,skk2,skk3,skk4=skuu1.get(),skuu2.get(),skuu3.get(),skuu4.get()
            qtt1,qtt2,qtt3,qtt4=quann1.get(),quann2.get(),quann3.get(),quann4.get()
            prr1,prr2,prr3,prr4=pricee1.get(),pricee2.get(),pricee3.get(),pricee4.get()
            ttt1,ttt2,ttt3,ttt4=totall1.get(),totall2.get(),totall3.get(),totall4.get()
            type1='Coproducts/scrap'
            raw1='''INSERT INTO rawmaterials (productionid,cid,Type,prod,sku,qty,price,total,prod1,sku1,qty1,price1,total1,prod2,sku2,qty2,price2,total2,prod3,sku3,qty3,price3,total3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cur.execute(raw1,[(v[0]),(cid),(type1),(pp1),(skk1),(qtt1),(prr1),(ttt1),(pp2),(skk2),(qtt2),(prr2),(ttt2),(pp3),(skk3),(qtt3),(prr3),(ttt3),(pp4),(skk4),(qtt4),(prr4),(ttt4)])
            try:
                pp5,pp6,pp7,pp8,pp9,pp10=prodd5.get(),prodd6.get(),prodd7.get(),prodd8.get(),prodd9.get(),prodd10.get()
                pp11,pp12,pp13,pp14,pp15,pp16,pp17,pp18,pp19,pp20=prodd11.get(),prodd12.get(),prodd13.get(),prodd14.get(),prodd15.get(),prodd16.get(),prodd17.get(),prodd18.get(),prodd19.get(),prodd20.get()
                skk5,skk6,skk7,skk8,skk9,skk10=skuu5.get(),skuu6.get(),skuu7.get(),skuu8.get(),skuu9.get(),skuu10.get()
                skk11,skk12,skk13,skk14,skk15,skk16,skk17,skk18,skk19,skk20=skuu11.get(),skuu12.get(),skuu13.get(),skuu14.get(),skuu15.get(),skuu16.get(),skuu17.get(),skuu18.get(),skuu19.get(),skuu20.get()
                qtt5,qtt6,qtt7,qtt8,qtt9,qtt10=quann5.get(),quann6.get(),quann7.get(),quann8.get(),quann9.get(),quann10.get()
                qtt11,qtt12,qtt13,qtt14,qtt15,qtt16,qtt17,qtt18,qtt19,qtt20=quann11.get(),quann12.get(),quann13.get(),quann14.get(),quann15.get(),quann16.get(),quann17.get(),quann18.get(),quann19.get(),quann20.get()       
                prr5,prr6,prr7,prr8,prr9,prr10=pricee5.get(),pricee6.get(),pricee7.get(),pricee8.get(),pricee9.get(),pricee10.get()
                prr11,prr12,prr13,prr14,prr15,prr16,prr17,prr18,prr19,prr20=pricee11.get(),pricee12.get(),pricee13.get(),pricee14.get(),pricee15.get(),pricee16.get(),pricee17.get(),pricee18.get(),pricee19.get(),pricee20.get()        
                ttt5,ttt6,ttt7,ttt8,ttt9,ttt10=totall5.get(),totall6.get(),totall7.get(),totall8.get(),totall9.get(),totall10.get()
                ttt11,ttt12,ttt13,ttt14,ttt15,ttt16,ttt17,ttt18,ttt19,ttt20=totall11.get(),totall12.get(),totall13.get(),totall14.get(),totall15.get(),totall16.get(),totall17.get(),totall18.get(),totall19.get(),totall20.get()
                raw2='''INSERT INTO rawmaterials (prod4,sku4,qty4,price4,total4,prod5,sku5,qty5,price5,total5,prod6,sku6,qty6,price6,total6,prod7,sku7,qty7,price7,total7,prod8,sku8,qty8,price8,total8,prod9,sku9,qty9,price9,total9,prod10,sku10,qty10,price10,total10,
                        prod11,sku11,qty11,price11,total11,prod12,sku12,qty12,price12,total12,prod13,sku13,qty13,price13,total13,prod14,sku14,qty14,price14,total14,prod15,sku15,qty15,price15,total15,
                        prod16,sku16,qty16,price16,total16,prod17,sku17,qty17,price17,total17,prod18,sku18,qty18,price18,total18,prod19,sku19,qty19,price19,total19) 
                VALUES (%s,%s,%s,,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                cur.execute(raw2,[(v[0]),(cid),(type1),(pp1),(skk1),(qtt1),(prr1),(ttt1),(pp2),(skk2),(qtt2),(prr2),(ttt2),(pp3),(skk3),(qtt3),(prr3),(ttt3),(pp4),(skk4),(qtt4),(prr4),(ttt4),(pp5),(skk5),(qtt5),(prr5),(ttt5)
                ,(pp6),(skk6),(qtt6),(prr6),(ttt6),(pp7),(skk7),(qtt7),(prr7),(ttt7),(pp8),(skk8),(qtt8),(prr8),(ttt8),(pp9),(skk9),(qtt9),(prr9),(ttt9),(pp10),(skk10),(qtt10),(prr10),(ttt10),(pp11),(skk11),(qtt11),(prr11),(ttt11),(pp12),(skk12),(qtt12),(prr12),(ttt12)
                ,(pp13),(skk13),(qtt13),(prr13),(ttt13),(pp14),(skk14),(qtt14),(prr14),(ttt14),(pp15),(skk15),(qtt15),(prr15),(ttt15),(pp16),(skk16),(qtt16),(prr16),(ttt16),(pp17),(skk17),(qtt17),(prr17),(ttt17)
                ,(pp18),(skk18),(qtt18),(prr18),(ttt18),(pp19),(skk19),(qtt19),(prr19),(ttt19),(pp20),(skk20),(qtt20),(prr20),(ttt20)])
                mydata.commit()
            except:
                pass    
            estwin.destroy()
        hf2.place(relx=0.1,rely=0.10,relwidth=0.8,relheight=0.3)
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