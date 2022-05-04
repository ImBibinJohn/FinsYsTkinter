from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk
import  numpy
# matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# import click

from requests import options
def selected(event):
    if menu.get() == 'Pie':
        import piechart
    elif  menu.get() == 'Bubble':
        import bubblechart
    elif  menu.get() == 'Doughnut':
        import doughnut
    elif  menu.get() == 'Line':
        import linechart
    else :
        import cashposition


window = Tk()
window.title("finsYs")
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
window.geometry("%dx%d" %(width,height))
window['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=24,)
inv_heading= Label(window, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=4)
inv_heading.pack(pady=20)
cashposition=Label(window,text="Today: $ 3556345 USD",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 220, y =50)
cash=Label(window,text="CASH POSITION",font=('Helvitica',25),bg='#243e55',fg='white').place(x = 220, y =110)                
menu= StringVar()
menu.set("Change currency")
drop= OptionMenu(window, menu,"$ USD","₹ INR","¥ YEN","€ EURO")
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))

drop.place(x=1000,y=50,)
menu= StringVar()
menu.set("Bar Chart")
options=["Pie","Line","Bubble","Doughnut"]
drop= OptionMenu(window,menu,*options,command=selected )
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))

drop.place(x=1000,y=110)

# inv_heading= Label(window, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=50)
# inv_heading.pack(pady=20)
# # chart view

f = Figure(figsize=(11,6))
ax = f.add_subplot(111)

data = (20, 35, 30, 35, 27)

ind = numpy.arange(5)  # the x locations for the groups
width = .5

rects1 = ax.bar(ind, data, width)
f.set_facecolor("#243e55")
ax.set_facecolor("#2f516a")
canvas = FigureCanvasTkAgg(f, master=window)
canvas.draw()
canvas.get_tk_widget().pack()


window.mainloop()