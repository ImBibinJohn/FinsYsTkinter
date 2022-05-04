from tkinter import *
import tkinter.font as font

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


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



fig = matplotlib.figure.Figure(figsize=(11,6))
ax = fig.add_subplot(111)
# ax.set_facecolor("#2f516a")

ax.pie([20,30,50]) 
ax.legend(["20","30","50"])
fig.set_facecolor("#243e55")
circle=matplotlib.patches.Circle( (0,0), 0.7, color='#243e55')
ax.add_artist(circle)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
canvas.draw()
root.mainloop()

