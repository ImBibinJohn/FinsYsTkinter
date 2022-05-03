from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk
# import click

from requests import options
def selected(event):
    if menu.get() == 'Pie':
        import piechart
    elif  menu.get() == 'Bar':
        import barchart
    elif  menu.get() == 'Bubble':
        import bubblechart
    elif  menu.get() == 'Doughnut':
        import doughnut
    elif  menu.get() == 'Line':
        import linechart
    else :
        import cashposition

def add_invoice():
    x=4
window = Tk()
window.title('fynsYs')
window.geometry("700x700")
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
menu.set("Chart Type")
options=["Bar","Pie","Line","Bubble","Doughnut"]
drop= OptionMenu(window,menu,*options,command=selected )
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))

drop.place(x=1000,y=110)

inv_heading= Label(window, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=50)
inv_heading.pack(pady=20)
# chart view
window.mainloop()