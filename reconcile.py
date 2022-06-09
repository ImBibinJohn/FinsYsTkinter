

# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# import tkinter.font as font


# reconcile_form = tk.Tk()
# reconcile_form.title("finsYs")
# reconcile_form.geometry("1000x1000")
# reconcile_form['bg'] = '#2f516a'
# wrappen = ttk.LabelFrame(reconcile_form)
# mycanvas = Canvas(wrappen)
# mycanvas.pack(side=LEFT, fill="both", expand="yes")
# yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
# yscrollbar.pack(side=RIGHT, fill='y')

# mycanvas.configure(yscrollcommand=yscrollbar.set)
# mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
#     scrollregion=mycanvas.bbox('all')))

# full_frame = Frame(mycanvas, width=2000, height=1600, bg='#2f516a')
# mycanvas.create_window((0, 0), window=full_frame, anchor="nw")


# heading_frame = Frame(mycanvas)
# mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
# headingfont = font.Font(family='Times New Roman', size=25,)
# credit_heading = Label(heading_frame, text="RECONCILED", fg='#fff',
#                        bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=75)
# credit_heading.pack(padx=0, pady=0)

# # form fields
# sub_headingfont = font.Font(family='Times New Roman', size=20,)
# form_frame = Frame(mycanvas, width=1600, height=800, bg='#243e55')
# mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

# text1 = font.Font(family='Times New Roman', size=13,)
# text1 = Label(form_frame, text="Open your statement and we'll get started.",
#               bg='#243e55', fg='#fff', font=text1)
# text1.place(x=520, y=0,)

# text2 = font.Font(family='Times New Roman', size=18,)
# text2 = Label(form_frame,
#               text="Which account do you want to reconcile?", bg='#243e55', font=text2, fg='#fff')
# text2.place(x=260, y=80,)


# title_lab = tk.Label(form_frame, text="Account",
#                      bg='#243e55', fg='#fff', font=text1)
# place_input = StringVar()
# drop2 = ttk.Combobox(form_frame, textvariable=place_input)

# drop2['values'] = ("PAYEE1 PAYEE2 PAYEE3 PAYEE4")

# title_lab.place(x=240, y=130, height=15, width=100)
# drop2.place(x=260, y=160, height=40, width=450)
# wrappen.pack(fill='both', expand='yes',)


# text3 = font.Font(family='Times New Roman', size=18,)
# text3 = Label(form_frame,
#               text="Add the following information", bg='#243e55', font=text3, fg='#fff')
# text3.place(x=260, y=240,)


# begining_date = Label(form_frame, text="Begining Balance",
#                       bg='#243e55', fg='#fff', font=text1)
# begining_date.place(x=260, y=280,)
# begining_date_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# begining_date_input.place(x=260, y=310, height=40)

# ending_balance = Label(form_frame, text="Ending Balance",
#                        bg='#243e55', fg='#fff', font=text1)
# ending_balance.place(x=450, y=280,)
# ending_balance_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# ending_balance_input.place(x=450, y=310, height=40)

# ending_date = Label(form_frame, text="Ending Date",
#                     bg='#243e55', fg='#fff', font=text1)
# ending_date.place(x=635, y=280,)
# ending_date_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# ending_date_input.place(x=635, y=310, height=40)


# text4 = font.Font(family='Times New Roman', size=18,)
# text4 = Label(form_frame,
#               text="Enter the service charge or interest earned, if necessary", bg='#243e55', font=text4, fg='#fff')
# text4.place(x=260, y=370,)


# date = Label(form_frame, text="Date",
#              bg='#243e55', fg='#fff', font=text1)
# date.place(x=260, y=420,)
# date_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# date_input.place(x=260, y=450, height=40)

# service_charge = Label(form_frame, text="Service Charge",
#                        bg='#243e55', fg='#fff', font=text1)
# service_charge.place(x=450, y=420,)
# service_charge_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# service_charge_input.place(x=450, y=450, height=40)

# expense_account = Label(form_frame, text="Expense Account",
#                         bg='#243e55', fg='#fff', font=text1)
# expense_account.place(x=635, y=420,)
# expense_account_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# expense_account_input.place(x=635, y=450, height=40)


# date1 = Label(form_frame, text="Date",
#               bg='#243e55', fg='#fff', font=text1)
# date1.place(x=260, y=515,)
# date1_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# date1_input.place(x=260, y=545, height=40)

# interest_earned = Label(form_frame, text="Interest Earned",
#                         bg='#243e55', fg='#fff', font=text1)
# interest_earned.place(x=450, y=515,)
# interest_earned_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# interest_earned_input.place(x=450, y=545, height=40)

