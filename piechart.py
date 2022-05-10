from tkinter import *
import tkinter.font as font
# import tkinter
# from turtle import color
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
# from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
# import matplotlib.figure
# import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
# import numpy as np


root = tk.Tk()
root.title("finsYs")
# width=root.winfo_screenwidth()
# height=root.winfo_screenheight()
# root.geometry("%dx%d" %(width,height))
# root['bg']='#2f516a'
# headingfont=font.Font(family='Helvitica', size=24,)
# inv_heading= Label(root, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=4)
# inv_heading.pack(pady=20)
# cashposition=Label(root,text="Today: $ 3556345 USD",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 220, y =50)
# cash=Label(root,text="CASH POSITION",font=('Helvitica',25),bg='#243e55',fg='white').place(x = 220, y =110)                


    

frameChartsLT = tk.Frame(root)
frameChartsLT.pack()

stockListExp = ['gst' , 'tax', 'expences', 'cgst', 'cashflow']
stockSplitExp = [15,25,40,10,10]

fig = Figure(figsize=(10,5), dpi=100)
ax = fig.add_subplot(111) 
fig.set_facecolor("#243e55")
colors = ( "#45BDEE", "#28A7EA", "#006CBB", 
          "#034698") 
ax.pie(stockSplitExp, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True,colors = colors)

chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
chart1.get_tk_widget().pack()

root.mainloop()

