from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
import mysql.connector as mysql
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry

def fun():#db connection
    global mydb1,mycursor
    mydb1=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsYs_tkinter'
        )
    mycursor = mydb1.cursor()

def add_custom():
    import addcustomer_form



#Delete salerecords
def delete_salerecords():
    focus_data = trees_data.focus()
    values=trees_data.item(focus_data,'values')
    salesrecpts_id=[values[-1]]
    mycursor.execute("DELETE FROM app1_salesrecpts WHERE salesrecptsid=%s",(salesrecpts_id))
    mydb1.commit()
    messagebox.showinfo('successfully Deleted')
    print('sucessfully deleted')
    trees_data.delete(focus_data)




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

full_frame=Frame(mycanvas,width=1345,height=2200,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1340,height=1900,bg='#243e55')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#243e55",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="SALES RECORDS", font=('times new roman', 28, 'bold'),padx=504, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F.place(x=20, y=50, width=1300, height=400)

menu= StringVar()
menu.set("New Transaction")

#Create a dropdown Menu
drop= OptionMenu(form_frame, menu,"Invoice", "Payment","Sales Receipt","Credit note","Estimate","Delayed Charge","Time Activity")
drop.place(x=1150,y=10,width=150)

global tree_data
tree_data = ttk.Treeview(F,height=15)
tree_data['show'] = 'headings'

sb = ttk.Scrollbar(F, orient="vertical", command=tree_data.yview)
sb.grid(row=1,column=1,sticky="NS",pady=5)

tree_data.configure(yscrollcommand=sb.set)

tree_data["columns"]=("1","2","3","4","5","6","7","8","9")

tree_data.column("1", width=140)
tree_data.column("2", width=140)
tree_data.column("3", width=140)
tree_data.column("4", width=140)
tree_data.column("5", width=140)
tree_data.column("6", width=140)
tree_data.column("7", width=140)
tree_data.column("8", width=140)
tree_data.column("9", width=130)


tree_data.heading("1", text="DATE")
tree_data.heading("2", text="TYPE")
tree_data.heading("3", text="NO.")
tree_data.heading("4", text="CUSTOMER")
tree_data.heading("5", text="DUE DATE")
tree_data.heading("6", text="BALANCE")
tree_data.heading("7", text="TOTAL BEFORE")
tree_data.heading("8", text="TAX")
tree_data.heading("9", text="TOTAL")

sql = 'SELECT saledate,salepay,saleno,salename,saledate,saaletotal,salesubtotal,saletaxamount,salegrandtotal,salesrecptsid from app1_salesrecpts'
mycursor.execute(sql)
trees_data=mycursor.fetchall()
total=mycursor.rowcount

for data in trees_data:
    tree_data.insert("", 'end',values=data)
    
tree_data.grid(row=1,column=0,padx=5,pady=5)


edit_btn = ttk.Button(F, text="Edit", command='')
edit_btn.place(relx=0.35, rely=0.88, relheight=0.1, relwidth=0.1)
del_btn = ttk.Button(F, text="Delete",command=delete_salerecords)
del_btn.place(relx=0.5, rely=0.88, relheight=0.1, relwidth=0.1)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)



root.mainloop()





