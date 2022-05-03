
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font

# comment
window = tk.Tk()
window.title("finsYs")
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
window.geometry("%dx%d" %(width,height))
window['bg']='#2f516a'
wrappen=ttk.LabelFrame(window)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=13500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((40,40),window=heading_frame,anchor="nw")
headingfont=font.Font(family='Arial', size=25,)
addcustomer_heading= tk.Label(heading_frame, text="CASH FLOW ANALYZER",fg='#fff',bg='#243e55',height=2,bd=1,relief="raised",font=headingfont,width=76)
addcustomer_heading.pack()

#form fields
sub_headingfont=font.Font(family='Times New Roman', size=26)
form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
mycanvas.create_window((40,140),window=form_frame,anchor="nw")



label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=395,y=160)

label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=525,y=160)

label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=655,y=160)
label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=785,y=160)
label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=915,y=160)
label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=1045,y=160)
label=Label(form_frame,text="TOTAL",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=1175,y=160)

menu= StringVar()
menu.set("Filter By")
drop= OptionMenu(form_frame, menu,"Date","Month","Month range")
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))
drop.place(x=1250,y=50,)
wrappen.pack(fill='both',expand='yes',)



r1=Label(form_frame,text="Beginning Cash\nBalance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r1.place(x=70,y=220)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=225,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=225,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=225,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=225,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=225,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=225,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=225,height=40)

r2=Label(form_frame,text="Cash Inflows (Income):",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r2.place(x=70,y=300)

r3=Label(form_frame,text="Accts. Rec. \nCollections",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r3.place(x=80,y=370)
input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=375,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=375,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=375,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=375,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=375,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=375,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=375,height=40)


r4=Label(form_frame,text="Loan Proceeds",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r4.place(x=80,y=459)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=456,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=456,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=456,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=456,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=456,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=456,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=456,height=40)


r5=Label(form_frame,text="Sales & Reciepts",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r5.place(x=80,y=539)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=536,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=536,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=536,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=536,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=536,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=536,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=536,height=40)


r6=Label(form_frame,text="Other :",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r6.place(x=80,y=619)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=610,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=610,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=610,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=610,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=610,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=610,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=610,height=40)


r7=Label(form_frame,text="Total Cash\nInflows",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r7.place(x=80,y=699)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=690,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=690,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=690,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=690,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=690,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=690,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=690,height=40)

r8=Label(form_frame,text="Cash Outflow(Expenses):",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r8.place(x=80,y=769)

r9=Label(form_frame,text="Advertising\nPromotional",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r9.place(x=80,y=849)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=855,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=855,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=855,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=855,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=855,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=855,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=855,height=40)


r10=Label(form_frame,text="Bank Charges",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r10.place(x=80,y=939)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=935,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=935,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=935,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=935,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=935,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=935,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=935,height=40)

r11=Label(form_frame,text="Business Licenses \nand Permits",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r11.place(x=80,y=1019)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1025,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1025,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1025,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1025,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1025,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1025,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1025,height=40)

r12=Label(form_frame,text="Charitable Contributions",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r12.place(x=80,y=1119)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1115,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1115,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1115,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1115,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1115,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1115,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1115,height=40)

r13=Label(form_frame,text="Computer and \nInternet Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r13.place(x=80,y=1199)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1205,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1205,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1205,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1205,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1205,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1205,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1205,height=40)

r14=Label(form_frame,text="Continuing Education",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r14.place(x=80,y=1289)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1285,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1285,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1285,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1285,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1285,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1285,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1285,height=40)

r15=Label(form_frame,text="Depreciation Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r15.place(x=80,y=1379)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1375,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1375,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1375,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1375,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1375,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1375,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1375,height=40)

r16=Label(form_frame,text="Dues and Subscriptions",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r16.place(x=80,y=1469)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1465,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1465,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1465,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1465,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1465,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1465,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1465,height=40)

r17=Label(form_frame,text="Housekeeping Charges",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r17.place(x=80,y=1555)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1555,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1555,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1555,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1555,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1555,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1555,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1555,height=40)

r18=Label(form_frame,text="Insurance Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r18.place(x=80,y=1649)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1645,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1645,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1645,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1645,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1645,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1645,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1645,height=40)

r19=Label(form_frame,text="Insurance Expense-General\nLiability Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r19.place(x=80,y=1739)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1735,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1735,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1735,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1735,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1735,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1735,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1735,height=40)

r20=Label(form_frame,text="Insurance Expense-Health\nInsurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r20.place(x=80,y=1825)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1825,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1825,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1825,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1825,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1825,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1825,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1825,height=40)


r21=Label(form_frame,text="Insurance Expense-Life\nand Disability Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r21.place(x=80,y=1919)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=1919,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=1919,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=1919,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=1919,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=1919,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=1919,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=1919,height=40)

r22=Label(form_frame,text="Insurance Expense-Professional\nLiability",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r22.place(x=80,y=2009)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2009,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2009,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2009,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2009,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2009,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2009,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2009,height=40)

r23=Label(form_frame,text="Interest Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r23.place(x=80,y=2099)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2099,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2099,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2099,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2099,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2099,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2099,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2099,height=40)

r24=Label(form_frame,text="Meals and entertainment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r24.place(x=80,y=2189)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2189,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2189,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2189,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2189,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2189,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2189,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2189,height=40)

r25=Label(form_frame,text="Office Supplies",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r25.place(x=80,y=2279)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2279,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2279,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2279,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2279,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2279,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2279,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2279,height=40)

r26=Label(form_frame,text="Postage and Delivery",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r26.place(x=80,y=2369)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2369,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2369,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2369,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2369,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2369,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2369,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2369,height=40)

r27=Label(form_frame,text="Printing and Reproduction",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r27.place(x=80,y=2459)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2455,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2455,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2455,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2455,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2455,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2455,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2455,height=40)

r28=Label(form_frame,text="Professional Fees",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r28.place(x=80,y=2549)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2549,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2549,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2549,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2549,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2549,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2549,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2549,height=40)

r29=Label(form_frame,text="Purchases",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r29.place(x=80,y=2639)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2639,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2639,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2639,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2639,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2639,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2639,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2639,height=40)



r30=Label(form_frame,text="Rent Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r30.place(x=80,y=2729)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2729,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2729,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2729,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2729,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2729,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2729,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2729,height=40)

r31=Label(form_frame,text="Repair and maintenance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r31.place(x=80,y=2819)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2819,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2819,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2819,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2819,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2819,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2819,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2819,height=40)

r32=Label(form_frame,text="Small Tools and Equipment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r32.place(x=80,y=2909)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2909,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2909,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2909,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2909,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2909,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2909,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2909,height=40)

r33=Label(form_frame,text="Swachh Bharat Cess Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r33.place(x=80,y=2999)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=2999,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=2999,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=2999,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=2999,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=2999,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=2999,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=2999,height=40)

r34=Label(form_frame,text="Taxes - Property",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r34.place(x=80,y=3089)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3089,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3089,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3089,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3089,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3089,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3089,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3089,height=40)

r35=Label(form_frame,text="Telephone Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r35.place(x=80,y=3179)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3179,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3179,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3179,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3179,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3179,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3179,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3179,height=40)

r36=Label(form_frame,text="Travel Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r36.place(x=80,y=3267)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3267,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3267,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3267,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3267,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3267,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3267,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3267,height=40)

r37=Label(form_frame,text="Uncategorised Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r37.place(x=80,y=3357)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3357,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3357,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3357,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3357,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3357,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3357,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3357,height=40)

r38=Label(form_frame,text="Utilities",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r38.place(x=80,y=3447)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3447,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3447,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3447,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3447,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3447,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3447,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3447,height=40)

r39=Label(form_frame,text="Cash and cash\n equivalents",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r39.place(x=80,y=3537)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3537,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3537,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3537,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3537,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3537,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3537,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3537,height=40)

r40=Label(form_frame,text="Accounts Receivable \n(Debtors)",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r40.place(x=80,y=3627)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3627,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3627,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3627,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3627,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3627,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3627,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3627,height=40)


r41=Label(form_frame,text="Deferred CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r41.place(x=80,y=3717)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3717,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3717,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3717,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3717,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3717,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3717,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3717,height=40)

r42=Label(form_frame,text="Deferred GST\n Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r42.place(x=80,y=3807)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3807,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3807,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3807,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3807,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3807,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3807,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3807,height=40)

r43=Label(form_frame,text="Deferred IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r43.place(x=80,y=3897)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3897,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3897,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3897,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3897,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3897,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3897,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3897,height=40)

r44=Label(form_frame,text="Deferred Krishi Kalyan \nCess Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r44.place(x=80,y=3987)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=3987,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=3987,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=3987,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=3987,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=3987,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=3987,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=3987,height=40)

r45=Label(form_frame,text="Deferred Service \nTax Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r45.place(x=80,y=4077)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4077,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4077,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4077,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4077,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4077,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4077,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4077,height=40)

r46=Label(form_frame,text="Deferred SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r46.place(x=80,y=4167)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4167,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4167,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4167,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4167,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4167,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4167,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4167,height=40)

r47=Label(form_frame,text="Deferred VAT \nInput Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r47.place(x=80,y=4257)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4257,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4257,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4257,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4257,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4257,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4257,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4257,height=40)

r48=Label(form_frame,text="GST Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r48.place(x=80,y=4347)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4347,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4347,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4347,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4347,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4347,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4347,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4347,height=40)

r49=Label(form_frame,text="Inventory Asset",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r49.place(x=80,y=4437)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4437,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4437,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4437,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4437,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4437,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4437,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4437,height=40)

r50=Label(form_frame,text="Krishi Kalyan \nCess Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r50.place(x=80,y=4527)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4527,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4527,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4527,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4527,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4527,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4527,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4527,height=40)

r51=Label(form_frame,text="Prepaid Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r51.place(x=80,y=4617)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4617,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4617,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4617,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4617,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4617,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4617,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4617,height=40)

r52=Label(form_frame,text="Service Tax Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r52.place(x=80,y=4707)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4707,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4707,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4707,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4707,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4707,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4707,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4707,height=40)

r53=Label(form_frame,text="TDS Receivable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r53.place(x=80,y=4797)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4797,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4797,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4797,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4797,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4797,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4797,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4797,height=40)


r54=Label(form_frame,text="Uncategorised Asset",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r54.place(x=80,y=4887)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4887,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4887,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4887,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4887,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4887,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4887,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4887,height=40)


r55=Label(form_frame,text="Undeposited Funds",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r55.place(x=80,y=4977)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=4977,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=4977,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=4977,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=4977,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=4977,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=4977,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=4977,height=40)



r56=Label(form_frame,text="Accumulated Depreciation",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r56.place(x=80,y=5067)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5067,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5067,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5067,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5067,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5067,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5067,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5067,height=40)



r57=Label(form_frame,text="Buildings and\n Improvements",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r57.place(x=80,y=5157)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5157,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5157,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5157,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5157,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5157,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5157,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5157,height=40)



r58=Label(form_frame,text="Furniture and \nEquipment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r58.place(x=80,y=5247)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5247,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5247,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5247,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5247,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5247,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5247,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5247,height=40)


r59=Label(form_frame,text="Land",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r59.place(x=80,y=5337)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5337,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5337,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5337,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5337,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5337,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5337,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5337,height=40)

r60=Label(form_frame,text="Leasehold Improvements",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r60.place(x=80,y=5427)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5427,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5427,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5427,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5427,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5427,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5427,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5427,height=40)

r61=Label(form_frame,text="Vehicles",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r61.place(x=80,y=5517)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5517,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5517,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5517,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5517,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5517,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5517,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5517,height=40)

r62=Label(form_frame,text="CGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r62.place(x=80,y=5607)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5607,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5607,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5607,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5607,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5607,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5607,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5607,height=40)

r63=Label(form_frame,text="CST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r63.place(x=80,y=5697)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5697,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5697,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5697,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5697,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5697,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5697,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5697,height=40)


r64=Label(form_frame,text="CST Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r64.place(x=80,y=5787)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5787,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5787,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5787,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5787,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5787,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5787,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5787,height=40)


r65=Label(form_frame,text="GST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r65.place(x=80,y=5877)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5877,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5877,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5877,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5877,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5877,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5877,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5877,height=40)


r66=Label(form_frame,text="GST Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r66.place(x=80,y=5967)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=5967,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=5967,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=5967,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=5967,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=5967,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=5967,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=5967,height=40)


r67=Label(form_frame,text="IGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r67.place(x=80,y=6057)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6057,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6057,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6057,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6057,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6057,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6057,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6057,height=40)


r68=Label(form_frame,text="Input CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r68.place(x=80,y=6147)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6147,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6147,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6147,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6147,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6147,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6147,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6147,height=40)


r69=Label(form_frame,text="Input CGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r69.place(x=80,y=6237)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6237,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6237,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6237,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6237,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6237,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6237,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6237,height=40)


r70=Label(form_frame,text="Input IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r70.place(x=80,y=6327)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6327,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6327,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6327,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6327,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6327,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6327,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6327,height=40)


r71=Label(form_frame,text="Input IGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r71.place(x=80,y=6417)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6417,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6417,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6417,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6417,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6417,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6417,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6417,height=40)


r72=Label(form_frame,text="Input Krishi \nKalyan Cess",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r72.place(x=80,y=6507)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6507,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6507,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6507,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6507,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6507,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6507,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6507,height=40)

r73=Label(form_frame,text="Input Krishi Kalyan\n Cess RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r73.place(x=80,y=6597)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6597,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6597,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6597,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6597,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6597,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6597,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6597,height=40)

r74=Label(form_frame,text="Input Service Tax",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r74.place(x=80,y=6687)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6687,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6687,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6687,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6687,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6687,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6687,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6687,height=40)


r75=Label(form_frame,text="Input Service Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r75.place(x=80,y=6777)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6777,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6777,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6777,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6777,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6777,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6777,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6777,height=40)


r76=Label(form_frame,text="Input SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r76.place(x=80,y=6867)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6867,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6867,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6867,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6867,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6867,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6867,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6867,height=40)


r77=Label(form_frame,text="Input SGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r77.place(x=80,y=6957)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=6957,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=6957,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=6957,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=6957,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=6957,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=6957,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=6957,height=40)


r78=Label(form_frame,text="Input VAT 14%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r78.place(x=80,y=7047)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7047,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7047,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7047,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7047,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7047,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7047,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7047,height=40)

r79=Label(form_frame,text="Input VAT 4%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r79.place(x=80,y=7137)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7137,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7137,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7137,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7137,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7137,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7137,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7137,height=40)

r80=Label(form_frame,text="Input VAT 5%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r80.place(x=80,y=7227)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7227,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7227,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7227,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7227,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7227,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7227,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7227,height=40)

r81=Label(form_frame,text="Krishi Kalyan Cess Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r81.place(x=80,y=7317)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7317,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7317,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7317,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7317,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7317,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7317,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7317,height=40)

r82=Label(form_frame,text="Krishi Kalyan Cess Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r82.place(x=80,y=7407)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7407,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7407,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7407,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7407,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7407,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7407,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7407,height=40)

r83=Label(form_frame,text="Output CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r83.place(x=80,y=7497)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7497,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7497,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7497,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7497,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7497,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7497,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7497,height=40)

r84=Label(form_frame,text="Output CGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r84.place(x=80,y=7587)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7587,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7587,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7587,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7587,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7587,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7587,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7587,height=40)

r85=Label(form_frame,text="Output CST 2%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r85.place(x=80,y=7677)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7677,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7677,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7677,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7677,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7677,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7677,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7677,height=40)

r86=Label(form_frame,text="Output IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r86.place(x=80,y=7767)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7767,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7767,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7767,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7767,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7767,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7767,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7767,height=40)

r87=Label(form_frame,text="Output IGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r87.place(x=80,y=7857)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7857,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7857,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7857,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7857,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7857,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7857,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7857,height=40)

r88=Label(form_frame,text="Output Krishi Kalyan Cess",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r88.place(x=80,y=7947)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=7947,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=7947,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=7947,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=7947,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=7947,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=7947,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=7947,height=40)

r89=Label(form_frame,text="Output Krishi \nKalyan Cess RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r89.place(x=80,y=8037)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8037,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8037,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8037,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8037,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8037,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8037,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8037,height=40)

r90=Label(form_frame,text="Output Service Tax",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r90.place(x=80,y=8127)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8127,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8127,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8127,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8127,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8127,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8127,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8127,height=40)

r91=Label(form_frame,text="Output Service Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r91.place(x=80,y=8217)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8217,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8217,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8217,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8217,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8217,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8217,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8217,height=40)

r92=Label(form_frame,text="Output SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r92.place(x=80,y=8307)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8307,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8307,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8307,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8307,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8307,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8307,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8307,height=40)

r93=Label(form_frame,text="Output SGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r93.place(x=80,y=8397)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8397,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8397,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8397,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8397,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8397,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8397,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8397,height=40)


r94=Label(form_frame,text="Output VAT 14%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r94.place(x=80,y=8487)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8487,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8487,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8487,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8487,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8487,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8487,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8487,height=40)

r95=Label(form_frame,text="Output VAT 4%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r95.place(x=80,y=8577)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8577,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8577,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8577,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8577,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8577,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8577,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8577,height=40)

r96=Label(form_frame,text="Output VAT 5%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r96.place(x=80,y=8667)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8667,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8667,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8667,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8667,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8667,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8667,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8667,height=40)

r97=Label(form_frame,text="Service Tax Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r97.place(x=80,y=8757)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8757,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8757,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8757,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8757,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8757,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8757,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8757,height=40)

r98=Label(form_frame,text="Service Tax Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r98.place(x=80,y=8847)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8847,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8847,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8847,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8847,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8847,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8847,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8847,height=40)

r99=Label(form_frame,text="SGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r99.place(x=80,y=8937)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=8937,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=8937,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=8937,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=8937,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=8937,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=8937,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=8937,height=40)

r100=Label(form_frame,text="Swachh Bharat\n Cess Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r100.place(x=80,y=9027)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9027,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9027,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9027,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9027,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9027,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9027,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9027,height=40)

r101=Label(form_frame,text="Swachh Bharat\n Cess Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r101.place(x=80,y=9117)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9117,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9117,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9117,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9117,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9117,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9117,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9117,height=40)

r102=Label(form_frame,text="TDS Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r102.place(x=80,y=9207)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9207,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9207,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9207,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9207,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9207,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9207,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9207,height=40)

r103=Label(form_frame,text="VAT Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r103.place(x=80,y=9297)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9297,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9297,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9297,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9297,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9297,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9297,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9297,height=40)

r104=Label(form_frame,text="Opening Balance Equity",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r104.place(x=80,y=9387)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9387,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9387,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9387,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9387,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9387,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9387,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9387,height=40)

r105=Label(form_frame,text="Retained Earnings",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r105.place(x=80,y=9477)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9477,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9477,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9477,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9477,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9477,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9477,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9477,height=40)

r106=Label(form_frame,text="Billable Expense Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r106.place(x=80,y=9567)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9567,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9567,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9567,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9567,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9567,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9567,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9567,height=40)

r107=Label(form_frame,text="Consulting Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r107.place(x=80,y=9657)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9657,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9657,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9657,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9657,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9657,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9657,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9657,height=40)

r108=Label(form_frame,text="Product Sales",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r108.place(x=80,y=9747)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9747,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9747,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9747,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9747,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9747,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9747,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9747,height=40)

r109=Label(form_frame,text="Sales",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r109.place(x=80,y=9837)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9837,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9837,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9837,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9837,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9837,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9837,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9837,height=40)

r110=Label(form_frame,text="Sales - Hardware",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r110.place(x=80,y=9927)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=9927,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=9927,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=9927,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=9927,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=9927,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=9927,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=9927,height=40)

r111=Label(form_frame,text="Sales - Software",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r111.place(x=80,y=10017)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10017,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10017,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10017,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10017,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10017,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10017,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10017,height=40)

r112=Label(form_frame,text="Sales - Support\n and Maintenance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r112.place(x=80,y=10107)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10107,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10107,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10107,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10107,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10107,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10107,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10107,height=40)

r113=Label(form_frame,text="Sales Discounts",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r113.place(x=80,y=10197)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10197,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10197,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10197,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10197,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10197,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10197,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10197,height=40)

r114=Label(form_frame,text="Sales of Product Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r114.place(x=80,y=10287)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10287,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10287,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10287,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10287,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10287,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10287,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10287,height=40)

r115=Label(form_frame,text="Uncategorised Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r115.place(x=80,y=10377)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10377,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10377,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10377,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10377,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10377,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10377,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10377,height=40)

r116=Label(form_frame,text="Cost of sales",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r116.place(x=80,y=10467)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10467,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10467,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10467,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10467,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10467,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10467,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10467,height=40)

r117=Label(form_frame,text="Equipment \nRental for Jobs",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r117.place(x=80,y=10557)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10557,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10557,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10557,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10557,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10557,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10557,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10557,height=40)

r118=Label(form_frame,text="Freight and Shipping Costs",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r118.place(x=80,y=10647)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10647,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10647,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10647,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10647,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10647,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10647,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10647,height=40)

r119=Label(form_frame,text="Merchant Account Fees",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r119.place(x=80,y=10737)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10737,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10737,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10737,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10737,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10737,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10737,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10737,height=40)

r120=Label(form_frame,text="Purchases - Hardware \nfor Resale",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r120.place(x=80,y=10827)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10827,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10827,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10827,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10827,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10827,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10827,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10827,height=40)

r121=Label(form_frame,text="Purchases - Software\n for Resale",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r121.place(x=80,y=10917)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=10917,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=10917,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=10917,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=10917,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=10917,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=10917,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=10917,height=40)

r122=Label(form_frame,text="Subcontracted Services",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r122.place(x=80,y=11007)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11007,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11007,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11007,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11007,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11007,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11007,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11007,height=40)

r123=Label(form_frame,text="Tools and Craft Supplies",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r123.place(x=80,y=11097)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11097,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11097,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11097,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11097,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11097,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11097,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11097,height=40)

r124=Label(form_frame,text="Finance Charge Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r124.place(x=80,y=11187)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11187,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11187,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11187,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11187,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11187,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11187,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11187,height=40)


r125=Label(form_frame,text="Insurance Proceeds Received",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r125.place(x=80,y=11277)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11277,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11277,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11277,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11277,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11277,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11277,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11277,height=40)



r126=Label(form_frame,text="Interest Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r126.place(x=80,y=11367)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11367,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11367,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11367,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11367,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11367,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11367,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11367,height=40)


r127=Label(form_frame,text="Proceeds from \nSale of Assets",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r127.place(x=80,y=11457)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11457,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11457,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11457,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11457,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11457,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11457,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11457,height=40)


r128=Label(form_frame,text="Shipping and \nDelivery Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r128.place(x=80,y=11547)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11547,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11547,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11547,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11547,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11547,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11547,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11547,height=40)


r129=Label(form_frame,text="Ask My Accountant",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r129.place(x=80,y=11637)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11637,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11637,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11637,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11637,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11637,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11637,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11637,height=40)


r130=Label(form_frame,text="CGST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r130.place(x=80,y=11727)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11727,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11727,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11727,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11727,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11727,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11727,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11727,height=40)


r131=Label(form_frame,text="GST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r131.place(x=80,y=11817)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11817,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11817,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11817,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11817,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11817,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11817,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11817,height=40)


r132=Label(form_frame,text="IGST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r132.place(x=80,y=11907)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11907,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11907,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11907,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11907,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11907,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11907,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11907,height=40)


r133=Label(form_frame,text="Miscellaneous Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r133.place(x=80,y=11997)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=11997,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=11997,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=11997,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=11997,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=11997,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=11997,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=11997,height=40)


r134=Label(form_frame,text="Political Contributions",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r134.place(x=80,y=12087)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12087,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12087,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12087,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12087,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12087,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12087,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12087,height=40)


r135=Label(form_frame,text="SGST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r135.place(x=80,y=12177)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12177,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12177,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12177,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12177,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12177,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12177,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12177,height=40)


r136=Label(form_frame,text="Tax write-of",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r136.place(x=80,y=12267)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12267,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12267,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12267,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12267,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12267,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12267,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12267,height=40)


r137=Label(form_frame,text="Vehicle Expenses",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r137.place(x=80,y=12357)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12357,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12357,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12357,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12357,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12357,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12357,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12357,height=40)


r138=Label(form_frame,text="Other Cash Out Flows:",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r138.place(x=80,y=12447)

r139=Label(form_frame,text="Capital\nPurchases",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r139.place(x=80,y=12537)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=12537,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=12537,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=12537,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=12537,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=12537,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=12537,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=12537,height=40)

r140=Label(form_frame,text="Loan Principal",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r140.place(x=80,y=12627)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=12627,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=12627,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=12627,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=12627,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=12627,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=12627,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=12627,height=40)

r141=Label(form_frame,text="Owner's Draw",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r141.place(x=80,y=12717)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=12717,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=12717,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=12717,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=12717,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=12717,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=12717,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=12717,height=40)

r142=Label(form_frame,text="Other:",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r142.place(x=80,y=12807)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=12807,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=12807,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=12807,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=12807,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=12807,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=12807,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=12807,height=40)

r143=Label(form_frame,text="Subtotal",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r143.place(x=80,y=12897)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=12897,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=12897,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=12897,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=12897,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=12897,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=12897,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=12897,height=40)

r144=Label(form_frame,text="Total Cash\nOutflows",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r144.place(x=80,y=12987)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=12989,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=12989,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=12989,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=12989,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=12989,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=12989,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=12989,height=40)

r145=Label(form_frame,text="Ending Cash\nBalance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r145.place(x=80,y=13077)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=270,y=13079,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=420,y=13079,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=550,y=13079,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=680,y=13079,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=810,y=13079,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=940,y=13079,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1070,y=13079,height=40)





window.mainloop()
