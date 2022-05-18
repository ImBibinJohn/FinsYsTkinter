
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
import datetime as dt
from webbrowser import get
import mysql.connector
from tkinter import messagebox


def fun():#db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='finsYs_tkinter'
        )
    mycursor = mydb.cursor()
# def get_product(*args):
#     print("selected product is")

#getting selected customer's email 
def get_email(event):
    option=drop2.get()
    mail_query="SELECT * FROM app1_customer "
    mycursor.execute(mail_query,option)
    table2=mycursor.fetchall()
    for i in table2:
        email.set(i[9])
        billto.set(i[12:17])
        # invno.set()



def add_custom():
    import addcustomer_form

#getting terms from dropdown
def get_terms(event):
    options=terms_input.get()
    if options=="Add New Term":
        invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
        invno_lab.place(x=500,y=400,)
        invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invno)
        invno_input.place(x=500,y=430,height=40)
    elif options=="Add New Term":
        invno_input.place_remove()

#getting selected product1 and quantity and set some entry feild value

def get_selected_product(event):
    global createsubtotal
    createsubtotal=0
    selected_product=[]
    product=product_drop1.get()
    quantity=qty_input1.get()
    selected_product.append(product)
    for product in inv_data:
        product_details="SELECT * FROM app1_inventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn.set(i[4])
            desc.set(i[11])
            price.set(i[12])
            sale_price=i[12]
            tota_price=int(sale_price)*int(quantity)
            total.set(tota_price)
    createsubtotal=createsubtotal+tota_price    
    subtotal.set(createsubtotal)
    for product in noninv_data:
        product_details="SELECT * FROM app1_noninventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn.set(i[4])
            desc.set(i[7])
            price.set(i[8])
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity)
            total.set(tota_price) 
    # createsubtotal=createsubtotal+tota_price
    # subtotal.set(createsubtotal)
    for product in bundleinv_data:
        product_details="SELECT * FROM app1_bundle WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn.set(i[4])
            desc.set(i[7])
            price.set(i[8])
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity)
            total.set(tota_price)   
    createsubtotal=createsubtotal+tota_price
    subtotal.set(createsubtotal) 

#getting selected product2 and set some entry feild value
def get_selected_product2(event):
    
    selected_product=[]
    product=product_drop2.get()
    selected_product.append(product)
    quantity2=qty_input2.get()
    for product in inv_data:
        product_details="SELECT * FROM app1_inventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn2.set(i[4])
            desc2.set(i[11])
            price2.set(i[12])
            sale_price=i[12]
            tota_price=int(sale_price)*int(quantity2)
            total2.set(tota_price)
    for product in noninv_data:
        product_details="SELECT * FROM app1_noninventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn2.set(i[4])
            desc2.set(i[7])
            price2.set(i[8]) 
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity2)
            total2.set(tota_price)
    for product in bundleinv_data:
        product_details="SELECT * FROM app1_bundle WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn2.set(i[4])
            desc2.set(i[7])
            price2.set(i[8])    
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity2)
            total2.set(tota_price)

def get_selected_product3(event):
    selected_product=[]
    product=product_drop3.get()
    selected_product.append(product)
    quantity3=qty_input3.get()
    for product in inv_data:
        product_details="SELECT * FROM app1_inventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn3.set(i[4])
            desc3.set(i[11])
            price3.set(i[12])
            sale_price=i[12]
            tota_price=int(sale_price)*int(quantity3)
            total3.set(tota_price)
    for product in noninv_data:
        product_details="SELECT * FROM app1_noninventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn3.set(i[4])
            desc3.set(i[7])
            price3.set(i[8])
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity3)
            total3.set(tota_price)
    for product in bundleinv_data:
        product_details="SELECT * FROM app1_bundle WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn3.set(i[4])
            desc3.set(i[7])
            price3.set(i[8])    
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity3)
            total3.set(tota_price)

