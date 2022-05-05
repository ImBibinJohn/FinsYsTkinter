import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox as MessageBox
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from requests import get
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql


    
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

form_frame=Frame(mycanvas,width=1340,height=1900,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)


accounttype=StringVar()
beginningbalance=StringVar()
endingbalance=StringVar()
endingdate=StringVar()
edat=StringVar()
serchar=StringVar()
expacc=StringVar()
idat1=StringVar()
intear=StringVar()
incacc=StringVar()

def addData():
    if accounttype.get() =="" or  beginningbalance.get() =="" or  endingbalance.get() =="":
        tkinter.messagebox.showerror("add data", "Enter Correct details")
    else:
        sqlcon = pymysql.connect(host ="localhost",user="root",password="",database="finsys_tkinter")
        cur = sqlcon.cursor()
        cur.execute("INSERT INTO recon1 (accounttype,beginningbalance,endingbalance ,endingdate,edat,serchar,expacc ,idat1 ,intear ,incacc) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
        
        accounttype.get(),
        beginningbalance.get(),
        endingbalance.get(),
        endingdate.get(),
        edat.get(),
        serchar.get(),
        expacc.get(),
        idat1.get(),
        intear.get(),
        incacc.get(),
        
        ))
        sqlcon.commit()
        sqlcon.close()
        tkinter.messagebox.showinfo("ADD", "Record entered successfully")
    

