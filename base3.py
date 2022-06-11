from ast import Lambda
from tkinter import *
import tkinter
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter.font import Font
from  tkinter import ttk
from PIL import Image


#create the class
class base:
    def __init__(self,root):
        self.root=root  
        self.root.title('FinsYs')
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        self.root.geometry("%dx%d" %(width,height))
        self.root.configure(bg="#2f516f")
        self.main()
        
    def main(self):
        
        Frame_login=Frame(self.root,bg="#213e57")
        Frame_login.place(x=0,y=0,height=700,width=1365)
        
        lab = Label(Frame_login,bg="#213b52")
        lab.place(x=0,y=0,width=1365,height=160)
        
        btn2=Button(lab,command=self.Register,text="Next >>>",cursor="hand2",font=("times new roman",12,'bold'),fg="white",bg="orangered",bd=0,width=13,height=1)
        btn2.place(x=1210,y=120)
        
        # Load the image
        image=Image.open('logo-icon.png')
        img=image.resize((50, 50))
        my_img1=ImageTk.PhotoImage(img)
        label=Label(lab, image=my_img1,bg="#fff")
        label.place(x=10,y=0)
        
        
        F2 = LabelFrame(lab,text="Fin sYs", font=('times new roman', 18, 'bold'), bd=0, fg="#fff", bg="#213b52")
        F2.place(x=65, y=20, width=100, height=50)
    
        btn = Button(lab,text='Dashboard',bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'),width=13,height=1)
        btn.place(x=10,y=120)
        
        #dropdown
        OptionList = [
        "Online Banking",
        "Offline Banking",
        "Bank Reconcilation"
        ]

        variable = tk.StringVar(lab)
        variable.set('Banking')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=160,y=120)

        2
        OptionList = [
        "Sales Records",
        "Invoices",
        "Customers"
        "Product and Services"
        ]
        variable = tk.StringVar(lab)
        variable.set('Sales')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=310,y=120)
        
        # 3
        OptionList = [
        "Expenses",
        "Suppliers",
        ]
        variable = tk.StringVar(lab)
        variable.set('Expenses')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=460,y=120)

        # 4
        OptionList = [
        "Employee",
        "Payslip"
        ]
        variable = tk.StringVar(lab)
        variable.set('Payroll')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=610,y=120)
        
        # 5
        OptionList = [
        "Profit and loss",
        "Balance sheet",
        "Accounts receivables",
        "Accounts payables"
        ]
        variable = tk.StringVar(lab)
        variable.set('Report')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=760,y=120)

        # 6
        OptionList = [
        "GST",
        "New..."
        ]
        variable = tk.StringVar(lab)
        variable.set('Taxes')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=910,y=120)

        # 7
        OptionList = [
        "Chart of Accounts",
        "Reconcile"
        ]
        variable = tk.StringVar(lab)
        variable.set('Accounting')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=1060,y=120)

        
        
        
        
        
        
    def Register(self):
        
        # Frame_login1=Frame(self.root,bg="white")
        # Frame_login1.place(x=0,y=0,height=700,width=1365)
        
        frame_input3=Frame(self.root,bg="#213e57")
        frame_input3.place(x=0,y=0,height=700,width=1365)
        
        lab = Label(frame_input3,bg="#213b52")
        lab.place(x=0,y=0,width=1365,height=160)
        
        
        
        btn2=Button(lab,command=self.main,text="<<",cursor="hand2",font=("Helvetica",15,'bold'),fg="white",bg="orangered",bd=0,width=5,height=1)
        btn2.place(x=10,y=120)
        
        # 8
        OptionList = [
        "Chart of Accounts",
        "Reconcile"
        ]
        variable = tk.StringVar(lab)
        variable.set('My Accountant')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=90,y=120)

        # 9
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Cash Management')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=270,y=120)
        
        # 10
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Production')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=450,y=120)
        
        # 11
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Quality Management')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=630,y=120)
        
        # 12
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Project Management')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=810,y=120)
        
        # 13
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Usage Decisions')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=990,y=120)
        
        # 14
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Accounts and Payable')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=1170,y=120)
        

        
    # def register(self):
    #     if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
    #         messagebox.showerror("Error","All Fields Are Required",parent=self.root)
    #     elif self.entry2.get()!=self.entry4.get():
    #         messagebox.showerror("Error","password and Confirm Password Should Be Same",parent=self.root)
    #     else:
    #         try:
    #             con=pymysql.connect(host="localhost",user="root",password="",database="finsys_tkinter")
    #             cur=con.cursor()
    #             cur.execute("select * from register where emailid=%s",self.entry3.get()) 
    #             row=cur.fetchone()
    #             if row!=None:
    #                 messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
    #             else:
    #                 cur.execute("insert into register values(%s,%s,%s,%s"),(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get())
    #                 con.commit()
    #                 con.close()
    #                 messagebox.showinfo("Success", "Register Successfull",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
                
    # def appscreen(self):
        
    #     Frame_login=Frame(self.root,bg="white")
    #     Frame_login.place(x=0,y=0,height=700,width=1000)
    #     label1=Label(Frame_login,text="Hi! Welcome To Seek coding", font=("times new roman",32,'bold'),fg="black",bg="white")
    #     label1.place(x=375,y=100)
        
    #     btn2=Button(Frame_login,command=self.loginform,text="Logout",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
    #     btn2.place(x=700,y=20)                                 
        
        

root=Tk()
ob = base(root)
root.mainloop()