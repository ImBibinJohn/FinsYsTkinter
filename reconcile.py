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


def time():
    def getdetails():
        Ddate1 = date1.get()
        Ddate2 = date2.get()
        Ddate3 = date3.get()

        Aaccount = account.get()
        Bbeginning_balance = beginning_balance.get()
        Eending_balance = ending_balance.get()
        Sservice_charge = service_charge.get()
        Iinterest_earned = interest_earned.get()
        Eexpense_account = expense_account.get()
        Iincome_account = income_account.get()

        tg = '''INSERT INTO main_account (date1,account,date2,date3,beginning_balance,ending_balance,service_charge,interest_earned,expense_account,income_account) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(tg, [(Ddate1), (Aaccount), (Ddate2), (Ddate3), (Bbeginning_balance), (
            Eending_balance), (Sservice_charge), (Iinterest_earned), (Eexpense_account), (Iincome_account)])

        mydata.commit()
        win.destroy()
    win = tk.Tk()
    win.title('Time Activity')
    win.geometry('1500x1000')
    win['bg'] = '#2f516f'
    f1 = tk.Frame(win, bg='#243e54')
    tk.Label(f1, text='Reconciled', font=('Times New Roman', 30),
             bg='#243e54', fg='#fff').place(relx=0.4, rely=0.1)
    f1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    f2 = tk.Frame(win, bg='#243e54')
    size = (400, 500)

    text1 = font.Font(family='Times New Roman', size=13,)
    text1 = Label(f2, text="Open your statement and we'll get started.",
                  bg='#243e55', fg='#fff', font=text1)
    text1.place(x=390, y=0,)

    text2 = font.Font(family='Times New Roman', size=15,)
    text2 = Label(f2,
                  text="Which account do you want to reconcile?", bg='#243e55', font=text2, fg='#fff')
    text2.place(x=260, y=40,)

    tk.Label(f2, text='Account', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.23, rely=0.15)

    def comboinput1():
        cur.execute("SELECT variable1 FROM accounts")
        val = cur.fetchall()
        for row in val:
            tm.append(row)
    global tm
    tm = ['-----']
    comboinput1()
    account = ttk.Combobox(f2, values=tm)
    account.current(0)
    account.place(relx=0.23, rely=0.21, relwidth=0.48, relheight=0.05)

    text3 = font.Font(family='Times New Roman', size=15,)
    text3 = Label(f2,
                  text="Add the following information", bg='#243e55', font=text3, fg='#fff')
    text3.place(x=250, y=150,)

    tk.Label(f2, text='Begining Balance', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.23, rely=0.35)
    beginning_balance = tk.Entry(f2)
    beginning_balance.place(relx=0.23, rely=0.4, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Ending Balance', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.40, rely=0.34)
    ending_balance = tk.Entry(f2)
    ending_balance.place(relx=0.40, rely=0.4, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Date', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.57, rely=0.34)
    date1 = StringVar()
    DateEntry(f2, textvariable=date1).place(
        relx=0.57, rely=0.4, relwidth=0.14, relheight=0.05)

    text4 = font.Font(family='Times New Roman', size=15,)
    text4 = Label(f2,
                  text="Enter the service charge or interest earned, if necessary", bg='#243e55', font=text4, fg='#fff')
    text4.place(x=250, y=250,)

    tk.Label(f2, text='Date', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.23, rely=0.54)
    date2 = StringVar()
    DateEntry(f2, textvariable=date2).place(
        relx=0.23, rely=0.60, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Service Charge', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.40, rely=0.54)
    service_charge = tk.Entry(f2)
    service_charge.place(relx=0.40, rely=0.6, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Expense Account', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.57, rely=0.55)

    def comboinput2():
        cur.execute("SELECT variable1 FROM expense_account")
        val = cur.fetchall()
        for row in val:
            ym.append(row)
    global ym
    ym = ['-----']
    comboinput2()
    expense_account = ttk.Combobox(f2, values=ym)
    expense_account.current(0)
    expense_account.place(relx=0.57, rely=0.60, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Date', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.23, rely=0.70)
    date3 = StringVar()
    DateEntry(f2, textvariable=date3).place(
        relx=0.23, rely=0.75, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Interest Earned', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.40, rely=0.70)
    interest_earned = tk.Entry(f2)
    interest_earned.place(relx=0.40, rely=0.75, relwidth=0.14, relheight=0.05)

    tk.Label(f2, text='Income Account', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.57, rely=0.70)

    def comboinput3():
        cur.execute("SELECT variable1 FROM income_account")
        val = cur.fetchall()
        for row in val:
            um.append(row)
    global um
    um = ['-----']
    comboinput3()
    income_account = ttk.Combobox(f2, values=um)
    income_account.current(0)
    income_account.place(relx=0.57, rely=0.75, relwidth=0.14, relheight=0.05)

    tk.Button(f2, text='Start Reconciling', font=('times new roman', 16), bg='#2f516f',
              command=getdetails).place(relx=0.37, rely=0.85, relwidth=0.2, relheight=0.05)
    f2.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)
    win.mainloop()


time()
