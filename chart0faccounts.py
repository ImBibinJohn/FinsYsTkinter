

from cgitb import text
from faulthandler import disable
import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
from tkcalendar import DateEntry, Calendar
from tkinter import messagebox
from datetime import datetime, date, timedelta
import datetime as dt
from PIL import Image, ImageTk
# import click
from requests import options
from xml.dom.minicompat import StringTypes

from tkinter import StringVar
import mysql.connector
mydata = mysql.connector.connect(host='localhost', user='root', password='', database='finsysinfox21', port='3307')


cur = mydata.cursor()

# yyyyy


def selected(event):
    if menu.get() == 'Chart Of Accounts':
        import chart0faccounts
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
            
            #data fetched from app1_accountype
            sql="select * from app1_accountype where accountname=%s"
            cur.execute(sql,typelist)
            pro=cur.fetchone()

            sql2="select Pid from producttable where Pname=%s"
            cur.execute(sql2,typelist)
            product_id=cur.fetchone()

            


            # cur.execute("select cid from app1_company where id_id=%s",(uid))
            # cmp1=cur.fetchone()
            detlist=[]
            accname = f.get()
            detail_type = l.get()
            detlist.append(detail_type)
            description = co.get()
            sub_account = cb.get()
            deftaxcode = nb.get()
            finsys_amt = balanceinput.get()
            cmp=cmp1
            asof=asof_input.get()

             #fetch data from app1_accountype
            prosql="select * from app1_accountype where accountname=%s"
            cur.execute(prosql,detlist)
            prodetdata=cur.fetchone()
            


            # fetch data from app1_accounts
            sql3="select *  from app1_accounts "
            cur.execute(sql3)
            accounts_data=cur.fetchall()
            fet_data=[]
           
            for data in accounts_data:
            
                if data[3]==accname and data[1]==type and data[10]==cmp:
                    reda=data
                    fet_data.append(reda)

            # fetch data from app1_accounts1
            sql3="select *  from app1_accounts1 "
            cur.execute(sql3)
            accounts_data=cur.fetchall()
            fet_data1=[]
            for data in accounts_data:

                if data[3]==accname and data[1]==type and data[10]==cmp:
                    reda1=data
                    fet_data1.append(reda1)
            




            if  prodetdata!=None :
                if fet_data!=None or fet_data1!=None:
                    messagebox.showerror('error',f"Account with {accname} already exists. Please provide another name.")
            else:
                sql="INSERT INTO app1_accounts (acctype,detype,name,description,gst,deftaxcode,balance,asof,balfordisp,cid_id,productid_id,proid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
                val=(type,detail_type,accname,description,sub_account,deftaxcode,finsys_amt,asof,finsys_amt,cmp[0],product_id[0],pro[0])
                cur.execute(sql,val)
                mydata.commit()

                # sql1="INSERT INTO app1_accounts1 (detype,balance,cid_id) VALUES(%s,%s,%s)" #adding values into db
                # val1=(detail_type,finsys_amt,cmp[0])
                # cur.execute(sql1,val1)
               


                sql2="INSERT INTO app1_accountype (accountname,accountbal,cid_id) VALUES(%s,%s,%s)" #adding values into db
                val2=(detail_type,finsys_amt,cmp[0])
                cur.execute(sql2,val2)
                mydata.commit()

                cur.execute("select * from app1_accounts1 where name=%s and cid_id=%s ",("Opening Balance Equity",cmp[0]))
                balaceeq=cur.fetchone()
                balance=round(balaceeq[7]+float(finsys_amt),2)

                cur.execute("UPDATE app1_accounts1 SET balance =%s where accounts1id=%s and cid_id=%s",(balance,balaceeq[0],cmp[0]))
                mydata.commit()
                
                messagebox.showinfo(title='Success',message='New Account Added')
                add.destroy()




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


    drop.place(x=1150, y=110)


    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=30)  # font
    lb = tk.Label(head, text='CHART OF ACCOUNTS', bg='#243e54',fg="#fff")
    lb['font'] = f
    lb.place(relx=0.35, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    ff = font.Font(family='Times New Roman', size=15)  # font
    bt1 = tk.Button(hd, text='Run Report',command="",)
    bt2=Button(hd,text="New",command=add_account)
    # bt2 = tk.Button(hd, text='New',command="add_account", bg='#243e54')
    bt3 = tk.Button(hd, text='Import',
                    command="")


    bt1['font'] = ff
    bt2['font'] = ff
    bt3['font'] = ff

    bt1.place(relx=0.65, rely=0.05)
    bt2.place(relx=0.75, rely=0.05)
    bt3.place(relx=0.80, rely=0.05)

    # text1 = font.Font(familyext1 = Label(A, text="Fi='Times New Roman', size=13,)
    # tlter by name",bg='#243e55', fg='#fff', font=text1)
    searchbox=StringVar()
    searchbox_input=Entry(A, text="Search Here",textvariable=searchbox,bg="#2f516f",fg="#fff",width=35)
    searchbox_input.insert(0,"Filter By Name")
    searchbox_input.bind("<KeyRelease>",Searching)
    searchbox_input.place(x=200,y=175,height=40)


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

    treevv.column(1, minwidth=30, width=10, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=40, anchor=CENTER)
    treevv.column(6, minwidth=30, width=60, anchor=CENTER)
    treevv.column(7, minwidth=30, width=60, anchor=CENTER)



    cur.execute(
        "SELECT accounts1id,name,acctype,detype,deftaxcode,balance FROM app1_accounts1")
    val2 = cur.fetchall()
    if val2:
        for x in val2:
            treevv.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5]))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)


    cur.execute(
        "SELECT accountsid,name,acctype,detype,deftaxcode,balance FROM app1_accounts")
    val = cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5]))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)


    

    def editcoa():
        def changeedit():

            type = cm1.get()
            name = f.get()
            detail_type = l.get()
            description = co.get()
            sub_account = cb.get()
            deftaxcode = nb.get()
            finsys_amt = balanceinput.get()

           # bn=bm.get()

            print(b)
            # cur.execute("""UPDATE chartofaccounts SET type =%s, name =%s, detail_type =%s, description =%s, sub_account =%s, deftaxcode =%s, finsys_amt =%s, WHERE id =%s""",
            #            (type, name, detail_type, description, sub_account, deftaxcode, finsys_amt, b[0],))

            cur.execute("""UPDATE app1_accounts SET type =%s, name =%s, detail_type =%s, description =%s, finsys_amt =%s, deftaxcode =%s, sub_account =%s WHERE id =%s""",
                        (type, name, detail_type, description, finsys_amt, deftaxcode, sub_account, b[0],))
            mydata.commit()
            D.destroy()

        # Get selected item to Edit
        global edit, bm,s,accdata
        str = treevv.focus()
        values = treevv.item(str, 'values')
        print(values)
        b = [values[0]]
        n=[values[1]]
        print("b is           ",n[0])
        cur.execute(
            "SELECT name FROM app1_accounts ")

        accdata= cur.fetchall()
    
        for x in accdata:
            
            if values[1] in x:
                cur.execute(
                    "SELECT acctype,name,detype,description,gst,deftaxcode,balance FROM app1_accounts WHERE name=%s", (n))

                s = cur.fetchone()
                print("Edited data is1",s)
                break
            else:
                cur.execute(
                    "SELECT acctype,name,detype,description,gst,deftaxcode,balance FROM app1_accounts1 WHERE name=%s", (n))

                s = cur.fetchone()
                print("Edited data2 is",s)
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
                for x in accdata:
                    print("name in x",x)
                    if name in x:
                        if sub_account==None:
                            cur.execute("UPDATE  app1_accounts SET description=%s,gst=%s,deftaxcode=%s where accountsid=%s",(description,'',deftaxcode, b[0]))

                            mydata.commit()
                            edit.destroy()
                            messagebox.showinfo(title='Success',message='Account updated')
                        else:
                            cur.execute("UPDATE  app1_accounts SET description=%s,gst=%s,deftaxcode=%s where accountsid=%s",(description,sub_account,deftaxcode, b[0]))

                            mydata.commit()
                            edit.destroy()
                            messagebox.showinfo(title='Success',message='Account updated')
                    else:
                        if sub_account==None:
                            cur.execute("UPDATE  app1_accounts1 SET description=%s,gst=%s,deftaxcode=%s,balance=%s where accountsid=%s",(description,'',deftaxcode,finsys_amt, b[0]))

                            mydata.commit()
                            edit.destroy()
                            messagebox.showinfo(title='Success',message='Account updated')
                        else:
                            cur.execute("UPDATE  app1_accounts1 SET description=%s,gst=%s,deftaxcode=%s,balance=%s where accounts1id=%s",(description,sub_account,deftaxcode,finsys_amt, b[0]))

                            mydata.commit()
                            edit.destroy()
                            messagebox.showinfo(title='Success',message='Account updated')
                        
                # # cmp[0],product_id[0],pro[0]
                # # (sql,val)
                
                


        cur.execute('select Pname,Pid from producttable')
        product_data=cur.fetchall()
        cur.execute('select Itemname from itemstable')
        item_data=cur.fetchall()
        print("dataaaaaaaaaa",product_data)

        # global edit, bm
        edit = tk.Toplevel(A)
        edit.title('Edit Account')
        edit.geometry('1300x1000')
        
       
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


        global D
        D.geometry('1500x700')
        mycanvas = tk.Canvas(D, width=1500, height=1200)
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
        typeinput = StringVar()
        cm1 = tk.Entry(hd1, textvariable=typeinput)
        cm1.insert(1, s[1])
        cm1.place(relx=0.04, rely=0.10, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Name', bg='#243e54', font=(
            'times new roman', 14)).place(relx=0.5, rely=0.05)
        nameinput = StringVar()
        f = tk.Entry(hd1, textvariable=nameinput)
        f.insert(1, s[2])
        f.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Detail Type', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.04, rely=0.25)
        detailtypeinput = StringVar()
        l = tk.Entry(hd1, textvariable=detailtypeinput)
        l.insert(1, s[3])
        l.place(relx=0.04, rely=0.30, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Description', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.5, rely=0.25)
        descriptioninput = StringVar()
        co = tk.Entry(hd1, textvariable=descriptioninput)
        #co.insert(1, s[4])
        co.place(relx=0.5, rely=0.30, relwidth=0.4, relheight=0.065)

        message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
        text_box = Text(hd1)
        text_box.place(relx=0.04, rely=0.40, relwidth=0.4, relheight=0.2)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        Checkbutton(hd1, text="", bg='#243e54',
                    font=('times new roman', 12)).place(relx=0.5, rely=0.45)
        tk.Label(hd1, text='Is sub-account', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.52, rely=0.45)
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
        cb.insert(1, s[4])
        cb.place(relx=0.5, rely=0.50, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.5, rely=0.63)
        defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                               '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
        nb = ttk.Combobox(hd1, values=defaulttaxcodeinput)
        nb.insert(1, s[5])
        nb.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Balance', font=('times new roman', 14),
                 bg='#243e54').place(relx=0.05, rely=0.65)
        balanceinput = StringVar()
        bo = tk.Entry(hd1, textvariable=balanceinput)
        bo.insert(1, s[6])
        bo.place(relx=0.05, rely=0.70, relwidth=0.4, relheight=0.065)

        sub = tk.Button(hd1, text='SUBMIT', font=15, bg='#243e54',
                        command=changeedit).place(relx=0.5, rely=0.79)

        hd1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.9)

        tk.Frame(frame, bg='#2f516f').place(
            relx=0, rely=0.92, relwidth=1, relheight=0.08)
        D.mainloop()

    def accrecivabales():

        str = treevv.focus()
        values = treevv.item(str, 'values')
        print(values)
        b = [values[0]]

        prlframe=Toplevel(A)
        prlframe.title('Account Receivables')
        prlframe.geometry('2000x2000')
        #dash['bg'] = '#2f516f'
        cid=10
        mycanvas=tk.Canvas(prlframe,width=1800,height=1200)
        mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(prlframe,orient='vertical',command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT,fill=Y)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        profitlossframe=tk.Frame(mycanvas)
        profitlossframe['bg']='#2f516f'
        mycanvas.create_window((0,0),window=profitlossframe,anchor='nw',width=1500,height=2200)

        pframe=tk.Frame(profitlossframe,bg='#243e54',width=2000)
        tk.Label(pframe,text=values[1]+" REPORT",font=('Times New Roman',30),bg='#243e54',fg="#fff").place(relx=0.4,rely=0.05)
        pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

        form_frame=tk.Frame(profitlossframe,bg='#243e54')


        def menuuu(e):
            global dte,dtee,fromdate,todate
            toda = date.today()
            tod = toda.strftime("%Y-%m-%d")
            dropp=drop.get()
            if dropp=='Custom':            
                tk.Label(form_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.45,rely=0.1)
                dte=StringVar()
                DateEntry(form_frame,textvariable=dte,date_pattern='y-mm-dd').place(relx=0.45,rely=0.23,relwidth=0.2,relheight=0.15)
                tk.Label(form_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.70,rely=0.1)
                dtee=StringVar()
                DateEntry(form_frame,textvariable=dtee,date_pattern='y-mm-dd').place(relx=0.70,rely=0.23,relwidth=0.2,relheight=0.15)
            elif dropp=='Today':
                fromdate = tod
                todate = tod 
            elif dropp=='This month':
                fromdate = toda.strftime("%Y-%m-01")
                todate = toda.strftime("%Y-%m-31")
            elif dropp=='This financial year':
                if int(toda.strftime("%m")) >= 1 and int(toda.strftime("%m")) <= 3:
                    pyear = int(toda.strftime("%Y")) - 1
                    fromdate = f'{pyear}-03-01'
                    todate = f'{toda.strftime("%Y")}-03-31'
                else:
                    pyear = int(toda.strftime("%Y")) + 1
                    fromdate = f'{toda.strftime("%Y")}-03-01'
                    todate = f'{pyear}-03-31'
        tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
        options=["All dates", "Custom","Today","This month","This financial year"]
        drop= ttk.Combobox(form_frame,values=options,font=16)
        drop.current(0)
        drop.bind('<<ComboboxSelected>>',menuuu)
        drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
        #buttons
        def cleartree():#to clear treeview
            for item in treevvv.get_children():
                treevvv.delete(item) 
        def accrecifetch():
            period=drop.get()
            if period=='All dates':
                cleartree()
                accrevalldates()  
            elif period=='Today':
                cleartree()
                accrevtoday() 
            elif period=='Custom':
                global fromdate,todate
                fromdate=dte.get()
                todate=dtee.get()
                cleartree()
                customvalues()   
            elif period=='This month':
                cleartree()
                customvalues()    
            elif period=='This financial year':
                cleartree()
                customvalues()      
        tk.Button(form_frame,text = "Run Report",font=('times new roman', 16, 'bold'),command="").place(relx=0.55,rely=0.5,relwidth=0.15)
        tk.Button(form_frame,text = "Back",font=('times new roman', 16, 'bold'),command=main).place(relx=0.75,rely=0.5,relwidth=0.15)
        form_frame.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.1)

        # b = treevv.item(treevv.focus())["values"][0]
        # print(b)
        # sql='SELECT * FROM qualitycertificate WHERE cid=%s'
        # val=(b,)
        # cur.execute(sql,val)
        # s = cur.fetchone()
        # D = tk.Toplevel(A)
        # print(s)
           
        # F2 = LabelFrame(form_frame, font=('times new roman', 15, ),border=0, fg="Black", bg="#e5e9ec")
        # F2.place(x=0, y=10, width=800, height=200)
        # size=(800,210)

        # ax=ImageTk.PhotoImage(Image.open('f2.png').resize(size))
           
        # tk.Label(F2,image=ax,bg='#e5e9ec', border=0).place(relx=0.00,rely=-0,relheight=1,relwidth=1 )
            
        # tk.Label(form_frame, text="Assets", bg='#fff',fg='#000').place(relx=0.03,rely=-0,relheight=1,relwidth=1 )
        # tk.Label(form_frame, text="Current Assets", bg='#fff',fg='#000').place(relx=0.04,rely=-0,relheight=1,relwidth=1 )
        # tk.Label(form_frame, text="Bank", bg='#fff',fg='#000').place(relx=0.05,rely=-0,relheight=1,relwidth=1 )
        # tk.Label(form_frame, text="Account Receivables(Debtors)", bg='#fff',fg='#000').place(relx=0.06,rely=-0,relheight=1,relwidth=1 )

        # datel = Label(form_frame, text="Account Receivables(Debtors)", bg='#fff',fg='#000')
        # datel.place(x=200, y=190, width=100)
        # datel_input = StringVar()
        # datel_input = Entry(form_frame, width=25, bg="#fff",fg='#000')
        # datel_input.place(x=350, y=190, height=40)
        # try:
        #     datel_input.insert(0, s[1])
        # except:
        #      pass
        
        # skul = Label(form_frame, text="Total Account Receivables(Debtors)", bg='#fff',fg='#000')
        # skul.place(x=200, y=240, width=100)
        # skul_input = StringVar()
        # skul_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
        # skul_input.place(x=350, y=240, height=40)
        # try:
        #         skul_input.insert(0, s[3])
        # except:
        #         pass

        # proname = Label(form_frame, text="Total Current Assets", bg='#fff', fg='#000')
        # proname.place(x=200, y=290, width=100)
        # proname_input = StringVar()
        # proname_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
        # proname_input.place(x=350, y=290, height=40)
        # try:
        #     proname_input.insert(0, s[2])
        # except:
        #     pass
            
        # idl = Label(form_frame, text="Total Assets", bg='#fff', fg='#000')
        # idl.place(x=200, y=340, width=100)
        # idl_input = StringVar()
        # idl_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
        # idl_input.place(x=350, y=340, height=40)
        # try:
        #         idl_input.insert(0, s[0])
        # except:
        #         pass
        
        # tk.Label(form_frame, text="Liabilities and Equity", bg='#fff',fg='#000').place(relx=0.06,rely=-0,relheight=1,relwidth=1 )
        # tk.Label(form_frame, text="Current Liabilities", bg='#fff',fg='#000').place(relx=0.06,rely=-0,relheight=1,relwidth=1 )
        # tk.Label(form_frame, text="Accounts Payable(Creditors)", bg='#fff',fg='#000').place(relx=0.06,rely=-0,relheight=1,relwidth=1 )

        
        # cusname = tk.Label(form_frame, text="Total Accounts Payable(Creditors)", bg='#fff', fg='#000')
        # cusname.place(x=200, y=390, height=15, width=100)
        # cusname_input = StringVar()
        # cusname_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
        # cusname_input.place(x=350, y=390, height=40)
        # try:
        #         cusname_input.insert(0, s[4])
        # except:
        #         pass

        # insdate = tk.Label(
        #         form_frame, text="Total Current Liabilities", bg='#fff', fg='#000')
        # place_input = StringVar()
        # insdate.place(x=200, y=440, height=15, width=100)
        # insdate_input = Entry(form_frame, width=25, bg="#fff",fg='#000')
        # insdate_input.place(x=350, y=440, height=40)
        # try:
        #         insdate_input.insert(0, s[5])
        # except:
        #         pass
        
        # tk.Label(form_frame, text="Equity", bg='#fff',fg='#000').place(relx=0.06,rely=-0,relheight=1,relwidth=1 )

        # refl = Label(form_frame, text="Profit for the Year", bg='#fff',fg='#000', font=('times new roman',16,'bold'))
        # refl.place(x=200, y=490, width=160)
        # ref_input = StringVar()
        # ref1_input = Entry(form_frame, width=5, bg='#fff', fg='#000')
        # ref1_input.place(x=350, y=490, height=40)
 
        # try:
        #         ref1_input.insert(0, s[3])
        # except:
        #         pass
            
        # refl1 = Label(form_frame, text="Total Equity", bg='#fff',fg='#000', font=('times new roman',16,'bold'))
        # refl1.place(x=200, y=540, width=160)
        # ref1_input = StringVar()
        # ref11_input = Entry(form_frame, width=5, bg='#fff', fg='#000')
        # ref11_input.place(x=350, y=540, height=40)
 
        # try:
        #         ref1_input.insert(0, s[3])
        # except:
        #         pass
    
        # refl2 = Label(form_frame, text="Total Liabilities and Equity", bg='#fff',fg='#000', font=('times new roman',16,'bold'))
        # refl2.place(x=200, y=590, width=160)
        # ref1_input = StringVar()
        # ref12_input = Entry(form_frame, width=5, bg='#fff', fg='#000')
        # ref12_input.place(x=350, y=590, height=40)
 
        # try:
        #         ref1_input.insert(0, s[3])
        # except:
        #         pass
            
            
        # D.mainloop()


        tableframe=tk.Frame(profitlossframe,bg='#243e54')
        tableframe.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.75)

        #image
        # imageframe=tk.Frame(tableframe,bg='#add8e6')
        # size=(200,200)
        # cc='kijuk tech'
        # cur.execute("SELECT cimg,cname FROM app1_company WHERE cname =%s and cid =%s",([cc,cid]))
        # image=cur.fetchone()
        # img=image[0]
        # print("img",img)
        # cv=Image.open(img).resize(size)
        # ax=ImageTk.PhotoImage(cv,master=prlframe)
        # ay=tk.Label(imageframe,image=ax,bg='#243e54')
        # ay.place(relx=0.02,rely=0.08,relheight=0.8,relwidth=0.2)
        # tk.Label(imageframe,text=image[1], font=('times new roman', 25, 'bold'),bg="#add8e6").place(relx=0.25,rely=0.4,relwidth=0.2)
        # imageframe.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.15)
        #contents
        conttframe=tk.Frame(tableframe,bg='#fff')
        conttframe.place(relx=0.025,rely=0.07,relwidth=0.95,relheight=0.6)
        mycanvass=tk.Canvas(conttframe,width=1200,height=800)
        mycanvass.place(relx=1,rely=1,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(conttframe,orient='vertical',command=mycanvass.yview)
        yscrollbar.pack(side=RIGHT,fill=Y)
        mycanvass.configure(yscrollcommand=yscrollbar.set)
        mycanvass.bind('<Configure>',lambda e:mycanvass.configure(scrollregion=mycanvass.bbox('all')))
        contframe=tk.Frame(mycanvass)
        contframe['bg']='white'
        mycanvass.create_window((0,0),window=contframe,anchor='nw',width=1100,height=2200)
        #table view
        style=ttk.Style()
        style.theme_use('default')
        style.configure('Treeview',background='silver',foreground='#000',fieldbackground='white')
        treevvv = ttk.Treeview(conttframe, height=10, columns=(1,2,3,4,5,6,7), show='headings') 
        treevvv.heading(1, text='Date')
        treevvv.heading(2, text='TRANSACTION TYPE')#headings
        treevvv.heading(3, text='NO')
        treevvv.heading(4, text='NAME')
        treevvv.heading(5, text='ACCOUNT')
        treevvv.heading(6, text='CLR')
        treevvv.heading(7, text='AMOUNT')
        

        treevvv.column(1, minwidth=10, width=120,anchor=CENTER)#coloumns
        treevvv.column(2, minwidth=30, width=130,anchor=CENTER)
        treevvv.column(3, minwidth=30, width=100,anchor=CENTER)
        treevvv.column(4, minwidth=30, width=100,anchor=CENTER)
        treevvv.column(5, minwidth=30, width=200,anchor=CENTER)
        treevvv.column(6, minwidth=30, width=100,anchor=CENTER)
        treevvv.column(7, minwidth=30, width=100,anchor=CENTER)
            
        treevvv.place(relx=0,rely=0,relwidth=1)  
        def accrevalldates():#all dates
            cur.execute( "SELECT accounts1id,name,acctype,detype,deftaxcode,balance,asof FROM app1_accounts1 ")
            val = cur.fetchall()
            try:
                for x in val:
                    treevvv.insert('', 'end', values=(x[8], x[2], 0, x[3], x[1],0,x[9]))
            except:
                pass
            treevvv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
           
           
           
           
        #     cur.execute("SELECT customername, SUM(baldue) FROM app1_invoice WHERE cid=%s GROUP BY customername",([cid]))
        #     vall=cur.fetchall()
        #     trans='Invoice Balance Due'
        #     try:
        #         for i in vall:
        #             treevvv.insert('', 'end',values=(i[0],trans,i[1],0,0,0,0,i[1]))
        #     except:
        #         pass 
        #     transs='Credit Note' 
        #     cur.execute("SELECT customer,SUM(grndtot) FROM app1_credit WHERE cid =%s GROUP BY customer",([cid]))
        #     val=cur.fetchall()   
        #     try:
        #         for j in val:
        #             treevvv.insert('', 'end',values=(j[0],transs,j[1],0,0,0,0,j[1]))
        #     except:
        #         pass          
        # tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
        def accrevtoday():#today values
            cur.execute( "SELECT accounts1id,name,acctype,detype,deftaxcode,balance,asof FROM app1_accounts1 ",(fromdate,cid))
            val = cur.fetchall()
            try:
                for x in val:
                    treevvv.insert('', 'end', values=(x[8], x[2], 0, x[3], x[1],0,x[9]))
            except:
                pass
            treevvv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
           
           
            
            # cur.execute("SELECT customername,SUM(baldue) FROM app1_invoice WHERE invoicedate =%s and cid =%s GROUP BY customername",(fromdate,cid))
            # vall=cur.fetchall()
            # trans='Invoice Balance Due'
            # try:
            #     for i in vall:
            #         treevvv.insert('', 'end',values=(i[0],trans,i[1],0,0,0,0,i[1]))
            # except:
            #     pass 
            # transs='Credit Note' 
            # cur.execute("SELECT customer,SUM(grndtot) FROM app1_credit WHERE creditdate =%s and cid =%s GROUP BY customer",(fromdate,cid))
            # val=cur.fetchall()   
            # try:
            #     for j in val:
            #         treevvv.insert('', 'end',values=(j[0],transs,j[1],0,0,0,0,j[1]))
            # except:
            #     pass 
        def customvalues():#other values
            cur.execute( "SELECT accounts1id,name,acctype,detype,deftaxcode,balance,asof FROM app1_accounts1 ",(fromdate,todate,cid))
            val = cur.fetchall()
            try:
                for x in val:
                    treevvv.insert('', 'end', values=(x[8], x[2], 0, x[3], x[1],0,x[9]))
            except:
                pass
            treevvv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
           
           
            
            
            # cur.execute("SELECT customername,SUM(baldue) FROM app1_invoice WHERE invoicedate BETWEEN %s and %s and cid =%s GROUP BY customername",(fromdate,todate,cid))
            # vall=cur.fetchall()
            # trans='Invoice Balance Due'
            # try:
            #     for i in vall:
            #             treevvv.insert('', 'end',values=(i[0],trans,i[1],0,0,0,0,i[1]))
            # except:
            #     pass  
            # transs='Credit Note' 
            # cur.execute("SELECT customer,SUM(grndtot) FROM app1_credit WHERE creditdate BETWEEN %s and %s and cid =%s GROUP BY customer",(fromdate,todate,cid))
            # val=cur.fetchall()   
            # try:
            #     for j in val:
            #         treevvv.insert('', 'end',values=(j[0],transs,j[1],0,0,0,0,j[1]))
            # except:
            #     pass          
        cur.execute( "SELECT accounts1id,name,acctype,detype,deftaxcode,balance,asof FROM app1_accounts1 ")
        val = cur.fetchall()
        try:
                for x in val:
                    treevv.insert('', 'end', values=(x[8], x[2], 0, x[3], x[1],0,x[9]))
        except:
                pass
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
           
           

# find datas for treeview insertion


        # uid=[4]
        # cur.execute("select cid from app1_company where id_id=%s",(uid))
        # cmp1=cur.fetchone()
        
        # cur.execute("SELECT name FROM app1_accounts ")

        # accdata= cur.fetchall()
    
        # for x in accdata:
        #     if values[1] in x:
        #         pass
        #     else:
        #         cur.execute("select * from app1_accounts1 where accounts1id=%s and cid_id=%s",(b[0],cmp1[0]))
        #         account=cur.fetchone()
        # oplist=['Input CGST', 'Input SGST','Input IGST']
        # oplist2=['Output IGST','Output SGST','Output CGST']
        
        # if account[3] == 'Account Receivable(Debtors)':
        #     cur.execute("select * from app1_invoice where  cid_id=%s",(cmp1))
        #     invoic=cur.fetchall()
        #     cur.execute("select * from app1_credit where  cid_id=%s",(cmp1))
        #     creditnote=cur.fetchall()
        #     cur.execute("select * from app1_payment where  cid_id=%s",(cmp1))
        #     paymen=cur.fetchall()
        #     cur.execute("select * from app1_salesrecpts where  cid_id=%s",(cmp1))
        #     salesofline=cur.fetchall()
        #     trans='Invoice'
        #     accname=account[3]
        #     try:
        #         for i in invoic:
        #             treevvv.insert('', 'end',values=(i[5],trans,i[3],i[1],accname,0,i[17]))
        #     except:
        #         pass
        #     trans='Credit Note'
        #     try:
        #         for i in creditnote:
        #             treevvv.insert('', 'end',values=(i[4],trans,i[5],i[1],accname,0,i[16]))
        #     except:
        #         pass 
        #     trans='Payment'
        #     try:
        #         for i in paymen:
        #             treevvv.insert('', 'end',values=(i[4],trans,i[6],i[1],accname,0,i[14]))
        #     except:
        #         pass 
        #     trans='Sales Receipt'
        #     try:
        #         for i in salesofline:
        #             if i[41]=="True":
        #                 treevvv.insert('', 'end',values=(i[4],trans,i[8],i[1],accname,0,i[19]))
        #     except:
        #         pass 

        # elif account[3] == 'Accounts Payable(Creditors)':
        #     ty='openbalance'
        #     cur.execute("select * from app1_bills where  cid_id=%s and payornot=%s",(cmp1[0],'openbalance'))
        #     bill=cur.fetchall()
        #     ty=''
        #     cur.execute("select * from app1_bills where  cid_id=%s and payornot=%s",(cmp1[0],ty))
        #     bill2=cur.fetchall()
        #     ty='debit'
        #     cur.execute("select * from app1_bills where  cid_id=%s and payornot=%s",(cmp1[0],ty))
        #     bill3=cur.fetchall()
        #     cur.execute("select * from app1_suplrcredit where  cid_id=%s",(cmp1))
        #     debit=cur.fetchall()
        #     cur.execute("select * from app1_expences where  cid_id=%s",(cmp1))
        #     expence=cur.fetchall()
        #     trans='payment'
        #     accname=account[3]
        #     try:
        #         for i in bill:
                    
        #             treevvv.insert('', 'end',values=(i[4],trans,i[6],i[1],accname,0,i[58]))
        #     except:
        #         pass   
        #     try:
        #         for i in bill2:
                    
        #             treevvv.insert('', 'end',values=(i[4],trans,i[6],i[1],accname,0,i[58]))
        #     except:
        #         pass 
        #     trans='bill'
        #     try:
        #         for i in bill3:
                    
        #             treevvv.insert('', 'end',values=(i[4],trans,i[6],i[1],accname,0,i[58]))
        #     except:
        #         pass 
        #     trans='Payment'
        #     try:
        #         for i in debit:
                    
        #             treevvv.insert('', 'end',values=(i[3],trans,i[4],i[1],accname,0,i[54]))
        #     except:
        #         pass 
        #     trans='Expence'
        #     try:
        #         for i in expence:
                    
        #             treevvv.insert('', 'end',values=(i[2],trans,i[4],i[1],accname,0,i[56]))
        #     except:
        #         pass       
            
    
        # elif account[3] in oplist:
        #     global supp
        #     cur.execute("select * from app1_company where  cid=%s",(cmp1))
        #     cmp=cur.fetchone()
        #     cur.execute("select * from app1_suplrcredit where  cid_id=%s",(cmp1))
        #     deb=cur.fetchall()
        #     debit = []
        #     accname=account[3]
        #     for i in deb:
        #         name = i[1]
        #         x = name.split()
        #         if len(x) == 3:
        #             firstname = x[0]
        #             lastname = x[1] + ' ' + x[2]
        #             cur.execute("select * from app1_supplier where firstname=%s and lastname=%s and cid_id=%s",(firstname,lastname,cmp1[0]))
        #             supp=cur.fetchone()
        #         else:
        #             cur.execute("select * from app1_supplier where firstname=%s and lastname=%s and cid_id=%s",(x[0],x[1],cmp1[0]))
        #             supp=cur.fetchone()

        #         if supp[21]==cmp[4]:
        #             debit.append(
        #                 [i[3], i[4], i[1], float(i[54]) / 2])
                    
        #     cur.execute("select * from app1_expences where  cid_id=%s",(cmp1))
        #     expen=cur.fetchall()
        #     expence = []
        #     for i in expen:
        #         name = i[1]
        #         x = name.split()
        #         if len(x) == 3:
        #             firstname = x[0]
        #             lastname = x[1] + ' ' + x[2]
        #             cur.execute("select * from app1_supplier where firstname=%s and lastname=%s and cid_id=%s",(firstname,lastname,cmp1[0]))
        #             supp=cur.fetchone()
        #         else:
        #             cur.execute("select * from app1_supplier where firstname=%s and lastname=%s and cid_id=%s",(x[0],x[1],cmp1[0]))
        #             supp=cur.fetchone()
        #         if supp[21]==cmp[4]:
        #             expence.append([i[2], i[4], (i[1]).replace(
        #                 u'\xa0', u''), float(i[55]) / 2])
        #     trans='Expence'    
        #     try:
        #         for i in expence:
                    
        #             treevvv.insert('', 'end',values=(i[0],trans,i[1],i[2],accname,0,i[3]))
        #     except:
        #         pass 
                
        #     trans='Debit Note'   
        #     try:
        #         for i in debit:
                    
        #             treevvv.insert('', 'end',values=(i[0],trans,i[1],i[2],accname,0,i[3]))
        #     except:
        #         pass 


        # elif account[3] in oplist2:
        #     cur.execute("select * from app1_invoice where cid_id=%s ",(cmp1))
        #     invoi=cur.fetchall()
        #     cur.execute("select * from app1_company where  cid=%s",(cmp1))
        #     cmp=cur.fetchone()
        #     accname=account[3]
        #     invoic = []
        #     for i in invoi:
        #         if i[8] == cmp[4]:
        #             invoic.append(
        #                 [i[5], i[3], (i[1]).replace(u'\xa0', u''), float(i[40]) / 2])
           
        #     cur.execute("select * from app1_credit where cid_id=%s ",(cmp1))
        #     creditnot=cur.fetchall()
        #     creditnote = []
        #     for i in creditnot:
        #         if i[6] == cmp[4]:
        #             creditnote.append(
        #                 [i[4], i[5], (i[1]).replace(u'\xa0', u''), float(i[17]) / 2])
        #     # salesrcpt = salesrecpts.objects.filter(cid=cmp1)
        #     cur.execute("select * from app1_salesrecpts where cid_id=%s ",(cmp1))
        #     salesrcpt=cur.fetchall()
        #     salesrecipt = []
        #     for i in salesrcpt:
        #         if i[6] ==cmp[4]:
        #             salesrecipt.append(
        #                 [i[4], i[5], (i[1]).replace(u'\xa0', u''), float(i[18]) / 2])
        #     trans='Expence'    
        #     try:
        #         for i in invoic:
                    
        #             treevvv.insert('', 'end',values=(i[0],trans,i[1],i[2],accname,0,i[3]))
        #     except:
        #         pass 
                
        #     trans='Debit Note'   
        #     try:
        #         for i in creditnote:
                    
        #             treevvv.insert('', 'end',values=(i[0],trans,i[1],i[2],accname,0,i[3]))
        #     except:
        #         pass    

        #     trans='Debit Note'   
        #     try:
        #         for i in salesrecipt:
                    
        #             treevvv.insert('', 'end',values=(i[0],trans,i[1],i[2],accname,0,i[3]))
        #     except:
        #         pass      
            


    def set():
        str = treevv.focus()
        values = treevv.item(str, 'values')
        b = [values[0]]

    edit_btn = Button(hd, text="Edit", command=editcoa)
    edit_btn.place(relx=0.51, rely=0.85, relheight=0.1, relwidth=0.1)
    runreport_btn = Button(hd, text="Run Report",command=accrecivabales)
    runreport_btn.place(relx=0.40, rely=0.85, relheight=0.1, relwidth=0.1)

    treevv.bind("<<TreeviewSelect>>")
    A.mainloop()


main()