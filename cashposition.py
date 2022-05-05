import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
import mysql.connector
import  numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.cm as cm
import matplotlib.figure
import matplotlib.patches

def clear_frame():
   form_frame.destroy()

def selected(event):
    if menu.get() == 'Pie':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,240),window=form_frame,anchor="nw")
        stockListExp = ['gst' , 'tax', 'expences', 'cgst', 'cashflow']
        stockSplitExp = [15,25,40,10,10]
        fig = Figure(figsize=(11,6))
        ax = fig.add_subplot(111) 
        fig.set_facecolor("#243e55")
        colors = ( "#45BDEE", "#28A7EA", "#006CBB", 
          "#034698") 
        ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,colors = colors)
        chart1 = FigureCanvasTkAgg(fig,form_frame)
        chart1.get_tk_widget().pack()

    elif  menu.get() == 'Bubble':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,240),window=form_frame,anchor="nw")
        np.random.seed(19680801)
        x = np.random.rand(40)
        y = np.random.rand(40)
        z = np.random.rand(40)
        colors = cm.rainbow(np.random.rand(40))
        fig = Figure(figsize=(11,6), dpi=100)
        ax = fig.add_subplot(111) 
        fig.set_facecolor("#243e55")

        ax.scatter(x, y, s=z*1000,c=colors)
        ax.set_facecolor("#60a1d1")

        chart1 = FigureCanvasTkAgg(fig,master=form_frame)
        chart1.get_tk_widget().pack()
    elif  menu.get() == 'Doughnut':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,240),window=form_frame,anchor="nw")

        fig = matplotlib.figure.Figure(figsize=(11,6))
        ax = fig.add_subplot(111)
        ax.pie([20,30,50]) 
        ax.legend(["20","30","50"])
        fig.set_facecolor("#243e55")
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='#243e55')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=form_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    elif menu.get()=='Bar':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,240),window=form_frame,anchor="nw")

        f = Figure(figsize=(11,6))
        ax = f.add_subplot(111)

        data = (20, 35, 30, 35, 27)

        ind = np.arange(5) 
        width = .5

        rects1 = ax.bar(ind, data, width)
        f.set_facecolor("#243e55")
        ax.set_facecolor("#2f516a")
        canvas = FigureCanvasTkAgg(f, master=form_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else :
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,240),window=form_frame,anchor="nw")
        fig = Figure(figsize=(11, 6))
        t = np.arange(0, 10, .5)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        canvas = FigureCanvasTkAgg(fig, master=form_frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack()
        fig.set_facecolor("#243e55")
    


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

headingfont=font.Font(family='Arial', size=28,)
heading_frame=Frame(mycanvas,width=1200,bg='#243e55',height=200)
mycanvas.create_window((150,20),window=heading_frame,anchor="nw")
# inv_heading= Label(mycanvas, borderwidth=1, relief="raised",width=180,bg='#243e55', fg='#fff',height=13)
# inv_heading.pack(pady=20)
cashposition=Label(heading_frame,text="Today: $ 3556345 USD",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 80, y =50)
cash=Label(heading_frame,text="CASH POSITION",font=headingfont,bg='#243e55',fg='white').place(x = 60, y =110)                

menu= StringVar()
menu.set("Change currency")
drop= OptionMenu(heading_frame, menu,"$ USD","₹ INR","¥ YEN","€ EURO")
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))

drop.place(x=950,y=50,)
menu= StringVar()
menu.set("Bar Chart")
options=["Pie","Line","Bubble","Doughnut","Bar"]
drop= OptionMenu(heading_frame,menu,*options,command=selected )
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))
drop.place(x=950,y=110)
wrappen.pack(fill='both',expand='yes',)

form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
mycanvas.create_window((200,240),window=form_frame,anchor="nw")

f = Figure(figsize=(11,6))
ax = f.add_subplot(111)

data = (20, 35, 30, 35, 27)

ind = np.arange(5)  # the x locations for the groups
width = .5

rects1 = ax.bar(ind, data, width)
f.set_facecolor("#243e55")
ax.set_facecolor("#2f516a")
canvas = FigureCanvasTkAgg(f, master=form_frame)
canvas.draw()
canvas.get_tk_widget().pack()


window.mainloop()