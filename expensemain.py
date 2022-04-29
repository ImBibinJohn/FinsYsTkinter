import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
# from tkcalendar import DateEntry, Calendar


def main():

    global A, data
    A = tk.Tk()
    A.title('suppliers')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'

    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=30)  # font
    lb = tk.Label(head, text='EXPENSES', bg='#243e54')
    lb['font'] = f
    lb.place(relx=0.4, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    ff = font.Font(family='Times New Roman', size=15)  # font
    bt = tk.Button(hd, text='New Transaction',
                   command="", bg='#243e54')
    bt['font'] = ff
    bt.place(relx=0.85, rely=0.05)

    # table view

    treevv = ttk.Treeview(hd, height=7, columns=(
        1, 2, 3, 4, 5, 6), show='headings')
    treevv.heading(1, text='DATE')  # headings
    treevv.heading(2, text='TYPE')
    treevv.heading(3, text='PAYEE')
    treevv.heading(4, text='TAX')
    treevv.heading(5, text='AMOUNT')
    treevv.heading(6, text='ACTION')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    #treevv.column(7, minwidth=30, width=120,anchor=CENTER)
    data = ['22/03/22', 'Payment', 'Dhyan Kumar',
            '0.0', '100000', '']
    data1 = ['12/04/22', 'Payment', 'Dhyan Kumar',
             '0.0', '300000', '']
    treevv.insert('', 'end', text=data, values=(data))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    def delete():
        # Get selected item to Delete
        selected_item = treevv.selection()[0]
        treevv.delete(selected_item)

    edit_btn = ttk.Button(hd, text="Edit", command='')
    edit_btn.place(relx=0.35, rely=0.8, relheight=0.1, relwidth=0.1)
    del_btn = ttk.Button(hd, text="Delete", command=delete)
    del_btn.place(relx=0.5, rely=0.8, relheight=0.1, relwidth=0.1)
    A.mainloop()


main()
