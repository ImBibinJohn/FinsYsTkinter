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

# yyyyy


def selected(event):
    if menu.get() == 'Chart Of Accounts':
        import test
    elif menu.get() == 'Reconcile':
        import reconcile

    else:
        import chart0faccounts


def plus():
    def valueget():
        ac = cm1.get()
        n = e3.get()
        dtype = cmb.get()
        desc = e5.get()
        gtype = cb.get()
        gstval = e6.get()
        d = '''INSERT INTO accounts_1 (acctype,detype,name,description,gst,deftaxcode) 
        VALUES (%s,%s,%s,%s,%s,%s)'''
        cur.execute(d, [(ac), (dtype), (n), (desc), (gtype), (gstval), ])
        mydata.commit()
        print('sucessfully added')
        C.destroy()

    global C
    C = tk.Toplevel(A)
    C.title('account create')
    C.geometry('2000x2000')
    C['bg'] = '#2f516f'

    frame1 = tk.LabelFrame(C, borderwidth=0, bg='#243e54')
    l1 = tk.Label(frame1, text='ACCOUNT CREATE',
                  bg='#243e54', font=('Times New Roman', 30))
    l1.place(relx=0.35, rely=0.1)
    frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    frame2 = tk.Frame(C, bg='#243e54')
    l2 = tk.Label(frame2, text='Account Type', bg='#243e54',
                  font=('times new roman', 14))
    l2.place(relx=0.04, rely=0.05)
    acc = ['Cost of Goods Sold', 'Expenses', 'Other Expense']
    cm1 = ttk.Combobox(frame2, values=acc)
    cm1.current(0)
    cm1.place(relx=0.04, rely=0.15, relwidth=0.4, relheight=0.065)

    l3 = tk.Label(frame2, text='Name', bg='#243e54', font=(
        'times new roman', 14)).place(relx=0.5, rely=0.05)
    e3 = StringVar()
    tk.Entry(frame2, textvariable=e3).place(
        relx=0.5, rely=0.15, relwidth=0.4, relheight=0.065)

    l4 = tk.Label(frame2, text='Detail Type', bg='#243e54', font=(
        'times new roman', 14)).place(relx=0.04, rely=0.25)

    def comboinput():
        cur.execute("SELECT itemname FROM itemmodel")
        val = cur.fetchall()
        for row in val:
            cont.append(row[0])
    cont = []
    comboinput()
    cmb = ttk.Combobox(frame2, values=cont)
    cmb.place(relx=0.04, rely=0.35, relwidth=0.4, relheight=0.065)

    l5 = tk.Label(frame2, text='Description', bg='#243e54', font=(
        'times new roman', 14)).place(relx=0.5, rely=0.25)
    e5 = StringVar()
    tk.Entry(frame2).place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.065)

    message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box = Text(frame2)
    text_box.place(relx=0.04, rely=0.55, relwidth=0.4, relheight=0.2)
    text_box.insert('end', message)
    text_box.config(state='disabled')
    Checkbutton(frame2, text="Is sub-account ", bg='#243e54',
                font=('times new roman', 12)).place(relx=0.5, rely=0.45)
    bal = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
           'Input Credit', 'Deferred Service Tax Input Credit', 'Deferred SGST', 'Deferred VAT Input Credit',
           'GST Refund', 'Inventory Asset', 'Paid Insurance', 'Service Tax Refund', 'TDS Receivable', 'Uncategorised Asset',
           'Accumulated Depreciation', 'Buildings and Improvements', 'Furniture and Equipment', 'Land', 'Leasehold Improvements',
           'CGST Payable', 'CST Payable', 'CST Suspense', 'GST Payable', 'GST Suspense', 'IGST Payable', 'Input CGST', 'Input CGST Tax RCM',
           'Input IGST', 'Input IGST Tax RCM', 'Input Krishi Kalyan Cess', 'Input Krishi Kalyan Cess RCM', 'Input Service Tax',
           'Input Service Tax RCM', 'Input VAT 14%', 'Input VAT 4%', 'Input VAT 5%', 'Krishi Kalyan Cess Payable', 'Krishi Kalyan Cess Suspense',
           'Output CGST', 'Output CGST Tax RCM', 'Output CST 2%', 'Output IGST', 'Output IGST Tax RCM', 'Output Krishi Kalyan Cess',
           'Output Krishi Kalyan Cess DCM', 'Output Service Tax', 'Output Service Tax RCM', 'Output SGST', 'Output SGST Tax RCM',
           'Output VAT 14%', 'Output VAT 4%', 'Output VAT 5%', 'Service Tax Payable', 'Service Tax Suspense', 'SGST Payable', 'Swachh Bharat Cess Payable',
           'TDS Payable', 'VAT Payable', 'VAT Suspense', 'Opening Balance', 'Equity']

    cb = ttk.Combobox(frame2, values=bal)
    cb.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)

    l6 = tk.Label(frame2, text='Default Tax Code', bg='#243e54',
                  font=('times new roman', 14)).place(relx=0.5, rely=0.63)
    val = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
           '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
    e6 = ttk.Combobox(frame2, values=val)
    e6.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.065)

    sub1 = tk.Button(frame2, text='Update', font=15, bg='#2f516f',
                     command=valueget).place(relx=0.45, rely=0.9)
    frame2.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
    C.mainloop()


