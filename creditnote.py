
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font


def add_custom():
    import add_new_customer_form


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

email=Label(form_frame,text="EMAIL",bg='#243e55',fg='#fff')
email.place(x=530,y=100,)
email_input=Entry(form_frame,width=55,bg='#243e55',fg='#fff')
email_input.place(x=530,y=130,height=40)

billing_ad=Label(form_frame,text="BILLING ADDRESS",bg='#243e55',fg='#fff')
billing_ad.place(x=30,y=200,)
billing_input=Entry(form_frame,width=75,bg='#243e55',fg='#fff')
billing_input.place(x=30,y=230,height=90)

credit_note=Label(form_frame,text="CREDIT NOTE",bg='#243e55',fg='#fff')
credit_note.place(x=530,y=200,)
credit_input=Entry(form_frame,width=55,bg='#243e55',fg='#fff')
credit_input.place(x=530,y=230,height=40)

place_of_supp=tk.Label(form_frame,text="PLACE OF SUPPLY",bg='#243e55',fg='#fff')
place_drop=ttk.Combobox(form_frame)
place_drop['values']=("KERALA","TAMILNADU","ANDHRA PRADESH","KARNATAKA")
place_of_supp.place(x=20,y=330,height=15,width=100)
place_drop.place(x=30,y=360,height=40,width=450)

invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
invoice_drop=ttk.Combobox(form_frame)
invoice_drop['values']=("OCT2022-DEC2022","","","")
invoice_period.place(x=20,y=330,height=15,width=100)
invoice_drop.place(x=30,y=620,height=40,width=450)

invoice_no=tk.Label(form_frame,text="SELECT INVOICE NO",bg='#243e55',fg='#fff')
invoice_no_drop=ttk.Combobox(form_frame)
invoice_no_drop['values']=("SELECT INVOICE NO","","","")
invoice_no.place(x=530,y=330,height=15,width=100)
invoice_no_drop.place(x=530,y=360,height=40,width=450)

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
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=10,y=120,height=15,width=100)
pro_drop.place(x=10,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=10,y=210,height=15,width=100)
pro_drop.place(x=10,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
pro_drop.place(x=10,y=310,height=40,width=150)



#row 1
discription_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription_input.place(x=260,y=150,height=40,width=180)
#row2
discription_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription_input.place(x=260,y=240,height=40,width=180)
#row3
discription_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription_input.place(x=260,y=310,height=40,width=180)

#row 1
quantity_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input.place(x=480,y=150,height=40,width=150)
#row2
quantity_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input.place(x=480,y=240,height=40,width=150)
#row3
quantity_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input.place(x=480,y=310,height=40,width=150)


#row 1
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input.place(x=680,y=150,height=40,width=150)
#row2
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input.place(x=680,y=240,height=40,width=150)
#row3
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input.place(x=680,y=310,height=40,width=150)

#row 1
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input.place(x=850,y=150,height=40,width=100)
#row2
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input.place(x=850,y=240,height=40,width=100)
#row3
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input.place(x=850,y=310,height=40,width=100)
#row1
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=1250,y=150,height=15,width=150)
pro_drop.place(x=1000,y=150,height=40,width=150)
#row2
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=1110,y=240,height=15,width=150)
pro_drop.place(x=1000,y=240,height=40,width=150)
#row3
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=1000,y=310,height=15,width=150)
pro_drop.place(x=1000,y=310,height=40,width=150)

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

button=tk.Button(form3_frame, text="SAVE",) 
button.place(x=1050,y=280,width=100)

credit_form.mainloop()