def get_selected_product4(event):
    selected_product=[]
    product=product_drop4.get()
    selected_product.append(product)
    quantity4=qty_input4.get()
    for product in inv_data:
        product_details="SELECT * FROM app1_inventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn4.set(i[4])
            desc4.set(i[11])
            price4.set(i[12])
            sale_price=i[12]
            tota_price=int(sale_price)*int(quantity4)
            total4.set(tota_price)
    for product in noninv_data:
        product_details="SELECT * FROM app1_noninventory WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn4.set(i[4])
            desc4.set(i[7])
            price4.set(i[8]) 
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity4)
            total4.set(tota_price)
    for product in bundleinv_data:
        product_details="SELECT * FROM app1_bundle WHERE name=%s"
        mycursor.execute(product_details,selected_product)
        data=mycursor.fetchall()
        for i in data:
            hsn4.set(i[4])
            desc4.set(i[7])
            price4.set(i[8])  
            sale_price=i[8]
            tota_price=int(sale_price)*int(quantity4)
            total4.set(tota_price)  

#get total  and set subtotal 
def get_total(event):
    total1=total_input1.get()
    print("total1",total1)
    # price=price_input1.get()
    # total_price=int(price)*int(quantity)
    # total.set(total_price)

def save_invoice():
    global select_customer,email,invoice_date,terms,Due_date,billto,invno,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,tax2,grand,amt_received,balance
    select_customer=select_customer.get()
    email=email.get()
    invoice_date=invoice_date.get()
    terms=terms.get()
    Due_date=Due_date.get()
    billto=billto.get()
    invno=invno.get()
    place_of_supply=place_of_supply.get()
    product=product.get()
    hsn=hsn.get()
    desc=desc.get()
    qty=qty.get()
    price=price.get()
    total=total.get()
    tax=tax.get()
    subtotal=subtotal.get()
    tax2=tax2.get()
    grand=grand.get()
    amt_received=amt_received.get()
    balance=balance.get()
    sql="INSERT INTO app1_invoice (customername,email,invoiceno ,terms,invoicedate,duedate,bname ,placosupply ,product ,hsn,description,qty ,price ,total,tax ,subtotal ,grandtotal ,product2 ,hsn2,description2 ,qty2,price2,total2,tax2,product3,hsn3,description3,qty3,price3,total3,tax3,product4,hsn4,description4,qty4,price4,total4,tax4,amtrecvd,taxamount,baldue) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(select_customer,email,invno,terms,invoice_date,Due_date,billto,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,grand,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,amt_received,taxamount,balance)
    mycursor.execute(sql,val)
    mydb.commit()
    mydb.close()
    messagebox.showinfo('New Customer Added')








