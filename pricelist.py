import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def pricelist():
    pricewin=tk.Tk()
    pricewin.title('ADD PRICE LIST')
    pricewin.geometry('1500x700')
    pricewin['bg'] = '#2f516f'
    cid=2
    frame=tk.Frame(pricewin,bg='#243e54')
    frame.place(relx=0.15,rely=0.2,relwidth=0.7,relheight=0.4)
    tk.Label(frame,text='Product Name',bg='#243e54',font=('Times New Roman',16)).place(relx=0.2,rely=0.1)
    tk.Label(frame,text='SKU',bg='#243e54',font=('Times New Roman',16)).place(relx=0.45,rely=0.1)
    tk.Label(frame,text='PRICE',bg='#243e54',font=('Times New Roman',16)).place(relx=0.7,rely=0.1)
    def pricelistprod(w):
        prodd=prod.get()
    prod=ttk.Combobox(frame)
    prod.bind('<<ComboboxSelected>>',pricelistprod)
    prod.place(relx=0.2,rely=0.25,relheight=0.1,relwidth=0.2)
    sku=tk.Entry(frame)
    sku.place(relx=0.45,rely=0.25,relheight=0.1,relwidth=0.2)
    price=tk.Entry(frame)
    price.place(relx=0.7,rely=0.25,relheight=0.1,relwidth=0.2)
    tk.Button(frame,text='CREATE',bg='green',font=('Times New Roman',16)).place(relx=0.3,rely=0.6,relheight=0.2,relwidth=0.4)
    pricewin.mainloop()
pricelist()    