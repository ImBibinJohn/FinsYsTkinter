
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
import mysql.connector

def add_custom():
    import add_new_customer

#db connects here ****
def db_connection():
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='finsys_tkinter'
        )
    mycursor = mydb.cursor()


#to save credit formdata
def save_credit_data():
        db_connection()      
        mail=mail.get("1.0","end")
        biladdr=biladdr.get()
        creditno=creditno.get()
        place=place.get()
        invnum=invnum.get()
        invperiod=invperiod.get()
        product1=product1.get()
        product2=product2.get()
        product3=product3.get()
        descrip1=descrip1.get()
        descrip2=descrip2.get()
        descrip3=descrip3.get()
        qty1=qty1.get()
        qty2=qty2.get()
        qty3=qty3.get()
        price1=price1.get()
        price2=price2.get()
        price3=price3.get()
        total1=total1.get()
        total2=total2.get()
        total3=total3.get()
        tax1=tax1.get()
        tax2=tax2.get()
        tax3=tax3.get()
        sql="INSERT INTO credit (mail,biladdr,creditdate,creditno,place,invnum,invperiod,product,descrip,qty,price,tax,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%S,%S)" #adding values into db
        # val=(sql,mail,biladdr,,creditno,place,invnum,invperiod,product,descrip,qty,price,tax,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3)
        mycursor.execute(sql,[(mail),(biladdr),(creditno),(place),(invnum),(product1),(product2),(product3),(descrip1),(descrip2),(descrip3),(price1),(price2),(price3),(total1),(total2),(total3),(tax1),(tax2),(tax3)])
        mydb.commit()
        mydb.close()


#declaring global variables
# global  email,billingad,creditnote,placeofsup,invoiceperiod,invoicedate,pro1,pro2,pro3,descrip1,descrip2,descrip3,qty1,qty2,qty3,price1,price2,price3,total1,total2,total3,tax1,tax2,tax3
# email=StringVar(form_frame,email)
# billingad=StringVar()
# creditnote=StringVar()
# placeofsup=StringVar()
# invoiceperiod=StringVar()
# invoicedate=StringVar()
# pro1=StringVar()
# pro2=StringVar()
# pro3=StringVar()
# descrip1=StringVar()
# descrip2=StringVar()
# descrip3=StringVar()
# qty1=StringVar()
# qty2=StringVar()
# qty3=StringVar()
# price1=StringVar()
# price2=StringVar()
# price3=StringVar()
# total1=StringVar()
# total2=StringVar()
# total3=StringVar()
# tax1=StringVar()
# tax2=StringVar()
# tax3=StringVar()



#ihsdjrifjsiof
credit_form = tk.Tk()
credit_form.title("finsYs")
credit_form.geometry("1000x1000")
credit_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(credit_form)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=1600,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((0,40),window=heading_frame,anchor="nw")
headingfont=font.Font(family='Times New Roman', size=25,)
credit_heading=Label(heading_frame, text="CREDIT NOTE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=headingfont,width=70)
credit_heading.pack()

#form fields
sub_headingfont=font.Font(family='Times New Roman', size=20,)
form_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="fin sYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=sub_headingfont,width=80)
form_heading.pack()

title_lab=tk.Label(form_frame,text="CUSTOMER",bg='#243e55',fg='#fff')
place_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = place_input)

drop2['values']=("SELECT_CUSTOMER")

title_lab.place(x=10,y=100,height=15,width=100)
drop2.place(x=30,y=130,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_custom)
add_custom.place(x=335,y=230)

mailLab=Label(form_frame,text="EMAIL",bg='#243e55',fg='#fff')
mailLab.place(x=530,y=100,)
mail=Entry(form_frame,width=55,bg='#243e55',fg='#fff')
mail.place(x=530,y=130,height=40)

biladdrLab=Label(form_frame,text="BILLING ADDRESS",bg='#243e55',fg='#fff')
biladdrLab.place(x=30,y=200,)
biladdr=Entry(form_frame,width=75,bg='#243e55',fg='#fff')
biladdr.place(x=30,y=230,height=90)

credit_note=Label(form_frame,text="CREDIT NOTE",bg='#243e55',fg='#fff')
credit_note.place(x=530,y=200,)
creditno=Entry(form_frame,width=55,bg='#243e55',fg='#fff')
creditno.place(x=530,y=230,height=40)