fun()
invoice_form = tk.Tk()
invoice_form.title("finsYs")
invoice_form.geometry("5000x2000")
invoice_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(invoice_form)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=2500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((150,40),window=heading_frame,anchor="nw")
invoice_heading= tk.Label(heading_frame, text="INVOICE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
invoice_heading.pack()

#form fields

form_frame=Frame(mycanvas,width=1600,height=1900,bg='#243e55')
mycanvas.create_window((150,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=50)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="FinsYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
form_heading.pack()

#get customer datas from customer table
mycursor.execute('select * from app1_customer ')
customers=mycursor.fetchall()


#set today date 
date = dt.datetime.now()
format_date = f"{date:%Y - %d - %m }"
today_date = Label(form_frame, text=format_date, fg="white", bg="black", font=("helvetica", 40))

#company details
user_id=[2]
mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
cmp1=mycursor.fetchone()

# cmp1=[1]

mycursor.execute("SELECT cname,cemail,state FROM app1_company WHERE id_id=%s",(user_id))
cmp_data=mycursor.fetchone()


#invetory data
mycursor.execute("SELECT * FROM app1_inventory WHERE cid_id=%s",(cmp1))
inventory_data=mycursor.fetchall()

#bundle data
mycursor.execute("SELECT * FROM app1_bundle WHERE cid_id=%s",(cmp1))
bundle_data=mycursor.fetchall()

#noninventor data
mycursor.execute("SELECT * FROM app1_noninventory WHERE cid_id=%s",(cmp1))
noninventory_data=mycursor.fetchall()

#service data
mycursor.execute("SELECT * FROM app1_service WHERE cid_id=%s",(cmp1))
services_data=mycursor.fetchall()



global select_customer,email,invoice_date,terms,Due_date,billto,invno,cmpname,cpmemail,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,tax2,grand,amt_received,balance

select_customer=StringVar()
email=StringVar()
invoice_date=StringVar()
terms=StringVar()
Due_date=StringVar()
billto=StringVar()
invno=StringVar()
place_of_supply=StringVar()
product=StringVar()
hsn=StringVar()
desc=StringVar()
qty=StringVar()
price=StringVar()
total=StringVar()
tax=StringVar()
subtotal=StringVar()
taxamount=StringVar()
grand=StringVar()
amt_received=StringVar()
balance=StringVar()






company_name_lab=Label(form_frame,text=cmp_data[0],bg='#243e55',fg='#fff',font="Helvetica 22 bold")
company_name_lab.place(x=50,y=70,)

company_email_lab=Label(form_frame,text=cmp_data[1],bg='#243e55',fg='#fff',font="Helvetica 10 bold")
company_email_lab.place(x=50,y=120,)

select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')

drop2=ttk.Combobox(form_frame,textvariable = select_customer)
customer_values=customers[0]
for cust in  customers:
    if customer_values[-1]==cmp1[0]:
        
        drop2['values']=(cust[2]+cust[3])
    else:
        messagebox.showerror('error', 'invalid data')
drop2.bind("<<ComboboxSelected>>",get_email)
select_customer_lab.place(x=30,y=200,height=15)
drop2.place(x=30,y=230,height=40,width=335)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=2,command=add_custom)
add_custom.place(x=370,y=230)

email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
email_lab.place(x=500,y=200,)
email_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=email)
email_input.place(x=500,y=230,height=40)

invoice_date_lab=Label(form_frame,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.place(x=30,y=300,)
invoice_date.set(format_date)
invoice_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invoice_date)
invoice_date_input.place(x=30,y=330,height=40)

terms_lab=Label(form_frame,text="Terms",bg='#243e55',fg='#fff')
terms_lab.place(x=500,y=300,)
terms_input=ttk.Combobox(form_frame,textvariable = terms)
terms_input['values']=("Due on Receipt","NET15","NET30","NET60","Add New Term")
# terms_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=terms)
terms_input.bind("<<ComboboxSelected>>",get_terms)
terms_input.place(x=500,y=330,height=40,width=335)

Due_date_lab=Label(form_frame,text="Due Date",bg='#243e55',fg='#fff')
Due_date_lab.place(x=970,y=300,height=40)
Due_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=Due_date)
Due_date_input.place(x=970,y=330,height=40)

billto_lab=Label(form_frame,text="Bill To",bg='#243e55',fg='#fff')
billto_lab.place(x=30,y=400,)
billto_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=billto)
billto_input.place(x=30,y=430,height=150)


# invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
# invno_lab.place(x=500,y=400,)
# invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invno)
# invno_input.place(x=500,y=430,height=40)

place_of_supply_lab=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')

