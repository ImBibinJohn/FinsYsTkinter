from math import prod
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


#edir customer 
def edit_sale():
    #update data
    def chan_data():
        fun()
        global custom,emal,amount,billaddress,date,salerecno,place,paymethod,refno,deposit,product,hsn,desc,qty,price,total,tax,subtotal,tax2,grand
        custom=custom_name.get()
        emal=email_id.get()
        amount=gamount.get()
        billaddress=saleaddress.get()
        date=saledate.get()
        salerecno=saleno.get()
        place=salesplace.get()
        paymethod=salepay.get()
        refno=salerefno.get()
        deposit=saledeposit.get()
        product=e_product.get()
        hsn=e_hsn.get()
        desc=e_desc.get()
        qty=e_qty.get()
        price=e_price.get()
        total=e_total.get()
        tax=e_tax.get()
        subtotal=e_subtotal.get()
        tax2=e_tax2.get()
        grand=e_grand.get()
        mycursor.execute(("UPDATE app1_inventory SET name =%s, hsn =%s, category =%s, initialqty =%s, salesprice =%s, cxq =%s"))
        mycursor.execute("UPDATE app1_salesrecpts SET salename =%s, saleemail =%s, saleaddress =%s, saledate =%s, saleno =%s, salesplace =%s, salepay =%s, salerefno =%s, saledeposit =%s, e_product =%s, e_hsn =%s, e_desc =%s, e_qty =%s, e_price =%s, e_total =%s, e_tax =%s, e_grand =%s where salesrecptsid=%s"
            ,(custom, emal, amount, billaddress,date, salerecno, place, paymethod, refno, deposit, product, hsn, desc, qty, price, total, tax, subtotal, tax2, grand,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,amt_received,taxamount,balance,cid_id, data[0]))
        mydb1.commit()
        messagebox.showinfo('successfully Updated')
        mydb1.close()
        

# selected_item = tree_data.selection()[0]
    global customer_name
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    salesrecpts_id=[values[-1]]
    mycursor.execute("SELECT * FROM app1_salesrecpts WHERE salesrecptsid=%s",(salesrecpts_id))
    data=mycursor.fetchone()
    
    
# edit product all table
    
