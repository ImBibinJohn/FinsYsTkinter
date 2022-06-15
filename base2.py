from tkinter import *
from tkinter.ttk import *
import tkinter as tk

root = tk.Tk()
root.geometry("800x400")

# Create Toolbar
# Toolbar images
img1 = tk.PhotoImage(file = r"default.png")
img2 = tk.PhotoImage(file = r"default.png")
img3 = tk.PhotoImage(file = r"default.png")

toolbar = tk.Frame(root, bd=1, relief=RAISED) 
toolbar.pack(side=TOP, fill=X)

menubtn1 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
text="",image=img1)
menubtn1.pack(side=LEFT, padx=0, pady=0)

menubtn2 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
text="", image=img2)
menubtn2.pack(side=LEFT, padx=0, pady=0)

menubtn3 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
text="", image=img3)
menubtn3.pack(side=LEFT, padx=0, pady=0)

# drop down menubtn1
menu = tk.Menu(menubtn1, tearoff=0)
menubtn1.config(menu=menu)

menu.insert_command(0, label='Submit', command=lambda: 
print('Submit clicked'))
imgvar1 = tk.PhotoImage(file=r'default.png') 
menu.insert_cascade(1, image=imgvar1, command=lambda: print('Im pop out clicked'))

imgvar2 = tk.PhotoImage(file=r'default.png')
menu.insert_cascade(2, image=imgvar2, command=lambda: print('Im pop out clicked'))

imgvar3 = tk.PhotoImage(file=r'default.png')
menu.insert_cascade(3, image=imgvar3, command=lambda: print('Im pop out clicked'))

imgvar4 = tk.PhotoImage(file=r'default.png')
menu.insert_cascade(4, image=imgvar4, command=lambda: print('Im pop out clicked'))
menu.insert_separator(4)

imgvar5 = tk.PhotoImage(file=r'default.png')
menu.insert_cascade(5, image=imgvar5, command=lambda: print('Im pop out clicked'))

root.mainloop()