import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
# import click
# from requests import options


# def selected(event):
#     if menu.get() == 'Expenses':
#         import expenses
#     elif menu.get() == 'Payment':
#         import payment
#     elif menu.get() == 'Debit Note ':
#         import debitnote
#     else:
#         import expensemain
import mysql.connector

my_connect = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="fynsystkinter",
    port="3307"
)
my_conn = my_connect.cursor()


def main():

    global A, data, menu
    A = tk.Tk()
    A.title('Expenses')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'

    # menu = StringVar()
    # menu.set("New Transaction")
    # options = ["Expenses", "Payment", "Debit Note ", "Expenses Main"]
    # drop = OptionMenu(A, menu, *options, command=selected)
    # drop.config(bg='#243e55', fg="white", font=('Arial', 18))
    # drop['menu'].config(bg='#2f516a', fg="white", font=('Arial', 18))
    # drop.place(x=1000, y=110)

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
    # treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    # treevv.column(7, minwidth=30, width=120,anchor=CENTER)

    r_set = my_conn.execute(
        "SELECT 'date','type','payee','tax','amount' FROM expenses")
    i = 0
    for i in r_set:
        for j in range(len(r_set)):
            e = Entry(A, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, r_set[j])
        i = i+1
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
