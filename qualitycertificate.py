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



mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
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
    A = tk.Tk()
    A.title('View')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'

    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=25)  # font
    lb = tk.Label(head, text='QUALITY CERTIFICATE', bg="#243e55", height=2,bd=5, relief="groove", font=f, width=106)
    lb['font'] = f
    lb.place(relx=0.05, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.85)
    form2_frame=tk.Frame(hd,bg='#243e54')


    form2_frame.place(relx=0.01,rely=0.075,relwidth=0.8,relheight=0.09)
    
    def addnew():
        def addit():
            global D, qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate
                 
            qc_date = datel_input.get()
            qc_sku = skul_input.get
            qc_pname = proname_input.get()
            qc_customername = cusname_input.get()
            qc_inspdate  = insdate_input.get()
                
                    
            con = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="fynsystkinter", port='3307')
            cur = con.cursor()
            d='''INSERT INTO qualitycertificate(qc_date,qc_sku,qc_pname,qc_custumername,qc_inspdate) VALUES (%s,%s,%s,%s,%s)'''
            cur.execute(d,[(qc_date),(qc_sku),(qc_pname),(qc_customername),(qc_inspdate)])
                    
            con.commit()
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            expense_form.destroy()
            
            # Get selected item to Edit
        D = tk.Toplevel(A)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="Create Quality Certificate", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
        credit_heading.pack(padx=0, pady=0)

            # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
        mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

        datel = Label(form_frame, text="Date", bg='#243e55', fg='#fff')
        datel.place(x=30, y=30,)
        datel_input = StringVar()
        datel_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=datel_input)
        datel_input.place(x=30, y=50, height=40)
        
        
        skul = tk.Label(form_frame, text="SKU Number", bg='#243e55', fg='#fff')
        skul.place(x=300, y=30, height=15, width=80)
        skul_input = StringVar()
        skul_input = Entry(form_frame, width=25, bg='#2f516f', fg='#fff')
        skul_input.place(x=300, y=50, height=40)
        wrappen.pack(fill='both', expand='yes',)

        proname = Label(form_frame, text="Product Name", bg='#243e55', fg='#fff')
        proname.place(x=600, y=30,)
        proname_input = StringVar()
        proname_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        proname_input.place(x=600, y=50, height=40)
        
        
        cusname = tk.Label(form_frame, text="Customer Name", bg='#243e55', fg='#fff')
        cusname.place(x=30, y=100, height=15, width=120)
        cusname_input = StringVar()
        cusname_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        cusname_input.place(x=30, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)


        insdate = tk.Label(form_frame, text="Inspected Date", bg='#243e55', fg='#fff')
        insdate_input = StringVar()
        insdate.place(x=600, y=100, height=15, width=150)
        insdate_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=insdate_input)
        insdate_input.place(x=600, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)

        submit = tk.Button(form_frame, text="Save", command=addit)
        submit.place(x=580, y=400, width=100)

        D.mainloop()


    def viewq():
    # table view
        
        treevv = ttk.Treeview(hd, height=7, columns=(1, 2, 3, 4, 5, 6), show='headings')
        treevv.heading(1, text='ID')  # headings
        treevv.heading(2, text='DATE')  # headings
        treevv.heading(3, text='PRODUCT NAME')
        treevv.heading(4, text='SKU')
        treevv.heading(5, text='NAME')
        treevv.heading(6, text='INSPECTION DATE')
       

        treevv.column(1, minwidth=10, width=40, anchor=CENTER)  # coloumns
        treevv.column(2, minwidth=30, width=140, anchor=CENTER)
        treevv.column(3, minwidth=30, width=140, anchor=CENTER)
        treevv.column(4, minwidth=30, width=140, anchor=CENTER)
        treevv.column(5, minwidth=30, width=140, anchor=CENTER)
        treevv.column(6, minwidth=30, width=140, anchor=CENTER)
       
       
        cur.execute("SELECT cid,qc_date,qc_sku,qc_pname,qc_custumername,qc_inspdate FROM qualitycertificate")
        val = cur.fetchall()
        if val:
            for x in val:
                treevv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4],x[5]))
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

        def editexp():
            def changeedit():

                mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
                cur = mydata.cursor()
                global D, cid,qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate
                    
                qc_date = datel_input.get()
                qc_sku = skul_input.get
                qc_pname = proname_input.get()
                qc_customername = cusname_input.get()
                qc_inspdate   = insdate.get()
                    
            
                print(cid,qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate)

                cur.execute("""UPDATE qualitycertificate SET qc_date =%s, qc_sku =%s, qc_pname =%s, qc_custumername =%s, qc_inspdate =%s  WHERE cid=%s""",[qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate, b])
                mydata.commit()
                MessageBox.showinfo("Insert Status", "Updated Successfully")
                mydata.close()
                expense_form.destroy()

            # Get selected item to Edit

            b = treevv.item(treevv.focus())["values"][0]
            print(b)
            sql='SELECT * FROM qualityinspection WHERE cid=%s'
            val=(b,)
            cur.execute(sql,val)
            s = cur.fetchone()
            D = tk.Toplevel(A)
            print(s)

            mycanvas.configure(yscrollcommand=yscrollbar.set)
            mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

            full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
            mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

            heading_frame = Frame(mycanvas)
            mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
            headingfont = font.Font(family='Times New Roman', size=25,)
            credit_heading = Label(heading_frame, text="Edit Quality Inspection", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
            credit_heading.pack(padx=0, pady=0)

            # form fields
            sub_headingfont = font.Font(family='Times New Roman', size=20,)
            form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
            mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

            datel = Label(form_frame, text="Date", bg='#243e55', fg='#fff')
            datel.place(x=30, y=30,)
            datel_input = StringVar()
            datel_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=datel_input)
            datel_input.place(x=30, y=50, height=40)
            try:
                datel_input.insert(0, s[1])
            except:
                pass
        
        
            skul = tk.Label(form_frame, text="SKU Number", bg='#243e55', fg='#fff')
            skul.place(x=300, y=30, height=15, width=80)
            skul_input = StringVar()
            skul_input = Entry(form_frame, width=25, bg='#2f516f', fg='#fff')
            skul_input.place(x=300, y=50, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                skul_input.insert(0, s[3])
            except:
                pass

            proname = Label(
                form_frame, text="Product Name", bg='#243e55', fg='#fff')
            proname.place(x=600, y=30,)
            proname_input = StringVar()
            proname_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
            proname_input.place(x=600, y=50, height=40)
            try:
                proname_input.insert(0, s[2])
            except:
                pass
            
            idl = Label(
                form_frame, text="ID", bg='#243e55', fg='#fff')
            idl.place(x=1100, y=30,)
            idl_input = StringVar()
            idl_input = Entry(form_frame, width=10, bg='#2f516f', fg='#fff')
            idl_input.place(x=1100, y=50, height=40)
            try:
                idl_input.insert(0, s[0])
            except:
                pass
        
        
            cusname = tk.Label(form_frame, text="Customer Name", bg='#243e55', fg='#fff')
            cusname.place(x=30, y=100, height=15, width=120)
            cusname_input = StringVar()
            cusname_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
            cusname_input.place(x=30, y=130, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                idl_input.insert(0, s[4])
            except:
                pass


            insdate = tk.Label(
                form_frame, text="Inspected Date", bg='#243e55', fg='#fff')
            place_input = StringVar()
            insdate.place(x=600, y=100, height=15, width=150)
            insdate_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=datel_input)
            insdate_input.place(x=600, y=130, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                idl_input.insert(0, s[5])
            except:
                pass

            

            
            
            submit = tk.Button(form_frame, text="Save", command=changeedit)
            submit.place(x=580, y=400, width=100)
            

            D.mainloop()


        def delete():
            # Get selected item to Delete
            selected_item = treevv.selection()[0]
            treevv.delete(selected_item)
            
        def view():
            print("View")

        view_btn = ttk.Button(hd, text="View", command=view)
        view_btn.place(relx=0.2, rely=0.8, relheight=0.1, relwidth=0.1)
        edit_btn = ttk.Button(hd, text="Edit", command=editexp)
        edit_btn.place(relx=0.45, rely=0.8, relheight=0.1, relwidth=0.1)
        del_btn = ttk.Button(hd, text="Delete", command=delete)
        del_btn.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.1)
        
        hd.mainloop()

    tk.Button(form2_frame,text = "ADD",fg="#000",font=('times new roman', 19, 'bold'),command=addnew).place(relx=0.3,rely=0.4,relwidth=0.25)
    tk.Button(form2_frame,text = "VIEW",fg="#000",font=('times new roman', 19, 'bold'),command=viewq).place(relx=0.7,rely=0.4,relwidth=0.25)
    A.mainloop()

main()
