
from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk

import mysql.connector
from tkinter import messagebox

def fun():#db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='finsys_tkinter'
        )
    mycursor = mydb.cursor()

def add_customer():
   import addcustomer_form

customer =tk.Tk()
fun()
customer.title('fynsYs')
customer.geometry("2000x2000")
customer['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=25,)
inv_heading= Label(customer, text="CUSTOMERS",bd=10,relief="groove",font=headingfont,bg='#243e55', fg='#fff',height=2,pady=2)
inv_heading.pack(fill=X)

content_label=Label(customer,relief="groove",bg='#243e55', fg='#fff',width=500,height=30)

add_customer=Button(content_label,text="Add Customer",background='#243e55', foreground="white",command=add_customer)
add_customer.place(x=1450,y=100)

style = ttk.Style()
style.theme_use('classic')


custom_data = ttk.Treeview(content_label)


custom_data['columns']= ('customer', 'gst_type','gstin','panno','email','mobile','action')
custom_data.column("#0", width=0,  stretch=NO)
custom_data.column("customer",anchor=CENTER )
custom_data.column("gst_type",anchor=CENTER, )
custom_data.column("gstin",anchor=CENTER,)
custom_data.column("panno",anchor=CENTER,)
custom_data.column("email",anchor=CENTER,)
custom_data.column("mobile",anchor=CENTER)
custom_data.column("action",anchor=CENTER)

custom_data.heading("#0",text="",anchor=CENTER)
custom_data.heading("customer",text="CUSTOME",anchor=CENTER)
custom_data.heading("gst_type",text="GST TYPE",anchor=CENTER)
custom_data.heading("gstin",text="GSTIN",anchor=CENTER)
custom_data.heading("panno",text="PAN NO",anchor=CENTER)
custom_data.heading("email",text="EMAIL ID",anchor=CENTER)
custom_data.heading("mobile",text="MOBILE NO",anchor=CENTER)
custom_data.heading("action",text="ACTION",anchor=CENTER)

custom_data.place(x=180,y=200)

sql='SELECT firstname,gsttype,gstin,panno,email,mobile from customer'
mycursor.execute(sql)
customer_data=mycursor.fetchall()
total=mycursor.rowcount


for data in customer_data: 
    custom_data.insert("", 'end',values=data)


content_label.place(x=0,y=150)
customer.mainloop()
