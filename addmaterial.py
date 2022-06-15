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
    mycanvass.create_window((0,0),window=frame1,anchor='nw',width=1500,height=2000)
            #PRODUCT     
    tk.Label(frame1,text='PRODUCT NAME',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.01)
    product=tk.Entry(frame1)
    product.place(relx=0.15,rely=0.03,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.01)
    sku=tk.Entry(frame1)
    sku.place(relx=0.45,rely=0.03,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='HSN',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.05)
    hsn=tk.Entry(frame1)
    hsn.place(relx=0.15,rely=0.07,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='QUANTITY',font=('times new roman', 14),bg='#2f516f').place(relx=0.45,rely=0.05)
    quanty=tk.Entry(frame1)
    quanty.place(relx=0.45,rely=0.07,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='Manufacturing Date',bg='#2f516f',font=('times new roman', 14)).place(relx=0.15,rely=0.09)
    mandate=StringVar()
    DateEntry(frame1,textvariable=mandate,date_pattern='y-mm-dd').place(relx=0.15,rely=0.11,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='Expiry Date',bg='#2f516f',font=('times new roman', 14)).place(relx=0.45,rely=0.09)
    expdate=StringVar()
    DateEntry(frame1,textvariable=expdate,date_pattern='y-mm-dd').place(relx=0.45,rely=0.11,relwidth=0.2,relheight=0.015)
    tk.Label(frame1,text='Manufacture',bg='#243e54',font=('Times New Roman',30)).place(relx=0.31,rely=0.14)
    #components
    tk.Label(frame1,text='Product Name',font=('times new roman', 14),bg='#2f516f').place(relx=0.01,rely=0.2)
    tk.Label(frame1,text='SKU',font=('times new roman', 14),bg='#2f516f').place(relx=0.1,rely=0.2)
    tk.Label(frame1,text='Quantity',font=('times new roman', 14),bg='#2f516f').place(relx=0.15,rely=0.2)
    tk.Label(frame1,text='Price',font=('times new roman', 14),bg='#2f516f').place(relx=0.2,rely=0.2)
    tk.Label(frame1,text='Amount',font=('times new roman', 14),bg='#2f516f').place(relx=0.25,rely=0.2)
    hf2.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.6)
    estwin.mainloop() 
addmaterial()    