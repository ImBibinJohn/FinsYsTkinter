import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
from tkcalendar import DateEntry, Calendar

import click
from requests import options
from xml.dom.minicompat import StringTypes

from tkinter import StringVar
import mysql.connector
mydata = mysql.connector.connect(
    host='localhost', user='root', password='', database='finsys_tkinter')
cur = mydata.cursor()


def fetch():
    def getdetails():

        name = timename.get()
        type = timecus.get()
        detail_type = timebill.get()
        tax_rate = timbill.get()
        finsys_amt = time.get()
        bank_amt = hr.get()+':'+min.get()
        endtime = eh.get()+':'+em.get()
        ttime = timeh.get()+':'+timem.get()
        text = timetext.get("1.0", "end")
        tg = '''INSERT INTO chartofaccounts (timdate,timname,timcus,timcheck,timebill,timecheckk,timestart,timeend,tyme,timedes) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(tg, [(date), (name), (cus), (checkbill), (bill),
                    (timecheck), (starttime), (endtime), (ttime), (text)])
        # print(date,name,cus,checkbill,bill,timecheck,starttime,endtime,ttime,text)
        mydata.commit()
        A.destroy()


def selected(event):
    if menu.get() == 'Chart Of Accounts':
        import chart0faccounts
    elif menu.get() == 'Reconcile':
        import reconcile

    else:
        import chart0faccounts


def main():

    global A, data, menu
    A = tk.Tk()
    A.title('suppliers')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'

    menu = StringVar()
    menu.set("Chart Type")
    options = ["Chart Of Accounts", "Reconcile"]
    drop = OptionMenu(A, menu, *options, command=selected)
    drop.config(bg='#243e55', fg="white", font=('Arial', 18))
    drop['menu'].config(bg='#2f516a', fg="white", font=('Arial', 18))

    drop.place(x=1000, y=110)

    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=30)  # font
    lb = tk.Label(head, text='CHART OF ACCOUNTS', bg='#243e54')
    lb['font'] = f
    lb.place(relx=0.3, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    ff = font.Font(family='Times New Roman', size=15)  # font
    bt1 = tk.Button(hd, text='Run Report',
                    command="", bg='#243e54')
    bt2 = tk.Button(hd, text='New',
                    command="", bg='#243e54')
    bt3 = tk.Button(hd, text='Import',
                    command="", bg='#243e54')
    bt1['font'] = ff
    bt2['font'] = ff
    bt3['font'] = ff
    bt1.place(relx=0.65, rely=0.05)
    bt2.place(relx=0.75, rely=0.05)
    bt3.place(relx=0.80, rely=0.05)
    text1 = font.Font(family='Times New Roman', size=13,)
    text1 = Label(A, text="Filter by name",
                  bg='#243e55', fg='#fff', font=text1)
    text1.place(x=160, y=170,)

    # table view

    treevv = ttk.Treeview(hd, height=7, columns=(
        1, 2, 3, 4, 5, 6, 7), show='headings')
    treevv.heading(1, text='NAME')  # headings
    treevv.heading(2, text='TYPE')
    treevv.heading(3, text='DETAIL TYPE')
    treevv.heading(4, text='TAX RATE')
    treevv.heading(5, text='FINSYS AMOUNT')
    treevv.heading(6, text='BANK AMOUNT')
    treevv.heading(7, text='ACTION')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    treevv.column(7, minwidth=30, width=140, anchor=CENTER)
    #treevv.column(7, minwidth=30, width=120,anchor=CENTER)
    data = ['Dhyan Kumar', 'Account Receivable(Debtors)', 'Account Receivable(Debtors)',
            '99120.0', '100000', '']
    data1 = ['Dhyan Kumar', 'Current Assets', 'Deferred Service Tax Input Credit',
             '99120.0', '75048.0', '']
    treevv.insert('', 'end', text=data, values=(data))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    A.mainloop()


main()