drop2=ttk.Combobox(form_frame,textvariable=place_of_supply)
drop2['values']=(cmp_data[2],"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
 
place_of_supply_lab.place(x=30,y=600,)
drop2.place(x=30,y=630,height=40,width=335)

# table form

#col-1
product_lab=Label(form_frame,text="PRODUCT / SERVICES",bg='#243e55',fg='#fff')
product_lab.place(x=100,y=730,)

product_drop1=ttk.Combobox(form_frame,textvariable = product)
product1=[]
for proinv in inventory_data: 
    if proinv[-1] == cmp1[0] :
        inv_data=proinv[2]
        product1.append(inv_data)

for proinv in noninventory_data: 
    if proinv[-1] == cmp1[0] :
        noninv_data=proinv[2]
        product1.append(noninv_data)

for proinv in bundle_data: 
    if proinv[-1] == cmp1[0] :
        bundleinv_data=proinv[2]
        product1.append(bundleinv_data)
        
product_drop1['values']=product1
product_drop1.bind("<<ComboboxSelected>>",get_selected_product)

product_drop1.place(x=70,y=780,height=40,width=200)

product2=StringVar()
product_drop2=ttk.Combobox(form_frame,textvariable = product2)

# product2_data=[]
# for proinv in inventory_data: 
#     if proinv[-1] == cmp1[0] :
#         inv_data=proinv[2]
#         product2_data.append(inv_data)
       
# for proinv in noninventory_data: 
#     if proinv[-1] == cmp1[0] :
#         noninv_data=proinv[2]
#         product2_data.append(noninv_data)


# for proinv in bundle_data: 
#     if proinv[-1] == cmp1[0] :
#         bundleinv_data=proinv[2]
#         product2_data.append(bundleinv_data)
        
product_drop2['values']=product1
product_drop2.bind("<<ComboboxSelected>>",get_selected_product2)

product_drop2.place(x=70,y=850,height=40,width=200)

product3=StringVar()
product_drop3=ttk.Combobox(form_frame,textvariable = product3)
# product3_data=[]
# for proinv in inventory_data: 
#     if proinv[-1] == cmp1[0] :
#         inv_data=proinv[2]
#         product3_data.append(inv_data)
       
# for proinv in noninventory_data: 
#     if proinv[-1] == cmp1[0] :
#         noninv_data=proinv[2]
#         product3_data.append(noninv_data)


# for proinv in bundle_data: 
#     if proinv[-1] == cmp1[0] :
#         bundleinv_data=proinv[2]
#         product3_data.append(bundleinv_data)
        
product_drop3['values']=product1
product_drop3.bind("<<ComboboxSelected>>",get_selected_product3)
product_drop3.place(x=70,y=930,height=40,width=200)

product4=StringVar()
product_drop4=ttk.Combobox(form_frame,textvariable = product4)
product_drop4['values']=product1
product_drop4.bind("<<ComboboxSelected>>",get_selected_product4)
product_drop4.place(x=70,y=1000,height=40,width=200)

#col-2

hsn_lab=Label(form_frame,text="HSN",bg='#243e55',fg='#fff')
hsn_lab.place(x=350,y=730,)

hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn)
hsn_input1.place(x=300,y=780,height=40)

hsn2=StringVar()
hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn2)
hsn_input2.place(x=300,y=850,height=40)

hsn3=StringVar()
hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn3)
hsn_input3.place(x=300,y=930,height=40)

hsn4=StringVar()
hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn4)
hsn_input4.place(x=300,y=1000,height=40)

#col-3

desc_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
desc_lab.place(x=550,y=730,)


desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc)
desc_input1.place(x=500,y=780,height=40)

desc2=StringVar()
desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc2)
desc_input2.place(x=500,y=850,height=40)

desc3=StringVar()
desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc3)
desc_input3.place(x=500,y=930,height=40)

desc4=StringVar()
desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc4)
desc_input4.place(x=500,y=1000,height=40)

#col-4
qty_lab=Label(form_frame,text="QUANTITY",bg='#243e55',fg='#fff')
qty_lab.place(x=800,y=730,)

qty_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty)
qty_input1.place(x=750,y=780,height=40)

qty_input1.bind("<KeyRelease>",get_selected_product)


qty2=StringVar()
qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty2)
qty_input2.place(x=750,y=850,height=40)
qty_input2.bind("<KeyRelease>",get_selected_product2)


qty3=StringVar()
qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty3)
qty_input3.place(x=750,y=930,height=40)
qty_input3.bind("<KeyRelease>",get_selected_product3)


