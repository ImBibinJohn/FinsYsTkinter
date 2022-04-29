import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
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
mycanvas.create_window((0,0),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1300,height=1900,bg='#243e55')
mycanvas.create_window((20,60),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#243e55",width=100)
form_lable.place(x=0,y=0)

san_lbl = Label(form_frame, text="Reconcile Inventory Asset", font=('times new roman', 20, 'bold'), bg="#243e55", fg="#fff")
san_lbl.place(x=500)
san_lbl = Label(form_frame, text="Statement ending date : 2022-04-07", font=('times new roman', 11, 'bold'),width=26, bg="#243e55", fg="#fff")
san_lbl.place(x=535,y=70)

# Label Widget
a = Label(form_frame, bg="#243e55", fg="#fff",font=('times new roman', 10, 'bold'))
a.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.4)
san1_lbl = Label(a, text="₹ 677777", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san1_lbl.grid(row=1, column=0, padx=10, pady=0, sticky='W')
san2_lbl = Label(a, text="STATEMENT ENDING BALANCE", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san2_lbl.grid(row=2, column=0, padx=10, pady=0, sticky='W')
san3_lbl = Label(a, text="-", font=('times new roman', 25, 'bold'), bg="#243e55", fg="#fff")
san3_lbl.grid(row=1, column=1, padx=10, pady=0, sticky='W')
san4_lbl = Label(a, text="₹ 2328343", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san4_lbl.grid(row=1, column=2, padx=10, pady=0, sticky='W')
san5_lbl = Label(a, text="CLEARED BALANCE", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san5_lbl.grid(row=2, column=2, padx=10, pady=0, sticky='W')

a1 = Label(form_frame, bg="#243e55", fg="#fff",font=('times new roman', 10, 'bold'))
a1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.4)
san6_lbl = Label(a1, text="₹ 2333333", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san6_lbl.grid(row=1, column=0, padx=10, pady=0, sticky='W')
san7_lbl = Label(a1, text="BEGINNING BALANCE", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san7_lbl.grid(row=2, column=0, padx=10, pady=0, sticky='W')
san8_lbl = Label(a1, text="-", font=('times new roman', 25, 'bold'), bg="#243e55", fg="#fff")
san8_lbl.grid(row=1, column=1, padx=10, pady=0, sticky='W')
san9_lbl = Label(a1, text="₹ 5000", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san9_lbl.grid(row=1, column=2, padx=10, pady=0, sticky='W')
san10_lbl = Label(a1, text="PAYMENTS", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san10_lbl.grid(row=2, column=2, padx=10, pady=0, sticky='W')
san11_lbl = Label(a1, text="+", font=('times new roman', 25, 'bold'), bg="#243e55", fg="#fff")
san11_lbl.grid(row=1, column=3, padx=10, pady=0, sticky='W')
san12_lbl = Label(a1, text="₹ 10", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san12_lbl.grid(row=1, column=4, padx=10, pady=0, sticky='W')
san13_lbl = Label(a1, text="DEPOSITS", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san13_lbl.grid(row=2, column=4, padx=10, pady=0, sticky='W')

# Separator object
separator = ttk.Separator(form_frame, orient='vertical')
separator.place(relx=0.70, rely=0.1, relwidth=0.2, relheight=0.1)
# Label Widget
san14_lbl = Label(separator, font=('times new roman', 10, 'bold'),fg="#fff")
san14_lbl.grid(row=1, column=4, padx=10, pady=0, sticky='W')
san15_lbl = Label(separator, font=('times new roman', 10, 'bold'), fg="#fff")
san15_lbl.grid(row=2, column=4, padx=10, pady=0, sticky='W')
san16_lbl = Label(separator, text="₹ -1650566", font=('times new roman', 14, 'bold'), fg="#243e55")
san16_lbl.grid(row=3, column=8, padx=10, pady=0, sticky='W')
san17_lbl = Label(separator, text="DIFFERENCES", font=('times new roman', 14, 'bold'), fg="#243e55")
san17_lbl.grid(row=4, column=8, padx=10, pady=0, sticky='W')


F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F.place(x=25, y=600, width=1250, height=400)

b = Button(F,text = "Payments",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=500,y=5,width=200,height=40) 
b = Button(F,text = "Deposits",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=700,y=5,width=200,height=40) 
b = Button(F,text = "All",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=900,y=5,width=100,height=40) 

F1 = LabelFrame(F, font=('times new roman', 15, 'bold'),fg="Black", bg="#243e55")
F1.place(x=0, y=50, width=1235, height=300)

tree = ttk.Treeview(F1,height=10)
tree['show'] = 'headings'

sb = ttk.Scrollbar(F1, orient="vertical", command=tree.yview)
sb.grid(row=3,column=1,sticky="NS",pady=5)

tree.configure(yscrollcommand=sb.set)

tree["columns"]=("1","2","3","4","5","6","7","8")

tree.column("1", width=130)
tree.column("2", width=150)
tree.column("3", width=150)
tree.column("4", width=155)
tree.column("5", width=155)
tree.column("6", width=155)
tree.column("7", width=155)
tree.column("8", width=155)


tree.heading("1", text="DATE")
tree.heading("2", text="TYPE")
tree.heading("3", text="REF NO.")
tree.heading("4", text="ACCOUNT")
tree.heading("5", text="PAYEE")
tree.heading("6", text="MEMO")
tree.heading("7", text="DEPOSIT(INR)")
tree.heading("8", text="PAYMENT(INR)")

tree.grid(row=3,column=0,padx=5,pady=5)
data=['21-04-2022','Journel','4','4554 1236 8585 1221','100000','service charge','5000000','100000']
item1 = tree.insert("", "end", values=(data))



wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

 

root.mainloop()


