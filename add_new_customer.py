from calendar import c
import tkinter as tk
from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector

#db connection
def db_connection():
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='finsys_tkinter'
        )
    mycursor = mydb.cursor()


#saving_customer datas here
def save_data():
    db_connection()
    global title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry
    title=title.get()
    first_name=first_name.get()
    last_name=last_name.get()
    company=company.get()
    location=location.get()
    gst=gst.get()
    gstin=gstin.get()
    pan_no=pan_no.get()
    email=email.get()
    website=website.get()
    mobile=mobile.get()
    street=street.get()
    city=city.get()
    state=state.get()
    pin=pin.get()
    country=country.get()
    shipstreet=shipstreet.get()
    shipcity=shipcity.get()
    shipstate=shipstate.get()
    shippin=shippin.get()
    shipcountry=shipcountry.get()

    sql='SELECT * FROM customer WHERE firstname=%s AND lastname=%s'# selecting entire table from db,taking username , nd check the existance
    val=(first_name,last_name)
    mycursor.execute(sql,val)
    if mycursor.fetchone()is not None:
        messagebox.showerror('error', 'First Name and Last Name already exist!!')
    else:
        sql="INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        val=(title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo('New Customer Added')




add_new_customer_form = tk.Tk()
add_new_customer_form.title("finsYs")
add_new_customer_form.geometry("2000x2000")
add_new_customer_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(add_new_customer_form)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=2000,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((-150,40),window=heading_frame,anchor="nw")
# headingfont=font.Font(family='Times New Roman', size=25,)
addcustomer_heading= tk.Label(heading_frame, text="ADD CUSTOMER",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
addcustomer_heading.pack()

#form fields

form_frame=Frame(mycanvas,width=1600,height=1000,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="Customer Information",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=90)
form_heading.pack(fill=X)

title_lab=tk.Label(form_frame,text="Title",bg='#243e55',fg='#fff')
place_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = place_input)

drop2['values']=("Mr","Mrs","Miss","Ms")

title_lab.place(x=10,y=100,height=15,width=100)
drop2.place(x=30,y=130,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)


fname=Label(form_frame,text="First Name",bg='#243e55',fg='#fff')
fname.place(x=530,y=100,)
fname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
fname_input.place(x=530,y=130,height=40)


lname=Label(form_frame,text="Last Name",bg='#243e55',fg='#fff')
lname.place(x=950,y=100,)
lname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
lname_input.place(x=950,y=130,height=40)

company=Label(form_frame,text="Company",bg='#243e55',fg='#fff')
company.place(x=30,y=200,)
company_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
company_input.place(x=30,y=230,height=40)

location=Label(form_frame,text="Location",bg='#243e55',fg='#fff')
location.place(x=530,y=200,)
location_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
location_input.place(x=530,y=230,height=40)

GST_lab=tk.Label(form_frame,text="GST Type",bg='#243e55',fg='#fff')
GST_drop=ttk.Combobox(form_frame)
GST_drop['values']=("Consumer","GST Registered-Regular","GST Registered-Composition","Overseas")
GST_lab.place(x=20,y=300,height=15,width=100)
GST_drop.place(x=30,y=330,height=40,width=450)

gstin_lab=Label(form_frame,text="GSTIN",bg='#243e55',fg='#fff')
gstin_lab.place(x=530,y=300,)
gstin_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
gstin_input.place(x=530,y=330,height=40)

pan_no_lab=Label(form_frame,text="PAN NO",bg='#243e55',fg='#fff')
pan_no_lab.place(x=950,y=300,)
pan_no_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
pan_no_input.place(x=950,y=330,height=40)

email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
email_lab.place(x=30,y=400,)
email_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
email_input.place(x=30,y=430,height=40)

web_lab=Label(form_frame,text="Website",bg='#243e55',fg='#fff')
web_lab.place(x=530,y=400,)
web_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
web_input.place(x=530,y=430,height=40)


mobile=Label(form_frame,text="Mobile",bg='#243e55',fg='#fff')
mobile.place(x=950,y=400,)
mobile_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
mobile_input.place(x=950,y=430,height=40)

#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=650,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,650),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="Billing Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
street_lab.place(x=30,y=100,)
street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff')
street_input.place(x=30,y=130,height=80)


city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
city_lab.place(x=30,y=250,)
city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
city_input.place(x=30,y=280,height=40)


state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
state_lab.place(x=370,y=250,)
state_drop=ttk.Combobox(form2_frame)
state_drop['values']=("Kerala","Karnataka","Tamilnadu")
state_drop.place(x=370,y=280,height=40,width=330)

pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
pin_lab.place(x=30,y=350,)
pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
pin_input.place(x=30,y=380,height=40)

country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
country_lab.place(x=370,y=350,)
country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
country_input.place(x=370,y=380,height=40)

CheckVar1 = IntVar()
terms_condition=Checkbutton(form2_frame, variable = CheckVar1,onvalue = 1, offvalue = 0,bg='#243e55')
terms_condition.place(x=30,y=450,)   
terms_condition_lab= Label(form2_frame,text = " Agree to Terms and Conditions",bg='#243e55',fg='#fff') 
terms_condition_lab.place(x=70,y=450,)


#Shipping Address

CheckVar2 = IntVar()
same_address=Checkbutton(form2_frame, variable = CheckVar2,onvalue = 1, offvalue = 0,bg='#243e55')
same_address.place(x=1100,y=30,)   
same_address_lab= Label(form2_frame,text = "Same as Billing Address",bg='#243e55',fg='#fff') 
same_address_lab.place(x=1150,y=30,)

shipping_heading=tk.Label(form2_frame, text="Shipping Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
shipping_heading.place(x=750,y=10,)



street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
street_lab.place(x=750,y=100,)
street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff')
street_input.place(x=750,y=130,height=80)


city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
city_lab.place(x=750,y=250,)
city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
city_input.place(x=750,y=280,height=40)


state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
state_lab.place(x=1020,y=250,)
state_drop=ttk.Combobox(form2_frame)
state_drop['values']=("Kerala","Karnataka","Tamilnadu")
state_drop.place(x=1020,y=280,height=40,width=300)

pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
pin_lab.place(x=750,y=350,)
pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
pin_input.place(x=750,y=380,height=40)

country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
country_lab.place(x=1020,y=350,)
country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
country_input.place(x=1020,y=380,height=40)

submit_button=Button(form2_frame,text="Submit Form",background="#2f516a", foreground="white",width=40,height=2)

submit_button.place(x=600,y=500)



add_new_customer_form.mainloop()
