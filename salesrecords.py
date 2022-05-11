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

import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='finsys_tkinter',
    )
mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE salesrecpts(salesrecptsid int PRIMARY KEY AUTO_INCREMENT,salename VARCHAR(255),saleemail VARCHAR(255),saleaddress VARCHAR(255),saledate VARCHAR(255),saleno VARCHAR(255),salesplace VARCHAR(255),salepay VARCHAR(255),salerefno VARCHAR(255),saledeposit VARCHAR(255),salepro VARCHAR(255),salehsn VARCHAR(255),saledescription VARCHAR(255),saleqty VARCHAR(255),saleprice VARCHAR(255),saaletotal VARCHAR(255),salesubtotal VARCHAR(255),tax VARCHAR(255),saletaxamount VARCHAR(255),salegrandtotal VARCHAR(255),category2 VARCHAR(255),categoryhsn2 VARCHAR(255),descrptin2 VARCHAR(255),catqty2 VARCHAR(255),catprice2 VARCHAR(255),cattotal2 VARCHAR(255),tax1 VARCHAR(255),category3 VARCHAR(255),categoryhsn3 VARCHAR(255),descrptin3 VARCHAR(255),catqty3 VARCHAR(255),catprice3 VARCHAR(255),cattotal3 VARCHAR(255),tax2 VARCHAR(255),category4 VARCHAR(255),categoryhsn4 VARCHAR(255),descrptin4 VARCHAR(255),catqty4 VARCHAR(255),catprice4 VARCHAR(255),cattotal4 VARCHAR(255),tax3 VARCHAR(255),offline VARCHAR(255))')

    


def add_custom():
    import addcustomer_form

