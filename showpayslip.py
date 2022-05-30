from enum import auto
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
from tkinter.tix import AUTO
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from requests import get
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql
from tkinter.tix import AUTO

def fun():#db connection
    global mydb1,mycursor
    mydb1=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsYs_tkinter'
        )
    mycursor = mydb1.cursor()
def edit():
    global customer_name
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    payslip_id=[values[-1]]
    mycursor.execute("SELECT * FROM app1_payslip WHERE payslipid=%s",(payslip_id))
    data=mycursor.fetchone()

#Delete payslip
def delete_payslip():
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    payslip_id=[values[-1]]
    print(payslip_id)
    mycursor.execute("DELETE FROM app1_payslip WHERE payslipid=%s",(payslip_id))
    mydb1.commit()
    messagebox.showinfo('successfully Deleted')
    print('sucessfully deleted')
    tree_data.delete(focus_data)

root = tk.Tk()
fun()
root.title("finsYs")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")
wrappen=ttk.LabelFrame(root)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=1345,height=500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=700,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="PAYSLIP", font=('times new roman', 28, 'bold'),padx=580, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=30, pady=30, bd=0, fg="Black", bg="#243e55")
F.place(x=30, y=30, width=1270, height=450)


global tree_data
tree_data = ttk.Treeview(F,height=15)
tree_data['show'] = 'headings'

sb = ttk.Scrollbar(F, orient="vertical", command=tree_data.yview)
sb.grid(row=0,column=1,sticky="NS",pady=30)

tree_data.configure(yscrollcommand=sb.set)

tree_data["columns"]=("1","2","3","4","5")

tree_data.column("1", width=220)
tree_data.column("2", width=240)
tree_data.column("3", width=240)
tree_data.column("4", width=240)
tree_data.column("5", width=240)


tree_data.heading("1", text="EMPLOYEE ID")
tree_data.heading("2", text="EMPLOYEE NAME")
tree_data.heading("3", text="DESIGNATION")
tree_data.heading("4", text="DATE OF PAYMENT")
tree_data.heading("5", text="NET SALARY")

sql = 'SELECT employeenumber,empname,desig,paydate,netsal,payslipid from app1_payslip'
mycursor.execute(sql)
trees_data=mycursor.fetchall()
total=mycursor.rowcount

for data in trees_data:
    tree_data.insert("", 'end',values=data)
    
tree_data.grid(row=0,column=0,padx=5,pady=5)


edit_btn = ttk.Button(F, text="Edit", command='edit_sale')
edit_btn.place(relx=0.35, rely=0.85, relheight=0.1, relwidth=0.1)
del_btn = ttk.Button(F, text="Delete",command=delete_payslip)
del_btn.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.1)

wrappen.pack(fill='both',expand='yes',)




root.mainloop()