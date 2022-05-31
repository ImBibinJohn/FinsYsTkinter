from enum import auto
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
from tkinter.tix import AUTO
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from requests import get
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql
from tkinter.tix import AUTO


root = tk.Tk()
# fun()
root.title("finsYs")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")
wrappen=ttk.LabelFrame(root)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=1345,height=2500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=2400,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="EDIT EMPLOYEE", font=('times new roman', 25, 'bold'),padx=527, pady=2, bd=5, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=50, pady=20, bd=0, fg="Black", bg="#243e55")
F.place(x=30, y=30, width=1270, height=1800)

label1=Label(F, text="Employee Information", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=450,y=5)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("emp.png"))

# # Create a Label Widget to display the text or Image
# label = Label(F, image = img,width=500,)
# label.pack()


canvas= Canvas(F, width= 500, height= 1000,bg="#243e55",)
canvas.pack()

#Load an image in the script
img= (Image.open("emp.png"))

#Resize the Image using resize method
resized_image= img.resize((500,1000), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)










wrappen.pack(fill='both',expand='yes',)




root.mainloop()