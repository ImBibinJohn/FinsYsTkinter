# import tkinter as tk
# from tkinter import *
# from tkinter import VERTICAL, ttk
# import tkinter.font as font
# from tkcalendar import DateEntry, Calendar


# def main():

#     global A, data
#     A = tk.Tk()
#     A.title('suppliers')
#     A.geometry('1500x1000')
#     A['bg'] = '#2f516f'

#     # head frame
#     head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
#     f = font.Font(family='Times New Roman', size=30)  # font
#     lb = tk.Label(head, text='CHART OF ACCOUNTS', bg='#243e54')
#     lb['font'] = f
#     lb.place(relx=0.3, rely=0.2)
#     head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

#     # contents frame
#     hd = tk.Frame(A, bg='#243e54')
#     hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
#     ff = font.Font(family='Times New Roman', size=15)  # font
#     bt1 = tk.Button(hd, text='Run Report',
#                     command="", bg='#243e54')
#     bt2 = tk.Button(hd, text='New',
#                     command="", bg='#243e54')
#     bt3 = tk.Button(hd, text='Import',
#                     command="", bg='#243e54')
#     bt1['font'] = ff
#     bt2['font'] = ff
#     bt3['font'] = ff
#     bt1.place(relx=0.65, rely=0.05)
#     bt2.place(relx=0.75, rely=0.05)
#     bt3.place(relx=0.80, rely=0.05)
#     text1 = font.Font(family='Times New Roman', size=13,)
#     text1 = Label(A, text="Filter by name",
#                   bg='#243e55', fg='#fff', font=text1)
#     text1.place(x=160, y=170,)

#     # table view

#     treevv = ttk.Treeview(hd, height=7, columns=(
#         1, 2, 3, 4, 5, 6, 7), show='headings')
#     treevv.heading(1, text='NAME')  # headings
#     treevv.heading(2, text='TYPE')
#     treevv.heading(3, text='DETAIL TYPE')
#     treevv.heading(4, text='TAX RATE')
#     treevv.heading(5, text='FINSYS AMOUNT')
#     treevv.heading(6, text='BANK AMOUNT')
#     treevv.heading(7, text='ACTION')
#     #treevv.heading(7, text='Actions')

#     treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
#     treevv.column(2, minwidth=30, width=140, anchor=CENTER)
#     treevv.column(3, minwidth=30, width=140, anchor=CENTER)
#     treevv.column(4, minwidth=30, width=140, anchor=CENTER)
#     treevv.column(5, minwidth=30, width=140, anchor=CENTER)
#     treevv.column(6, minwidth=30, width=140, anchor=CENTER)
#     treevv.column(7, minwidth=30, width=140, anchor=CENTER)
#     #treevv.column(7, minwidth=30, width=120,anchor=CENTER)
#     data = ['Dhyan Kumar', 'Account Receivable(Debtors)', 'Account Receivable(Debtors)',
#             '99120.0', '100000', '']
#     data1 = ['Dhyan Kumar', 'Current Assets', 'Deferred Service Tax Input Credit',
#              '99120.0', '75048.0', '']
#     treevv.insert('', 'end', text=data, values=(data))
#     treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

#     A.mainloop()


# main()



from cgitb import text
from faulthandler import disable
import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
from tkcalendar import DateEntry, Calendar
from tkinter import messagebox
import datetime as dt
# import click
# from requests import options
# from xml.dom.minicompat import StringTypes

from tkinter import StringVar
import mysql.connector
mydata = mysql.connector.connect(

    host='localhost', user='root', password='root', database='finsYs_tkinter')

cur = mydata.cursor()

# yyyyy


def selected(event):
    if menu.get() == 'Chart Of Accounts':
        import test
    elif menu.get() == 'Reconcile':
        import reconcile

    else:
        import chart0faccounts