tit = Label(heading_frame, text="Reconcile An Account", font=('times new roman', 30, 'bold'),padx=475, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()
head_label = Label(heading_frame,text="Open your statement and let's get started.", font=('times new roman', 9, 'bold'),padx=0, pady=2,width=189, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
head_label.pack()

F2 = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F2.place(x=5, y=100, width=500, height=700)
size=(500,700)
ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
tk.Label(F2,image=ax,bg='#243e54').place(relx=0.00,rely=-0,relheight=1,relwidth=1)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)


F2 = LabelFrame(form_frame, text="Which account do you want to reconcile..??", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F2.place(x=510, y=100, width=830, height=700)

CheckVar1 = IntVar()

sanitizer1_lbl=tk.Label(F2,text="Account",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold'))

drop1=ttk.Combobox(F2,textvariable=accounttype)

drop1['values']=("Checking","Savings","Inventory Asset","Prepaid Expenses","Uncategorized Asset","Truck")

sanitizer1_lbl.place(x=10,y=50,height=15,width=100)
drop1.place(x=280,y=50,height=30,width=450)
wrappen.pack(fill='both',expand='yes',)


sanitize_lbl = Label(F2, text="Enter the following from your statement.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitize_lbl.place(x=10,y=110)

mask_lbl = Label(F2, text="Beginning balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
mask_lbl.place(x=10,y=160)
mask_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE,textvariable=beginningbalance)
mask_txt.place(x=10,y=200)

hand_gloves_lbl = Label(F2, text="Ending balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
hand_gloves_lbl.place(x=280,y=160)
hand_gloves_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief =GROOVE,textvariable=endingbalance)
hand_gloves_txt.place(x=280,y=200)

syrup_lbl = Label(F2, text="Ending date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
syrup_lbl.place(x=550,y=160)
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=endingdate)
cal.place(x=550,y=200)

sanitize_lbl = Label(F2, text="Enter the service charge or interest earned, if necessary.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitize_lbl.place(x=10,y=280)

cream_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
cream_lbl.place(x=10,y=340)
#Create a Calendar using DateEntry
cal1 = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=edat)
cal1.place(x=10,y=380)

thermal_gun_lbl = Label(F2, text="Service charge", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_gun_lbl.place(x=280,y=340)
thermal_gun_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff",bd=5,relief=GROOVE,textvariable=serchar)
thermal_gun_txt.place(x=280,y=380)

select_customer_lab=tk.Label(F2,text="Expense Account",font=('times new roman', 16, 'bold'),bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(F2,width=22,textvariable=expacc)

drop2['values']=('Advertising/Promotional',
            'Bank charges',
            'Business Licenses and Permits',
            'Charitable Contributions',
            'Computer and Internet Expense',
            'Continuing Education',
            'Depreciation Expense',
            'Dues and Subscriptions',
            'Housekeeping Charges',
            'Insurance Expense',
            'Insurance Expense-General Liability Insurance',
            'Insurance Expense-Health Insurance',
            'Insurance Expense-Life and Disability Insurance',
            'Insurance Expense-Professional Liability',
            'Interest Expense',
            'Meals and entertainment',
            'Office Supplies',
            'Postage and Delivery',
            'Printing and Reproduction',
            'Professional Fees',
            'Purchases',
            'Rent Expense',
            'Repair and maintenance',
            'Small Tools and Equipment',
            'Swachh Bharat Cess Expense',
            'Taxes - Property',
            'Telephone Expense',
            'Travel Expense',
            'Uncategorised Expense',
            'Utilities',
            'Cash and cash equivalents',
            'Accounts Receivable (Debtors)',
            'Deferred CGST',
            'Deferred GST Input Credit',
            'Deferred IGST',
            'Deferred Krishi Kalyan Cess Input Credit',
            'Deferred Service Tax Input Credit',
            'Deferred SGST',
            'Deferred VAT Input Credit',
            'GST Refund',
            'Inventory Asset',
            'Krishi Kalyan Cess Refund',
            'Prepaid Insurance',
            'Service Tax Refund',
            'TDS Receivable',
            'Uncategorised Asset',
            'Undeposited Funds',
            'Accumulated Depreciation',
            'Buildings and Improvements',
            'Furniture and Equipment',
            'Land',
            'Leasehold Improvements',
            'Vehicles',
            'CGST Payable',
            'CST Payable',
            'CST Suspense',
            'GST Payable',
            'GST Suspense',
            'IGST Payable',
            'Input CGST',
            'Input CGST Tax RCM',
            'Input IGST',
            'Input IGST Tax RCM',
            'Input Krishi Kalyan Cess',
            'Input Krishi Kalyan Cess RCM',
            'Input Service Tax',
            'Input Service Tax RCM',
            'Input SGST',
            'Input SGST Tax RCM',
            'Input VAT 14%',
            'Input VAT 4%',
            'Input VAT 5%',
            'Krishi Kalyan Cess Payable',
            'Krishi Kalyan Cess Suspense',
            'Output CGST',
            'Output CGST Tax RCM',
            'Output CST 2%',
            'Output IGST',
            'Output IGST Tax RCM',
            'Output Krishi Kalyan Cess',
            'Output Krishi Kalyan Cess RCM',
            'Output Service Tax',
            'Output Service Tax RCM',
            'Output SGST',
            'Output SGST Tax RCM',
            'Output VAT 14%',
            'Output VAT 4%',
            'Output VAT 5%',
            'Service Tax Payable',
            'Service Tax Suspense',
            'SGST Payable',
            'Swachh Bharat Cess Payable',
            'Swachh Bharat Cess Suspense',
            'TDS Payable',
            'VAT Suspense',
            'Opening Balance Equity',
            'Retained Earnings',
            'Billable Expense Income',
            'Consulting Income',
            'Product Sales',
            'Sales',
            'Sales - Hardware',
            'Sales - Software',
            'Sales - Support and Maintenance',
            'Sales Discounts',
            'Sales of Product Income',
            'Uncategorised Income',
            'Cost of sales',
            'Equipment Rental for Jobs',
            'Freight and Shipping Costs',
            'Merchant Account Fees',
            'Purchases - Hardware for Resale',
            'Purchases - Software for Resale'
            'Subcontracted Services',
            'Tools and Craft Supplies',
            'Finance Charge Income',
            'Insurance Proceeds Received',
            'Interest Income',
            'Proceeds from Sale of Assets',
            'Shipping and Delivery Income',
            'Ask My Accountant',
            'CGST write-off',
            'GST write-off',
            'IGST write-off',
            'Miscellaneous Expense',
            'Political Contributions',
            'SGST write-off',
            'Tax write-of',
            'Vehicle Expenses')

select_customer_lab.place(x=550,y=340)
drop2.place(x=550,y=380,width=250,height=33)
wrappen.pack(fill='both',expand='yes')

thermal_zone_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zone_lbl.place(x=10,y=440)
#Create a Calendar using DateEntry
cal2 = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=idat1)
cal2.place(x=10,y=480)

thermal_zoo_lbl = Label(F2, text="Interest earned", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zoo_lbl.place(x=280,y=440)
thermal_zoo_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE,textvariable=intear)
thermal_zoo_txt.place(x=280,y=480)

select_customer_lab1=tk.Label(F2,text="Income Account",font=('times new roman', 16, 'bold'),bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop3=ttk.Combobox(F2,width=22, textvariable = incacc)

drop3['values']=('Advertising/Promotional',
            'Bank charges',
            'Business Licenses and Permits',
            'Charitable Contributions',
            'Computer and Internet Expense',
            'Continuing Education',
            'Depreciation Expense',
            'Dues and Subscriptions',
            'Housekeeping Charges',
            'Insurance Expense',
            'Insurance Expense-General Liability Insurance',
            'Insurance Expense-Health Insurance',
            'Insurance Expense-Life and Disability Insurance',
            'Insurance Expense-Professional Liability',
            'Interest Expense',
            'Meals and entertainment',
            'Office Supplies',
            'Postage and Delivery',
            'Printing and Reproduction',
            'Professional Fees',
            'Purchases',
            'Rent Expense',
            'Repair and maintenance',
            'Small Tools and Equipment',
            'Swachh Bharat Cess Expense',
            'Taxes - Property',
            'Telephone Expense',
            'Travel Expense',
            'Uncategorised Expense',
            'Utilities',
            'Cash and cash equivalents',
            'Accounts Receivable (Debtors)',
            'Deferred CGST',
            'Deferred GST Input Credit',
            'Deferred IGST',
            'Deferred Krishi Kalyan Cess Input Credit',
            'Deferred Service Tax Input Credit',
            'Deferred SGST',
            'Deferred VAT Input Credit',
            'GST Refund',
            'Inventory Asset',
            'Krishi Kalyan Cess Refund',
            'Prepaid Insurance',
            'Service Tax Refund',
            'TDS Receivable',
            'Uncategorised Asset',
            'Undeposited Funds',
            'Accumulated Depreciation',
            'Buildings and Improvements',
            'Furniture and Equipment',
            'Land',
            'Leasehold Improvements',
            'Vehicles',
            'CGST Payable',
            'CST Payable',
            'CST Suspense',
            'GST Payable',
            'GST Suspense',
            'IGST Payable',
            'Input CGST',
            'Input CGST Tax RCM',
            'Input IGST',
            'Input IGST Tax RCM',
            'Input Krishi Kalyan Cess',
            'Input Krishi Kalyan Cess RCM',
            'Input Service Tax',
            'Input Service Tax RCM',
            'Input SGST',
            'Input SGST Tax RCM',
            'Input VAT 14%',
            'Input VAT 4%',
            'Input VAT 5%',
            'Krishi Kalyan Cess Payable',
            'Krishi Kalyan Cess Suspense',
            'Output CGST',
            'Output CGST Tax RCM',
            'Output CST 2%',
            'Output IGST',
            'Output IGST Tax RCM',
            'Output Krishi Kalyan Cess',
            'Output Krishi Kalyan Cess RCM',
            'Output Service Tax',
            'Output Service Tax RCM',
            'Output SGST',
            'Output SGST Tax RCM',
            'Output VAT 14%',
            'Output VAT 4%',
            'Output VAT 5%',
            'Service Tax Payable',
            'Service Tax Suspense',
            'SGST Payable',
            'Swachh Bharat Cess Payable',
            'Swachh Bharat Cess Suspense',
            'TDS Payable',
            'VAT Suspense',
            'Opening Balance Equity',
            'Retained Earnings',
            'Billable Expense Income',
            'Consulting Income',
            'Product Sales',
            'Sales',
            'Sales - Hardware',
            'Sales - Software',
            'Sales - Support and Maintenance',
            'Sales Discounts',
            'Sales of Product Income',
            'Uncategorised Income',
            'Cost of sales',
            'Equipment Rental for Jobs',
            'Freight and Shipping Costs',
            'Merchant Account Fees',
            'Purchases - Hardware for Resale',
            'Purchases - Software for Resale'
            'Subcontracted Services',
            'Tools and Craft Supplies',
            'Finance Charge Income',
            'Insurance Proceeds Received',
            'Interest Income',
            'Proceeds from Sale of Assets',
            'Shipping and Delivery Income',
            'Ask My Accountant',
            'CGST write-off',
            'GST write-off',
            'IGST write-off',
            'Miscellaneous Expense',
            'Political Contributions',
            'SGST write-off',
            'Tax write-of',
            'Vehicle Expenses')

select_customer_lab1.place(x=550,y=440)
drop3.place(x=550,y=480,width=250,height=33)
wrappen.pack(fill='both',expand='yes')

b1 = Button(F2,text = "Start Reconciling",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=addData)  
b1.place(x=280,y=560,width=250,height=40) 

# btn = Button(root, text="bank reconcilation",command=bank)
# btn.pack()
root.mainloop()


