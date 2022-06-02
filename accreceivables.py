import tkinter as tk
from tkinter import ttk
from tkinter import *
import zlib
import matplotlib.figure
import matplotlib.patches
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from tkcalendar import DateEntry
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cursor=mydata.cursor()
#cc
def accrecivabales():
    prlframe=tk.Tk()
    prlframe.title('Balance Sheet')
    prlframe.geometry('1500x1000')
    #dash['bg'] = '#2f516f'
    cid=2
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
    tk.Label(pframe,text='A/R AGEING SUMMARY REPORT',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')

    def menuuu(e):
        dropp=drop.get()
        def datedateee():
            fdate=dte.get()
            ldate=dtee.get()   
        if dropp=='Custom':            
            tk.Label(form_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.45,rely=0.1)
            dte=StringVar()
            DateEntry(form_frame,textvariable=dte).place(relx=0.45,rely=0.23,relwidth=0.2,relheight=0.15)
            tk.Label(form_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.70,rely=0.1)
            dtee=StringVar()
            DateEntry(form_frame,textvariable=dtee).place(relx=0.70,rely=0.23,relwidth=0.2,relheight=0.15)
            datedateee()

    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= ttk.Combobox(form_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menuuu)
    drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
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
    set.heading("CUSTOMER NAME",text="CUSTOMER NAME",anchor=CENTER )
    set.heading("TRANSACTION TYPE",text="TRANSACTION TYPE",anchor=CENTER, )
    set.heading("CURRENT",text="CURRENT",anchor=CENTER,)
    set.heading("0-30",text="0-30",anchor=CENTER,)
    set.heading("30-60",text="30-60",anchor=CENTER,)
    set.heading("60-90",text="60-90",anchor=CENTER)
    set.heading("90 AND OVER",text="90 AND OVER",anchor=CENTER)
    set.heading("TOTAL",text="TOTAL",anchor=CENTER)
    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
   
    prlframe.mainloop()
accrecivabales()   