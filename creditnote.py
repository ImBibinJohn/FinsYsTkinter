
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
        port='3308',
        database='finsys_tkinter'
        )
    mycursor = mydb.cursor()


#to save credit formdata
def save_credit_data():
        db_connection()      
        mail=email.get()
        biladdr=biladdress.get()
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
        sql= '''INSERT INTO app1_credit (mail,biladdr,creditdate,creditno,place,invnum,invperiod,product,descrip,qty,price,tax,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%S,%S)''' #adding values into db
        val=(mail,biladdr,creditno,place,invnum,invperiod,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3)
        # mycursor.execute(sql,[(mail),(biladdr),(creditno),(place),(invnum),(product1),(product2),(product3),(descrip1),(descrip2),(descrip3),(price1),(price2),(price3),(total1),(total2),(total3),(tax1),(tax2),(tax3)])
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()


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

#declaring global variables
email=tk.StringVar()
biladdress=tk.StringVar()
creditno=tk.StringVar()
place=tk.StringVar()
invnum=tk.StringVar()
invperiod=tk.StringVar()
product1=tk.StringVar()
product2=tk.StringVar()
product3=tk.StringVar()
descrip1=tk.StringVar()
descrip2=tk.StringVar()
descrip3=tk.StringVar()
qty1=tk.StringVar()
qty2=tk.StringVar()
qty3=tk.StringVar()
price1=tk.StringVar()
price2=tk.StringVar()
price3=tk.StringVar()
total1=tk.StringVar()
total2=tk.StringVar()
total3=tk.StringVar()
tax1=tk.StringVar()
tax2=tk.StringVar()
tax3=tk.StringVar() 

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_custom)
add_custom.place(x=335,y=230)

mailLab=Label(form_frame,text="EMAIL",bg='#243e55',fg='#fff')
mailLab.place(x=530,y=100,)
mail=Entry(form_frame,width=55,bg='#243e55',fg='#fff',textvariable=email)
mail.place(x=530,y=130,height=40)

biladdrLab=Label(form_frame,text="BILLING ADDRESS",bg='#243e55',fg='#fff')
biladdrLab.place(x=30,y=200,)
biladdr=Entry(form_frame,width=75,bg='#243e55',fg='#fff',textvariable=biladdress)
biladdr.place(x=30,y=230,height=90)

credit_note=Label(form_frame,text="CREDIT NOTE",bg='#243e55',fg='#fff')
credit_note.place(x=530,y=200,)
creditno=Entry(form_frame,width=55,bg='#243e55',fg='#fff')
creditno.place(x=530,y=230,height=40)

place_of_supp=tk.Label(form_frame,text="PLACE OF SUPPLY",bg='#243e55',fg='#fff')
place=ttk.Combobox(form_frame,textvariable=place)
place['values']=("KERALA","TAMILNADU","ANDHRA PRADESH","KARNATAKA")
place_of_supp.place(x=20,y=330,height=15,width=100)
place.place(x=30,y=360,height=40,width=450)

invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
invoice_drop=ttk.Combobox(form_frame,textvariable=invperiod)
invoice_drop['values']=("OCT2022-DEC2022","","","")
invoice_period.place(x=20,y=330,height=15,width=100)
invoice_drop.place(x=30,y=620,height=40,width=450)

invoice_no=tk.Label(form_frame,text="SELECT INVOICE NO",bg='#243e55',fg='#fff')
invnum=ttk.Combobox(form_frame,textvariable=invnum)
invnum['values']=("SELECT INVOICE NO","","","")
invoice_no.place(x=530,y=330,height=15,width=100)
invnum.place(x=530,y=360,height=40,width=450)



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
product1=ttk.Combobox(form2_frame,textvariable=product1)
product1['values']=("","","","")
pro.place(x=10,y=120,height=15,width=100)
product1.place(x=10,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product2=ttk.Combobox(form2_frame,textvariable=product2)
product2['values']=("","","","")
pro.place(x=10,y=210,height=15,width=100)
product2.place(x=10,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product3=ttk.Combobox(form2_frame,textvariable=product3)
product3['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
product3.place(x=10,y=310,height=40,width=150)



#row 1
descrip1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descrip1)
descrip1.place(x=260,y=150,height=40,width=180)
#row2
descrip2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descrip2)
descrip2.place(x=260,y=240,height=40,width=180)
#row3
descrip3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descrip3)
descrip3.place(x=260,y=310,height=40,width=180)

#row 1
qty1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qty1)
qty1.place(x=480,y=150,height=40,width=150)
#row2
qty2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qty2)
qty2.place(x=480,y=240,height=40,width=150)
#row3
qty3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qty3)
qty3.place(x=480,y=310,height=40,width=150)


#row 1
price1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=price1)
price1.place(x=680,y=150,height=40,width=150)
#row2
price2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=price3)
price2.place(x=680,y=240,height=40,width=150)
#row3
price3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=price3)
price3.place(x=680,y=310,height=40,width=150)

#row 1
total1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=total1)
total1.place(x=850,y=150,height=40,width=100)
#row2
total2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=total2)
total2.place(x=850,y=240,height=40,width=100)
#row3
total3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=total3)
total3.place(x=850,y=310,height=40,width=100)
#row1
tax1=ttk.Combobox(form2_frame,textvariable=tax1)
tax1['values']=("","","","")
tax1.place(x=1250,y=150,height=15,width=150)
tax1.place(x=1000,y=150,height=40,width=150)
#row2
tax2=ttk.Combobox(form2_frame,textvariable=tax2)
tax2['values']=("","","","")
tax2.place(x=1110,y=240,height=15,width=150)
tax2.place(x=1000,y=240,height=40,width=150)
#row3
tax3=ttk.Combobox(form2_frame,textvariable=tax3)
tax3['values']=("","","","")
tax3.place(x=1000,y=310,height=15,width=150)
tax3.place(x=1000,y=310,height=40,width=150)

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



