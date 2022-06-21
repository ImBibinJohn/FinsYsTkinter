import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
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
    edit_btn = Button(f2, text="Edit")
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