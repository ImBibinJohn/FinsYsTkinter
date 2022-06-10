from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter.font import Font
from PIL import Image,ImageTk
from  tkinter import ttk


root = Tk()
root.title('FinsYs')
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")

h=Scrollbar(root, orient='horizontal')
h.pack(side=BOTTOM, fill='x')

label1 = Label(root,bg="#213b52",)
label1.place(x=0,y=0,width="1355", height="250")


h.config()
h.pack(side=BOTTOM,expand='yes',)


# Load the image
image=Image.open('logo-icon.png')

# Resize the image in the given (width, height)
img=image.resize((50, 50))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(label1, image=my_img,bg="#213b52")
label.place(x=10,y=10)

F2 = LabelFrame(label1,text="Fin sYs", font=('times new roman', 18, 'bold'), bd=0, fg="#fff", bg="#213b52")
F2.place(x=65, y=20, width=100, height=50)

# Load the image
image=Image.open('imgtog.png')
img1=image.resize((40, 40))
my_img1=ImageTk.PhotoImage(img1)
label=Label(label1, image=my_img1,bg="#213b52")
label.place(x=200,y=10)



root.mainloop()