qty4=StringVar()
qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty4)
qty_input4.place(x=750,y=1000,height=40)
qty_input4.bind("<KeyRelease>",get_selected_product4)


#col-5
price_lab=Label(form_frame,text="PRICE",bg='#243e55',fg='#fff')
price_lab.place(x=1000,y=730,)

price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price)
price_input1.place(x=950,y=780,height=40)
# price_input1.bind("<KeyRelease>",get_qty)

price2=StringVar()
price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price2)
price_input2.place(x=950,y=850,height=40)

price3=StringVar()
price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price3)
price_input3.place(x=950,y=930,height=40)

price4=StringVar()
price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price4)
price_input4.place(x=950,y=1000,height=40)

#col-6
total_lab=Label(form_frame,text="TOTAL",bg='#243e55',fg='#fff')
total_lab.place(x=1200,y=730,)



total_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total)
total_input1.bind("<KeyRelease>",get_total)
total_input1.place(x=1150,y=780,height=40)


total2=StringVar()
total_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total2)
total_input2.place(x=1150,y=850,height=40)

total3=StringVar()
total_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total3)
total_input3.place(x=1150,y=930,height=40)

total4=StringVar()
total_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total4)
total_input4.place(x=1150,y=1000,height=40)

#ocol-7
tax_lab=Label(form_frame,text="TAX (%)",bg='#243e55',fg='#fff')
tax_lab.place(x=1400,y=730,)

tax1=StringVar()
tax_drop1=ttk.Combobox(form_frame,textvariable = tax)
tax_drop1['values']=(" ")
tax_drop1.place(x=1350,y=780,height=40,width=200)

tax2=StringVar()
tax_drop2=ttk.Combobox(form_frame,textvariable = tax2)
tax_drop2['values']=(" ")
tax_drop2.place(x=1350,y=850,height=40,width=200)

tax3=StringVar()
tax_drop3=ttk.Combobox(form_frame,textvariable = tax3)
tax_drop3['values']=(" ")
tax_drop3.place(x=1350,y=930,height=40,width=200)

tax4=StringVar()
tax_drop4=ttk.Combobox(form_frame,textvariable = tax4)
tax_drop4['values']=(" ")
tax_drop4.place(x=1350,y=1000,height=40,width=200)





subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
subtotal_lab.place(x=970,y=1200,height=40)
subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = subtotal)
subtotal_input.place(x=1100,y=1200,height=40)

taxamount_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
taxamount_lab.place(x=970,y=1300,height=40)
taxamount_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = taxamount)
taxamount_input.place(x=1100,y=1300,height=40)

grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
grand_lab.place(x=970,y=1400,height=40)
grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = grand)
grand_input.place(x=1100,y=1400,height=40)

amt_received_lab=Label(form_frame,text="Amount Received",bg='#243e55',fg='#fff')
amt_received_lab.place(x=970,y=1500,height=40)
amt_received_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = amt_received)
amt_received_input.place(x=1100,y=1500,height=40)

balance_lab=Label(form_frame,text="Balance Due",bg='#243e55',fg='#fff')
balance_lab.place(x=970,y=1600,height=40)
balance_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = balance)
balance_input.place(x=1100,y=1600,height=40)

submit_button=Button(form_frame,text="Save",background="#2f516a",command=save_invoice, foreground="white",width=20,height=2)

submit_button.place(x=1150,y=1700)
font=('Times', 15)
notice_lab=Label(form_frame,text="Notice :",bg='#243e55',fg='#808080',font=('Times', 15),)
notice_lab.place(x=30,y=1800,)

note_lab=Label(form_frame,text="Fin sYs Terms and Conditions Apply ",bg='#243e55',fg='#808080',)
note_lab.place(x=30,y=1825,)
note2_lab=Label(form_frame,text="Invoice was created on a computer and is valid without the signature and seal.  ",bg='#243e55',fg='#808080',)
note2_lab.place(x=30,y=1850,)


invoice_form.mainloop()





#