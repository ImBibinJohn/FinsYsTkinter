from tkinter import *
import tkinter.font as font
import matplotlib.cm as cm
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np


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


np.random.seed(19680801)
   
# frameChartsLT = tk.Frame(root)
# frameChartsLT.pack()

x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
colors = cm.rainbow(np.random.rand(40))

fig = Figure(figsize=(11,6), dpi=100)
ax = fig.add_subplot(111) 
fig.set_facecolor("#243e55")

ax.scatter(x, y, s=z*1000,c=colors)
ax.set_facecolor("#60a1d1")

chart1 = FigureCanvasTkAgg(fig)
chart1.get_tk_widget().pack()

root.mainloop()

