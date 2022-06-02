from tkinter import *
root=Tk()

root.geometry('500x500')
framee=LabelFrame(root,width=1000,height=50,bg='red')
framee.pack()
drop = ['Expenses','Suppliers']
variable = StringVar(framee)
variable.set("Expenses")
def bn(n):
    v=variable.get()
    if v=='Suppliers':
        import finsyssuppliers
    elif v=='Expenses':
        import advance
opt = OptionMenu(framee,variable,*drop,command=bn)
opt.config(bg='#243e55', fg="white", font=('Arial', 18))

opt['menu'].config(bg='#2f516a', fg="white", font=('Arial', 18))
opt.pack()
root.mainloop()