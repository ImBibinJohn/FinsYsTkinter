import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
import tkinter.messagebox as MessageBox
import click
import mysql.connector 
from tkcalendar import Calendar, DateEntry
import matplotlib.patches
from datetime import datetime, date, timedelta

mydata = mysql.connector.connect(
    host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
cur = mydata.cursor()

expense_form = tk.Tk()
expense_form.title("finsYs")
expense_form.geometry("1500x1000")
expense_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(expense_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')


def main():
        global A

        global data, menu
        A = tk.Tk()
        A.title('View')
        A.geometry('1500x1000')
        A['bg'] = '#2f516f'


        # head frame
        head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
        f = font.Font(family='Times New Roman', size=25)  # font
        lb = tk.Label(head, text='NEW CUSTOMER COMPLAINT', bg="#243e55", height=2,
                    bd=5, relief="groove", font=f, width=106)
        lb['font'] = f
        lb.place(relx=0.05, rely=0.2)
        head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

        # contents frame
        hd = tk.Frame(A, bg='#243e54')
        hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.8)



    
        
        def submit():

                mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
                cur = mydata.cursor()
                global D, cdate, complaint_qty, cdescription
                
                cdate = cdate_input.get()
                complaint_qty = complaintqty_input.get()
                cdescription = cdescription_input.get()
                invoiceno = invoice_input.get()
            

            
                
                
                con = mysql.connect(host="127.0.0.1", user="root",
                            password="", database="fynsystkinter", port='3307')
                cur = con.cursor()
                d='''INSERT INTO customercomplaint(cdate,product_name,invoiceno,skunumber,cdescription,complaint_qty) VALUES (%s,%s,%s,%s,%s,%s)'''
                cur.execute(d,[(cdate),(invoiceno),(cdescription),(complaint_qty)])
                
                con.commit()
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                expense_form.destroy()

        # Get selected item to Edit

   

        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
            scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="New Customer Complaint", fg='#fff',
                               bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
        credit_heading.pack(padx=0, pady=0)

        # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
        mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

        

        cd = Label(
            form_frame, text="Date", bg='#243e55', fg='#fff')
        cd.place(x=530, y=70,)
        cdate_input = StringVar()
        cdate_input = DateEntry(form_frame, width=49, bg="#2f516f", textvariable=cdate_input)
        cdate_input.place(x=530, y=100, height=40)
        

    
        invoice_lab = tk.Label(form_frame, text="Invoice Number", bg='#243e55', fg='#fff')
        invoice_lab.place(x=530, y=160, height=15, width=120)
        place_input = StringVar()
        invoice_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        invoice_input.place(x=530, y=190, height=40)
        wrappen.pack(fill='both', expand='yes',)

        complaint_lab = tk.Label(form_frame, text="Complaint Quantity", bg='#243e55', fg='#fff')
        complaint_lab.place(x=530, y=230, height=15, width=130)
        place_input = StringVar()
        complaintqty_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        complaintqty_input.place(x=530, y=260, height=40)
        wrappen.pack(fill='both', expand='yes',)


    
        cdescription = Label(form_frame, text="Description",
                           bg='#243e55', fg='#fff')
        cdescription.place(x=530, y=310,)
        cdescription_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        cdescription_input.place(x=530, y=330, height=90)
        wrappen.pack(fill='both', expand='yes',)

        

       
        submit = tk.Button(
            form_frame, text="Save", command=submit)
        submit.place(x=700, y=450, width=100)



        A.mainloop()


main()
