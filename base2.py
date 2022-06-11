from tkinter import  *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import filedialog
from tkinter.font import Font
from PIL import Image,ImageTk
from  tkinter import ttk
import datetime
import os

root = Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.title("F-Billing Revolution")
root.geometry("%dx%d" %(width,height))
icon1=PhotoImage(file='emp.png')
icon=icon1.subsample(1,1)

root.iconphoto(False,icon)

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabs = ttk.Frame(tabControl)
x=datetime.datetime.now()



image=Image.open('imgtog.png')
img1=image.resize((40, 40))
my_img1=ImageTk.PhotoImage(img1)
tabControl.add(tab1,image=my_img1 ,text='Recurring',compound=LEFT)

image=Image.open('imgtog.png')
img2=image.resize((40, 40))
my_img2=ImageTk.PhotoImage(img2)
tabControl.add(tab2, text ='Purchase Orders',image=my_img2, compound=LEFT,)
tabControl.place(x=10,y=30)

ttk.Label(tab1,
		text ="").grid(column = 0,row = 0,padx = 30,pady = 30)





root.mainloop()