def add_account():
    
    
    
    def sub_check():
        if sub_account.get()==1:
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
            cb.current(0)
            cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)
        else:
           
            cb = Entry(hd1)

            cb.insert(0, " Deffered CGST")
            cb.config(state='disabled')

            cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)
    def cancel():
        add.destroy()
        

    def save_data():
            typelist=[]
            type = typeinput.get()
            typelist.append(type)
            


            sql="select * from app1_accountype where accountname=%s"
         
            cur.execute(sql,typelist)

            pro=cur.fetchone()


            
            print("(typelist[0](typelist[0]",typelist[0])
            sql2="select Pid from producttable where Pname=%s"
            cur.execute(sql2,typelist)
            product_id=cur.fetchone()




            # cur.execute("select cid from app1_company where id_id=%s",(uid))
            # cmp1=cur.fetchone()

            name = f.get()
            detail_type = l.get()
            description = co.get()
            sub_account = cb.get()
            deftaxcode = nb.get()
            finsys_amt = balanceinput.get()
            cmp=cmp1
            asof=asof_input.get()
            if detail_type in pro:
                messagebox.showerror('error', 'Accept terms and conditions')

            else:
                sql="INSERT INTO app1_accounts (acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,productid_id,proid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
                val=(type,detail_type,name,description,sub_account,deftaxcode,finsys_amt,asof,finsys_amt,cmp[0],product_id[0],pro[0])
                cur.execute(sql,val)


                # sql1="INSERT INTO app1_accounts1 (detype,balance,cid_id) VALUES(%s,%s,%s)" #adding values into db
                # val1=(detail_type,finsys_amt,cmp[0])
                # cur.execute(sql1,val1)
                mydata.commit()
                # D.destroy()
                messagebox.showinfo(title='Success',message='New Account Added')






           
            # cur.execute("""UPDATE chartofaccounts SET type =%s, name =%s, detail_type =%s, description =%s, sub_account =%s, deftaxcode =%s, finsys_amt =%s, WHERE id =%s""",
            #            (type, name, detail_type, description, sub_account, deftaxcode, finsys_amt, b[0],))

            # cur.execute("""UPDATE chartofaccounts SET type =%s, name =%s, detail_type =%s, description =%s, finsys_amt =%s, deftaxcode =%s, sub_account =%s WHERE id =%s""",
            #             (type, name, detail_type, description, finsys_amt, deftaxcode, sub_account, b[0],))
            # mydata.commit()
            # D.destroy()

    cur.execute('select Pname,Pid from producttable')
    product_data=cur.fetchall()
    cur.execute('select Itemname from itemstable')
    item_data=cur.fetchall()
    print("dataaaaaaaaaa",product_data)

    global add, bm
    add = tk.Toplevel(A)
    add.title('Add Account')
    add.geometry('1000x800')
    
    # mycanvas = tk.Canvas(add, width=2000, height=1200)
    # mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    # yscrollbar = ttk.Scrollbar(
    #     add, orient='vertical', command=mycanvas.yview)
    # yscrollbar.pack(side=RIGHT, fill=Y)
    # mycanvas.configure(yscrollcommand=yscrollbar.set)
    # mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
    #     scrollregion=mycanvas.bbox('all')))
    # frame = tk.Frame(mycanvas)
    f2 = font.Font(family='Times New Roman', size=30)
    add['bg'] = '#2f516f'
    
    # mycanvas.create_window((0, 0), window=frame,
    #                         anchor='nw', width=2000, height=1000)

    # # contents frame
    uid=[4]
    cur.execute("select cid from app1_company where id_id=%s",(uid))
    cmp1=cur.fetchone()
    acc_heading= Label(add, text="Account",bd=0,relief="groove",bg='#2f516f',font=f2, fg='#fff',height=2,pady=2,width=100)
    acc_heading.pack()
    hd1 = tk.Frame(add,width=900,height=650)
    hd1['bg'] = '#243e54'
    hd1.place(relx=0.05, rely=0.1)

      # font

    tk.Label(hd1, text='Account Type', bg='#243e54', fg="#fff",font=(
        'times new roman', 14)).place(relx=0.04, rely=0.05)
    typeinput = StringVar()
    cm1 =ttk.Combobox(hd1,textvariable = typeinput)
    value=[]
    for pro_data in product_data:
        value.append(pro_data[0])
        cm1['values']=value
    cm1.place(relx=0.04, rely=0.10, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Name', bg='#243e54', fg="#fff",font=(
        'times new roman', 14)).place(relx=0.5, rely=0.05)
    nameinput = StringVar()
    f = tk.Entry(hd1, textvariable=nameinput,bg="#3E505C",fg="#fff")
 
    f.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Detail Type',fg="#fff", font=('times new roman', 14),
                bg='#243e54').place(relx=0.04, rely=0.2)
    detailtypeinput = StringVar()
    l =ttk.Combobox(hd1,textvariable = detailtypeinput)
    itemvalue=[]
    for it_data in item_data:
        itemvalue.append(it_data)
        l['values']=itemvalue
   
    l.place(relx=0.04, rely=0.25, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Description',fg="#fff", font=('times new roman', 14),
                bg='#243e54').place(relx=0.5, rely=0.2)
    descriptioninput = StringVar()
    co = tk.Entry(hd1, textvariable=descriptioninput,bg="#3E505C",fg="#fff")
    #co.insert(1, s[4])
    co.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.065)

    message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box = Text(hd1,bg="#3E505C",fg="#fff")
    text_box.place(relx=0.04, rely=0.35, relwidth=0.4, relheight=0.4)
    text_box.insert('end', message)
    text_box.config(state='disabled')
    sub_account= IntVar()
    sub_account_input=Checkbutton(hd1,onvalue=1, offvalue = 0 ,variable = sub_account, bg='#243e54',command=sub_check).place(relx=0.5, rely=0.35)
   

    tk.Label(hd1, text='Is sub-account', fg="#fff",font=('times new roman', 14),
                bg='#243e54').place(relx=0.55, rely=0.35)
    # subaccountinput="Deffered_CGST"
    
    cb = Entry(hd1,text="Deffered CGST",bg="#3E505C",fg="#fff")
    cb.insert(0, " Deffered CGST")
    # cb.config(state='disabled')

    cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),fg="#fff",
                bg='#243e54').place(relx=0.5, rely=0.5)
    defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                            '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
    nb = ttk.Combobox(hd1, values=defaulttaxcodeinput)
 
    nb.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Balance', font=('times new roman', 14),fg="#fff",
                bg='#243e54').place(relx=0.5, rely=0.65)
    balanceinput = StringVar()
    bo = tk.Entry(hd1, textvariable=balanceinput,bg="#3E505C",fg="#fff")

    bo.place(relx=0.5, rely=0.70, relwidth=0.19, relheight=0.065)

    tk.Label(hd1, text='as of', font=('times new roman', 14),fg="#fff",
                bg='#243e54').place(relx=0.71, rely=0.65)

    date = dt.datetime.now()
    formated_date = f"{date:%Y-%m-%d }"
    asof_input = StringVar()
    asof = tk.Entry(hd1, text=formated_date,textvariable=asof_input,bg="#3E505C",fg="#fff")
    asof.insert(0,formated_date)
    asof.place(relx=0.71, rely=0.70, relwidth=0.19 ,relheight=0.065)
    cancel_butt = tk.Button(hd1, text='Cancel', font=15, bg='#243e54',fg="#fff",
                    command=cancel).place(relx=0.1, rely=0.8)

    sub = tk.Button(hd1, text='SUBMIT', font=15, bg='#243e54',fg="#fff",
                    command=save_data).place(relx=0.2, rely=0.8)

    
    # tk.Frame(add, bg='#2f516f',width=100,height=500).place(x=100,y=92)
    # add.mainloop()











