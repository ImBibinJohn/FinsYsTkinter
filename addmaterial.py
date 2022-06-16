from re import I
import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
from datetime import datetime, date, timedelta
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def addmaterial():  
    estwin=tk.Tk()
    estwin.title('Materials')
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
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=900)
    hf1=tk.Frame(frame,bg='#243e54')
    tk.Label(hf1,text='MATERIAL MASTER',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    hf1.place(relx=0.1,rely=0.03,relwidth=0.8,relheight=0.1)
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
    product.place(relx=0.15,rely=0.025,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.01)
    sku=tk.Entry(frame1)
    sku.place(relx=0.45,rely=0.025,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='HSN',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.045)
    hsn=tk.Entry(frame1)
    hsn.place(relx=0.15,rely=0.06,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='QUANTITY',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.045)
    quanty=tk.Entry(frame1)
    quanty.place(relx=0.45,rely=0.06,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='Manufacturing Date',bg='#2f516f',font=('times new roman', 14)).place(relx=0.15,rely=0.08)
    mandate=StringVar()
    DateEntry(frame1,textvariable=mandate,date_pattern='y-mm-dd').place(relx=0.15,rely=0.10,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='Expiry Date',bg='#2f516f',font=('times new roman', 14)).place(relx=0.45,rely=0.08)
    expdate=StringVar()
    DateEntry(frame1,textvariable=expdate,date_pattern='y-mm-dd').place(relx=0.45,rely=0.10,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='Manufacture',bg='#243e54',font=('Times New Roman',30)).place(relx=0.31,rely=0.125)
    #components
    tk.Label(frame1,text='Components',bg='#243e54',font=('Times New Roman',20)).place(relx=0.14,rely=0.145)
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
    def calculatetotal(x):
        def clear_text():
            total.delete(0, END) 
        q=float(quan.get())
        r=float(price.get())
        tot=(q*r)
        subtot=tot
        clear_text()
        total.insert(0,tot)
    prod=ttk.Combobox(frame1,values=pro)
    prod.place(relx=0.01,rely=0.19,relheight=0.015,relwidth=0.08)
    sku=tk.Entry(frame1)
    sku.place(relx=0.105,rely=0.19,relheight=0.015,relwidth=0.06)
    quan=IntVar()  
    qty=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan)
    qty.bind('<FocusIn>',calculatetotal)
    qty.place(relx=0.18,rely=0.19,relheight=0.015,relwidth=0.05)
    price=IntVar()
    rate=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price)
    rate.bind('<FocusIn>',calculatetotal)
    rate.place(relx=0.245,rely=0.19,relheight=0.015,relwidth=0.05)
    total=tk.Entry(frame1,font=(8))
    total.place(relx=0.31,rely=0.19,relheight=0.015,relwidth=0.05)
    #row2
    def calculatetotal1(x):
        def clear_text1():
            total1.delete(0, END) 
        q1=float(quan1.get())
        r1=float(price1.get())
        tot1=(q1*r1)
        subtot=tot1
        clear_text1()
        total1.insert(0,tot1)
    prod1=ttk.Combobox(frame1,values=pro)
    prod1.place(relx=0.01,rely=0.21,relheight=0.015,relwidth=0.08)
    sku1=tk.Entry(frame1)
    sku1.place(relx=0.105,rely=0.21,relheight=0.015,relwidth=0.06)
    quan1=IntVar()  
    qty1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan1)
    qty1.bind('<FocusIn>',calculatetotal1)
    qty1.place(relx=0.18,rely=0.21,relheight=0.015,relwidth=0.05)
    price1=IntVar()
    rate1=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price1)
    rate1.bind('<FocusIn>',calculatetotal1)
    rate1.place(relx=0.245,rely=0.21,relheight=0.015,relwidth=0.05)
    total1=tk.Entry(frame1,font=(8))
    total1.place(relx=0.31,rely=0.21,relheight=0.015,relwidth=0.05)
    #row3
    def calculatetotal2(x):
        def clear_text2():
            total2.delete(0, END) 
        q2=float(quan2.get())
        r2=float(price2.get())
        tot2=(q2*r2)
        subtot=tot2
        clear_text2()
        total2.insert(0,tot2)
    prod2=ttk.Combobox(frame1,values=pro)
    prod2.place(relx=0.01,rely=0.23,relheight=0.015,relwidth=0.08)
    sku2=tk.Entry(frame1)
    sku2.place(relx=0.105,rely=0.23,relheight=0.015,relwidth=0.06)
    quan2=IntVar()  
    qty2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan2)
    qty2.bind('<FocusIn>',calculatetotal2)
    qty2.place(relx=0.18,rely=0.23,relheight=0.015,relwidth=0.05)
    price2=IntVar()
    rate2=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price2)
    rate2.bind('<FocusIn>',calculatetotal2)
    rate2.place(relx=0.245,rely=0.23,relheight=0.015,relwidth=0.05)
    total2=tk.Entry(frame1,font=(8))
    total2.place(relx=0.31,rely=0.23,relheight=0.015,relwidth=0.05)
    #row4
    def calculatetotal3(x):
        def clear_text3():
            total3.delete(0, END) 
        q3=float(quan3.get())
        r3=float(price3.get())
        tot3=(q3*r3)
        subtot=tot3
        clear_text3()
        total3.insert(0,tot3)
    prod3=ttk.Combobox(frame1,values=pro)
    prod3.place(relx=0.01,rely=0.25,relheight=0.015,relwidth=0.08)
    sku3=tk.Entry(frame1)
    sku3.place(relx=0.105,rely=0.25,relheight=0.015,relwidth=0.06)
    quan3=IntVar()  
    qty3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan3)
    qty3.bind('<FocusIn>',calculatetotal3)
    qty3.place(relx=0.18,rely=0.25,relheight=0.015,relwidth=0.05)
    price3=IntVar()
    rate3=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price3)
    rate3.bind('<FocusIn>',calculatetotal3)
    rate3.place(relx=0.245,rely=0.25,relheight=0.015,relwidth=0.05)
    total3=tk.Entry(frame1,font=(8))
    total3.place(relx=0.31,rely=0.25,relheight=0.015,relwidth=0.05)
    #row5
    def calculatetotal4(x):
        def clear_text4():
            total4.delete(0, END) 
        q4=float(quan4.get())
        r4=float(price4.get())
        tot4=(q4*r4)
        subtot=tot4
        clear_text4()
        total4.insert(0,tot4)
    prod4=ttk.Combobox(frame1,values=pro)
    prod4.place(relx=0.01,rely=0.27,relheight=0.015,relwidth=0.08)
    sku4=tk.Entry(frame1)
    sku4.place(relx=0.105,rely=0.27,relheight=0.015,relwidth=0.06)
    quan4=IntVar()  
    qty4=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan4)
    qty4.bind('<FocusIn>',calculatetotal4)
    qty4.place(relx=0.18,rely=0.27,relheight=0.015,relwidth=0.05)
    price4=IntVar()
    rate4=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price4)
    rate4.bind('<FocusIn>',calculatetotal4)
    rate4.place(relx=0.245,rely=0.27,relheight=0.015,relwidth=0.05)
    total4=tk.Entry(frame1,font=(8))
    total4.place(relx=0.31,rely=0.27,relheight=0.015,relwidth=0.05)
    #row6
    def calculatetotal5(x):
        def clear_text5():
            total5.delete(0, END) 
        q5=float(quan5.get())
        r5=float(price5.get())
        tot5=(q5*r5)
        subtot=tot5
        clear_text5()
        total5.insert(0,tot5)
    prod5=ttk.Combobox(frame1,values=pro)
    prod5.place(relx=0.01,rely=0.29,relheight=0.015,relwidth=0.08)
    sku5=tk.Entry(frame1)
    sku5.place(relx=0.105,rely=0.29,relheight=0.015,relwidth=0.06)
    quan5=IntVar()  
    qty5=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan5)
    qty5.bind('<FocusIn>',calculatetotal5)
    qty5.place(relx=0.18,rely=0.29,relheight=0.015,relwidth=0.05)
    price5=IntVar()
    rate5=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price5)
    rate5.bind('<FocusIn>',calculatetotal5)
    rate5.place(relx=0.245,rely=0.29,relheight=0.015,relwidth=0.05)
    total5=tk.Entry(frame1,font=(8))
    total5.place(relx=0.31,rely=0.29,relheight=0.015,relwidth=0.05)
    ##adding new row
    global x,btn
    x=0.31
    #row7
    def addnewrow1():  
        global x,prod6,btn1
        def calculatetotal6(xx):    
            def clear_text6():
                total6.delete(0, END) 
            q6=float(quan6.get())
            r6=float(price6.get())
            tot6=(q6*r6)
            subtot=tot6
            clear_text6()
            total6.insert(0,tot6)
        def clear1():
            btn.destroy()
        prod6=ttk.Combobox(frame1,values=pro)
        prod6.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
        sku6=tk.Entry(frame1)
        sku6.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
        quan6=IntVar()  
        qty6=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan6)
        qty6.bind('<FocusOut>',calculatetotal6)
        qty6.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
        price6=IntVar()
        rate6=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price6)
        rate6.bind('<FocusOut>',calculatetotal6)
        rate6.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
        total6=tk.Entry(frame1,font=(8))
        total6.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
        x=x+0.02
        clear1()
        btn1=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow2)
        btn1.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01) 
        #row8
    def addnewrow2():
        global x,prod7,btn2
        def calculatetotal7(xx):    
            def clear_text7():
                total7.delete(0, END) 
            q7=float(quan7.get())
            r7=float(price7.get())
            tot7=(q7*r7)
            subtot=tot7
            clear_text7()
            total7.insert(0,tot7)
        def clear2():
            btn1.destroy()
        prod7=ttk.Combobox(frame1,values=pro)
        prod7.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
        sku7=tk.Entry(frame1)
        sku7.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
        quan7=IntVar()  
        qty7=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan7)
        qty7.bind('<FocusOut>',calculatetotal7)
        qty7.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
        price7=IntVar()
        rate7=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price7)
        rate7.bind('<FocusOut>',calculatetotal7)
        rate7.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
        total7=tk.Entry(frame1,font=(8))
        total7.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
        x=x+0.02
        clear2()
        btn2=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow3)
        btn2.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01) 
        #row9
    def addnewrow3():
        global x,btn3
        def calculatetotal8(xx):    
            def clear_text8():
                total8.delete(0, END) 
            q8=float(quan8.get())
            r8=float(price8.get())
            tot8=(q8*r8)
            subtot=tot8
            clear_text8()
            total8.insert(0,tot8)
        def clear3():
            btn2.destroy()
        prod8=ttk.Combobox(frame1,values=pro)
        prod8.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
        sku8=tk.Entry(frame1)
        sku8.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
        quan8=IntVar()  
        qty8=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan8)
        qty8.bind('<FocusOut>',calculatetotal8)
        qty8.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
        price8=IntVar()
        rate8=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price8)
        rate8.bind('<FocusOut>',calculatetotal8)
        rate8.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
        total8=tk.Entry(frame1,font=(8))
        total8.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
        x=x+0.02
        clear3()
        btn3=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow4)
        btn3.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)  
        #row10
    def addnewrow4():
            global x,btn4
            def calculatetotal9(xx):    
                def clear_text9():
                    total9.delete(0, END) 
                q9=float(quan9.get())
                r9=float(price9.get())
                tot9=(q9*r9)
                subtot=tot9
                clear_text9()
                total9.insert(0,tot9)
            def clear4():
                btn3.destroy()
            prod9=ttk.Combobox(frame1,values=pro)
            prod9.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku9=tk.Entry(frame1)
            sku9.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan9=IntVar()  
            qty9=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan9)
            qty9.bind('<FocusOut>',calculatetotal9)
            qty9.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price9=IntVar()
            rate9=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price9)
            rate9.bind('<FocusOut>',calculatetotal9)
            rate9.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total9=tk.Entry(frame1,font=(8))
            total9.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear4()
            btn4=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow5)
            btn4.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                #row11
    def addnewrow5():
            global x,btn5
            def calculatetotal10(xx):    
                def clear_text10():
                    total10.delete(0, END) 
                q10=float(quan10.get())
                r10=float(price10.get())
                tot10=(q10*r10)
                subtot=tot10
                clear_text10()
                total10.insert(0,tot10)
            def clear5():
                btn4.destroy()
            prod10=ttk.Combobox(frame1,values=pro)
            prod10.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku10=tk.Entry(frame1)
            sku10.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan10=IntVar()  
            qty10=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan10)
            qty10.bind('<FocusOut>',calculatetotal10)
            qty10.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price10=IntVar()
            rate10=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price10)
            rate10.bind('<FocusOut>',calculatetotal10)
            rate10.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total10=tk.Entry(frame1,font=(8))
            total10.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear5()
            btn5=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow6)
            btn5.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01) 
         #row12   
    def addnewrow6():
            global x,btn6
            def calculatetotal11(xx):    
                def clear_text11():
                    total11.delete(0, END) 
                q11=float(quan11.get())
                r11=float(price11.get())
                tot11=(q11*r11)
                subtot=tot11
                clear_text11()
                total11.insert(0,tot11)
            def clear6():
                btn5.destroy()
            prod11=ttk.Combobox(frame1,values=pro)
            prod11.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku11=tk.Entry(frame1)
            sku11.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan11=IntVar()  
            qty11=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan11)
            qty11.bind('<FocusOut>',calculatetotal11)
            qty11.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price11=IntVar()
            rate11=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price11)
            rate11.bind('<FocusOut>',calculatetotal11)
            rate11.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total11=tk.Entry(frame1,font=(8))
            total11.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear6()
            btn6=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow7)
            btn6.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
             #row13  
    def addnewrow7():
            global x,btn7
            def calculatetotal12(xx):    
                def clear_text12():
                    total12.delete(0, END) 
                q12=float(quan12.get())
                r12=float(price12.get())
                tot12=(q12*r12)
                subtot=tot12
                clear_text12()
                total12.insert(0,tot12)
            def clear7():
                btn6.destroy()
            prod12=ttk.Combobox(frame1,values=pro)
            prod12.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku12=tk.Entry(frame1)
            sku12.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan12=IntVar()  
            qty12=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan12)
            qty12.bind('<FocusOut>',calculatetotal12)
            qty12.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price12=IntVar()
            rate12=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price12)
            rate12.bind('<FocusOut>',calculatetotal12)
            rate12.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total12=tk.Entry(frame1,font=(8))
            total12.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear7()
            btn7=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow8)
            btn7.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                 #row14 
    def addnewrow8():
            global x,btn8
            def calculatetotal13(xx):    
                def clear_text13():
                    total13.delete(0, END) 
                q13=float(quan13.get())
                r13=float(price13.get())
                tot13=(q13*r13)
                subtot=tot13
                clear_text13()
                total13.insert(0,tot13)
            def clear8():
                btn7.destroy()
            prod13=ttk.Combobox(frame1,values=pro)
            prod13.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku13=tk.Entry(frame1)
            sku13.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan13=IntVar()  
            qty13=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan13)
            qty13.bind('<FocusOut>',calculatetotal13)
            qty13.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price13=IntVar()
            rate13=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price13)
            rate13.bind('<FocusOut>',calculatetotal13)
            rate13.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total13=tk.Entry(frame1,font=(8))
            total13.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear8()
            btn8=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow9)
            btn8.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                     #row15 
    def addnewrow9():
            global x,btn9
            def calculatetotal14(xx):    
                def clear_text14():
                    total14.delete(0, END) 
                q14=float(quan14.get())
                r14=float(price14.get())
                tot14=(q14*r14)
                subtot=tot14
                clear_text14()
                total14.insert(0,tot14)
            def clear9():
                btn8.destroy()
            prod14=ttk.Combobox(frame1,values=pro)
            prod14.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku14=tk.Entry(frame1)
            sku14.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan14=IntVar()  
            qty14=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan14)
            qty14.bind('<FocusOut>',calculatetotal14)
            qty14.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price14=IntVar()
            rate14=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price14)
            rate14.bind('<FocusOut>',calculatetotal14)
            rate14.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total14=tk.Entry(frame1,font=(8))
            total14.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear9()
            btn9=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow10)
            btn9.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                         #row16
    def addnewrow10():
            global x,btn10
            def calculatetotal15(xx):    
                def clear_text15():
                    total15.delete(0, END) 
                q15=float(quan15.get())
                r15=float(price15.get())
                tot15=(q15*r15)
                subtot=tot15
                clear_text15()
                total15.insert(0,tot15)
            def clear10():
                btn9.destroy()
            prod15=ttk.Combobox(frame1,values=pro)
            prod15.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku15=tk.Entry(frame1)
            sku15.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan15=IntVar()  
            qty15=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan15)
            qty15.bind('<FocusOut>',calculatetotal15)
            qty15.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price15=IntVar()
            rate15=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price15)
            rate15.bind('<FocusOut>',calculatetotal15)
            rate15.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total15=tk.Entry(frame1,font=(8))
            total15.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear10()
            btn10=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow11)
            btn10.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)   
                             #row17 
    def addnewrow11():
            global x,btn11
            def calculatetotal16(xx):    
                def clear_text16():
                    total16.delete(0, END) 
                q16=float(quan16.get())
                r16=float(price16.get())
                tot16=(q16*r16)
                subtot=tot16
                clear_text16()
                total16.insert(0,tot16)
            def clear11():
                btn10.destroy()
            prod16=ttk.Combobox(frame1,values=pro)
            prod16.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku16=tk.Entry(frame1)
            sku16.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan16=IntVar()  
            qty16=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan16)
            qty16.bind('<FocusOut>',calculatetotal16)
            qty16.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price16=IntVar()
            rate16=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price16)
            rate16.bind('<FocusOut>',calculatetotal16)
            rate16.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total16=tk.Entry(frame1,font=(8))
            total16.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear11()
            btn11=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow12)
            btn11.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)                                                                     
    #row18
    def addnewrow12():
            global x,btn12
            def calculatetotal17(xx):    
                def clear_text17():
                    total17.delete(0, END) 
                q17=float(quan17.get())
                r17=float(price17.get())
                tot17=(q17*r17)
                subtot=tot17
                clear_text17()
                total17.insert(0,tot17)
            def clear12():
                btn11.destroy()
            prod17=ttk.Combobox(frame1,values=pro)
            prod17.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku17=tk.Entry(frame1)
            sku17.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan17=IntVar()  
            qty17=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan17)
            qty17.bind('<FocusOut>',calculatetotal17)
            qty17.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price17=IntVar()
            rate17=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price17)
            rate17.bind('<FocusOut>',calculatetotal17)
            rate17.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total17=tk.Entry(frame1,font=(8))
            total17.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear12()
            btn12=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow13)
            btn12.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
        #row19
    def addnewrow13():
            global x,btn13
            def calculatetotal18(xx):    
                def clear_text18():
                    total18.delete(0, END) 
                q18=float(quan18.get())
                r18=float(price18.get())
                tot18=(q18*r18)
                subtot=tot18
                clear_text18()
                total18.insert(0,tot18)
            def clear13():
                btn12.destroy()
            prod18=ttk.Combobox(frame1,values=pro)
            prod18.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku18=tk.Entry(frame1)
            sku18.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan18=IntVar()  
            qty18=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan18)
            qty18.bind('<FocusOut>',calculatetotal18)
            qty18.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price18=IntVar()
            rate18=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price18)
            rate18.bind('<FocusOut>',calculatetotal18)
            rate18.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total18=tk.Entry(frame1,font=(8))
            total18.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear13()
            btn13=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow14)
            btn13.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
            #row20
    def addnewrow14():
            global x,btn14
            def calculatetotal19(xx):    
                def clear_text19():
                    total19.delete(0, END) 
                q19=float(quan19.get())
                r19=float(price19.get())
                tot19=(q19*r19)
                subtot=tot19
                clear_text19()
                total19.insert(0,tot19)
            def clear14():
                btn13.destroy()
            prod19=ttk.Combobox(frame1,values=pro)
            prod19.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku19=tk.Entry(frame1)
            sku19.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan19=IntVar()  
            qty19=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan19)
            qty19.bind('<FocusOut>',calculatetotal19)
            qty19.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price19=IntVar()
            rate19=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price19)
            rate19.bind('<FocusOut>',calculatetotal19)
            rate19.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total19=tk.Entry(frame1,font=(8))
            total19.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear14()
            btn14=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow15)
            btn14.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)  
                #row21
    def addnewrow15():
            global x,btn15
            def calculatetotal20(xx):    
                def clear_text20():
                    total20.delete(0, END) 
                q20=float(quan20.get())
                r20=float(price20.get())
                tot20=(q20*r20)
                subtot=tot20
                clear_text20()
                total20.insert(0,tot20)
            def clear15():
                btn14.destroy()
            prod20=ttk.Combobox(frame1,values=pro)
            prod20.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku20=tk.Entry(frame1)
            sku20.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan20=IntVar()  
            qty20=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan20)
            qty20.bind('<FocusOut>',calculatetotal20)
            qty20.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price20=IntVar()
            rate20=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price20)
            rate20.bind('<FocusOut>',calculatetotal20)
            rate20.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total20=tk.Entry(frame1,font=(8))
            total20.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear15()
            btn15=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow16)
            btn15.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                    #row22
    def addnewrow16():
            global x,btn16
            def calculatetotal21(xx):    
                def clear_text21():
                    total21.delete(0, END) 
                q21=float(quan21.get())
                r21=float(price21.get())
                tot21=(q21*r21)
                subtot=tot21
                clear_text21()
                total21.insert(0,tot21)
            def clear16():
                btn15.destroy()
            prod21=ttk.Combobox(frame1,values=pro)
            prod21.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku21=tk.Entry(frame1)
            sku21.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan21=IntVar()  
            qty21=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan21)
            qty21.bind('<FocusOut>',calculatetotal21)
            qty21.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price21=IntVar()
            rate21=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price21)
            rate21.bind('<FocusOut>',calculatetotal21)
            rate21.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total21=tk.Entry(frame1,font=(8))
            total21.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear16()
            btn16=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow17)
            btn16.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
                        #row23
    def addnewrow17():
            global x,btn17
            def calculatetotal22(xx):    
                def clear_text22():
                    total22.delete(0, END) 
                q22=float(quan22.get())
                r22=float(price22.get())
                tot22=(q22*r22)
                subtot=tot22
                clear_text22()
                total22.insert(0,tot22)
            def clear17():
                btn16.destroy()
            prod22=ttk.Combobox(frame1,values=pro)
            prod22.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku22=tk.Entry(frame1)
            sku22.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan22=IntVar()  
            qty22=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan22)
            qty22.bind('<FocusOut>',calculatetotal22)
            qty22.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price22=IntVar()
            rate22=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price22)
            rate22.bind('<FocusOut>',calculatetotal22)
            rate22.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total22=tk.Entry(frame1,font=(8))
            total22.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear17()
            btn17=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow18)
            btn17.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
    #row24
    def addnewrow18():
            global x,btn18
            def calculatetotal23(xx):    
                def clear_text23():
                    total23.delete(0, END) 
                q23=float(quan23.get())
                r23=float(price23.get())
                tot23=(q23*r23)
                subtot=tot23
                clear_text23()
                total23.insert(0,tot23)
            def clear18():
                btn17.destroy()
            prod23=ttk.Combobox(frame1,values=pro)
            prod23.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku23=tk.Entry(frame1)
            sku23.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan23=IntVar()  
            qty23=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan23)
            qty23.bind('<FocusOut>',calculatetotal23)
            qty23.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price23=IntVar()
            rate23=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price23)
            rate23.bind('<FocusOut>',calculatetotal23)
            rate23.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total23=tk.Entry(frame1,font=(8))
            total23.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear18()
            btn18=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow19)
            btn18.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
        #row25
    def addnewrow19():
            global x,btn19
            def calculatetotal24(xx):    
                def clear_text24():
                    total24.delete(0, END) 
                q24=float(quan24.get())
                r24=float(price24.get())
                tot24=(q24*r24)
                subtot=tot24
                clear_text24()
                total24.insert(0,tot24)
            def clear19():
                btn18.destroy()
            prod24=ttk.Combobox(frame1,values=pro)
            prod24.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku24=tk.Entry(frame1)
            sku24.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan24=IntVar()  
            qty24=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan24)
            qty24.bind('<FocusOut>',calculatetotal24)
            qty24.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price24=IntVar()
            rate24=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price24)
            rate24.bind('<FocusOut>',calculatetotal24)
            rate24.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total24=tk.Entry(frame1,font=(8))
            total24.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear19()
            btn19=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow20)
            btn19.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
     #row26       
    def addnewrow20():
            global x,btn20
            def calculatetotal25(xx):    
                def clear_text25():
                    total25.delete(0, END) 
                q25=float(quan25.get())
                r25=float(price25.get())
                tot25=(q25*r25)
                subtot=tot25
                clear_text25()
                total25.insert(0,tot25)
            def clear20():
                btn19.destroy()
            prod25=ttk.Combobox(frame1,values=pro)
            prod25.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku25=tk.Entry(frame1)
            sku25.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan25=IntVar()  
            qty25=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan25)
            qty25.bind('<FocusOut>',calculatetotal25)
            qty25.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price25=IntVar()
            rate25=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price25)
            rate25.bind('<FocusOut>',calculatetotal25)
            rate25.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total25=tk.Entry(frame1,font=(8))
            total25.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear20()
            btn20=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow21)
            btn20.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
         #row27      
    def addnewrow21():
            global x,btn21
            def calculatetotal26(xx):    
                def clear_text26():
                    total26.delete(0, END) 
                q26=float(quan26.get())
                r26=float(price26.get())
                tot26=(q26*r26)
                subtot=tot26
                clear_text26()
                total26.insert(0,tot26)
            def clear21():
                btn20.destroy()
            prod26=ttk.Combobox(frame1,values=pro)
            prod26.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku26=tk.Entry(frame1)
            sku26.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan26=IntVar()  
            qty26=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan26)
            qty26.bind('<FocusOut>',calculatetotal26)
            qty26.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price26=IntVar()
            rate26=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price26)
            rate26.bind('<FocusOut>',calculatetotal26)
            rate26.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total26=tk.Entry(frame1,font=(8))
            total26.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear21()
            btn21=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow22)
            btn21.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)  
     #row28       
    def addnewrow22():
            global x,btn22
            def calculatetotal27(xx):    
                def clear_text27():
                    total27.delete(0, END) 
                q27=float(quan27.get())
                r27=float(price27.get())
                tot27=(q27*r27)
                subtot=tot27
                clear_text27()
                total27.insert(0,tot27)
            def clear22():
                btn21.destroy()
            prod27=ttk.Combobox(frame1,values=pro)
            prod27.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku27=tk.Entry(frame1)
            sku27.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan27=IntVar()  
            qty27=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan27)
            qty27.bind('<FocusOut>',calculatetotal27)
            qty27.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price27=IntVar()
            rate27=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price27)
            rate27.bind('<FocusOut>',calculatetotal27)
            rate27.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total27=tk.Entry(frame1,font=(8))
            total27.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear22()
            btn22=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow23)
            btn22.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
         #row29      
    def addnewrow23():
            global x,btn23
            def calculatetotal28(xx):    
                def clear_text28():
                    total28.delete(0, END) 
                q28=float(quan28.get())
                r28=float(price28.get())
                tot28=(q28*r28)
                subtot=tot28
                clear_text28()
                total28.insert(0,tot28)
            def clear23():
                btn22.destroy()
            prod28=ttk.Combobox(frame1,values=pro)
            prod28.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku28=tk.Entry(frame1)
            sku28.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan28=IntVar()  
            qty28=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan28)
            qty28.bind('<FocusOut>',calculatetotal28)
            qty28.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price28=IntVar()
            rate28=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price28)
            rate28.bind('<FocusOut>',calculatetotal28)
            rate28.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total28=tk.Entry(frame1,font=(8))
            total28.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear23()
            btn23=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow24)
            btn23.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
   #30     
    def addnewrow24():
            global x
            def calculatetotal29(xx):    
                def clear_text29():
                    total29.delete(0, END) 
                q29=float(quan29.get())
                r29=float(price29.get())
                tot29=(q29*r29)
                subtot=tot29
                clear_text29()
                total29.insert(0,tot29)
            def clear24():
                btn23.destroy()
            prod29=ttk.Combobox(frame1,values=pro)
            prod29.place(relx=0.01,rely=x,relheight=0.015,relwidth=0.08)
            sku29=tk.Entry(frame1)
            sku29.place(relx=0.105,rely=x,relheight=0.015,relwidth=0.06)    
            quan29=IntVar()  
            qty29=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=quan29)
            qty29.bind('<FocusOut>',calculatetotal29)
            qty29.place(relx=0.18,rely=x,relheight=0.015,relwidth=0.05)
            price29=IntVar()
            rate29=tk.Spinbox(frame1,from_=0,to=50,font=(8),textvariable=price29)
            rate29.bind('<FocusOut>',calculatetotal29)
            rate29.place(relx=0.245,rely=x,relheight=0.015,relwidth=0.05)
            total29=tk.Entry(frame1,font=(8))
            total29.place(relx=0.31,rely=x,relheight=0.015,relwidth=0.05)
            x=x+0.02
            clear24()                                                                           
                                                                                                                                                  
                                                                                   
                                                                 
                                                     

    btn=tk.Button(frame1,text='ADD PRODUCT',font=(6),command=addnewrow1)
    btn.place(relx=0.26,rely=x,relwidth=0.1,relheight=0.01)
    #coproducts/scrap
    #
    ##
    ######
    tk.Label(frame1,text='Coproducts/Scrap',bg='#243e54',font=('Times New Roman',20)).place(relx=0.54,rely=0.145)
    tk.Label(frame1,text='Product Name',font=('times new roman', 14),bg='#2f516f').place(relx=0.41,rely=0.17)
    tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.505,rely=0.17)
    tk.Label(frame1,text='Quantity',font=('times new roman', 14),bg='#2f516f').place(relx=0.585,rely=0.17)
    tk.Label(frame1,text='Price',font=('times new roman', 14),bg='#2f516f').place(relx=0.65,rely=0.17)
    tk.Label(frame1,text='Amount',font=('times new roman', 14),bg='#2f516f').place(relx=0.72,rely=0.17)
    #row11
    def calculatescraptotal11(x):
        def clear_scraptext():
            total11.delete(0, END) 
        q11=float(quan11.get())
        r11=float(price11.get())
        tot11=(q11*r11)
        subtot11=tot11
        clear_scraptext()
        total11.insert(0,tot11)
    prod11=ttk.Combobox(frame1)
    prod11.place(relx=0.41,rely=0.19,relheight=0.015,relwidth=0.08)
    sku11=tk.Entry(frame1)
    sku11.place(relx=0.505,rely=0.19,relheight=0.015,relwidth=0.06)
    quan11=IntVar()  
    qty11=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan11)
    qty11.bind('<FocusIn>',calculatescraptotal11)
    qty11.place(relx=0.585,rely=0.19,relheight=0.015,relwidth=0.05)
    price11=IntVar()
    rate11=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price11)
    rate11.bind('<FocusIn>',calculatescraptotal11)
    rate11.place(relx=0.65,rely=0.19,relheight=0.015,relwidth=0.05)
    total11=tk.Entry(frame1,font=(8))
    total11.place(relx=0.72,rely=0.19,relheight=0.015,relwidth=0.05)
    #row22
    def calculatescraptotal22(x):
        def clear_scraptext22():
            total22.delete(0, END) 
        q22=float(quan22.get())
        r22=float(price22.get())
        tot22=(q22*r22)
        subtot22=tot22
        clear_scraptext22()
        total22.insert(0,tot22)
    prod22=ttk.Combobox(frame1)
    prod22.place(relx=0.41,rely=0.21,relheight=0.015,relwidth=0.08)
    sku22=tk.Entry(frame1)
    sku22.place(relx=0.505,rely=0.21,relheight=0.015,relwidth=0.06)
    quan22=IntVar()  
    qty22=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan22)
    qty22.bind('<FocusIn>',calculatescraptotal22)
    qty22.place(relx=0.585,rely=0.21,relheight=0.015,relwidth=0.05)
    price22=IntVar()
    rate22=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price22)
    rate22.bind('<FocusIn>',calculatescraptotal22)
    rate22.place(relx=0.65,rely=0.21,relheight=0.015,relwidth=0.05)
    total22=tk.Entry(frame1,font=(8))
    total22.place(relx=0.72,rely=0.21,relheight=0.015,relwidth=0.05)
        #row33
    def calculatescraptotal33(x):
        def clear_scraptext33():
            total33.delete(0, END) 
        q33=float(quan33.get())
        r33=float(price33.get())
        tot33=(q33*r33)
        subtot33=tot33
        clear_scraptext33()
        total33.insert(0,tot33)
    prod33=ttk.Combobox(frame1)
    prod33.place(relx=0.41,rely=0.23,relheight=0.015,relwidth=0.08)
    sku33=tk.Entry(frame1)
    sku33.place(relx=0.505,rely=0.23,relheight=0.015,relwidth=0.06)
    quan33=IntVar()  
    qty33=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan33)
    qty33.bind('<FocusIn>',calculatescraptotal33)
    qty33.place(relx=0.585,rely=0.23,relheight=0.015,relwidth=0.05)
    price33=IntVar()
    rate33=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price33)
    rate33.bind('<FocusIn>',calculatescraptotal33)
    rate33.place(relx=0.65,rely=0.23,relheight=0.015,relwidth=0.05)
    total33=tk.Entry(frame1,font=(8))
    total33.place(relx=0.72,rely=0.23,relheight=0.015,relwidth=0.05)
            #row44
    def calculatescraptotal44(x):
        def clear_scraptext44():
            total44.delete(0, END) 
        q44=float(quan44.get())
        r44=float(price44.get())
        tot44=(q44*r44)
        subtot44=tot44
        clear_scraptext44()
        total44.insert(0,tot44)
    prod44=ttk.Combobox(frame1)
    prod44.place(relx=0.41,rely=0.25,relheight=0.015,relwidth=0.08)
    sku44=tk.Entry(frame1)
    sku44.place(relx=0.505,rely=0.25,relheight=0.015,relwidth=0.06)
    quan44=IntVar()  
    qty44=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=quan44)
    qty44.bind('<FocusIn>',calculatescraptotal44)
    qty44.place(relx=0.585,rely=0.25,relheight=0.015,relwidth=0.05)
    price44=IntVar()
    rate44=tk.Spinbox(frame1,from_=0,to=2147483647,font=(8),textvariable=price44)
    rate44.bind('<FocusIn>',calculatescraptotal44)
    rate44.place(relx=0.65,rely=0.25,relheight=0.015,relwidth=0.05)
    total44=tk.Entry(frame1,font=(8))
    total44.place(relx=0.72,rely=0.25,relheight=0.015,relwidth=0.05)

    hf2.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.6)
    estwin.mainloop() 
addmaterial()    