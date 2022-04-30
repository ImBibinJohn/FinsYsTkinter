import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
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

sanitizer1_lbl = Label(F2, text="Account", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitizer1_lbl.place(x=10,y=50)

menu= StringVar()
menu.set("Select Any Language")

#Create a dropdown Menu
drop= OptionMenu(F2, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
drop.place(x=280,y=50)

sanitize_lbl = Label(F2, text="Enter the following from your statement.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitize_lbl.place(x=10,y=110)

mask_lbl = Label(F2, text="Beginning balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
mask_lbl.place(x=10,y=160)
mask_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE)
mask_txt.place(x=10,y=200)

hand_gloves_lbl = Label(F2, text="Ending balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
hand_gloves_lbl.place(x=280,y=160)
hand_gloves_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief =GROOVE)
hand_gloves_txt.place(x=280,y=200)

syrup_lbl = Label(F2, text="Ending date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
syrup_lbl.place(x=550,y=160)
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE)
cal.place(x=550,y=200)

sanitize_lbl = Label(F2, text="Enter the service charge or interest earned, if necessary.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitize_lbl.place(x=10,y=280)

cream_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
cream_lbl.place(x=10,y=340)
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE)
cal.place(x=10,y=380)

thermal_gun_lbl = Label(F2, text="Service charge", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_gun_lbl.place(x=280,y=340)
thermal_gun_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff",bd=5,relief=GROOVE)
thermal_gun_txt.place(x=280,y=380)

select_customer_lab=tk.Label(F2,text="Expense Account",font=('times new roman', 16, 'bold'),bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(F2,width=22, textvariable = select_customer_input)

drop2['values']=("Select-Options")

select_customer_lab.place(x=550,y=340)
drop2.place(x=550,y=380,width=250,height=33)
wrappen.pack(fill='both',expand='yes')

thermal_zone_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zone_lbl.place(x=10,y=440)
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE)
cal.place(x=10,y=480)

thermal_zoo_lbl = Label(F2, text="Interest earned", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zoo_lbl.place(x=280,y=440)
thermal_zoo_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE)
thermal_zoo_txt.place(x=280,y=480)

select_customer_lab=tk.Label(F2,text="Income Account",font=('times new roman', 16, 'bold'),bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(F2,width=22, textvariable = select_customer_input)

drop2['values']=("Select-Options")

select_customer_lab.place(x=550,y=440)
drop2.place(x=550,y=480,width=250,height=33)
wrappen.pack(fill='both',expand='yes')

b1 = Button(F2,text = "Start Reconciling",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'))  
b1.place(x=280,y=560,width=250,height=40) 

root.mainloop()


