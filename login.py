

from textwrap import fill
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename

from tkinter import *
import tkinter
import PIL
from PIL import Image, ImageTk

from tkinter import messagebox
import mysql.connector
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

#create the class
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1925x2000+0+0")
        self.root.resizable(False,False)
        self.loginform()
        
    def loginform(self):
        
        Frame_login=Frame(self.root,bg="#213e57")
        Frame_login.place(x=0,y=0,height=950,width=950)
        
        label10=Label(Frame_login,text="New here ?",font=('times new roman',25,'bold'),fg="white",bg="#213e57")
        label10.place(x=330,y=40)
        
        label11=Label(Frame_login,text="Join here to start a business with FinsYs!",font=('times new roman',10,'bold'),fg="white",bg="#213e57")
        label11.place(x=290,y=90)
        
        btn2=Button(Frame_login,command=self.Register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="#213e57",bd=0,width=10,height=1)
        btn2.place(x=330,y=120)



        







        def get_svg(svg_file):
            drawing = svg2rlg(svg_file)
            renderPM.drawToFile(drawing, "temp.png",fmt="png")

    
        get_svg("log.svg")

        pimg =PIL.ImageTk.PhotoImage(Image.open("temp.png"))
        # size = img.size
        # frame = tk.Label(Frame_login, image=pimg)
        frame = tk.Canvas(Frame_login, width=800, height=700,background="#213e57")
        frame.place(x=350,y=300)
        frame.create_image(0,0,anchor='nw',image=pimg)
        
        




        # self.img=ImageTk.PhotoImage(Image.open("log.svg").resize(size))
        # self.img=Label(Frame_login,Image=self.img).place(relx=0.00,rely=-0,relheight=1,relwidth=1)
        # size=(500,700)
        # ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
        # Tk.Label(Frame_login,image=ax,bg='#243e54').place(relx=0.00,rely=-0,relheight=1,relwidth=1)
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=950,y=0,height=950,width=950)
        
        # self.img=ImageTk.PhotoImage(file="background2.jpg")
        # img=Label(Frame_login,image=self.img).place(x=0,y=0,width950,height=700)
        
        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=1250,y=200,height=400,width=300)
        
        label1=Label(frame_input,text="Sign in",font=('times in romen',32,'bold'),fg="black",bg="white")
        label1.place(x=75,y=20)
        
        username=Label(frame_input,text="Username",font=('Goudy old style',20),fg="black",bg="white")
        username.place(x=30,y=95)

        
        
        #email_txt
        self.username_txt=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")

        # self.username_txt.image = ImageTk.PhotoImage(Image.open("defaultimage.jpeg"))
        # imageLabel = tk.Label(frame, image=self.username_txt.image,width=80, height=70)
        # imageLabel.pack(side="right", fill="y")




        self.username_txt.place(x=30,y=145,width=270,height=35)
        
        log_password=Label(frame_input,text="Password",font=('Goudy old style',20),fg="black",bg="white")
        log_password.place(x=30,y=190)
        
        self.log_password_entry=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.log_password_entry.place(x=30,y=240,width=270,height=35)
        
        # btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        # btn1.place(x=125,y=300)
        
        btn2=Button(frame_input,text="Login",command=self.login,cursor='hand2',font=('times new roman',15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=80,y=330)
        
        




        # btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        # btn3.place(x=110,y=380)
        
    def login(self):
       
        if self.username_txt.get()=="" or self.log_password_entry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                self.database()
                mycursor.execute('select * from register where username=%s and password =%s',(self.username_txt.get(),self.log_password_entry.get()))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username and password',parent=self.root)
                else:
                    self.appscreen()
                    mycursor.close()
            except Exception as es:
                messagebox.showerror("Error",f'Error Due to : {str(es)}',parent=self.root)
                
                
    def create_canvas(self):
        canvas=Canvas(self,bg="blue",)
        coord=210,10
        arc=canvas.create_arc(coord,start=200,end=50,fill="red")
        canvas.pack()
    def Register(self):
        
        Frame_login1=Frame(self.root,bg="white")
        Frame_login1.place(x=0,y=0,height=950,width=1950)
        
        frame_input2=Frame(self.root,bg="white")
        frame_input2.place(x=200,y=0,height=950,width=950)


        
        label1=Label(frame_input2,text="Sign up",font=('times in roman',32,'bold'),fg="Black",bg="white")
        label1.place(x=45,y=50)
        
        
        # fname_label=Label(frame_input2,text="Firstname",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        # fname_label.place(x=0,y=150)
        
        self.fname_entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.fname_entry.place(x=0,y=190,width=300,height=35)
        self.fname_entry.insert(0,"First Name")
        
        # lname_label=Label(frame_input2,text="Lastname",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        # lname_label.place(x=00,y=250)
        
        self.lname_entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.lname_entry.place(x=0,y=250,width=300,height=35)
        self.lname_entry.insert(0,"Last Name")

        #  email_label=Label(frame_input2,text="Email",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        # email_label.place(x=0,y=450)
        #entry2
        self.email_entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.email_entry.place(x=0,y=300,width=300,height=35)
        self.email_entry.insert(0,"Email")



        # username_label=Label(frame_input2,text="Username",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        # username_label.place(x=300,y=250)
        
        self.username_entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.username_entry.place(x=0,y=350,width=300,height=35)
        self.username_entry.insert(1,"UserName")



        # password_lab=Label(frame_input2,text="Password",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        # password_lab.place(x=0,y=350)
        
        #entry3
        self.password_entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.password_entry.place(x=0,y=400,width=300,height=35)
        self.password_entry.insert(1,"Password")

       
        #entry5
        
        
        
        # cpass_label=Label(frame_input2,text="Confirm Password",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        # cpass_label.place(x=300,y=350)
         #entry-4
        self.cpass_entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.cpass_entry.place(x=00,y=450,width=300,height=35)
        self.cpass_entry.insert(1,"Conform Password")

        btn2=Button(frame_input2,command=lambda:[self.register(),self.company_datails()],text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=80,y=500)
        
        # btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg="white",fg="black",bd=0)
        # btn3.place(x=170,y=500)
        
        
        frame_input3=Frame(self.root,bg="#213e57")
        frame_input3.place(x=950,y=0,height=950,width=975)
        
        label15=Label(frame_input3,text="One of us ?",font=('times new roman',20,'bold'),fg="#fff",bg="#213e57")
        label15.place(x=400,y=120)
        
        label16=Label(frame_input3,text="click here for work with FinsYs.",font=('Goudy old style',14,'bold'),fg="#fff",bg="#213e57")
        label16.place(x=350,y=160)
        
        btn2=Button(frame_input3,command=self.loginform,text="SIGN IN",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=400,y=200)


        def get_svg2(svg_file):

            drawing = svg2rlg(svg_file)
            renderPM.drawToFile(drawing, "temp.png", fmt="PNG")

        get_svg2("register.svg")
        img = Image.open("temp.png")
        pimg = ImageTk.PhotoImage(img)
        # size = img.size
        frame = tk.Canvas(frame_input3, width=800, height=800)
        frame.place(x=0,y=250)
        frame.create_image(0,0,anchor='nw',image=pimg)
        





    def database(self):
        global mydb,mycursor
        mydb=mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='root',
        database='finsYs_tkinter'
        )
        mycursor = mydb.cursor()
        
    def register(self):

        
        if self.fname_entry.get()=="" or self.email_entry.get()=="" or self.lname_entry.get()=="" or self.password_entry.get()=="" or self.username_entry.get()=="" or self.cpass_entry.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.password_entry.get()!=self.cpass_entry.get():
            messagebox.showerror("Error","password and Confirm Password Should Be Same",parent=self.root)
        else:
            try:
                self.database()
                id=[]
                email_id=self.email_entry.get()
                id.append(email_id)
               
                # # con=mysql.connect(host="localhost",user="root",password="root",database="finsYs_tkinter")
                # # cur=con.cursor()
                # # mycursor.execute("select * from register where email=%s",email) 
                # # row=mycursor.fetchone()

                sql='SELECT id FROM register WHERE email=%s'# selecting entire table from db,taking username , nd check the existance
                val=id
                mycursor.execute(sql,id)

                exc_email=mycursor.fetchone()

                if exc_email is not None:
                    messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
                else:

                    sql="INSERT INTO register (first_name,last_name,password,username,email) VALUES(%s,%s,%s,%s,%s)" #adding values into db
                    val=(self.fname_entry.get(),self.lname_entry.get(),self.password_entry.get(),self.username_entry.get(),self.email_entry.get())
                    mycursor.execute(sql,val)
                    # mycursor.execute("insert into register((first_name,last_name,password,username,email) values(%s,%s,%s,%s,%s)",(self.fname_entry.get(),self.lname_entry.get(),self.password_entry.get(),self.username_entry.get(),self.email_entry.get()))
                    # print("hlo")
                    mydb.commit()
                    mycursor.close()
                    # messagebox.showinfo("Success", "Register Successfull",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
                
    def appscreen(self):
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1000)
        label1=Label(Frame_login,text="Hi! Welcome To Seek coding", font=("times new roman",32,'bold'),fg="black",bg="white")
        label1.place(x=375,y=100)
        
        btn2=Button(Frame_login,command=self.loginform,text="Logout",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=700,y=20)   

    def select_file(self):
    
        filename = askopenfilename(filetypes=(("jpg file", "*.jpg"), ("png file ",'*.png'), ("All files", "*.*"),))
        self.file_choose.select_clear()
        self.file_choose.insert(END, filename) # add this


    def company_datails(self):                              
        registeration=Frame(self.root,bg="#2f516a")
        registeration.place(x=0,y=0,height=950,width=1950)
        center_frame = Frame(registeration, padx=10, pady=10,bg="#fff")
        center_frame.place(y=50,x=600,width=800,height=800)
        Label(center_frame, text="We're Happy you're Here!", font=('Times', 30),bg="#fff").place(x=150,y=30)

        self.combany_name = Entry(center_frame, font=('Times', 14))
        self.combany_name.insert(0, 'Combany Name')
        self.combany_name.place(x=30,y=100,height=50,width=700)
        self.combany_address = Entry(center_frame, font=('Times', 14))
        self.combany_address.place(x=30,y=170,height=50,width=700)
        self.combany_address.insert(0, 'Combany Address')
        self.city = Entry(center_frame, font=('Times', 14))
        self.city.place(x=30,y=240,height=50,width=700)
        self.city.insert(0, 'City')

        self.state =ttk.Combobox(center_frame)
        self.state['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")



        self.state.place(x=30,y=310,height=50,width=700)
        self.state.insert(0, 'Choose')
        self.pin = Entry(center_frame, font=('Times', 14))
        self.pin.place(x=30,y=380,height=50,width=700)
        self.pin.insert(0, 'Pincode')
        self.cemail = Entry(center_frame, font=('Times', 14))
        self.cemail.place(x=30,y=450,height=50,width=700)
        self.cemail.insert(0, 'Email')

        self.Phone = Entry(center_frame, font=('Times', 14))
        self.Phone.place(x=30,y=520,height=50,width=700)
        self.Phone.insert(0, 'Phone Numer')

        self.file_choose=Entry(center_frame,font=40)
        self.file_choose.place(x=130,y=590,height=50,width=600)
        self.file_choose.insert(0, 'No file Selected')

        reg_ch = Button(center_frame, width=15, text='Browse...', font=('Times', 14), command=self.select_file)
        reg_ch.place(x=30,y=590,height=50,width=100)
        reg_btn = Button(center_frame, width=15, text='next', command=self.cmp_advce_details,font=('Times', 14), bg='#2f516a',fg='#fff')
        reg_btn.place(x=350,y=680,height=50,width=100)


    def cmp_advce_details(self):
        
        advce_details_frame = Frame(self.root, padx=10, pady=10,bg="#fff")
        advce_details_frame.place(y=50,x=600,width=800,height=800)
        Label(advce_details_frame, text="Let's Start Building Your FinsYs", font=('Times', 30),bg="#fff").place(x=150,y=30)

        self.business_name = Entry(advce_details_frame, font=('Times', 14))
        self.business_name.insert(0, 'Legal Business Name')
        self.business_name.place(x=30,y=100,height=50,width=700)

        self.your_industry=Label(advce_details_frame,text="Your Industry",background="white", foreground="black",font=14)
        self.your_industry.place(x=30,y=170)

        self.your_industry_input =ttk.Combobox(advce_details_frame)
        self.your_industry_input['values']=("Accounting Services" ,"Consultants, doctors, Lawyers and similar","Information Tecnology","Manufacturing","Professional Scientific and Technical Services","Restaurant/Bar and similar","Retail and Smilar","Other Finanacial Services")
        self.your_industry_input.place(x=30,y=200,height=50,width=700)
        self.your_industry_input.current(0)

        self.cmp_type=Label(advce_details_frame,text="Company type",background="white", foreground="black",font=14)
        self.cmp_type.place(x=30,y=270)

        self.cmp_type_input =ttk.Combobox(advce_details_frame)
        self.cmp_type_input['values']=("Private Limited Company" ,"Public Limited Company","Joint-Venture Company","Partnership Firm Company","One Person Company","Branch Office Company","Non Government Organization")
        self.cmp_type_input.place(x=30,y=300,height=50,width=700)
        self.cmp_type_input.current(0)

        self.radio=IntVar()            
        workers= Label(advce_details_frame,text = "Do you have an Accountant, Bookkeeper or Tax Pro ?",font=14,background='#fff') 
        workers.place(x=30,y=370)
        self.yes_input = Radiobutton(advce_details_frame, text="yes", variable=self.radio, value=1,font=14,background='#fff')  
        self.yes_input.place(x=30, y=400)
        self.no_input = Radiobutton(advce_details_frame, text="No", variable=self.radio, value=2,font=14,background='#fff')  

        self.no_input.place(x=130, y=400)

        paid_type=Label(advce_details_frame,text="How do you like to get paid?",background="white", foreground="black",font=14)
        paid_type.place(x=30,y=470)

        self.paid_type_input =ttk.Combobox(advce_details_frame)
        self.paid_type_input['values']=("Cash" ,"Cheque","Credit card/Debit card","Bank Transfer","Paypal/Other service")
        self.paid_type_input.place(x=30,y=500,height=50,width=700)
        self.paid_type_input.current(0)


        pre_btn = Button(advce_details_frame, width=15, text='Previous', font=('Times', 14), command=self.company_datails,bg='#2f516a',fg='#fff')
        pre_btn.place(x=250,y=580,height=50,width=100)
        sub_btn = Button(advce_details_frame, width=15, text='Submit', font=('Times', 14), command=lambda:[self.company_save(),self.loginform()],bg='#2f516a',fg='#fff')
        sub_btn.place(x=400,y=580,height=50,width=100)



    def company_save(self):
        if self.combany_name.get()=="" or self.combany_address.get()=="" or self.city.get()=="" or self.state.get()=="" or self.pin.get()=="" or self.cemail.get()=="" or self.Phone.get()=="" or self.business_name.get()=="" or self.your_industry_input.get()=="" or self.cmp_type_input.get()=="" or self.radio.get()=="" or self.paid_type_input.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
        else:
        
                self.database()
                if self.file_choose.get()!=	'No file Selected':
                    file_data=self.file_choose.get()
                else:
                    file_data='/var/www/python/infox_works/fynsYs-master/media/images/default.png'


                if self.radio.get()==1:
                    preworkers='Yes'
                else:
                    preworkers='No'
                
                


                id=[]
                email_id=self.email_entry.get()
                id.append(email_id)

                sql='SELECT * FROM register WHERE email=%s'# selecting entire table from db,taking username , nd check the existance
                
                mycursor.execute(sql,id)

                user_id=mycursor.fetchone()
                print("emaillllllll",user_id)


                
                sqll="INSERT INTO app1_company (cname,caddress,city,state,pincode,cemail,phone,cimg,bname,industry,ctype,abt,paid,id_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
                val=(self.combany_name.get(),self.combany_address.get(),self.city.get(),self.state.get(),self.pin.get(),self.cemail.get(),self.Phone.get(),file_data,self.business_name.get(),self.your_industry_input.get(),self.cmp_type_input.get(),preworkers,self.paid_type_input.get(),user_id[0])
                mycursor.execute(sqll,val)
                # mycursor.execute("insert into register((first_name,last_name,password,username,email) values(%s,%s,%s,%s,%s)",(self.fname_entry.get(),self.lname_entry.get(),self.password_entry.get(),self.username_entry.get(),self.email_entry.get()))
                # print("hlo")
                mydb.commit()
                mycursor.close()



    def images(self,image_name):
        pass

# class Root:
#     def __init__(self,image_name):
#         root = tk.Tk()
#         img = Image.open(image_name)
#         pimg = ImageTk.PhotoImage(img)
#         size = img.size
#         frame = tk.Canvas(root, width=size[0], height=size[1])
#         frame.pack()
#         frame.create_image(0,0,anchor='nw',image=pimg)
#         root.mainloop()
# root = Root("temp.png")

root=Tk()

ob = Login(root)
root.mainloop()