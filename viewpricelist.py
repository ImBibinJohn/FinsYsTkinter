import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def viewpricelist():
    global treevv
    viewpricewin=tk.Tk()
    viewpricewin.title('View Materials')
    viewpricewin.geometry('1500x900')
    viewpricewin['bg'] = '#2f516f'
    f1=tk.Frame(viewpricewin,bg='#243e54')
    tk.Label(f1,text='PRICE LIST',bg='#243e54',font=('Times New Roman',24)).place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    f1.place(relx=0.1,rely=0.05,relheight=0.1,relwidth=0.8)
    f2=tk.Frame(viewpricewin,bg='#243e54')
    serch=tk.Entry(f2)
    serch.place(relx=0,rely=0,relwidth=0.2,relheight=0.07)
    search=tk.Button(f2,text='Search',bg='#243e54',font=('Times New Roman',14))
    search.place(relx=0.25,rely=0,relwidth=0.15,relheight=0.07)
    #tree
        #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='black',fieldbackground='#243e54')
    style.map('Treeview',background=[('selected','green')])
    treevv = ttk.Treeview(f2, height=20, columns=(1,2,3,4), show='headings') 
    treevv.heading(1, text='ID')
    treevv.heading(2, text='PRODUCT NAME')#headings
    treevv.heading(3, text='SKU')
    treevv.heading(4, text='PRICE')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=10, width=20,anchor=CENTER)#coloumns
    treevv.column(2, minwidth=30, width=260,anchor=CENTER)
    treevv.column(3, minwidth=30, width=160,anchor=CENTER)
    treevv.column(4, minwidth=30, width=160,anchor=CENTER)
    treevv.place(relx=0,rely=0.1,relwidth=1,relheight=0.7)
    edit_btn = Button(f2, text="Edit")
    edit_btn.place(relx=0.35,rely=0.85,relheight=0.1,relwidth=0.1)
    del_btn = Button(f2, text="Delete")
    del_btn.place(relx=0.5,rely=0.85,relheight=0.1,relwidth=0.1)  
    f2.place(relx=0.1,rely=0.2,relheight=0.7,relwidth=0.8)
    viewpricewin.mainloop()
viewpricelist()
