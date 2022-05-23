
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkcalendar import DateEntry

delay_form = tk.Tk()
delay_form.title("finsYs")
delay_form.geometry("1000x1000")
delay_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(delay_form)
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
credit_heading=Label(heading_frame, text="DELAYED CHARGE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=headingfont,width=70)
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

title_lab.place(x=10,y=200,height=15,width=100)
drop2.place(x=30,y=230,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)


delayed_charge_date=Label(form_frame,text="DELAYED CHARGE DATE",bg='#243e55',fg='#fff')
delayed_charge_date.place(x=30,y=300,)
delayed_input=DateEntry(form_frame,width=55,bg='#243e55',fg='#fff')
delayed_input.place(x=30,y=330,height=40,width=450)



#invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
#invoice_drop=ttk.Combobox(form_frame)
#invoice_drop['values']=("OCT2022-DEC2022","","","")
#invoice_period.place(x=20,y=330,height=15,width=100)
#invoice_drop.place(x=30,y=360,height=40,width=450)

#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,650),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

label=tk.Label(form2_frame,text="PRODUCT/SERVICE\t\tDESCRIPTION\t\tQUANTITY\t\tRATE\t\tTOTAL\t\tTAX\t",bg='#243e55' ,fg="white",font=('Arial',))
label.place(x=60,y=60)

#row1
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product1=ttk.Combobox(form2_frame)
product1['values']=("","","","")
pro.place(x=10,y=120,height=15,width=100)
product1.place(x=60,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product2=ttk.Combobox(form2_frame)
product2['values']=("","","","")
pro.place(x=10,y=210,height=15,width=100)
product2.place(x=60,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product3=ttk.Combobox(form2_frame)
product3['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
product3.place(x=60,y=310,height=40,width=150)




#row 1
description_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
description_input1.place(x=320,y=150,height=40,width=150)
#row2
description_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
description_input2.place(x=320,y=240,height=40,width=150)
#row3
description_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
description_input3.place(x=320,y=310,height=40,width=150)

#row 1
quantity_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input1.place(x=530,y=150,height=40,width=150)
#row2
quantity_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input2.place(x=530,y=240,height=40,width=150)
#row3
quantity_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input3.place(x=530,y=310,height=40,width=150)


#row 1
price_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input1.place(x=720,y=150,height=40,width=150)
#row2
price_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input2.place(x=720,y=240,height=40,width=150)
#row3
price_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input3.place(x=720,y=310,height=40,width=150)

#row 1
total_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input1.place(x=890,y=150,height=40,width=150)
#row2
total_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input2.place(x=890,y=240,height=40,width=150)
#row3
total_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input3.place(x=890,y=310,height=40,width=150)
#row1
tax1=ttk.Combobox(form2_frame)
tax1['values']=("","","","")
tax1.place(x=1050,y=150,height=40,width=150)
#row2
tax2=ttk.Combobox(form2_frame)
tax2['values']=("","","","")
tax2.place(x=1050,y=240,height=40,width=150)
#row3
tax3=ttk.Combobox(form2_frame)
tax3['values']=("","","","")
tax3.place(x=1050,y=310,height=40,width=150)

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

delay_form.mainloop()