def main():

    global A, data, menu
    A = tk.Tk()
    A.title('chartofaccounts')
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

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background='silver',
                    foreground='black', fieldbackground='#243e54')
    style.map('Treeview', background=[('selected', 'green')])
    treevv = ttk.Treeview(hd, height=7, columns=(
        1, 2, 3, 4, 5, 6, 7), show='headings')

    treevv.heading(1, text='ID')
    treevv.heading(2, text='NAME')  # headings
    treevv.heading(3, text='TYPE')
    treevv.heading(4, text='DETAIL TYPE')
    treevv.heading(5, text='TAX RATE')
    treevv.heading(6, text='FINSYS AMOUNT')
    treevv.heading(7, text='BANK AMOUNT')
    # treevv.heading7, text='Actions'4

    treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    treevv.column(7, minwidth=30, width=140, anchor=CENTER)

    cur.execute(
        "SELECT id,name,type,detail_type,tax_rate,finsys_amt,bank_amt FROM chartofaccounts")
    val = cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5], x[6]))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    def editcoa():
        def changeedit():

            accounttype = accounttypeinput.get()
            name = nameinput.get()
            detailtype = detailtypeinput.get()
            description = descriptioninput.get()
            subaccount = subaccountinput.get()
            defaulttaxcode = defaulttaxcodeinput.get()
            finsys_amt = balanceinput.get()

           # bn=bm.get()
            print(accounttype, name, detailtype,
                  description, subaccount, defaulttaxcode, b)
            cur.execute("""UPDATE chartofaccounts SET accounttype =%s, name =%s, detailtype =%s, description =%s, subaccount =%s, defaulttaxcode =%s, finsys_amt =%s, WHERE id =%s""",
                        (accounttype, name, detailtype, description, subaccount, defaulttaxcode, finsys_amt, b[0],))
            mydata.commit()
            D.destroy()

        # Get selected item to Edit
        global D, bm
        str = treevv.focus()
        values = treevv.item(str, 'values')
        print(values)
        b = [values[0]]
        cur.execute("SELECT * FROM chartofaccounts WHERE id=%s", (b))
        s = cur.fetchone()
        D = tk.Toplevel(A)
        D.title('Edit COA')
        D.geometry('1500x700')
        mycanvas = tk.Canvas(D, width=1800, height=1200)
        mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        yscrollbar = ttk.Scrollbar(
            D, orient='vertical', command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
            scrollregion=mycanvas.bbox('all')))
        frame = tk.Frame(mycanvas)
        frame['bg'] = '#2f516f'
        mycanvas.create_window((0, 0), window=frame,
                               anchor='nw', width=1500, height=1000)

        # contents frame
        hd1 = tk.Frame(frame)
        hd1['bg'] = '#243e54'
        f2 = font.Font(family='Times New Roman', size=20)  # font

        tk.Label(hd1, text='Account Type', bg='#243e54', font=(
            'times new roman', 14)).place(relx=0.04, rely=0.05)
        # title.grid(row=3,column=2,padx=20,pady=20)
        accounttypeinput = StringVar()
        cm1 = ttk.Combobox(hd1, values=accounttypeinput)
        cm1.insert(1, s[1])
        cm1.place(relx=0.04, rely=0.15, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Name', bg='#243e54', font=(
            'times new roman', 14)).place(relx=0.5, rely=0.05)
        nameinput = StringVar()
        f = tk.Entry(hd1, textvariable=nameinput)
        f.insert(1, s[2])
        f.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Detail Type', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.04, rely=0.25)
        detailtypeinput = StringVar()
        l = tk.Entry(hd1, textvariable=detailtypeinput)
        l.insert(1, s[3])
        l.place(relx=0.68, rely=0.08, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Description', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.5, rely=0.25)
        descriptioninput = StringVar()
        co = tk.Entry(hd1, textvariable=descriptioninput)
        co.insert(1, s[4])
        co.place(relx=0.5, rely=0.35, relwidth=0.4, relheight=0.065)

        message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
        text_box = Text(hd1)
        text_box.place(relx=0.04, rely=0.55, relwidth=0.4, relheight=0.2)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        Checkbutton(hd1, text="Is sub-account ", bg='#243e54',
                    font=('times new roman', 12)).place(relx=0.5, rely=0.45)
        subaccountinput = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
                           'Input Credit', 'Deferred Service Tax Input Credit', 'Deferred SGST', 'Deferred VAT Input Credit',
                           'GST Refund', 'Inventory Asset', 'Paid Insurance', 'Service Tax Refund', 'TDS Receivable', 'Uncategorised Asset',
                           'Accumulated Depreciation', 'Buildings and Improvements', 'Furniture and Equipment', 'Land', 'Leasehold Improvements',
                           'CGST Payable', 'CST Payable', 'CST Suspense', 'GST Payable', 'GST Suspense', 'IGST Payable', 'Input CGST', 'Input CGST Tax RCM',
                           'Input IGST', 'Input IGST Tax RCM', 'Input Krishi Kalyan Cess', 'Input Krishi Kalyan Cess RCM', 'Input Service Tax',
                           'Input Service Tax RCM', 'Input VAT 14%', 'Input VAT 4%', 'Input VAT 5%', 'Krishi Kalyan Cess Payable', 'Krishi Kalyan Cess Suspense',
                           'Output CGST', 'Output CGST Tax RCM', 'Output CST 2%', 'Output IGST', 'Output IGST Tax RCM', 'Output Krishi Kalyan Cess',
                           'Output Krishi Kalyan Cess DCM', 'Output Service Tax', 'Output Service Tax RCM', 'Output SGST', 'Output SGST Tax RCM',
                           'Output VAT 14%', 'Output VAT 4%', 'Output VAT 5%', 'Service Tax Payable', 'Service Tax Suspense', 'SGST Payable', 'Swachh Bharat Cess Payable',
                           'TDS Payable', 'VAT Payable', 'VAT Suspense', 'Opening Balance', 'Equity']

        cb = ttk.Combobox(hd1, values=subaccountinput)
        cb.insert(1, s[5])
        cb.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.5, rely=0.63)
        defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                               '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
        eemail = tk.Entry(hd1, textvariable=defaulttaxcodeinput)
        eemail.insert(1, s[6])
        eemail.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Balance', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.5, rely=0.85)
        balanceinput = StringVar()
        bo = tk.Entry(hd1, textvariable=descriptioninput)
        bo.insert(1, s[7])
        bo.place(relx=0.5, rely=0.90, relwidth=0.4, relheight=0.065)

        sub = tk.Button(hd1, text='SUBMIT', font=15, bg='#243e54',
                        command=changeedit).place(relx=0.5, rely=0.79)

        hd1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.9)

        tk.Frame(frame, bg='#2f516f').place(
            relx=0, rely=0.92, relwidth=1, relheight=0.08)
        D.mainloop()

    def set():
        str = treevv.focus()
        values = treevv.item(str, 'values')
        b = [values[0]]
    edit_btn = Button(hd, text="Edit", command=editcoa)
    edit_btn.place(relx=0.50, rely=0.85, relheight=0.1, relwidth=0.1)

    treevv.bind("<<TreeviewSelect>>")
    A.mainloop()


main()
