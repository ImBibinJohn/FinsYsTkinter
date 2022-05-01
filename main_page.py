import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import ttk, filedialog, scrolledtext, messagebox
from datetime import date
from tkcalendar import DateEntry
import datetime
import center_tk_window
import os
from tkinter.filedialog import askopenfile
from tkinter import filedialog as fd

root = tk.Tk()
root.title('FinsYs Tkinter')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

tabControl = ttk.Notebook(root)
invs= ttk.Frame(tabControl)
inv=PhotoImage(file='invoice.png')
invo=inv.subsample(1,1)
tabControl.add(invs, text ='Invoices',image=invo,compound=LEFT)


label = Label(root, text="Registration form",width=20,font=("bold", 20))
label.grid(padx=90,pady=53)

invs = ttk.Frame(tabControl)
tabControl.add(invs, text='Invoices', compound=LEFT)


tabControl.pack(expand=1, fill="both", pady=20)

frame0 = tk.Frame(invs)
frame0.pack(fill=tk.X)
c1 = Label(frame0)

c1.pack(side=tk.LEFT)

root.mainloop()
