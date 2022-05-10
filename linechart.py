from tkinter import *
import tkinter.font as font
import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure

import numpy as np


root = Tk()
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

fig = Figure(figsize=(11, 6), dpi=100)
t = np.arange(0, 10, .5)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack()
fig.set_facecolor("#243e55")

tkinter.mainloop()