# income_account = Label(form_frame, text="Income Account",
#                        bg='#243e55', fg='#fff', font=text1)
# income_account.place(x=635, y=515,)
# income_account_input = Entry(form_frame, width=25, bg='#243e55', fg='#fff')
# income_account_input.place(x=635, y=545, height=40)


# button = tk.Button(form_frame, text="Start Reconciling",)
# button.place(x=490, y=620, width=100)

# reconcile_form.mainloop()






import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
from tkcalendar import DateEntry, Calendar

from tkinter import messagebox


from tkinter import StringVar
import mysql.connector
mydata = mysql.connector.connect(

    host='localhost', user='root', password='root', database='finsYs_tkinter')

cur = mydata.cursor()






def time():
    def show_result():
        messagebox.showinfo('successfull render')
        reconcile=Toplevel(win)
        reconcile.geometry('2000x1000')
        reconcile['bg'] = '#2f516f'
        head_frame = tk.Frame(reconcile, bg='#243e54',height=200,width=1000)
        head_frame.place(relx=0.1, rely=0.05,)
        tk.Label(head_frame, text='Reconciled', font=('Times New Roman', 30),
                bg='#243e54', fg='#fff').place(relx=0.4, rely=0.1)
        tk.Label(head_frame, text='Reconciled', font=('Times New Roman', 30),
                bg='#243e54', fg='#fff').place(relx=0.4, rely=0.3)
        tk.Label(head_frame, text='Reconciled', font=('Times New Roman', 30),
        bg='#243e54', fg='#fff').place(relx=0.4, rely=0.5)
    


    def getdetails():
        Ddate1 = date1.get()
        Ddate2 = date2.get()
        Ddate3 = date3.get()
        acc_list=[]
        Aaccount = selected_account.get()
        acc_list.append(Aaccount)
        print("Aaccount",Aaccount)
        Bbeginning_balance = beginning_balance.get()
        Eending_balance = ending_balance.get()
        Sservice_charge = service_charge.get()
        Iinterest_earned = interest_earned.get()
        Eexpense_account = expense_account.get()
        Iincome_account = income_account.get()

        cur.execute("select * from app1_expenseaccount where account=%s",(acc_list))
        expexists=cur.fetchone()
        if expexists != None:
            exp_id=[expexists[10]]
            cur.execute("select * from app1_incomeaccount where expenceincomeid_id=%s",(exp_id))
            incomeacc=cur.fetchone()
        # incomeacc


        # print("dataaaaaaa",expexists)
        # print(expexists[10])
        # for d in expexists:
        #     print("it iss",d)
        if expexists!= None and expexists[10]==cmp[0] and incomeacc[6]==cmp[0]:
            show_result()

        else:
            cur.execute("select * from app1_accountype where accountname=%s and cid_id=%s",(Aaccount,cmp[0]))
            account_data=cur.fetchone()
            print("account_data",account_data)

        
            #datas added to Expenseaccount
            tg = '''INSERT INTO app1_expenseaccount (enddate,account,dat,begbal,endbal,serchar,expacc,cid_id,expaccountypid_id) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            val=(Ddate1, Aaccount, Ddate2, Bbeginning_balance, Eending_balance, Sservice_charge,Eexpense_account,cmp[0],account_data[0])
            cur.execute(tg,val)
            mydata.commit()
            cur.execute("select * from app1_expenseaccount where cid_id=%s",cmp)
            expense_data=cur.fetchall()
            last_entry=expense_data[-1]
            
            #datas added to income account
            incomesql = '''INSERT INTO app1_incomeaccount (dat1,intear,incacc,cid_id,expenceincomeid_id) 
            VALUES (%s,%s,%s,%s,%s)'''
            val2=(Ddate3, Iinterest_earned, Iincome_account,cmp[0],last_entry[0])
            cur.execute(incomesql,val2)

            mydata.commit()



            messagebox.showinfo('successfull added')
            show_result()
            win.destroy()
    win = tk.Tk()
    win.title('Time Activity')
    win.geometry('2000x1000')
    win['bg'] = '#2f516f'
    f1 = tk.Frame(win, bg='#243e54')
    tk.Label(f1, text='Reconciled', font=('Times New Roman', 30),
             bg='#243e54', fg='#fff').place(relx=0.4, rely=0.1)
    f1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    f2 = tk.Frame(win, bg='#243e54')
    size = (400, 500)

    uid=[4]
    cur.execute("select cid from app1_company where id_id=%s",(uid))
    cmp=cur.fetchone()
   

    text1 = font.Font(family='Times New Roman', size=13,)
    text1 = Label(f2, text="Open your statement and we'll get started.",
                  bg='#243e55', fg='#fff', font=text1)
    text1.place(x=390, y=0,)

    text2 = font.Font(family='Times New Roman', size=20,)
    text2 = Label(f2,
                  text="Which account do you want to reconcile?", bg='#243e55', font=text2, fg='#fff')
    text2.place(x=350, y=60,)

    tk.Label(f2, text='Account', font=('times new roman', 15),
             bg='#243e55', fg='#fff').place(relx=0.23, rely=0.15)

    def comboinput1():
        cur.execute("SELECT accountname FROM app1_accountype")
        val = cur.fetchall()
        for row in val:
            tm.append(row[0])
    global tm
    tm = []
    comboinput1()
    
    selected_account=StringVar()
    account = ttk.Combobox(f2, values=tm,textvariable=selected_account)
    # account.current(0)
    account.place(relx=0.23, rely=0.21, relwidth=0.48, relheight=0.05)

    text3 = font.Font(family='Times New Roman', size=20)
    text3 = Label(f2,
                  text="Add the following information", bg='#243e55', font=text3, fg='#fff')
    text3.place(x=350, y=200,)

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

    text4 = font.Font(family='Times New Roman', size=20,)
    text4 = Label(f2,
                  text="Enter the service charge or interest earned, if necessary", bg='#243e55', font=text4, fg='#fff')
    text4.place(x=350, y=330,)

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

    # def comboinput2():
    #     cur.execute("SELECT variable1 FROM expense_account")
    #     val = cur.fetchall()
    #     for row in val:
    #         ym.append(row)
    # global ym
    # ym = ['-----']
    # comboinput2()
    ym=["expacc","Advertising/Promotional","Bank Charges","Business Licenses and Permits","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expense","Insurance Expense-General Liability Insurance","Insurance Expense-Health Insurance","Insurance Expense-Professional Liability","Interest Expense","Meals and Entertainment","Office Supplies","Postage ang Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintenance","Small Tools and Equipments","Swachh Bharath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expenses","Utilities","Ask My Accountant","CGST write-off","GST write-off","IGST write-off","Miscelleneous Expense","Political Contribution","Reconcilation Discrepancies","SGST write-off","Tax write-off","Vehicle Expenses","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Cedit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Buildings and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input SGST","Input SGST Tax RCM","Input VAT","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Service Tax RCM","Output SGST","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","Service Tax Suspense","SGST Payable","Swachh Bharat Cess Payable","Swachh Bharat Cess Suspense","TDS Payable","VAT Payable","VAT Suspense","Opening Balance Equity","Retained Earnings","Billable Expense Income","Consulting Income","Products Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintenance","Sales Discounts","Sales of Product Income","Uncategorised Income","Cost of Sales","Equipments Rental for Jobs","Freight and Shipping Cost","Merchant Account Fees","Purchase-Hardware for Resale","Purchase-Software for Resale","Sub-contracted Services","Tools and Craft Supplies","Finance Charge Income","Insurance Proceeds Received","Interest Income","Proceeds from Sale of Asset","Shipping and Delivery Income"]





    
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




    um=[ "incacc","Finance Charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale of Asset","Shipping and Delivery Income","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintenance","Sales Discounts","Sales of Product Income","Uncategorised Income","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CSGT Tax RCM","Output CGST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Service Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","Service Tax Suspense","SGST Payable","Swachh Bharat Cess Payable","Swachh Bharat Cess Suspense","TDS Payable","VAT Payable","Retained Earnings","VAT Suspense","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resale","Purchases-Software for Resale","Subcontracted Services","Tools and Craft Supplies","Advertising/Promotional","Bank Charges","Business License and Permits","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expense","Insurance Expense-General Liability Expenses","Insurance Expense-Health Insurance","Insurance Expense-Life and Disability Insurance","Interest Expense","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Rent Expense","Repair and Maintenance","Small Tools and Equipments","Swachh Bharat Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Ask My Accountant","CGST write-off","GST write-off","IGST write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST write-off","Tax write-off","Vehicle Expenses"]

    # def comboinput3():
    #     cur.execute("SELECT variable1 FROM income_account")
    #     val = cur.fetchall()
    #     for row in val:
    #         um.append(row)
    # global um
    # um = ['-----']
    # comboinput3()
    income_account = ttk.Combobox(f2, values=um)
    income_account.current(0)
    income_account.place(relx=0.57, rely=0.75, relwidth=0.14, relheight=0.05)

    tk.Button(f2, text='Start Reconciling', font=('times new roman', 16), bg='#2f516f',
              command=getdetails).place(relx=0.37, rely=0.85, relwidth=0.2, relheight=0.05)
    f2.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)
    win.mainloop()



time()

