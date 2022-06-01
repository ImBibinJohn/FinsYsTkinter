import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.figure
import matplotlib.patches
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cursor=mydata.cursor()
#cc
def balancesheet():
    prlframe=tk.Tk()
    prlframe.title('Balance Sheet')
    prlframe.geometry('1500x1000')
    #dash['bg'] = '#2f516f'
    mycanvas=tk.Canvas(prlframe,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(prlframe,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    profitlossframe=tk.Frame(mycanvas)
    profitlossframe['bg']='#2f516f'
    mycanvas.create_window((0,0),window=profitlossframe,anchor='nw',width=1500,height=2200)

    pframe=tk.Frame(profitlossframe,bg='#243e54')
    tk.Label(pframe,text='BALANCE SHEET',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')

    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    menu= StringVar()
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= OptionMenu(form_frame, menu,*options)
    drop.config(bg='#243e55', fg="white",font=('Arial',18))
    drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))
    drop.place(relx=0.05,rely=0.23,relwidth=0.3)
     #buttons
    tk.Button(form_frame,text = "Run Report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold')).place(relx=0.55,rely=0.5,relwidth=0.15)
    tk.Button(form_frame,text = "Back",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold')).place(relx=0.75,rely=0.5,relwidth=0.15)
    form_frame.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.1)

    tableframe=tk.Frame(profitlossframe,bg='#243e54')
    #image
    imageframe=tk.Frame(tableframe,bg='#add8e6')
    size=(200,200)
    cv=Image.open('timeact.png').resize(size)
    ax=ImageTk.PhotoImage(cv,master=prlframe)
    ay=tk.Label(imageframe,image=ax,bg='#243e54')
    ay.place(relx=0.02,rely=0.08,relheight=0.8,relwidth=0.2)
    tk.Label(imageframe,text="INFOX", font=('times new roman', 25, 'bold'),bg="#add8e6").place(relx=0.25,rely=0.4,relwidth=0.2)
    imageframe.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.15)
    #contents
    contframe=tk.Frame(tableframe,bg='white')
    contframe.place(relx=0.05,rely=0.17,relwidth=0.9,relheight=0.7)
    set = ttk.Treeview(contframe,height=0)
    set.place(relx=0,rely=0,relwidth=1)

    set['columns']= ('CUSTOMER NAME', 'TRANSACTION TYPE','CURRENT','0-30','30-60','60-90','90 AND OVER','TOTAL')
    set.column("#0", width=0,  stretch=NO)
    set.column("CUSTOMER NAME",width=120,anchor=CENTER )
    set.column("TRANSACTION TYPE",width=130,anchor=CENTER, )
    set.column("CURRENT",width=100,anchor=CENTER,)
    set.column("0-30",width=100,anchor=CENTER,)
    set.column("30-60",width=100,anchor=CENTER,)
    set.column("60-90",width=100,anchor=CENTER)
    set.column("90 AND OVER",width=100,anchor=CENTER)
    set.column("TOTAL",width=198,anchor=CENTER)


    #set.heading("#0",text="",anchor=CENTER)
    set.heading("CUSTOMER NAME",text="",anchor=CENTER )
    set.heading("TRANSACTION TYPE",text="",anchor=CENTER, )
    set.heading("CURRENT",text="",anchor=CENTER,)
    set.heading("0-30",text="",anchor=CENTER,)
    set.heading("30-60",text="",anchor=CENTER,)
    set.heading("60-90",text="",anchor=CENTER)
    set.heading("90 AND OVER",text="",anchor=CENTER)
    set.heading("TOTAL",text="TOTAL",anchor=CENTER)

    tk.Label(contframe,text = "Income",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
    tk.Label(contframe,text = " Total Income",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.08)
    tk.Label(contframe,text = " 0.0",bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.08)
    tk.Label(contframe,text = " Cost of Goods Sold ",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.12)
    tk.Label(contframe,text = " Gross Profit ",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.16)
    tk.Label(contframe,text = " 0.0",bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.16)
    tk.Label(contframe,text = "Other Income",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.20)
    tk.Label(contframe,text = " 0.0",bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.20)
    tk.Label(contframe,text = "Expenses",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.24)
    tk.Label(contframe,text = "Other Expenses",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.28)
    tk.Label(contframe,text = " 0.0",bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.28)
    tk.Label(contframe,text = "TOTAL EXPENSE",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.32)
    tk.Label(contframe,text = " 0.0",bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.32) 
    tk.Label(contframe,text = "PROFIT OR LOSS",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.36)
    tk.Label(contframe,text = " 0.0",bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.36) 

    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
   
    prlframe.mainloop()
balancesheet()   