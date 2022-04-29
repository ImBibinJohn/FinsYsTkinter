
import tkinter as tk
from tkinter import LEFT, RIGHT, Canvas, Frame, ttk


addcustomer_form = tk.Tk()
addcustomer_form.geometry("700x500")

wrappen=ttk.LabelFrame(addcustomer_form,width=800,height=800)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))


myframe=Frame(mycanvas)
mycanvas.create_window((0,0),window=myframe,anchor="nw")

wrappen.pack(fill='both',expand='yes',)

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()

invoice_date_lab=tk.Label(myframe,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.pack()
invoice_date_input=tk.Entry(myframe,width=40,bg='#243e55')
invoice_date_input.pack()




addcustomer_form.mainloop()