import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def dashboard():
    dash=tk.Tk()
    dash.title('Dashboard')
    dash.geometry('1500x1000')
    #dash['bg'] = '#2f516f'
    mycanvas=tk.Canvas(dash,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(dash,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    dashframe=tk.Frame(mycanvas)
    dashframe['bg']='#2f516f'
    mycanvas.create_window((0,0),window=dashframe,anchor='nw',width=1500,height=1200)
    
    #heading frame
    headdash=tk.Frame(dashframe,bg='#243e54')
    tk.Label(headdash,text='Company Name',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    headdash.place(relx=0.05,rely=0.03,relwidth=0.9,relheight=0.1)

    #profit and loss frame
    pframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(pframe,text='PROFIT AND LOSS',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    barframe=tk.Frame(pframe,bg='red')
    
    x=100
    y=123
    data = {'Income': x,
            'Expense': y,}

    group_data = list(data.values())
    group_names = list(data.keys())

    fig = matplotlib.figure.Figure(figsize=(20,2))
    abar = fig.add_subplot(111)

    # Default Settings
    abar.barh(group_names, group_data)

    #canvasbar = FigureCanvasTkAgg(fig, master=barframe)
    #canvasbar.get_tk_widget().place(relx=0,rely=0,relwidth=1,relheight=1)
    #canvasbar.draw()

    #barframe.place(relx=0,rely=0.5,relwidth=1,relheight=0.5)
    pframe.place(relx=0.05,rely=0.2,relwidth=0.27,relheight=0.3)
   

     #Expenses frame
    expframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(expframe,text='EXPENSES: ₹ ',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    expframe.place(relx=0.37,rely=0.2,relwidth=0.27,relheight=0.3)
    fig = matplotlib.figure.Figure(figsize=(2,2))
    ax = fig.add_subplot(111)
    sizes=123,0.00



    ax.pie(sizes,radius=1.4,labels=sizes) 
    fig.set_facecolor("#243e55")
    circle=matplotlib.patches.Circle( (0,0), 1.2, color='#243e55')
    ax.add_artist(circle)

    canvas = FigureCanvasTkAgg(fig, master=expframe)
    canvas.get_tk_widget().place(relx=0,rely=0.15,relwidth=1,relheight=0.8)
    canvas.draw()

     #Bank Account frame
    bankframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(bankframe,text='BANK ACCOUNTS',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    bankframe.place(relx=0.68,rely=0.2,relwidth=0.27,relheight=0.3)

      #Income frame
    incframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(incframe,text='INCOME: ₹',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    incframe.place(relx=0.05,rely=0.55,relwidth=0.27,relheight=0.3)

      #Invoice frame
    invframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(invframe,text='INVOICE',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    invframe.place(relx=0.37,rely=0.55,relwidth=0.27,relheight=0.3)

     #Sales frame
    salesframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(salesframe,text='SALES: ₹',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    salesframe.place(relx=0.68,rely=0.55,relwidth=0.27,relheight=0.3)

    dash.mainloop()
dashboard()    