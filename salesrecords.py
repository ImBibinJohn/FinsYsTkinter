import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox as MessageBox
import mysql.connector as mysql
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
def add_custom():
    import addcustomer_form

root = tk.Tk()
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

tree = ttk.Treeview(F,height=15)
tree['show'] = 'headings'

sb = ttk.Scrollbar(F, orient="vertical", command=tree.yview)
sb.grid(row=1,column=1,sticky="NS",pady=5)

tree.configure(yscrollcommand=sb.set)

tree["columns"]=("1","2","3","4","5","6","7","8","9","10")

tree.column("1", width=125)
tree.column("2", width=125)
tree.column("3", width=125)
tree.column("4", width=125)
tree.column("5", width=125)
tree.column("6", width=125)
tree.column("7", width=125)
tree.column("8", width=125)
tree.column("9", width=125)
tree.column("10", width=125)

tree.heading("1", text="DATE")
tree.heading("2", text="TYPE")
tree.heading("3", text="NO.")
tree.heading("4", text="CUSTOMER")
tree.heading("5", text="DUE DATE")
tree.heading("6", text="BALANCE")
tree.heading("7", text="TOTAL BEFORE")
tree.heading("8", text="TAX")
tree.heading("9", text="TOTAL")
tree.heading("10", text="ACTION")
datas = ["22-10-2022","artist","1","Alen","12-10-2022","500000","235600","25","725000","ACTION"]
item = tree.insert("", "end", values=(datas))

tree.grid(row=1,column=0,padx=5,pady=5)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

 

root.mainloop()


