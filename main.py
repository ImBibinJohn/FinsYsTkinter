
from tkinter import *

def invoice():
    
    import invoice
    

window = Tk()
window.geometry('320x150')
menubar = Menu(window)
Sale = Menu(menubar, tearoff=False)
Sale.add_command(label="Invoices", command=invoice)
Sale.add_command(label="Customers", command=invoice)
# Sale.add_command(label="Save", command=invoice)
menubar.add_cascade(label="File", menu=Sale)
window.config(menu=menubar)
window.mainloop() 