place_of_supp=tk.Label(form_frame,text="PLACE OF SUPPLY",bg='#243e55',fg='#fff')
place=ttk.Combobox(form_frame)
place['values']=("KERALA","TAMILNADU","ANDHRA PRADESH","KARNATAKA")
place_of_supp.place(x=20,y=330,height=15,width=100)
place.place(x=30,y=360,height=40,width=450)

invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
invoice_drop=ttk.Combobox(form_frame)
invoice_drop['values']=("OCT2022-DEC2022","","","")
invoice_period.place(x=20,y=330,height=15,width=100)
invoice_drop.place(x=30,y=620,height=40,width=450)

# invoice_no=tk.Label(form_frame,text="SELECT INVOICE NO",bg='#243e55',fg='#fff')=ttk.Combobox(form_frame)
# invnum['values']=("SELECT INVOICE NO","","","")
# invoice_no.place(x=530,y=330,height=15,width=100)
# invoice_no_drop.place(x=530,y=360,height=40,width=450)

#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,650),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

label=tk.Label(form2_frame,text="PRODUCT/SERVICE\t\tDESCRIPTION\t\tQUANTITY\t\tPRICE\t\tTOTAL\t\tTAX\t",bg='#243e55' ,fg="white",font=('Arial',))
label.place(x=5,y=20)

#row1
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
pro1_drop=ttk.Combobox(form2_frame)
pro1_drop['values']=("","","","")
pro.place(x=10,y=120,height=15,width=100)
pro1_drop.place(x=10,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
pro2_drop=ttk.Combobox(form2_frame,)
pro2_drop['values']=("","","","")
pro.place(x=10,y=210,height=15,width=100)
pro2_drop.place(x=10,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
pro3_drop=ttk.Combobox(form2_frame,)
pro3_drop['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
pro3_drop.place(x=10,y=310,height=40,width=150)



#row 1
discription1_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription1_input.place(x=260,y=150,height=40,width=180)
#row2
discription2_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription2_input.place(x=260,y=240,height=40,width=180)
#row3
discription3_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription3_input.place(x=260,y=310,height=40,width=180)

#row 1
quantity1_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity1_input.place(x=480,y=150,height=40,width=150)
#row2
quantity2_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity2_input.place(x=480,y=240,height=40,width=150)
#row3
quantity3_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity3_input.place(x=480,y=310,height=40,width=150)


#row 1
price1_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price1_input.place(x=680,y=150,height=40,width=150)
#row2
price2_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price2_input.place(x=680,y=240,height=40,width=150)
#row3
price3_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price3_input.place(x=680,y=310,height=40,width=150)

#row 1
total1_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total1_input.place(x=850,y=150,height=40,width=100)
#row2
total2_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total2_input.place(x=850,y=240,height=40,width=100)
#row3
total3_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total3_input.place(x=850,y=310,height=40,width=100)
#row1
tax_drop=ttk.Combobox(form2_frame)
tax_drop['values']=("","","","")
tax_drop.place(x=1250,y=150,height=15,width=150)
tax_drop.place(x=1000,y=150,height=40,width=150)
#row2
tax2_drop=ttk.Combobox(form2_frame)
tax2_drop['values']=("","","","")
pro.place(x=1110,y=240,height=15,width=150)
tax2_drop.place(x=1000,y=240,height=40,width=150)
#row3
tax3_drop=ttk.Combobox(form2_frame)
tax3_drop['values']=("","","","")
pro.place(x=1000,y=310,height=15,width=150)
tax3_drop.place(x=1000,y=310,height=40,width=150)

##################

sub_headingfont=font.Font(family='Times New Roman', size=18,)
form3_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,1100),window=form3_frame,anchor="nw")

sub_total=Label(form3_frame,text="SUB TOTAL",bg='#243e55',fg='#fff')
sub_total.place(x=900,y=110)
sub_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
sub_input.place(x=1000,y=100,height=40,width=200)

tax_amount=Label(form3_frame,text="TAX AMOUNT",bg='#243e55',fg='#fff')
tax_amount.place(x=900,y=160)
tax_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
tax_input.place(x=1000,y=150,height=40,width=200)

grand_total=Label(form3_frame,text="GRAND TOTAL",bg='#243e55',fg='#fff')
grand_total.place(x=900,y=210)
grand_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
grand_input.place(x=1000,y=200,height=40,width=200)

button=tk.Button(form3_frame, text="SAVE",command=save_credit_data) 
button.place(x=1050,y=280,width=100)

credit_form.mainloop()