def main():

    def Searching(event):
    # global searchbox_input

        query = searchbox_input.get()
        selections = []
        for child in treevv.get_children():
            if query in treevv.item(child)['values']:   # compare strings in  lower cases.
                print(treevv.item(child)['values'])
                selections.append(child)
        print('search completed')
        treevv.selection_set(selections)







        

    global A, data, menu
    A = tk.Tk()
    A.title('chartofaccounts')

    A.geometry('2000x2000')

    A['bg'] = '#2f516f'

    menu = StringVar()
    menu.set("Chart Type")
    options = ["Chart Of Accounts", "Reconcile"]
    drop = OptionMenu(A, menu, *options, command=selected)
    drop.config(bg='#243e55', fg="white", font=('Arial', 18))
    drop['menu'].config(bg='#2f516a', fg="white", font=('Arial', 18))


    drop.place(x=1400, y=140)


    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=30)  # font
    lb = tk.Label(head, text='CHART OF ACCOUNTS', bg='#243e54',fg="#fff")
    lb['font'] = f
    lb.place(relx=0.3, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    ff = font.Font(family='Times New Roman', size=15)  # font
    bt1 = tk.Button(hd, text='Run Report',command="", bg='#243e54',fg="#fff")
    bt2=Button(hd,text="New",background='#243e55', foreground="white",command=add_account)
    # bt2 = tk.Button(hd, text='New',command="add_account", bg='#243e54')
    bt3 = tk.Button(hd, text='Import',
                    command="", bg='#243e54',fg="#fff")

    bt1['font'] = ff
    bt2['font'] = ff
    bt3['font'] = ff

    bt1.place(relx=0.65, rely=0.05)
    bt2.place(relx=0.75, rely=0.05)
    bt3.place(relx=0.80, rely=0.05)

    # text1 = font.Font(familyext1 = Label(A, text="Fi='Times New Roman', size=13,)
    # tlter by name",bg='#243e55', fg='#fff', font=text1)
    searchbox=StringVar()
    searchbox_input=Entry(A, text="Search Here",textvariable=searchbox,bg="#243e55",fg="#fff",width=35)
    searchbox_input.insert(0,"Filter By Name")
    searchbox_input.bind("<KeyRelease>",Searching)
    searchbox_input.place(x=200,y=220,height=40)

    # searchbox_input.place(relx=0.3, rely=0.3)
    # table view

    style = ttk.Style()
    style.theme_use('default')
    style.configure('Treeview', background='silver',foreground='black', fieldbackground='#243e54')
    style.map('Treeview', background=[('selected', 'green')])
    treevv = ttk.Treeview(hd, height=7, columns=( 1, 2, 3, 4, 5, 6, 7), show='headings')

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
        "SELECT accountsid,name,acctype,detype,deftaxcode,balance FROM app1_accounts")
    val = cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5]))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    def editcoa():
        # def changeedit():

        #     type = cm1.get()
        #     name = f.get()
        #     detail_type = l.get()
        #     description = co.get()
        #     sub_account = cb.get()
        #     deftaxcode = nb.get()
        #     finsys_amt = balanceinput.get()

        #    # bn=bm.get()

        #     print(b)
        #     # cur.execute("""UPDATE chartofaccounts SET type =%s, name =%s, detail_type =%s, description =%s, sub_account =%s, deftaxcode =%s, finsys_amt =%s, WHERE id =%s""",
        #     #            (type, name, detail_type, description, sub_account, deftaxcode, finsys_amt, b[0],))

        #     cur.execute("""UPDATE app1_accounts SET type =%s, name =%s, detail_type =%s, description =%s, finsys_amt =%s, deftaxcode =%s, sub_account =%s WHERE id =%s""",
        #                 (type, name, detail_type, description, finsys_amt, deftaxcode, sub_account, b[0],))
        #     mydata.commit()
        #     D.destroy()

        # Get selected item to Edit
        global edit, bm
        str = treevv.focus()
        values = treevv.item(str, 'values')
        print(values)
        b = [values[0]]
        print("b is           ",b)
        cur.execute(
            "SELECT acctype,name,detype,description,gst,deftaxcode,balance FROM app1_accounts WHERE accountsid=%s", (b))

        s = cur.fetchone()
        print("Edited data is",s)
        
        def sub_check():
            if sub_account.get()==1:
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
                cb.current(0)
                cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)
            else:
            
                cb = Entry(hd1)

                cb.insert(0, " Deffered CGST")
                cb.config(state='disabled')

                cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)

        def changeedit():
                typelist=[]
                type = typeinput.get()
                typelist.append(type)
            

                name = f.get()
                detail_type = l.get()
                description = co.get()
                sub_account = cb.get()
                deftaxcode = nb.get()
                finsys_amt = balanceinput.get()

                cur.execute("UPDATE  app1_accounts SET acctype=%s,detype=%s,name=%s,description=%s,gst=%s,deftaxcode=%s,balance=%s where accountsid=%s",(type,detail_type,name,description,sub_account,deftaxcode,finsys_amt, b[0]))


                # cmp[0],product_id[0],pro[0]
                # (sql,val)
                mydata.commit()
                # D.destroy()
                messagebox.showinfo(title='Success',message='New Account Added')


        cur.execute('select Pname,Pid from producttable')
        product_data=cur.fetchall()
        cur.execute('select Itemname from itemstable')
        item_data=cur.fetchall()
        print("dataaaaaaaaaa",product_data)

        # global edit, bm
        edit = tk.Toplevel(A)
        edit.title('Edit Account')
        edit.geometry('2000x1500')
        
       
        f2 = font.Font(family='Times New Roman', size=30)
        edit['bg'] = '#2f516f'
        
        uid=[4]
        cur.execute("select cid from app1_company where id_id=%s",(uid))
        cmp1=cur.fetchone()
        acc_heading= Label(edit, text="Account",bd=0,relief="groove",bg='#2f516f',font=f2, fg='#fff',height=2,pady=2,width=100)
        acc_heading.pack()
        hd1 = tk.Frame(edit,width=1500,height=600)
        hd1['bg'] = '#243e54'
        hd1.place(relx=0.10, rely=0.1)

        # font

        tk.Label(hd1, text='Account Type', bg='#243e54', fg="#fff",font=(
            'times new roman', 14)).place(relx=0.04, rely=0.05)
        typeinput = StringVar()

        cm1 =ttk.Combobox(hd1,textvariable = typeinput)
        value=[]
        for pro_data in product_data:
            value.append(pro_data[0])
            cm1['values']=value
        cm1.insert(1, s[0])    
        cm1.place(relx=0.04, rely=0.10, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Name', bg='#243e54', fg="#fff",font=(
            'times new roman', 14)).place(relx=0.5, rely=0.05)
        nameinput = StringVar()
        f = tk.Entry(hd1, textvariable=nameinput,bg="#3E505C",fg="#fff")
        f.insert(1, s[1])    

        f.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Detail Type',fg="#fff", font=('times new roman', 14),
                    bg='#243e54').place(relx=0.04, rely=0.2)
        detailtypeinput = StringVar()
        l =ttk.Combobox(hd1,textvariable = detailtypeinput)
        itemvalue=[]
        for it_data in item_data:
            itemvalue.append(it_data)
            l['values']=itemvalue
        l.insert(1, s[2])    

        l.place(relx=0.04, rely=0.25, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Description',fg="#fff", font=('times new roman', 14),
                    bg='#243e54').place(relx=0.5, rely=0.2)
        descriptioninput = StringVar()
        co = tk.Entry(hd1, textvariable=descriptioninput,bg="#3E505C",fg="#fff")
        #co.insert(1, s[4])
        co.insert(1, s[3])    

        co.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.065)

        message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
        text_box = Text(hd1,bg="#3E505C",fg="#fff")
        text_box.place(relx=0.04, rely=0.35, relwidth=0.4, relheight=0.4)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        sub_account= IntVar()
        sub_account_input=Checkbutton(hd1,onvalue=1, offvalue = 0 ,variable = sub_account, bg='#243e54',command=sub_check).place(relx=0.5, rely=0.35)
    

        tk.Label(hd1, text='Is sub-account', fg="#fff",font=('times new roman', 14),
                    bg='#243e54').place(relx=0.55, rely=0.35)
        
        
        cb = Entry(hd1,text="Deffered CGST",bg="#3E505C",fg="#fff")
        cb.insert(0, s[4])
        

        cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),fg="#fff",
                    bg='#243e54').place(relx=0.5, rely=0.5)
        defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                                '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
        nb = ttk.Combobox(hd1, values=defaulttaxcodeinput)
        nb.insert(1, s[5])    

        nb.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Balance', font=('times new roman', 14),fg="#fff",
                    bg='#243e54').place(relx=0.5, rely=0.65)
        balanceinput = StringVar()
        bo = tk.Entry(hd1, textvariable=balanceinput,bg="#3E505C",fg="#fff")
        bo.insert(1, s[6])    

        bo.place(relx=0.5, rely=0.70, relwidth=0.19, relheight=0.065)

       
        sub = tk.Button(hd1, text='Update', font=15, bg='#243e54',fg="#fff",
                        command=changeedit).place(relx=0.4, rely=0.8)

        


































        # D.geometry('1500x700')
        # mycanvas = tk.Canvas(D, width=1500, height=1200)
        # mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        # yscrollbar = ttk.Scrollbar(
        #     D, orient='vertical', command=mycanvas.yview)
        # yscrollbar.pack(side=RIGHT, fill=Y)
        # mycanvas.configure(yscrollcommand=yscrollbar.set)
        # mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
        #     scrollregion=mycanvas.bbox('all')))
        # frame = tk.Frame(mycanvas)
        # frame['bg'] = '#2f516f'
        # mycanvas.create_window((0, 0), window=frame,
        #                        anchor='nw', width=1500, height=1000)

        # # contents frame
        # hd1 = tk.Frame(frame)
        # hd1['bg'] = '#243e54'
        # f2 = font.Font(family='Times New Roman', size=20)  # font

        # tk.Label(hd1, text='Account Type', bg='#243e54', font=(
        #     'times new roman', 14)).place(relx=0.04, rely=0.05)
        # typeinput = StringVar()
        # cm1 = tk.Entry(hd1, textvariable=typeinput)
        # cm1.insert(1, s[1])
        # cm1.place(relx=0.04, rely=0.10, relwidth=0.4, relheight=0.065)

        # tk.Label(hd1, text='Name', bg='#243e54', font=(
        #     'times new roman', 14)).place(relx=0.5, rely=0.05)
        # nameinput = StringVar()
        # f = tk.Entry(hd1, textvariable=nameinput)
        # f.insert(1, s[2])
        # f.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.065)

        # tk.Label(hd1, text='Detail Type', font=('times new roman', 14),
        #          bg='#243e54').place(relx=0.04, rely=0.25)
        # detailtypeinput = StringVar()
        # l = tk.Entry(hd1, textvariable=detailtypeinput)
        # l.insert(1, s[3])
        # l.place(relx=0.04, rely=0.30, relwidth=0.4, relheight=0.065)

        # tk.Label(hd1, text='Description', font=('times new roman', 14),
        #          bg='#243e54').place(relx=0.5, rely=0.25)
        # descriptioninput = StringVar()
        # co = tk.Entry(hd1, textvariable=descriptioninput)
        # #co.insert(1, s[4])
        # co.place(relx=0.5, rely=0.30, relwidth=0.4, relheight=0.065)

        # message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
        # text_box = Text(hd1)
        # text_box.place(relx=0.04, rely=0.40, relwidth=0.4, relheight=0.2)
        # text_box.insert('end', message)
        # text_box.config(state='disabled')
        # Checkbutton(hd1, text="", bg='#243e54',
        #             font=('times new roman', 12)).place(relx=0.5, rely=0.45)
        # tk.Label(hd1, text='Is sub-account', font=('times new roman', 14),
        #          bg='#243e54').place(relx=0.52, rely=0.45)
        # subaccountinput = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
        #                    'Input Credit', 'Deferred Service Tax Input Credit', 'Deferred SGST', 'Deferred VAT Input Credit',
        #                    'GST Refund', 'Inventory Asset', 'Paid Insurance', 'Service Tax Refund', 'TDS Receivable', 'Uncategorised Asset',
        #                    'Accumulated Depreciation', 'Buildings and Improvements', 'Furniture and Equipment', 'Land', 'Leasehold Improvements',
        #                    'CGST Payable', 'CST Payable', 'CST Suspense', 'GST Payable', 'GST Suspense', 'IGST Payable', 'Input CGST', 'Input CGST Tax RCM',
        #                    'Input IGST', 'Input IGST Tax RCM', 'Input Krishi Kalyan Cess', 'Input Krishi Kalyan Cess RCM', 'Input Service Tax',
        #                    'Input Service Tax RCM', 'Input VAT 14%', 'Input VAT 4%', 'Input VAT 5%', 'Krishi Kalyan Cess Payable', 'Krishi Kalyan Cess Suspense',
        #                    'Output CGST', 'Output CGST Tax RCM', 'Output CST 2%', 'Output IGST', 'Output IGST Tax RCM', 'Output Krishi Kalyan Cess',
        #                    'Output Krishi Kalyan Cess DCM', 'Output Service Tax', 'Output Service Tax RCM', 'Output SGST', 'Output SGST Tax RCM',
        #                    'Output VAT 14%', 'Output VAT 4%', 'Output VAT 5%', 'Service Tax Payable', 'Service Tax Suspense', 'SGST Payable', 'Swachh Bharat Cess Payable',
        #                    'TDS Payable', 'VAT Payable', 'VAT Suspense', 'Opening Balance', 'Equity']

        # cb = ttk.Combobox(hd1, values=subaccountinput)
        # cb.insert(1, s[4])
        # cb.place(relx=0.5, rely=0.50, relwidth=0.4, relheight=0.065)

        # tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),
        #          bg='#243e54').place(relx=0.5, rely=0.63)
        # defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
        #                        '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
        # nb = ttk.Combobox(hd1, values=defaulttaxcodeinput)
        # nb.insert(1, s[5])
        # nb.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.065)

        # tk.Label(hd1, text='Balance', font=('times new roman', 14),
        #          bg='#243e54').place(relx=0.05, rely=0.65)
        # balanceinput = StringVar()
        # bo = tk.Entry(hd1, textvariable=balanceinput)
        # bo.insert(1, s[6])
        # bo.place(relx=0.05, rely=0.70, relwidth=0.4, relheight=0.065)

        # sub = tk.Button(hd1, text='SUBMIT', font=15, bg='#243e54',
        #                 command=changeedit).place(relx=0.5, rely=0.79)

        # hd1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.9)

        # tk.Frame(frame, bg='#2f516f').place(
        #     relx=0, rely=0.92, relwidth=1, relheight=0.08)
        # D.mainloop()

    def set():
        str = treevv.focus()
        values = treevv.item(str, 'values')
        b = [values[0]]
    edit_btn = Button(hd, text="Edit", command=editcoa)
    edit_btn.place(relx=0.51, rely=0.85, relheight=0.1, relwidth=0.1)
    runreport_btn = Button(hd, text="Run Report")
    runreport_btn.place(relx=0.40, rely=0.85, relheight=0.1, relwidth=0.1)

    treevv.bind("<<TreeviewSelect>>")
    A.mainloop()


main()