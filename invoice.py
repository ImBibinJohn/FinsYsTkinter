from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk



def add_invoice():
    import invoice_form2


invoice =tk.Tk()
invoice.title('fynsYs')
invoice.geometry("5000x5000")
invoice['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=25,)
inv_heading= Label(invoice, text="INVOICES",bd=10,relief="groove",font=headingfont,bg='#243e55', fg='#fff',height=2,pady=2)
inv_heading.pack(fill=X)

content_label=Label(invoice,relief="groove",bg='#243e55', fg='#fff',width=500,height=30)

add_invoices=Button(content_label,text="Add Invoices",background='#243e55', foreground="white",command=add_invoice)
add_invoices.place(x=1650,y=100)

style = ttk.Style()
style.theme_use('classic')


set = ttk.Treeview(content_label)


set['columns']= ('invoice_no', 'invoice_date','customer','email_id','due_date','grade_total','balance_due','action')
set.column("#0", width=0,  stretch=NO)
set.column("invoice_no",anchor=CENTER )
set.column("invoice_date",anchor=CENTER, )
set.column("customer",anchor=CENTER,)
set.column("email_id",anchor=CENTER,)
set.column("due_date",anchor=CENTER,)
set.column("grade_total",anchor=CENTER)
set.column("balance_due",anchor=CENTER)
set.column("action",anchor=CENTER)

set.heading("#0",text="",anchor=CENTER)
set.heading("invoice_no",text="INVOICE NO",anchor=CENTER)
set.heading("invoice_date",text="INVOICE DATE",anchor=CENTER)
set.heading("customer",text="CUSTOMER",anchor=CENTER)
set.heading("email_id",text="EMAIL ID",anchor=CENTER)
set.heading("due_date",text="DUE DATE",anchor=CENTER)
set.heading("grade_total",text="GRADE TOTAL",anchor=CENTER)
set.heading("balance_due",text="BALANCE DUE",anchor=CENTER)
set.heading("action",text="ACTION",anchor=CENTER)
set.place(x=180,y=200)


add_invoice= Tk()


content_label.place(x=0,y=150)
invoice.mainloop()