#edir customer 
def edit_customer():
    #update data
    def change_data():
       
        global salename,saleemail,saleaddress,saledate,saleno,salesplace,salepay,salerefno,saledeposit,salepro,salehsn,saledescription,saleqty,saleprice,saaletotal,salesubtotal,tax,saletaxamount,salegrandtotal,category2,categoryhsn2,descrptin2,catqty2,catprice2,cattotal2,tax1,category3,categoryhsn3,descrptin3,catqty3,catprice3,cattotal3,tax2,category4,categoryhsn4,descrptin4,catqty4,catprice4,cattotal4,tax3,offline
        
        salename=drop2.get()
        saleemail=email_input.get()
        saleaddress=sale_address.get()
        saledate=sale_date.get()
        saleno=sale_no.get()
        salesplace=sales_place.get()
        salepay=sale_pay.get()
        salerefno=sale_refno.get()
        saledeposit=sale_deposit.get()
        salepro=sale_pro.get()
        salehsn=sale_hsn.get()
        saledescription=sale_description.get()
        saleqty=sale_qty.get()
        saleprice=sale_price.get()
        saaletotal=saale_total.get()
        salesubtotal=sale_subtotal.get()
        tax=t_ax.get()
        saletaxamount=sale_taxamount.get()
        salegrandtotal=sale_grandtotal.get()
        category2=category_2.get()
        categoryhsn2=category_hsn2.get()
        descrptin2=descrptin_2.get()
        catqty2=catqty_2.get()
        catprice2=catprice_2.get()
        cattotal2=cattotal_2.get()
        tax1=tax_1.get()
        category3=category_3.get()
        categoryhsn3=category_hsn3.get()
        descrptin3=descrptin_3.get()
        catqty3=catqty_3.get()
        catprice3=catprice_3.get()
        cattotal3=cattotal_3.get()
        tax2=tax_2.get()
        category4=category_4.get()
        categoryhsn4=category_hsn4.get()
        descrptin4=descrptin_4.get()
        catqty4=catqty_4.get()
        catprice4=catprice_4.get()
        cattotal4=cattotal_4.get()
        tax3=tax_3.get()
        offline=off_line.get()
        
        salename,saleemail,saleaddress,saledate,saleno,salesplace,salepay,salerefno,saledeposit,salepro,salehsn,saledescription,saleqty,saleprice,saaletotal,salesubtotal,tax,saletaxamount,salegrandtotal,category2,categoryhsn2,descrptin2,catqty2,catprice2,cattotal2,tax1,category3,categoryhsn3,descrptin3,catqty3,catprice3,cattotal3,tax2,category4,categoryhsn4,descrptin4,catqty4,catprice4,cattotal4,tax3,offline
        
        
        mycursor.execute("UPDATE app1_salesrecpts SET salename =%s, saleemail =%s, saleaddress =%s, saledate =%s, saleno =%s, salesplace =%s, salepay =%s, salerefno =%s, saledeposit =%s, salepro =%s,salehsn =%s, saledescription =%s,saleqty =%s, saleprice =%s, saaletotal =%s, salesubtotal=%s, tax =%s, saletaxamount =%s, salegrandtotal =%s, category2 =%s, categoryhsn2 =%s,descrptin2 =%s,catqty2 =%s,catprice2 =%s,cattotal2 =%s,tax1 =%s,category3 =%s,categoryhsn3 =%s,descrptin3 =%s,catqty3 =%s,catprice3 =%s,cattotal3 =%s,tax2 =%s,category4 =%s,categoryhsn4 =%s,descrptin4 =%s,catqty4 =%s,catprice4 =%s,cattotal4 =%s,tax3 =%s,offline =%s where salesrecptsid=%s"
            ,(etitle, efirst_name, elast_name, ecompany,elocation, egst, egstin, epan_no, eemail, ewebsite, emobile, estreet, ecity, estate, epin, ecountry, eshipstreet,eshipcity, eshipstate, eshippin, eshipcountry,data[0]))
        mydb.commit()
        messagebox.showinfo('successfully Updated')
        mydb.close()


    # selected_item = tree.selection()[0]
    global fname
    focus_data = tree.focus()
    values=tree.item(focus_data,'values')
    customer_id=[values[-1]]
    mycursor.execute("SELECT * FROM app1_customer WHERE customerid=%s",(customer_id))
    data=mycursor.fetchone()
    editcustomer_form = tk.Tk()
    editcustomer_form.title("finsYs")
    editcustomer_form.geometry("2000x2000")
    editcustomer_form['bg']='#2f516a'
    wrappen=ttk.LabelFrame(editcustomer_form)
    mycanvas=Canvas(wrappen)
    mycanvas.pack(side=LEFT,fill="both",expand="yes")
    yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill='y')

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    full_frame=Frame(mycanvas,width=2000,height=2000,bg='#2f516a')
    mycanvas.create_window((0,0),window=full_frame,anchor="nw")


    heading_frame=Frame(mycanvas)
    mycanvas.create_window((150,40),window=heading_frame,anchor="nw")
    addcustomer_heading= tk.Label(heading_frame, text="EDIT CUSTOMER",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
    addcustomer_heading.pack()


    form_frame=Frame(mycanvas,width=1600,height=1000,bg='#243e55')
    mycanvas.create_window((150,150),window=form_frame,anchor="nw")
    form_lable=tk.Label(form_frame,bg='#243e55',width=100)
    form_lable.place(x=0,y=0)
    form_heading=tk.Label(form_lable, text="Customer Information",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
    form_heading.pack(fill=X)


    global e_title,e_first_name,e_last_name,e_company,e_location,e_gst,e_gstin,e_pan_no,e_email,e_website,e_mobile,e_street,e_city,e_state,e_pin,e_country,e_shipstreet,e_shipcity,e_shipstate,e_shippin,e_shipcountry
    e_title=StringVar(form_frame)
    e_first_name=StringVar(form_frame)
    e_last_name=StringVar(form_frame)
    e_company=StringVar(form_frame)
    e_location=StringVar(form_frame)
    e_gst=StringVar(form_frame)
    e_gstin=StringVar(form_frame)
    e_pan_no=StringVar(form_frame)
    e_email=StringVar(form_frame)
    e_website=StringVar(form_frame)
    e_mobile=StringVar(form_frame)
    e_street=StringVar(form_frame)
    e_city=StringVar(form_frame)
    e_state=StringVar(form_frame)
    e_pin=StringVar(form_frame)
    e_country=StringVar(form_frame)
    e_shipstreet=StringVar(form_frame)
    e_shipcity=StringVar(form_frame)
    e_shipstate=StringVar(form_frame)
    e_shippin=StringVar(form_frame)
    e_shipcountry=StringVar(form_frame)

    #asssign existing datas into edit field
    existing_title=data[1]
    e_title.set(existing_title)

    existing_first_name=data[2]
    e_first_name.set(existing_first_name)

    existing_last_name=data[3]
    e_last_name.set(existing_last_name)
   
    existing_company=data[4]
    e_company.set(existing_company)
    
    existing_location=data[5]
    e_location.set(existing_location)
    
    existing_gst=data[6]
    e_gst.set(existing_gst)
    

    existing_gstin=data[7]
    e_gstin.set(existing_gstin)
    

    existing_pan_no=data[8]
    e_pan_no.set(existing_pan_no)
    

    existing_email=data[9]
    e_email.set(existing_email)
    

    existing_website=data[10]
    e_website.set(existing_website)
    

    existing_mobile=data[11]
    e_mobile.set(existing_mobile)
    

    existing_street=data[12]
    e_street.set(existing_street)
    

    existing_city=data[13]
    e_city.set(existing_city)
    e_city

    existing_state=data[14]
    e_state.set(existing_state)
    
    existing_pin=data[15]
    e_pin.set(existing_pin)
    

    existing_country=data[16]
    e_country.set(existing_country)
    
    existing_shipstreet=data[17]
    e_shipstreet.set(existing_shipstreet)
    

    existing_shipcity=data[18]
    e_shipcity.set(existing_shipcity)
    

    existing_shipstate=data[19]
    e_shipstate.set(existing_shipstate)
    

    existing_shippin=data[20]
    e_shippin.set(existing_shippin)
    

    existing_shipcountry=data[21]
    e_shipcountry.set(existing_shipcountry)
    


    title_lab=tk.Label(form_frame,text="Title",bg='#243e55',fg='#fff')
    drop2=ttk.Combobox(form_frame,textvariable = e_title)

    drop2['values']=("Mr","Mrs","Miss","Ms")

    title_lab.place(x=10,y=100,height=15,width=100)
    drop2.place(x=30,y=130,height=40,width=450)
    wrappen.pack(fill='both',expand='yes',)


    fname=Label(form_frame,text="First Name",bg='#243e55',fg='#fff')
    fname.place(x=530,y=100,)
    fname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_first_name)
    fname_input.place(x=530,y=130,height=40)


    lname=Label(form_frame,text="Last Name",bg='#243e55',fg='#fff')
    lname.place(x=1060,y=100,)
    lname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_last_name)
    lname_input.place(x=1060,y=130,height=40)

    company_lab=Label(form_frame,text="Company",bg='#243e55',fg='#fff')
    company_lab.place(x=30,y=200,)
    company_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_company)
    company_input.place(x=30,y=230,height=40)

    location_lab=Label(form_frame,text="Location",bg='#243e55',fg='#fff')
    location_lab.place(x=530,y=200,)
    location_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_location)
    location_input.place(x=530,y=230,height=40)

    GST_lab=tk.Label(form_frame,text="GST Type",bg='#243e55',fg='#fff')
    GST_drop=ttk.Combobox(form_frame,textvariable = e_gst)
    GST_drop['values']=("Consumer","GST Registered-Regular","GST unregistered","GST Registered-Composition","Overseas", "Deemed exports - EOU's STP's EHTP's")
    GST_lab.place(x=20,y=300,height=15,width=100)
    GST_drop.place(x=30,y=330,height=40,width=450)

    gstin_lab=Label(form_frame,text="GSTIN",bg='#243e55',fg='#fff')
    gstin_lab.place(x=530,y=300,)
    gstin_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_gstin)
    gstin_input.place(x=530,y=330,height=40)

    pan_no_lab=Label(form_frame,text="PAN NO",bg='#243e55',fg='#fff')
    pan_no_lab.place(x=1060,y=300,)
    pan_no_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_pan_no)
    pan_no_input.place(x=1060,y=330,height=40)

    email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
    email_lab.place(x=30,y=400,)
    email_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_email)
    email_input.place(x=30,y=430,height=40)

    web_lab=Label(form_frame,text="Website",bg='#243e55',fg='#fff')
    web_lab.place(x=530,y=400,)
    web_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_website)
    web_input.place(x=530,y=430,height=40)


    mobile_lab=Label(form_frame,text="Mobile",bg='#243e55',fg='#fff')
    mobile_lab.place(x=1060,y=400,)
    mobile_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_mobile)
    mobile_input.place(x=1060,y=430,height=40)

    #Billing session
    sub_headingfont=font.Font(family='Times New Roman', size=18,)
    form2_frame=Frame(mycanvas,width=1600,height=650,bg='#243e55',bd=1,relief="groove")
    mycanvas.create_window((150,650),window=form2_frame,anchor="nw")

    bill_heading=tk.Label(form2_frame, text="Billing Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
    bill_heading.place(x=30,y=10,)

    street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
    street_lab.place(x=30,y=100,)
    street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff',textvariable = e_street)
    street_input.place(x=30,y=130,height=80)


    city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
    city_lab.place(x=30,y=250,)
    city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_city)
    city_input.place(x=30,y=280,height=40)


    state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
    state_lab.place(x=370,y=250,)
    state_drop=ttk.Combobox(form2_frame,textvariable = e_state)
    state_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
    state_drop.place(x=370,y=280,height=40,width=330)

    pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
    pin_lab.place(x=30,y=350,)
    pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_pin)
    pin_input.place(x=30,y=380,height=40)

    country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
    country_lab.place(x=370,y=350,)
    country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_country)
    country_input.place(x=370,y=380,height=40)



    #Shipping Address 

    shipping_heading=tk.Label(form2_frame, text="Shipping Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
    shipping_heading.place(x=850,y=10,)



    street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
    street_lab.place(x=850,y=100,)
    street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff',textvariable = e_shipstreet)
    street_input.place(x=850,y=130,height=80)


    city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
    city_lab.place(x=850,y=250,)
    city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_shipcity)
    city_input.place(x=850,y=280,height=40)


    state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
    state_lab.place(x=1200,y=250,)
    state_drop=ttk.Combobox(form2_frame,textvariable = e_shipstate)
    state_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
    state_drop.place(x=1200,y=280,height=40,width=330)

    pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
    pin_lab.place(x=850,y=350,)
    pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_shippin)
    pin_input.place(x=850,y=380,height=40)

    country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
    country_lab.place(x=1200,y=350,)
    country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_country)
    country_input.place(x=1200,y=380,height=40)

    submit_button=Button(form2_frame,text="Submit Form",background="#2f516a", foreground="white",width=40,height=2,command=change_data)

    submit_button.place(x=600,y=500)


#Delete constomer
def delete_customer():
    focus_data = tree.focus()
    values=tree.item(focus_data,'values')
    customer_id=[values[-1]]
    mycursor.execute("DELETE FROM app1_customer WHERE customerid=%s",(customer_id))
    mydb.commit()
    messagebox.showinfo('successfully Delated')
    print('sucessfully deleted')
    tree.delete(focus_data)
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

def delete_sale():
    focus_data = tree.focus()
    values=tree.item(focus_data,'values')
    customer_id=[values[-1]]
    tree.execute("DELETE FROM app1_customer WHERE customerid=%s",(customer_id))
    mydb.commit()
    tkinter.messagebox.messagebox.showinfo('successfully Delated')
    print('sucessfully deleted')
    tree.delete(focus_data)

edit_btn = ttk.Button(F, text="Edit", command=edit_customer)
edit_btn.place(relx=0.35, rely=0.88, relheight=0.1, relwidth=0.1)
del_btn = ttk.Button(F, text="Delete", command=delete_customer)
del_btn.place(relx=0.5, rely=0.88, relheight=0.1, relwidth=0.1)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

 

root.mainloop()