def edit_customer():
    
    def get_email(event):
        name=[]
        options=drop2.get()
        name.append(options)
        for custm in customers_data:
            full_name=custm[2]+custm[3]
            if full_name==name[0]:
                first_name=custm[2]
                last_name=custm[3]
        mycursor.execute("SELECT * FROM app1_customer where firstname=%s and lastname=%s",(first_name,last_name))
        table2=mycursor.fetchall()
        for i in table2:
            email_id.set(i[9])
            saleaddress.set(i[12:17])




    def get_e_terms(event):
        global e_invno
        options=terms_input.get()
        if options=="Add New Term":
            invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
            invno_lab.place(x=500,y=400,)
            invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=e_invno)
            invno_input.place(x=500,y=430,height=40)
        else:
            e_invno.set(0)

    def get_selected_e_product(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4,final_total
        createsubtotal =0
        finding_tax1=0
        finding_tax2=0
        finding_tax3=0
        finding_tax4=0
        final_total=0
        selected_product=[]
        product=product_drop1.get()
        quantity=qty_input1.get()
        selected_product.append(product)
        for product in inv_data:
            product_details="SELECT * FROM app1_inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn.set(i[4])
                e_desc.set(i[11])
                e_price.set(i[12])
                e_sale_price=i[12]
                tota_price=int(e_sale_price)*int(quantity)
                e_total.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM app1_noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn.set(i[4])
                e_desc.set(i[7])
                e_price.set(i[8])
                e_sale_price=i[8]
                tota_price=int(e_sale_price)*int(quantity)
                e_total.set(tota_price) 
        
        for product in bundleinv_data:
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn.set(i[4])
                e_desc.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                e_price.set(sale_price)
                
                tota_price=int(sale_price)*int(quantity)
                e_total.set(tota_price)   
        createsubtotal=int(e_total.get())+int(e_total2.get())+int(e_total3.get())+int(e_total4.get())
        e_subtotal.set(createsubtotal)
        #get selected gst then find tax amount thenset it 
        gst=tax_drop1.get() 

        if gst=="18.0% GST(18%)":
            print("totla",tota_price)
            finding_tax1=int(tota_price)*(18/100)
        elif gst=="28.0% GST(28%)":
            finding_tax1=int(tota_price)*(28/100)
            
        elif gst=="12.0% GST(12%)":
            finding_tax1=int(tota_price)*(12/100)
            
        elif gst=="06.0% GST(06%)":
            finding_tax1=int(tota_price)*(6/100)
            
        elif gst=="05.0% GST(05%)":
            finding_tax1=int(tota_price)*(5/100)
            
        elif gst=="03.0% GST(03%)":
            finding_tax1=int(tota_price)*(3/100)
            
        else:
            finding_tax1=0
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        e_taxamount.set(finding_tax)
        
        if e_taxamount==None:
            final_total=0
            e_grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            e_grand.set(final_total)
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        e_balance.set(balancedue)
    
    
    
    
    
    
    
    
    
    

   

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

    full_frame=Frame(mycanvas,width=1345,height=2500,bg='#2f516a')
    mycanvas.create_window((0,0),window=full_frame,anchor="nw")


    heading_frame=Frame(mycanvas)
    mycanvas.create_window((0,40),window=heading_frame,anchor="nw")
    invoice_heading= tk.Label(heading_frame, text="CASH MEMO NO. 1003",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=74)
    invoice_heading.pack()


def get_selected_product(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4,final_total
        createsubtotal =0
        finding_tax1=0
        finding_tax2=0
        finding_tax3=0
        finding_tax4=0
        final_total=0
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
        
        for product in bundleinv_data:
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                price.set(sale_price)
                
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price)   
        createsubtotal=int(total.get())+int(total2.get())+int(total3.get())+int(total4.get())
        subtotal.set(createsubtotal)
        #get selected gst then find tax amount thenset it 
        gst=tax_drop1.get()

        if gst=="18.0% GST(18%)":
            print("totla",tota_price)
            finding_tax1=int(tota_price)*(18/100)
        elif gst=="28.0% GST(28%)":
            finding_tax1=int(tota_price)*(28/100)
            
        elif gst=="12.0% GST(12%)":
            finding_tax1=int(tota_price)*(12/100)
            
        elif gst=="06.0% GST(06%)":
            finding_tax1=int(tota_price)*(6/100)
            
        elif gst=="05.0% GST(05%)":
            finding_tax1=int(tota_price)*(5/100)
            
        elif gst=="03.0% GST(03%)":
            finding_tax1=int(tota_price)*(3/100)
            
        else:
            finding_tax1=0
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        taxamount.set(finding_tax)
        
        if taxamount==None:
            final_total=0
            grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            grand.set(final_total)
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        balance.set(balancedue)

    
    
    

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



    #form fields

    form_frame=Frame(mycanvas,width=1345,height=1900,bg='#243e55')
    mycanvas.create_window((0,150),window=form_frame,anchor="nw")
    form_lable=tk.Label(form_frame,bg='#243e55',width=100)
    form_lable.place(x=0,y=0)
    form_heading=tk.Label(form_lable, text="FinsYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=90)
    form_heading.pack()


    #get customer datas from customer table
    mycursor.execute('select * from app1_customer ')
    customers=mycursor.fetchall()
    customers_data=[]
    for cus in customers:
        customers_data.append(cus)


    global custom_name,email_id,gamount,saleaddress,saledate,saleno,salesplace,salepay,salerefno,saledeposit,e_product,e_hsn,e_desc,e_qty,e_price,e_total,e_tax,e_subtotal,e_tax2,e_grand,e_product2,e_product3,e_product4,e_hsn2,e_hsn3,e_hsn4,e_desc2,e_desc3,e_desc4,e_qty2,e_qty3,e_qty4,e_price2,e_price3,e_price4, e_total2,e_total3,e_total4,e_tax2,e_tax3,e_tax4
    custom_name=StringVar(form_frame) 
    email_id=StringVar(form_frame)
    gamount=StringVar(form_frame)
    saleaddress=StringVar(form_frame)
    saledate=StringVar(form_frame)
    saleno=StringVar(form_frame)
    salesplace=StringVar(form_frame)
    salepay=StringVar(form_frame)
    salerefno=StringVar(form_frame)
    saledeposit=StringVar(form_frame)
    e_product=StringVar(form_frame)
    e_hsn=StringVar(form_frame)
    e_desc=StringVar(form_frame)
    e_qty=StringVar(form_frame)
    e_price=StringVar(form_frame)
    e_total=StringVar(form_frame)
    e_tax=StringVar(form_frame)
    e_subtotal=StringVar(form_frame)
    e_tax2=StringVar(form_frame)
    e_grand=StringVar(form_frame)
    e_product2=StringVar()
    e_product3=StringVar()
    e_product4=StringVar()
    e_hsn2=StringVar()
    e_hsn3=StringVar()
    e_hsn4=StringVar()
    e_desc2=StringVar()
    e_desc3=StringVar()
    e_desc4=StringVar()
    e_qty2=StringVar()
    e_qty3=StringVar()
    e_qty4=StringVar()
    e_price2=StringVar()
    e_price3=StringVar()
    e_price4=StringVar()
    e_total2=StringVar()
    e_total3=StringVar()
    e_total4=StringVar()
    e_tax2=StringVar()
    e_tax3=StringVar()
    e_tax4=StringVar()
    
    
    
    existing_custom=data[1]
    custom_name.set(existing_custom)

    existing_email=data[2]
    email_id.set(existing_email)

    existing_amount=data[3]
    gamount.set(existing_amount)
    
    existing_billaddress=data[4]
    saleaddress.set(existing_billaddress)
    
    existing_date=data[5]
    saledate.set(existing_date)
    
    existing_salerecno=data[6]
    saleno.set(existing_salerecno)
    
    existing_place=data[7]
    salesplace.set(existing_place)
    
    existing_salepay=data[8]
    salepay.set(existing_salepay)
    
    existing_refno=data[9]
    salerefno.set(existing_refno)
    
    existing_deposit=data[10]
    saledeposit.set(existing_deposit)


    select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')
    select_customer_input=StringVar()
    drop2=ttk.Combobox(form_frame,textvariable = custom_name)

    drop2['values']=("Select-Options")

    select_customer_lab.place(x=30,y=150,height=15)
    drop2.place(x=30,y=180,height=40,width=300)
    wrappen.pack(fill='both',expand='yes',)

    # add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_custom)
    # add_custom.place(x=335,y=230)

    email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
    email_lab.place(x=500,y=150,)
    email_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=email_id)
    email_input.place(x=500,y=180,height=40,width=300)

    Due_date_lab=Label(form_frame,text="AMOUNT",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=150,height=40)
    Due_date_lab=Label(form_frame,text="0.00",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=180,height=40)

    invoice_date_lab=Label(form_frame,text="Billing Address",bg='#243e55',fg='#fff')
    invoice_date_lab.place(x=30,y=250,)
    invoice_date_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=gamount)
    invoice_date_input.place(x=30,y=280,height=170,width=300)

    terms_lab=Label(form_frame,text="Sales receipt Date:",bg='#243e55',fg='#fff')
    terms_lab.place(x=500,y=250,)
    terms_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=saleaddress)
    terms_input.place(x=500,y=280,height=40,width=300)

    Due_date_lab=Label(form_frame,text="Sales receipt No:",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=250)
    Due_date_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=saledate )
    Due_date_input.place(x=970,y=280,height=40,width=300)

    place_of_supply=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')
    place_input=StringVar()
    drop2=ttk.Combobox(form_frame,textvariable =saleno)
    drop2['values']=("Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh",
                     "Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir",
                     "Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram",
                     "Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamilnadu","Telangana","Tripura","Uttar Predesh",
                     "Uttarakhand","West Bengal","Other Territory")
    place_of_supply.place(x=30,y=490,)
    drop2.place(x=30,y=520,height=40,width=300)

    Due_date_labe=Label(form_frame,text="Payment Method:",bg='#243e55',fg='#fff')
    Due_date_labe.place(x=30,y=590)
    Due_datee_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=salesplace )
    Due_datee_input.place(x=30,y=620,height=40,width=300)
    
    Due_date_labe=Label(form_frame,text="Reference No:",bg='#243e55',fg='#fff')
    Due_date_labe.place(x=500,y=590)
    Due_datee_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=salepay )
    Due_datee_input.place(x=500,y=620,height=40,width=300)

    place_of_supply=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')
    place_input=StringVar()
    drop2=ttk.Combobox(form_frame,textvariable =salerefno)
    drop2['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit",
                    "Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund",
                    "TDS Receivable","Uncategorised Asset","Undeposited Funds")
    place_of_supply.place(x=970,y=590,)
    drop2.place(x=970,y=620,height=40,width=300)
    
    # table form
    h_lab=Label(form_frame,text="#",bg='#243e55',fg='#fff')
    h_lab.place(x=30,y=730)

    h_input1=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    h_input1.place(x=30,y=780,height=40,width=40)

    h_input2=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    h_input2.place(x=30,y=850,height=40,width=40)

    h_input3=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    h_input3.place(x=30,y=930,height=40,width=40)

    h_input4=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    h_input4.place(x=30,y=1000,height=40,width=40)


    #col-1
    product_lab=Label(form_frame,text="PRODUCT / SERVICES",bg='#243e55',fg='#fff')
    product_lab.place(x=90,y=730,)
    product_input1=StringVar()
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
    product_drop1.place(x=90,y=780,height=40,width=180)
    
    
    
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
    
    
    
    
    

    product_input2=StringVar()
    product_drop2=ttk.Combobox(form_frame,textvariable = product_input1)
    product_drop2['values']=(" ")
    product_drop2.place(x=90,y=850,height=40,width=180)

    product_input3=StringVar()
    product_drop3=ttk.Combobox(form_frame,textvariable = product_input1)
    product_drop3['values']=(" ")
    product_drop3.place(x=90,y=930,height=40,width=180)

    product_input4=StringVar()
    product_drop4=ttk.Combobox(form_frame,textvariable = product_input1)
    product_drop4['values']=(" ")
    product_drop4.place(x=90,y=1000,height=40,width=180)

    #col-2

    hsn_lab=Label(form_frame,text="HSN",bg='#243e55',fg='#fff')
    hsn_lab.place(x=350,y=730,)

    hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    hsn_input1.place(x=300,y=780,height=40)

    hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    hsn_input2.place(x=300,y=850,height=40)

    hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    hsn_input3.place(x=300,y=930,height=40)

    hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    hsn_input4.place(x=300,y=1000,height=40)

    #col-3

    desc_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
    desc_lab.place(x=500,y=730,)

    desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
    desc_input1.place(x=460,y=780,height=40)

    desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
    desc_input2.place(x=460,y=850,height=40)

    desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
    desc_input3.place(x=460,y=930,height=40)

    desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
    desc_input4.place(x=460,y=1000,height=40)

    #col-4
    qty_lab=Label(form_frame,text="QUANTITY",bg='#243e55',fg='#fff')
    qty_lab.place(x=690,y=730,)

    qty_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    qty_input1.place(x=650,y=780,height=40)

    qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    qty_input2.place(x=650,y=850,height=40)

    qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    qty_input3.place(x=650,y=930,height=40)

    qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    qty_input4.place(x=650,y=1000,height=40)

    #col-5
    price_lab=Label(form_frame,text="PRICE",bg='#243e55',fg='#fff')
    price_lab.place(x=860,y=730,)

    price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    price_input1.place(x=810,y=780,height=40)

    price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    price_input2.place(x=810,y=850,height=40)

    price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    price_input3.place(x=810,y=930,height=40)

    price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    price_input4.place(x=810,y=1000,height=40)

    #col-6
    total_lab=Label(form_frame,text="TOTAL",bg='#243e55',fg='#fff')
    total_lab.place(x=1010,y=730,)

    total_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    total_input1.place(x=970,y=780,height=40)

    total_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    total_input2.place(x=970,y=850,height=40)

    total_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    total_input3.place(x=970,y=930,height=40)

    total_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
    total_input4.place(x=970,y=1000,height=40)

    #ocol-7
    tax_lab=Label(form_frame,text="TAX (%)",bg='#243e55',fg='#fff')
    tax_lab.place(x=1180,y=730,)

    tax_input1=StringVar()
    tax_drop1=ttk.Combobox(form_frame,textvariable = tax_input1)
    tax_drop1['values']=(" ")
    tax_drop1.place(x=1130,y=780,height=40,width=180)

    tax_input2=StringVar()
    tax_drop2=ttk.Combobox(form_frame,textvariable = tax_input2)
    tax_drop2['values']=(" ")
    tax_drop2.place(x=1130,y=850,height=40,width=180)

    tax_input3=StringVar()
    tax_drop3=ttk.Combobox(form_frame,textvariable = tax_input3)
    tax_drop3['values']=(" ")
    tax_drop3.place(x=1130,y=930,height=40,width=180)

    tax_input4=StringVar()
    tax_drop4=ttk.Combobox(form_frame,textvariable = tax_input4)
    tax_drop4['values']=(" ")
    tax_drop4.place(x=1130,y=1000,height=40,width=180)





    subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
    subtotal_lab.place(x=900,y=1200,height=40)
    subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
    subtotal_input.place(x=1000,y=1200,height=40)

    tax2_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
    tax2_lab.place(x=900,y=1300,height=40)
    tax2_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
    tax2_input.place(x=1000,y=1300,height=40)

    grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
    grand_lab.place(x=900,y=1400,height=40)
    grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
    grand_input.place(x=1000,y=1400,height=40)


    submit_button=Button(form_frame,text="Save",background="#2f516a", foreground="white",width=20,height=2)

    submit_button.place(x=1100,y=1500)
    font=('Times', 15)



#Delete salerecords
def delete_salerecords():
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    salesrecpts_id=[values[-1]]
    mycursor.execute("DELETE FROM app1_salesrecpts WHERE salesrecptsid=%s",(salesrecpts_id))
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


edit_btn = ttk.Button(F, text="Edit", command=edit_sale)
edit_btn.place(relx=0.35, rely=0.88, relheight=0.1, relwidth=0.1)
del_btn = ttk.Button(F, text="Delete",command=delete_salerecords)
del_btn.place(relx=0.5, rely=0.88, relheight=0.1, relwidth=0.1)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)



root.mainloop()





