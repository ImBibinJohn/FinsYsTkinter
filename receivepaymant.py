import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font


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
mycanvas.create_window((0,40),window=heading_frame,anchor="nw")
invoice_heading= tk.Label(heading_frame, text="RECIEVE PAYMENT",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=74)
invoice_heading.pack()

#form fields

form_frame=Frame(mycanvas,width=1345,height=1900,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="Fin sYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=90)
form_heading.pack()




select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = select_customer_input)

drop2['values']=("Select-Options")

select_customer_lab.place(x=30,y=200,height=15)
drop2.place(x=30,y=230,height=40,width=250)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=4,height=2,command=add_custom)
add_custom.place(x=290,y=230)

email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
email_lab.place(x=500,y=200,)
email_input=Entry(form_frame,bg='#2f516a',fg='#fff')
email_input.place(x=500,y=230,height=40,width=300)

Due_date_lab=Label(form_frame,text="Find by invoice number",bg='#243e55',fg='#fff')
Due_date_lab.place(x=970,y=200,height=40)
Due_date_lab=Entry(form_frame,bg='#2f516a',fg='#fff')
Due_date_lab.place(x=970,y=230,height=40,width=300)

invoice_date_lab=Label(form_frame,text="Payment Date",bg='#243e55',fg='#fff')
invoice_date_lab.place(x=30,y=300,)
invoice_date_input=Entry(form_frame,bg='#2f516a',fg='#fff')
invoice_date_input.place(x=30,y=330,height=40,width=300)

select_customer_lab=tk.Label(form_frame,text="Payment Method",bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = select_customer_input)

drop2['values']=("Select-Options")

select_customer_lab.place(x=30,y=400,height=15)
drop2.place(x=30,y=430,height=40,width=300)
wrappen.pack(fill='both',expand='yes',)


select_customer_lab=tk.Label(form_frame,text="Deposit to",bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = select_customer_input)

drop2['values']=("Select-Options")

select_customer_lab.place(x=970,y=400,height=15)
drop2.place(x=970,y=430,height=40,width=250)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=4,height=2,command=add_custom)
add_custom.place(x=1230,y=430)

invoice_date_lab1=Label(form_frame,text="Amount Recieved",bg='#243e55',fg='#fff')
invoice_date_lab1.place(x=970,y=500,)
invoice_date_lab1=Label(form_frame,text="0.00",bg='#243e55',fg='#fff')
invoice_date_lab1.place(x=970,y=530,)

# table form
h_lab=Label(form_frame,text="#",bg='#243e55',fg='#fff')
h_lab.place(x=65,y=750)

h_input1=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
h_input1.place(x=40,y=780,height=40,width=60)

h_input2=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
h_input2.place(x=40,y=840,height=40,width=60)

h_input3=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
h_input3.place(x=40,y=900,height=40,width=60)

h_input4=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
h_input4.place(x=40,y=960,height=40,width=60)


#col-1
product_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
product_lab.place(x=210,y=750,)
product_input1=StringVar()
product_drop1=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop1['values']=(" ")
product_drop1.place(x=140,y=780,height=40,width=230)

product_input2=StringVar()
product_drop2=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop2['values']=(" ")
product_drop2.place(x=140,y=840,height=40,width=230)

product_input3=StringVar()
product_drop3=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop3['values']=(" ")
product_drop3.place(x=140,y=900,height=40,width=230)

product_input4=StringVar()
product_drop4=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop4['values']=(" ")
product_drop4.place(x=140,y=960,height=40,width=230)

#col-2

hsn_lab=Label(form_frame,text="DUE DATE",bg='#243e55',fg='#fff')
hsn_lab.place(x=470,y=750,)

hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input1.place(x=410,y=780,height=40,width=190)

hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input2.place(x=410,y=840,height=40,width=190)

hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input3.place(x=410,y=900,height=40,width=190)

hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input4.place(x=410,y=960,height=40,width=190)

#col-3

desc_lab=Label(form_frame,text="ORIGINAL AMOUNT",bg='#243e55',fg='#fff')
desc_lab.place(x=675,y=750,)

desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input1.place(x=640,y=780,height=40,width=190)

desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input2.place(x=640,y=840,height=40,width=190)

desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input3.place(x=640,y=900,height=40,width=190)

desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input4.place(x=640,y=960,height=40,width=190)

#col-4
qty_lab=Label(form_frame,text="OPEN BALANCE",bg='#243e55',fg='#fff')
qty_lab.place(x=915,y=750,)

qty_input1=Entry(form_frame,bg='#2f516a',fg='#fff')
qty_input1.place(x=870,y=780,height=40,width=190)

qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input2.place(x=870,y=840,height=40,width=190)

qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input3.place(x=870,y=900,height=40,width=190)

qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input4.place(x=870,y=960,height=40,width=190)

#col-5
price_lab=Label(form_frame,text="PAYMENT",bg='#243e55',fg='#fff')
price_lab.place(x=1155,y=750,)

price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input1.place(x=1100,y=780,height=40,width=190)

price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input2.place(x=1100,y=840,height=40,width=190)

price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input3.place(x=1100,y=900,height=40,width=190)

price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input4.place(x=1100,y=960,height=40,width=190)






subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
subtotal_lab.place(x=900,y=1100,height=40)
subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
subtotal_input.place(x=1000,y=1100,height=40)

tax2_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
tax2_lab.place(x=900,y=1150,height=40)
tax2_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
tax2_input.place(x=1000,y=1150,height=40)

grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
grand_lab.place(x=900,y=1200,height=40)
grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
grand_input.place(x=1000,y=1200,height=40)


submit_button=Button(form_frame,text="Save",background="#2f516a", foreground="white",width=20,height=2)

submit_button.place(x=1100,y=1260)
font=('Times', 15)
notice_lab=Label(form_frame,text="Notice :",bg='#243e55',fg='#808080',font=('Times', 15))
notice_lab.place(x=30,y=1800,)

note_lab=Label(form_frame,text="Fin sYs Terms and Conditions Apply ",bg='#243e55',fg='#808080',)
note_lab.place(x=30,y=1825,)
note2_lab=Label(form_frame,text="Invoice was created on a computer and is valid without the signature and seal.  ",bg='#243e55',fg='#808080',)
note2_lab.place(x=30,y=1850,)


root.mainloop()


