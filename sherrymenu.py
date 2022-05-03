from tkinter import *


root=Tk()
menubar=Menu(root)

def call():
    from  finsyssuppliers import sherrymain   
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='Expenses')
expmenu=Menu(menubar)
expmenu.add_command(label='Time Activity')
expmenu.add_command(label='Advance Payment')

filemenu.add_command(label='Suppliers',command=call)
filemenu.add_separator()

menubar.add_cascade(label='Expenses',menu=filemenu)

root.config(menu=menubar)

root.mainloop()