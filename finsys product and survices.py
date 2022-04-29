import os
from re import L
import shutil
import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
from tkinter import filedialog
import tkinter.font as font
from turtle import bgcolor
from click import command, style
from regex import P
from tkcalendar import DateEntry,Calendar
from PIL import Image,ImageTk


def upload_file():
        # global filename,img, b2
        f_types =[('Png files','.png'),('Jpg Files', '.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        # shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
        # image = Image.open(filename)
        # resize_image = image.resize((350, 350))
        # img = ImageTk.PhotoImage(resize_image)
        # b2 = Button(imageFrame,image=img)
        # b2.place(x=130, y=80)

def suplus():
    C=tk.Toplevel(B)
    C.title('account create')
    C.geometry('1400x700')
    C['bg'] = '#2f516f'

    frame1 = tk.LabelFrame(C,borderwidth=0,bg='#243e54')
    l1=tk.Label(frame1,text='ACCOUNT CREATE',bg='#243e54',foreground='white',font=('poppins',30))
    l1.place(relx=0.35,rely=0.1)
    frame1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    frame2=tk.Frame(C,bg='#243e54')
    l2=tk.Label(frame2,text='Account Type',bg='#243e54',foreground='white',font=('poppins', 14))
    l2.place(relx=0.04,rely=0.05)
    acc=['Cost of goods sold']
    cm1=ttk.Combobox(frame2,values=acc)
    cm1.current(0)
    cm1.place(relx=0.04,rely=0.15,relwidth=0.4,relheight=0.065)
    
    l3=tk.Label(frame2,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.05)
    e3=tk.Entry(frame2).place(relx=0.5,rely=0.15,relwidth=0.4,relheight=0.065)

    l4=tk.Label(frame2,text='Detail Type',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.04,rely=0.25)
    cont2=['Suppliers and materials cost']
    cmb=ttk.Combobox(frame2,values=cont2).place(relx=0.04,rely=0.35,relwidth=0.4,relheight=0.065)
    
    l5=tk.Label(frame2,text='Description',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.25)
    e5=tk.Entry(frame2).place(relx=0.5,rely=0.35,relwidth=0.4,relheight=0.065)

    message='''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box=Text(frame2)
    text_box.place(relx=0.04,rely=0.55,relwidth=0.4,relheight=0.2)
    text_box.insert('end',message)
    text_box.config(state='disabled')
    Checkbutton(frame2, text = "Is sub-account ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.5,rely=0.45)
    bal=['Deferred CGST','Deferred GST Input Credit','Deferred Krishi Kalyan Cess',
         'Input Credit','Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit',
        'GST Refund','Inventory Asset','Paid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset',
        'Accumulated Depreciation','Buildings and Improvements','Furniture and Equipment','Land','Leasehold Improvements',
        'CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable','Input CGST','Input CGST Tax RCM',
        'Input IGST','Input IGST Tax RCM','Input Krishi Kalyan Cess','Input Krishi Kalyan Cess RCM','Input Service Tax',
        'Input Service Tax RCM','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable','Krishi Kalyan Cess Suspense',
        'Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST','Output IGST Tax RCM','Output Krishi Kalyan Cess',
         'Output Krishi Kalyan Cess DCM','Output Service Tax','Output Service Tax RCM','Output SGST','Output SGST Tax RCM',
        'Output VAT 14%','Output VAT 4%','Output VAT 5%','Service Tax Payable','Service Tax Suspense','SGST Payable','Swachh Bharat Cess Payable',
        'TDS Payable','VAT Payable','VAT Suspense','Opening Balance','Equity']

    cb=ttk.Combobox(frame2,values=bal).place(relx=0.5,rely=0.55,relwidth=0.4,relheight=0.065)
    l6=tk.Label(frame2,text='Default Tax Code',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.63)
  
    val=['18.0% IGST',' 14.00% ST','0% IGST','Out of Scope','0% GST','14.5% ST','14.0% VAT','6.0% IGST','28.0% IGST','15.0% ST','28.0% GST','12.0% GST','18.0% GST',
    '3.0% GST','0.2% IGST','5.0% GST','6.0% GST','0.2% GST','Exempt IGST','3.0% IGST','4.0% VAT','5.0% IGST','12.36% ST','5.0% VAT','Exempt GST','12.0% IGST','2.0% CST']
    e6=ttk.Combobox(frame2,values=val).place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.065)
    sub1=tk.Button(frame2,text='CREATE',font=15,bg='#5193e6',foreground='white').place(relx=0.45,rely=0.9)
    frame2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
    C.mainloop()


def stplus():
    C=tk.Toplevel(B)
    C.title('account create')
    C.geometry('1400x700')
    C['bg'] = '#2f516f'

    frame1 = tk.LabelFrame(C,borderwidth=0,bg='#243e54')
    l1=tk.Label(frame1,text='ACCOUNT CREATE',bg='#243e54',foreground='white',font=('poppins',30))
    l1.place(relx=0.35,rely=0.1)
    frame1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    frame2=tk.Frame(C,bg='#243e54')
    l2=tk.Label(frame2,text='Account Type',bg='#243e54',foreground='white',font=('poppins', 14))
    l2.place(relx=0.04,rely=0.05)
    acc=['Income']
    cm1=ttk.Combobox(frame2,values=acc)
    cm1.current(0)
    cm1.place(relx=0.04,rely=0.15,relwidth=0.4,relheight=0.065)
    
    l3=tk.Label(frame2,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.05)
    e3=tk.Entry(frame2).place(relx=0.5,rely=0.15,relwidth=0.4,relheight=0.065)

    l4=tk.Label(frame2,text='Detail Type',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.04,rely=0.25)
    cont2=['Sales of product income']
    cmb=ttk.Combobox(frame2,values=cont2).place(relx=0.04,rely=0.35,relwidth=0.4,relheight=0.065)
    
    l5=tk.Label(frame2,text='Description',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.25)
    e5=tk.Entry(frame2).place(relx=0.5,rely=0.35,relwidth=0.4,relheight=0.065)

    message='''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box=Text(frame2)
    text_box.place(relx=0.04,rely=0.55,relwidth=0.4,relheight=0.2)
    text_box.insert('end',message)
    text_box.config(state='disabled')
    Checkbutton(frame2, text = "Is sub-account ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.5,rely=0.45)
    bal=['Deferred CGST','Deferred GST Input Credit','Deferred Krishi Kalyan Cess',
         'Input Credit','Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit',
        'GST Refund','Inventory Asset','Paid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset',
        'Accumulated Depreciation','Buildings and Improvements','Furniture and Equipment','Land','Leasehold Improvements',
        'CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable','Input CGST','Input CGST Tax RCM',
        'Input IGST','Input IGST Tax RCM','Input Krishi Kalyan Cess','Input Krishi Kalyan Cess RCM','Input Service Tax',
        'Input Service Tax RCM','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable','Krishi Kalyan Cess Suspense',
        'Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST','Output IGST Tax RCM','Output Krishi Kalyan Cess',
         'Output Krishi Kalyan Cess DCM','Output Service Tax','Output Service Tax RCM','Output SGST','Output SGST Tax RCM',
        'Output VAT 14%','Output VAT 4%','Output VAT 5%','Service Tax Payable','Service Tax Suspense','SGST Payable','Swachh Bharat Cess Payable',
        'TDS Payable','VAT Payable','VAT Suspense','Opening Balance','Equity']

    cb=ttk.Combobox(frame2,values=bal).place(relx=0.5,rely=0.55,relwidth=0.4,relheight=0.065)
    l6=tk.Label(frame2,text='Default Tax Code',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.63)
  
    val=['18.0% IGST',' 14.00% ST','0% IGST','Out of Scope','0% GST','14.5% ST','14.0% VAT','6.0% IGST','28.0% IGST','15.0% ST','28.0% GST','12.0% GST','18.0% GST',
    '3.0% GST','0.2% IGST','5.0% GST','6.0% GST','0.2% GST','Exempt IGST','3.0% IGST','4.0% VAT','5.0% IGST','12.36% ST','5.0% VAT','Exempt GST','12.0% IGST','2.0% CST']
    e6=ttk.Combobox(frame2,values=val).place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.065)
    sub1=tk.Button(frame2,text='CREATE',font=15,bg='#5193e6',foreground='white').place(relx=0.45,rely=0.9)
    frame2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
    C.mainloop()
    
def splus():
    C=tk.Toplevel(B)
    C.title('account create')
    C.geometry('1400x700')
    C['bg'] = '#2f516f'

    frame1 = tk.LabelFrame(C,borderwidth=0,bg='#243e54')
    l1=tk.Label(frame1,text='ACCOUNT CREATE',bg='#243e54',foreground='white',font=('poppins',30))
    l1.place(relx=0.35,rely=0.1)
    frame1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    frame2=tk.Frame(C,bg='#243e54')
    l2=tk.Label(frame2,text='Account Type',bg='#243e54',foreground='white',font=('poppins', 14))
    l2.place(relx=0.04,rely=0.05)
    acc=['Current Assets']
    cm1=ttk.Combobox(frame2,values=acc)
    cm1.current(0)
    cm1.place(relx=0.04,rely=0.15,relwidth=0.4,relheight=0.065)
    
    l3=tk.Label(frame2,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.05)
    e3=tk.Entry(frame2).place(relx=0.5,rely=0.15,relwidth=0.4,relheight=0.065)

    l4=tk.Label(frame2,text='Detail Type',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.04,rely=0.25)
    cont2=['Inventory']
    cmb=ttk.Combobox(frame2,values=cont2).place(relx=0.04,rely=0.35,relwidth=0.4,relheight=0.065)
    
    l5=tk.Label(frame2,text='Description',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.25)
    e5=tk.Entry(frame2).place(relx=0.5,rely=0.35,relwidth=0.4,relheight=0.065)

    message='''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box=Text(frame2)
    text_box.place(relx=0.04,rely=0.55,relwidth=0.4,relheight=0.2)
    text_box.insert('end',message)
    text_box.config(state='disabled')
    Checkbutton(frame2, text = "Is sub-account ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.5,rely=0.45)
    bal=['Deferred CGST','Deferred GST Input Credit','Deferred Krishi Kalyan Cess',
         'Input Credit','Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit',
        'GST Refund','Inventory Asset','Paid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset',
        'Accumulated Depreciation','Buildings and Improvements','Furniture and Equipment','Land','Leasehold Improvements',
        'CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable','Input CGST','Input CGST Tax RCM',
        'Input IGST','Input IGST Tax RCM','Input Krishi Kalyan Cess','Input Krishi Kalyan Cess RCM','Input Service Tax',
        'Input Service Tax RCM','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable','Krishi Kalyan Cess Suspense',
        'Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST','Output IGST Tax RCM','Output Krishi Kalyan Cess',
         'Output Krishi Kalyan Cess DCM','Output Service Tax','Output Service Tax RCM','Output SGST','Output SGST Tax RCM',
        'Output VAT 14%','Output VAT 4%','Output VAT 5%','Service Tax Payable','Service Tax Suspense','SGST Payable','Swachh Bharat Cess Payable',
        'TDS Payable','VAT Payable','VAT Suspense','Opening Balance','Equity']

    cb=ttk.Combobox(frame2,values=bal).place(relx=0.5,rely=0.55,relwidth=0.4,relheight=0.065)
    l6=tk.Label(frame2,text='Default Tax Code',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.5,rely=0.63)
  
    val=['18.0% IGST',' 14.00% ST','0% IGST','Out of Scope','0% GST','14.5% ST','14.0% VAT','6.0% IGST','28.0% IGST','15.0% ST','28.0% GST','12.0% GST','18.0% GST',
    '3.0% GST','0.2% IGST','5.0% GST','6.0% GST','0.2% GST','Exempt IGST','3.0% IGST','4.0% VAT','5.0% IGST','12.36% ST','5.0% VAT','Exempt GST','12.0% IGST','2.0% CST']
    e6=ttk.Combobox(frame2,values=val).place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.065)
    sub1=tk.Button(frame2,text='CREATE',font=15,bg='#5193e6',foreground='white').place(relx=0.45,rely=0.9)
    frame2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
    C.mainloop()
    
    
def select_product():
    
    global B
    B=tk.Toplevel(A)
    B.title('Add products')
    B.geometry('1400x700')
    mycanvas=tk.Canvas(B,width=1500,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

    head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f1 = font.Font(family='poppins',size=30)#font
    lb1=tk.Label(head1,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    
    lb1['font']=f1
    lb1.place(relx=0.2,rely=0.2)
    head1.place(relx=0,rely=0.05,relwidth=1,relheight=0.08)
    
    head3 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f2 = font.Font(family='poppins',size=25)#font
    lb2=tk.Label(head3,text='INVENTORY',bg='#243e54',foreground='white')
    bu = Button(head3,text = "Choose Type",command=selectproduct,bg="#5193e6",fg="#fff",font=('mali', 10, 'bold'))  
    bu.place(relx=0.5,rely=0.2,width=250,height=40) 
    
    lb2['font']=f2
    lb2.place(relx=0.3,rely=0.2)
    head3.place(relx=0,rely=0.15,relwidth=1,relheight=0.08)
    
    
    
    
    
    


    #contents frame
    hd1= tk.LabelFrame(frame,borderwidth=0,bg='#243e54') 
   
    f3 = font.Font(family='poppins',size=18)#font
    hd1.place(relx=0,rely=0.06,relwidth=1,relheight=0.1)
    
    but2 = Button(hd1,text = "UPLOAD IMAGE",command=upload_file,bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    but2.place(relx=0.8,rely=0.02,width=250,height=30) 

    tk.Label(hd1,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
    productname=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='SKU',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.35,rely=0.05)
    sku=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='HSN Code',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.05)
    phsncode=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    
    
    tk.Label(hd1,text='Unit',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.13)
    valu=['CHOOSE','BAG Bags','BAL Bale BOU','BDL Bundles','BKL Buckles','BOX Box','BTL Bottles','CAN Cans','CTN Cartons','CCM Cubic centimeters','CBM Cubic meters','CMS Centimeters','DRM Drums','DOZ Dozens','GGK Great gross GYD','GRS GrossGMS','KME Kilometre','KGS Kilograms','KLR Kilo litre','MTS Metric ton','MLT Mili litre','MTR Meters','NOS Numbers','PAC Packs','PCS Pieces','PRS Pairs','QTL Quintal','ROL Rolls','SQY Square Yards','SET Sets','SQF Square feet','SQM Square meters','TBS Tablets','TUB Tubes','TGM Ten Gross','THD Thousands','TON Tonnes','UNT Units','lons','YDS Yards']
    punit=ttk.Combobox(hd1,values=valu)
    punit.current(0)
    punit.place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Catogory',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.13)
    eemail=tk.Entry(hd1,bg='#2f516f')
    eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Low stock alert',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.13)
    emobile=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
    
    tk.Label(hd1,text='Description',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.20)
    eopen=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Sales price/rate',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.20)
    e_accno=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

    web=tk.Label(hd1,text='Initial quantity on hand',font=('poppins', 14),bg='#243e54',foreground='white')
    web.place(relx=0.68,rely=0.20)
    eweb=tk.Entry(hd1,bg='#2f516f')
  
    eweb.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Purchasing information',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.28)
    ebill=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Cost',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.28)
    Checkbutton(frame, text = "Inclusive of purchase tax ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.4,rely=0.55)
    eterms=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)
    

    tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.35)
    gstvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    egst=ttk.Combobox(hd1,values=gstvalues)
    egst.current(0)
    egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Purchase TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.35)
    purchasetaxvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    egst_in=ttk.Combobox(hd1,values=purchasetaxvalues)
    egst_in.current(0)
    egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Income account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.35)
    incometaxvalues=['Billable Expense Income','Product Sales','Sales','Sales-Hardware','Sales-Software','Sales-Support and Maintanance','Sales of Product Income','Uncategorised Income']
    inctax_in=ttk.Combobox(hd1,values=incometaxvalues)
    inctax_in.current(0)
    inctax_in
    inctax_in.place(relx=0.68,rely=0.38,relwidth=0.27,relheight=0.035)  
    

    date=tk.Label(hd1,text='As of date',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.42)
    edate=DateEntry(hd1,bg='#2f516f').place(relx=0.02,rely=0.45,relwidth=0.3,relheight=0.035)
    tk.Button(hd1,text='+',font=(14),command=stplus).place(relx=0.955,rely=0.38,relwidth=0.025,relheight=0.035)
    
    defexp=tk.Label(hd1,text='Inventory asset account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.42)
    defvalues=['Inventory Assets']
    edefexp=ttk.Combobox(hd1,values=defvalues)
    edefexp.current(0)
    edefexp.place(relx=0.35,rely=0.45,relwidth=0.27,relheight=0.035)  

    tk.Button(hd1,text='+',font=(14),command=splus).place(relx=0.625,rely=0.45,relwidth=0.025,relheight=0.035)
    
    

    tds=tk.Label(hd1,text='Expense account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.42)
    defvalue=['Cost of sales']
    etds=ttk.Combobox(hd1,values=defvalue)
    etds.current(0)
    etds.place(relx=0.68,rely=0.45,relwidth=0.27,relheight=0.035) 
    tk.Button(hd1,text='+',font=(14),command=suplus).place(relx=0.955,rely=0.45,relwidth=0.025,relheight=0.035)
    
    

    street=tk.Label(hd1,text='Reverse Charge %',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.53)
    estreet=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.57,relwidth=0.63,relheight=0.035)  
    
    city=tk.Label(hd1,text='Preferred Supplier',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.68,rely=0.53)
    ecity=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.57,relwidth=0.3,relheight=0.035)

    

    


    sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#5193e6',foreground='white').place(relx=0.02,rely=0.65)

    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    
    # tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.4,relwidth=1,relheight=0.01)
    B.mainloop()
    
def select_product3():
    def add_product26():
        L=tk.Toplevel(B)
        L.title('PRODUCT / SERVICE INFORMATION')
        L.geometry('1400x700')
    
    global B
    B=tk.Toplevel(A)
    B.title('PRODUCT / SERVICE INFORMATION')
    B.geometry('1400x700')
    mycanvas=tk.Canvas(B,width=1500,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

    head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f1 = font.Font(family='poppins',size=30)#font
    lb1=tk.Label(head1,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    

    # but = Button(root,text = "UPLOAD IMAGE",bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    # but.place(x=550,y=350,width=250,height=40) 
    
    lb1['font']=f1
    lb1.place(relx=0.2,rely=0.2)
    head1.place(relx=0,rely=0.05,relwidth=1,relheight=0.08)
    
    head3 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f2 = font.Font(family='poppins',size=25)#font
    lb2=tk.Label(head3,text='BUNDLE',bg='#243e54',foreground='white')
    bu = Button(head3,text = "Choose Type",command=selectproduct,bg="#5193e6",fg="#fff",font=('mali', 10, 'bold'))  
    bu.place(relx=0.5,rely=0.2,width=250,height=40) 
    
    lb2['font']=f2
    lb2.place(relx=0.3,rely=0.2)
    head3.place(relx=0,rely=0.15,relwidth=1,relheight=0.08)
    
    
    
    
    
    


    #contents frame
    hd1= tk.LabelFrame(frame,borderwidth=0,bg='#243e54') 
   
    f3 = font.Font(family='poppins',size=18)#font
    hd1.place(relx=0,rely=0.06,relwidth=1,relheight=0.1)
    
    but2 = Button(hd1,text = "UPLOAD IMAGE",bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    but2.place(relx=0.8,rely=0.02,width=250,height=30) 

    tk.Label(hd1,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
    productname=tk.Entry(hd1).place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='SKU',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.35,rely=0.05)
    sku=tk.Entry(hd1).place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Description',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.05)
    phsncode=tk.Entry(hd1).place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    
    tk.Label(hd1,text='Products/services included in the bundle',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.15)
    tk.Label(hd1,text='PRODUCT/SERVICE',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.20)
  
    defvalue=['choose','laptop','smartphone','smartwatch']
    etds=ttk.Combobox(hd1,values=defvalue)
    etds.current(0)
    etds.place(relx=0.02,rely=0.25,relheight=0.035,relwidth=0.12)

    etds1=ttk.Combobox(hd1,values=defvalue)
    etds1.current(0)
    etds1.place(relx=0.02,rely=0.30,relheight=0.035,relwidth=0.12)
    

    etds2=ttk.Combobox(hd1,values=defvalue)
    etds2.current(0)
    etds2.place(relx=0.02,rely=0.35,relheight=0.035,relwidth=0.12)

    etds3=ttk.Combobox(hd1,values=defvalue)
    etds3.current(0)
    etds3.place(relx=0.02,rely=0.40,relheight=0.035,relwidth=0.12)



#col-2

    tk.Label(hd1,text='HSN',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.18,rely=0.20)
    phsncode=tk.Entry(hd1).place(relx=0.15,rely=0.25,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode1=tk.Entry(hd1).place(relx=0.15,rely=0.30,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0.20,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode2=tk.Entry(hd1).place(relx=0.15,rely=0.35,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode3=tk.Entry(hd1).place(relx=0.15,rely=0.40,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    

    tk.Label(hd1,text='DESCRIPTION',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.28,rely=0.20)
    phsncode=tk.Entry(hd1).place(relx=0.28,rely=0.25,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode1=tk.Entry(hd1).place(relx=0.28,rely=0.30,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0.20,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode2=tk.Entry(hd1).place(relx=0.28,rely=0.35,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode3=tk.Entry(hd1).place(relx=0.28,rely=0.40,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)



    tk.Label(hd1,text='QTY',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.43,rely=0.20)
    phsncode=tk.Entry(hd1).place(relx=0.41,rely=0.25,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode1=tk.Entry(hd1).place(relx=0.41,rely=0.30,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0.20,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode2=tk.Entry(hd1).place(relx=0.41,rely=0.35,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode3=tk.Entry(hd1).place(relx=0.41,rely=0.40,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)



    tk.Label(hd1,text='PRICE',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.56,rely=0.20)
    phsncode=tk.Entry(hd1).place(relx=0.54,rely=0.25,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode1=tk.Entry(hd1).place(relx=0.54,rely=0.30,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0.20,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode2=tk.Entry(hd1).place(relx=0.54,rely=0.35,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode3=tk.Entry(hd1).place(relx=0.54,rely=0.40,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

#col-6
    tk.Label(hd1,text='TOTAL',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.69,rely=0.20)
    phsncode=tk.Entry(hd1).place(relx=0.67,rely=0.25,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode1=tk.Entry(hd1).place(relx=0.67,rely=0.30,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0.20,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode2=tk.Entry(hd1).place(relx=0.67,rely=0.35,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

    phsncode3=tk.Entry(hd1).place(relx=0.67,rely=0.40,relwidth=0.12,relheight=0.035)
    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)

#ocol-7
    tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.82,rely=0.20)
    defvalue=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    etds=ttk.Combobox(hd1,values=defvalue)
    etds.current(0)
    etds.place(relx=0.80,rely=0.25,relheight=0.035,relwidth=0.12)

    defvalue=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    etds=ttk.Combobox(hd1,values=defvalue)
    etds.current(0)
    etds.place(relx=0.80,rely=0.30,relheight=0.035,relwidth=0.12)

    defvalue=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    etds=ttk.Combobox(hd1,values=defvalue)
    etds.current(0)
    etds.place(relx=0.80,rely=0.35,relheight=0.035,relwidth=0.12)

    defvalue=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    etds=ttk.Combobox(hd1,values=defvalue)
    etds.current(0)
    etds.place(relx=0.80,rely=0.40,relheight=0.035,relwidth=0.12)


    B.mainloop()
    
def select_product2():
    def add_product25():
        L=tk.Toplevel(B)
        L.title('PRODUCT / SERVICE INFORMATION')
        L.geometry('1400x700')
    
    global B
    B=tk.Toplevel(A)
    B.title('PRODUCT / SERVICE INFORMATION')
    B.geometry('1400x700')
    mycanvas=tk.Canvas(B,width=1500,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

    head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f1 = font.Font(family='poppins',size=30)#font
    lb1=tk.Label(head1,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    

    # but = Button(root,text = "UPLOAD IMAGE",bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    # but.place(x=550,y=350,width=250,height=40) 
    
    lb1['font']=f1
    lb1.place(relx=0.2,rely=0.2)
    head1.place(relx=0,rely=0.05,relwidth=1,relheight=0.08)
    
    head3 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f2 = font.Font(family='poppins',size=25)#font
    lb2=tk.Label(head3,text='SERVICES',bg='#243e54',foreground='white')
    bu = Button(head3,text = "Choose Type",command=selectproduct,bg="#5193e6",fg="#fff",font=('mali', 10, 'bold'))  
    bu.place(relx=0.5,rely=0.2,width=250,height=40) 
    
    lb2['font']=f2
    lb2.place(relx=0.3,rely=0.2)
    head3.place(relx=0,rely=0.15,relwidth=1,relheight=0.08)
    
    
    
    
    
    


    #contents frame
    hd1= tk.LabelFrame(frame,borderwidth=0,bg='#243e54') 
   
    f3 = font.Font(family='poppins',size=18)#font
    hd1.place(relx=0,rely=0.06,relwidth=1,relheight=0.1)
    
    but2 = Button(hd1,text = "UPLOAD IMAGE",bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    but2.place(relx=0.8,rely=0.02,width=250,height=30) 

    tk.Label(hd1,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
    productname=tk.Entry(hd1).place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='SKU',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.35,rely=0.05)
    sku=tk.Entry(hd1).place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='SAC Code',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.05)
    phsncode=tk.Entry(hd1).place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    
    
    tk.Label(hd1,text='Unit',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.13)
    valu=['BAG Bags','BAL Bale BOU','BDL Bundles','BKL Buckles','BOX Box','BTL Bottles','CAN Cans','CTN Cartons','CCM Cubic centimeters','CBM Cubic meters','CMS Centimeters','DRM Drums','DOZ Dozens','GGK Great gross GYD','GRS GrossGMS','KME Kilometre','KGS Kilograms','KLR Kilo litre','MTS Metric ton','MLT Mili litre','MTR Meters','NOS Numbers','PAC Packs','PCS Pieces','PRS Pairs','QTL Quintal','ROL Rolls','SQY Square Yards','SET Sets','SQF Square feet','SQM Square meters','TBS Tablets','TUB Tubes','TGM Ten Gross','THD Thousands','TON Tonnes','UNT Units','lons','YDS Yards']
    punit=ttk.Combobox(hd1,values=valu).place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Catogory',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.13)
    eemail=tk.Entry(hd1)
    eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

    # tk.Label(hd1,text='Low stock alert',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.13)
    # emobile=tk.Entry(hd1).place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
    
    tk.Label(hd1,text='Description',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.20)
    Checkbutton(frame, text = "I sell this product/service to my customers. ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.1,rely=0.48)
    eopen=tk.Entry(hd1).place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Sales price/rate',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.20)
    Checkbutton(frame, text = "Inclusive of purchase tax ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.4,rely=0.48)
    e_accno=tk.Entry(hd1).place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.20)
    gstvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    egst=ttk.Combobox(hd1,values=gstvalues)
    egst.current(0)
    egst.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Abatement %',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.28)
    ebill=tk.Entry(hd1).place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.035)

    # tk.Label(hd1,text='Cost',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.28)
    # Checkbutton(frame, text = "Inclusive of purchase tax ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.4,rely=0.55)
    # eterms=tk.Entry(hd1).place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)
    

    # tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.35)
    # gstvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    # egst=ttk.Combobox(hd1,values=gstvalues)
    # egst.current(0)
    # egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

    # tk.Label(hd1,text='Purchase TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.35)
    # purchasetaxvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    # egst_in=ttk.Combobox(hd1,values=purchasetaxvalues)
    # egst_in.current(0)
    # egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Income account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.28)
    incometaxvalues=['Billable Expense Income','Product Sales','Sales','Sales-Hardware','Sales-Software','Sales-Support and Maintanance','Sales of Product Income','Uncategorised Income']
    inctax_in=ttk.Combobox(hd1,values=incometaxvalues)
    inctax_in.current(0)
    inctax_in
    inctax_in.place(relx=0.68,rely=0.31,relwidth=0.27,relheight=0.035)  
    

    # date=tk.Label(hd1,text='As of date',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.42)
    # edate=DateEntry(hd1).place(relx=0.02,rely=0.45,relwidth=0.3,relheight=0.035)
    # tk.Button(hd1,text='+',font=(14),command=stplus).place(relx=0.955,rely=0.38,relwidth=0.025,relheight=0.035)
    
    defexp=tk.Label(hd1,text='Service Type',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.28)
    defvalues=['Stock Broking','General Insurance','Courier','Advertising Agency','Consulting Engineer','Custom House Agent','Steamer Agent','Clearing and Forwarding','Man power Recruiting','Air Travel Agent','Tour operator','Rent a Cab','Architect','Interior Director','Management Consultment','Chartered Accountant'
,'Cost Accountant','Company Secretary','Real Estate Agent','Security Agency','Credit Rating Agency','Market Research Agency','Underwriter','Beauty Parlor','Cargo Handling','Cable Operators'
,'Dry Cleaning','Event Management','Fashion Designer','Life insurance','Scientific and Technical Consultancy','Photograghy','Convention Services','Video Tape Production','Sound Recording','Broadcasting'
,'Insurance Auxilary Service','Banking and Other Financial','Port Serrvices','Authorised Service Station','Health Club and fitness centres','Rail Travel Agent','Storage and Warehousing','Business Auxillary','Commercial Coaching','Erection or Installation'
,'Franchise Service','Internet Cafe','Maintenance or repair','Techincal testing','Technical Inspection','Foreign exchange broking','Port','Airport Services','Air Transport','Business Exhibition','Goods Transport','Construction of commerce complex','Intellectual property service','Opinion poll service','Outdoor Catering','Television and Radio Programme Production','Survey and exploration of minerals','Pandal and shamiana','Travel Agent','Forward Contract Brokerage','Transport through pipeline','Site Preparation','Dredging','Survey and map making','Cleaning Service','Clubs and Association Service','Packaging Service','Mailing list Compilation','Residential Complex Construction','Share transfer Agent','Atm Manintenance','Recovery Agent','Sale of space for advertisement','Sponsorship','International Air travel','Containerised rail transport','Business Support Service','Action Service','Public Relation Management','Ship Management','Internet Telephony','Cruise Ship tour','Credit Card','Telecommuniction Service','Mining of Mi,Oil or gas','Renting Immovable Property','Works Contract','Development of Consent','Asset Management','Design Services','Information Technology Services','ULIP Management','Stock Exchange Service','Services for transaction in Goods','Clearing House Services','Supply of Tangible goods','Online Information Retrieval','Mandap keeper']
    edefexp=ttk.Combobox(hd1,values=defvalues)
    edefexp.current(0)
    edefexp.place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)  

    tk.Button(hd1,text='+',font=(14),command=splus).place(relx=0.955,rely=0.31,relwidth=0.025,relheight=0.035)
    
    tk.Label(hd1,text='Purchasing information',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.42)
    Checkbutton(frame, text = "I Purchase this product/service from Supplier. ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.01,rely=0.7)
    sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#5193e6',foreground='white').place(relx=0.02,rely=0.65)

    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    
    tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.92,relwidth=1,relheight=0.08)
    B.mainloop()
    
def select_product1():
    def add_product24():
        L=tk.Toplevel(B)
        L.title('Add products')
        L.geometry('1400x700')
    
    global B
    B=tk.Toplevel(A)
    B.title('Add products')
    B.geometry('1400x700')
    mycanvas=tk.Canvas(B,width=1500,height=1000)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

    head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f1 = font.Font(family='poppins',size=30)#font
    lb1=tk.Label(head1,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    

    # but = Button(root,text = "UPLOAD IMAGE",bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    # but.place(x=550,y=350,width=250,height=40) 
    
    lb1['font']=f1
    lb1.place(relx=0.2,rely=0.2)
    head1.place(relx=0,rely=0.05,relwidth=1,relheight=0.08)
    
    head3 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f2 = font.Font(family='poppins',size=25)#font
    lb2=tk.Label(head3,text='NON INVENTORY',bg='#243e54',foreground='white')
    bu = Button(head3,text = "Choose Type",command=selectproduct,bg="#5193e6",fg="#fff",font=('mali', 10, 'bold'))  
    bu.place(relx=0.5,rely=0.2,width=250,height=40) 
    
    lb2['font']=f2
    lb2.place(relx=0.3,rely=0.2)
    head3.place(relx=0,rely=0.15,relwidth=1,relheight=0.08)
    
    
    
    
    
    


    #contents frame
    hd1= tk.LabelFrame(frame,borderwidth=0,bg='#243e54') 
   
    f3 = font.Font(family='poppins',size=18)#font
    hd1.place(relx=0,rely=0.06,relwidth=1,relheight=0.1)
    
    but2 = Button(hd1,text = "UPLOAD IMAGE",bg="black",fg="#fff",font=('mali', 10, 'bold'))  
    but2.place(relx=0.8,rely=0.02,width=250,height=30) 

    tk.Label(hd1,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
    productname=tk.Entry(hd1).place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='SKU',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.35,rely=0.05)
    sku=tk.Entry(hd1).place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='HSN Code',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.05)
    phsncode=tk.Entry(hd1).place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    
    
    tk.Label(hd1,text='Unit',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.13)
    valu=['BAG Bags','BAL Bale BOU','BDL Bundles','BKL Buckles','BOX Box','BTL Bottles','CAN Cans','CTN Cartons','CCM Cubic centimeters','CBM Cubic meters','CMS Centimeters','DRM Drums','DOZ Dozens','GGK Great gross GYD','GRS GrossGMS','KME Kilometre','KGS Kilograms','KLR Kilo litre','MTS Metric ton','MLT Mili litre','MTR Meters','NOS Numbers','PAC Packs','PCS Pieces','PRS Pairs','QTL Quintal','ROL Rolls','SQY Square Yards','SET Sets','SQF Square feet','SQM Square meters','TBS Tablets','TUB Tubes','TGM Ten Gross','THD Thousands','TON Tonnes','UNT Units','lons','YDS Yards']
    punit=ttk.Combobox(hd1,values=valu).place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Catogory',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.13)
    eemail=tk.Entry(hd1)
    eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

    # tk.Label(hd1,text='Low stock alert',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.13)
    # emobile=tk.Entry(hd1).place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
    
    tk.Label(hd1,text='Description',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.20)
    Checkbutton(frame, text = "I sell this product/service to my customers. ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.1,rely=0.48)
    eopen=tk.Entry(hd1).place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Sales price/rate',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.20)
    Checkbutton(frame, text = "Inclusive of purchase tax ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.31,rely=0.55)
     
    e_accno=tk.Entry(hd1).place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

    web=tk.Label(hd1,text='Initial quantity on hand',font=('poppins', 14),bg='#243e54',foreground='white')
    web.place(relx=0.68,rely=0.20)
    eweb=tk.Entry(hd1)
  
    eweb.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Purchasing information',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.28)
    Checkbutton(frame, text = "I Purchase this product/service from Supplier. ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.01,rely=0.58)
    
    tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.35)
    gstvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
    egst=ttk.Combobox(hd1,values=gstvalues)
    egst.current(0)
    egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Income account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.13)
    incometaxvalues=['Billable Expense Income','Product Sales','Sales','Sales-Hardware','Sales-Software','Sales-Support and Maintanance','Sales of Product Income','Uncategorised Income']
    inctax_in=ttk.Combobox(hd1,values=incometaxvalues)
    inctax_in.current(0)
    inctax_in.place(relx=0.68,rely=0.16,relwidth=0.27,relheight=0.035)  
    tk.Button(hd1,text='+',font=(14),command=stplus).place(relx=0.955,rely=0.16,relwidth=0.025,relheight=0.035)
    


    sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#5193e6',foreground='white').place(relx=0.02,rely=0.65)

    hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    
    tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.92,relwidth=1,relheight=0.07)
    B.mainloop()
    
    
def selectproduct():
    P=tk.Toplevel(A)
    P.title('PRODUCT AND SERVICES')
    P.geometry('1500x1000')
    P['bg'] = '#2f516f'
    mycanvas=tk.Canvas(P,width=1500,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(P,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1200)
    
    
    head5 = tk.LabelFrame(P,borderwidth=0,bg='#243e54')
    f5 = font.Font(family='poppins',size=30)#font
    lb5=tk.Label(head5,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    lb5['font']=f5
    lb5.place(relx=0.25,rely=0.2)
    head5.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
    
    head6 = tk.LabelFrame(P,borderwidth=0,bg='#243e54')
    head7 =tk.LabelFrame(head6,borderwidth=0,bg='#2f516f')
    head7.place(relx=0.05,rely=0.07,relwidth=0.4,relheight=0.4)
    size=(100, 100)

    ax7=ImageTk.PhotoImage(Image.open('1.png').resize(size))
    sub=tk.Button(head7,text='Add item',command=select_product,font=15,bg='#5193e6',foreground='white').place(relx=0.42,rely=0.79)

    tk.Label(head7, image=ax7, bg='#2f516f').place(relx=0.25,rely=0.2,relheight=0.5,relwidth=0.5)
    lowstock=tk.Label(head7,text='Inventory',bg='#2f516f',font=('poppins', 20),foreground='white').place(relx=0.35,rely=0.1)
    
    head8 =tk.LabelFrame(head6,borderwidth=0,bg='#2f516f')
    head8.place(relx=0.5,rely=0.07,relwidth=0.4,relheight=0.4)
    size=(100, 100)

    ax8=ImageTk.PhotoImage(Image.open('2.png').resize(size))
    sub=tk.Button(head8,text='Add item',command=select_product1,font=15,bg='#5193e6',foreground='white').place(relx=0.42,rely=0.79)

    tk.Label(head8, image=ax8, bg='#2f516f').place(relx=0.25,rely=0.2,relheight=0.5,relwidth=0.5)
    lowstock=tk.Label(head8,text='Non-Inventory',bg='#2f516f',font=('poppins', 20),foreground='white').place(relx=0.35,rely=0.1)
    
    head9 =tk.LabelFrame(head6,borderwidth=0,bg='#2f516f')
    head9.place(relx=0.05,rely=0.52,relwidth=0.4,relheight=0.4)
    size=(100, 100)

    ax9=ImageTk.PhotoImage(Image.open('3.png').resize(size))
    sub=tk.Button(head9,text='Add item',command=select_product2,font=15,bg='#5193e6',foreground='white').place(relx=0.42,rely=0.79)

    tk.Label(head9, image=ax9, bg='#2f516f').place(relx=0.25,rely=0.2,relheight=0.5,relwidth=0.5)
    lowstock=tk.Label(head9,text='Services',bg='#2f516f',font=('poppins', 20),foreground='white').place(relx=0.35,rely=0.1)
    
    head10 =tk.LabelFrame(head6,borderwidth=0,bg='#2f516f')
    head10.place(relx=0.5,rely=0.52,relwidth=0.4,relheight=0.4)
    size=(90, 90)

    ax10=ImageTk.PhotoImage(Image.open('4.png').resize(size))
    sub=tk.Button(head10,text='Add item',command=select_product3,font=15,bg='#5193e6',foreground='white').place(relx=0.42,rely=0.79)

    tk.Label(head10, image=ax10, bg='#2f516f').place(relx=0.25,rely=0.2,relheight=0.5,relwidth=0.5)
    lowstock=tk.Label(head10,text='Bundle',bg='#2f516f',font=('poppins', 20),foreground='white').place(relx=0.35,rely=0.1)

    
    head6.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.8)
    
    
    P.mainloop()

def main():

    global A,data
    A=tk.Tk()
    A.title('PRODUCT AND SERVICES')
    style=ttk.Style(A)
    style.theme_use("clam",)
    style.configure("Treeview",background="#243e54",fieldbackground="#243e54",foreground="white")
    A.geometry('1400x1000')
    A['bg'] = '#2f516f'

    #head frame
    head = tk.LabelFrame(A,borderwidth=0,bg='#243e54')
    f = font.Font(family='Poppins',size=30)#font
    lb=tk.Label(head,text='PRODUCT AND SERVICES',bg='#243e54',foreground='white')
    lb['font']=f
    lb.place(relx=0.3,rely=0.2)
    head.place(relx=0.02,rely=0.20,relwidth=0.95,relheight=0.1)

    #contents frame
    
    hdk=tk.Frame(A,bg='#243e54')
    hdk.place(relx=0.02,rely=0.35,relwidth=0.95,relheight=0.5)
    ff = font.Font(family='Poppins',size=15)#font
    size=(70, 70)

    ax=ImageTk.PhotoImage(Image.open('lowstock.png').resize(size))

    tk.Label(hdk, image=ax, bg='#243e54').place(relx=0.2,rely=0.01,relheight=0.3,relwidth=0.15)
    lowstock=tk.Label(hdk,text='LOW STOCK : 0',bg='#243e54',font=('poppins', 18),foreground='white').place(relx=0.22,rely=0.28)
    axy=ImageTk.PhotoImage(Image.open('outofstock.png').resize(size))
    
    tk.Label(hdk, image=axy,bg='#243e54').place(relx=0.5,rely=0.01,relheight=0.3,relwidth=0.15)
    outofstock=tk.Label(hdk,text='OUT OF STOCK : 0',bg='#243e54',font=('poppins', 18),foreground='white').place(relx=0.51,rely=0.28)
    
    bt=tk.Button(hdk,text='Add products',command=selectproduct,bg='#5193e6',foreground='white')
    bt['font']=ff
    bt.place(relx=0.85,rely=0.3)

    def psfile_image(event):
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("pubg.jpg")
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img,image=image)
        psimage.photo = image
        psimage.pack()
    def prfile_image(event):
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("pubg2.jpg")
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img,image=image)
        psimage.photo = image
        psimage.pack()
    
    #table view
    
     
    treevv = ttk.Treeview(hdk, height=7, columns=(1,2,3,4,5,6,7), show='headings') 
    ttk.Style().configure("treeview",bgcolor="black")
    treevv.bg='#243e54'
    treevv.heading(1, text='IMAGE')#headings
    treevv.heading(2, text='TYPE')
    treevv.heading(3, text='NAME')
    treevv.heading(4, text='SKU')
    treevv.heading(5, text='HSN/SAC')
    treevv.heading(6, text='QUANTITY')
    treevv.heading(7, text='ACTION')

    treevv.column(1, minwidth=30, width=140,anchor=CENTER)#coloumns
    treevv.column(2, minwidth=30, width=140,anchor=CENTER)
    treevv.column(3, minwidth=30, width=140,anchor=CENTER)
    treevv.column(4, minwidth=30, width=140,anchor=CENTER)
    treevv.column(5, minwidth=30, width=140,anchor=CENTER)
    treevv.column(6, minwidth=30, width=140,anchor=CENTER)
    treevv.bind('<Double-Button-1>' , psfile_image)
    treevv.bind('<Double-Button-2>' , prfile_image)
    
    #treevv.column(7, minwidth=30, width=120,anchor=CENTER)
    image = Image.open("pubg.jpg")
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    treevv.insert('', 'end', values= ('Product pic','Inventory','Carlo','M24','M416','2000'))
    treevv.insert('', 'end', values= ('Product pic','Non inventory','Sara','AWM','M762','22000'))
    treevv.photo = image
    # data=['lowstock.png','Inventory','carlo','M24','m416','2000']
    # treevv.insert('', 'end', text=data, values=(data))
    treevv.place(relx=0,rely=0.5,relwidth=1,relheight=0.6)


    def edit_product():
    
        selected_item = treevv.selection()[0]
        global B
        B=tk.Toplevel(A)
        B.title('Add products')
        B.title('edit products')
        B.geometry('1400x700')
        mycanvas=tk.Canvas(B,width=1500,height=1200)
        mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT,fill=Y)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        frame=tk.Frame(mycanvas)
        frame['bg']='#2f516f'
        mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

        head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
        f1 = font.Font(family='poppins',size=30)#font
        lb1=tk.Label(head1,text='PRODUCT / SERVICE INFORMATION',bg='#243e54',foreground='white')
    
        lb1['font']=f1
        lb1.place(relx=0.2,rely=0.2)
        head1.place(relx=0,rely=0.05,relwidth=1,relheight=0.08)
    
        head3 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
        f2 = font.Font(family='poppins',size=25)#font
        lb2=tk.Label(head3,text='INVENTORY',bg='#243e54',foreground='white')
        bu = Button(head3,text = "Choose Type",command=selectproduct,bg="#5193e6",fg="#fff",font=('mali', 10, 'bold'))  
        bu.place(relx=0.5,rely=0.2,width=250,height=40) 
    
        lb2['font']=f2
        lb2.place(relx=0.3,rely=0.2)
        head3.place(relx=0,rely=0.15,relwidth=1,relheight=0.08)
    
    
    
    
    
    


    #contents frame
        hd1= tk.LabelFrame(frame,borderwidth=0,bg='#243e54') 
   
        f3 = font.Font(family='poppins',size=18)#font
        hd1.place(relx=0,rely=0.06,relwidth=1,relheight=0.1)
    
        but2 = Button(hd1,text = "UPLOAD IMAGE",command=upload_file,bg="black",fg="#fff",font=('mali', 10, 'bold'))  
        but2.place(relx=0.8,rely=0.02,width=250,height=30) 

        tk.Label(hd1,text='Name',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
        productname=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='SKU',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.35,rely=0.05)
        sku=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='HSN Code',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.05)
        phsncode=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    
    
        tk.Label(hd1,text='Unit',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.13)
        valu=['CHOOSE','BAG Bags','BAL Bale BOU','BDL Bundles','BKL Buckles','BOX Box','BTL Bottles','CAN Cans','CTN Cartons','CCM Cubic centimeters','CBM Cubic meters','CMS Centimeters','DRM Drums','DOZ Dozens','GGK Great gross GYD','GRS GrossGMS','KME Kilometre','KGS Kilograms','KLR Kilo litre','MTS Metric ton','MLT Mili litre','MTR Meters','NOS Numbers','PAC Packs','PCS Pieces','PRS Pairs','QTL Quintal','ROL Rolls','SQY Square Yards','SET Sets','SQF Square feet','SQM Square meters','TBS Tablets','TUB Tubes','TGM Ten Gross','THD Thousands','TON Tonnes','UNT Units','lons','YDS Yards']
        punit=ttk.Combobox(hd1,values=valu)
        punit.current(0)
        punit.place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Catogory',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.13)
        eemail=tk.Entry(hd1,bg='#2f516f')
        eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Low stock alert',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.13)
        emobile=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
    
        tk.Label(hd1,text='Description',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.20)
        eopen=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Sales price/rate',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.20)
        e_accno=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

        web=tk.Label(hd1,text='Initial quantity on hand',font=('poppins', 14),bg='#243e54',foreground='white')
        web.place(relx=0.68,rely=0.20)
        eweb=tk.Entry(hd1,bg='#2f516f')
  
        eweb.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Purchasing information',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.28)
        ebill=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Cost',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.28)
        Checkbutton(frame, text = "Inclusive of purchase tax ",bg='#243e54',foreground='white',font=('poppins', 12)).place(relx=0.4,rely=0.55)
        eterms=tk.Entry(hd1,bg='#2f516f').place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)
    

        tk.Label(hd1,text='TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.35)
        gstvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
        egst=ttk.Combobox(hd1,values=gstvalues)
        egst.current(0)
        egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Purchase TAX',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.35)
        purchasetaxvalues=['CHOOSE','28.0% GST (28%)','28.0% IGST (28%)','18.0% GST (18%)','18.0% IGST (18%)','15.0% ST (100%)','14.5% ST (100%)','14.00% ST (100%)','14.0% VAT (100%).36','12.36% ST (100%)','12.0% GST (12%)','12.0% IGST (12%)','6.0% GST (6%)','6.0% IGST (6%)','5.0% GST (5%)','5.0% IGST (5%)','5.0% VAT (100%)','4.0% VAT (100%)','3.0% GST (3%)','3.0% IGST (3%)','2.0% CST (100%)','25>0.25% GST (0.25%)25','0.25% IGST (0.25%)','0% GST (0%)','0% IGST (0%)','Exempt GST (0%)','Exempt IGST (0%)','Out of Scope(0%)']
        egst_in=ttk.Combobox(hd1,values=purchasetaxvalues)
        egst_in.current(0)
        egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Income account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.35)
        incometaxvalues=['Billable Expense Income','Product Sales','Sales','Sales-Hardware','Sales-Software','Sales-Support and Maintanance','Sales of Product Income','Uncategorised Income']
        inctax_in=ttk.Combobox(hd1,values=incometaxvalues)
        inctax_in.current(0)
        inctax_in
        inctax_in.place(relx=0.68,rely=0.38,relwidth=0.27,relheight=0.035)  
    

        date=tk.Label(hd1,text='As of date',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.02,rely=0.42)
        edate=DateEntry(hd1,bg='#2f516f').place(relx=0.02,rely=0.45,relwidth=0.3,relheight=0.035)
        tk.Button(hd1,text='+',font=(14),command=stplus).place(relx=0.955,rely=0.38,relwidth=0.025,relheight=0.035)
    
        defexp=tk.Label(hd1,text='Inventory asset account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.35,rely=0.42)
        defvalues=['Inventory Assets']
        edefexp=ttk.Combobox(hd1,values=defvalues)
        edefexp.current(0)
        edefexp.place(relx=0.35,rely=0.45,relwidth=0.27,relheight=0.035)  

        tk.Button(hd1,text='+',font=(14),command=splus).place(relx=0.625,rely=0.45,relwidth=0.025,relheight=0.035)

    

        tds=tk.Label(hd1,text='Expense account',font=('poppins', 14),bg='#243e54',foreground='white').place(relx=0.68,rely=0.42)
        defvalue=['Cost of sales']
        etds=ttk.Combobox(hd1,values=defvalue)
        etds.current(0)
        etds.place(relx=0.68,rely=0.45,relwidth=0.27,relheight=0.035) 
        tk.Button(hd1,text='+',font=(14),command=suplus).place(relx=0.955,rely=0.45,relwidth=0.025,relheight=0.035)
    
    

        street=tk.Label(hd1,text='Reverse Charge %',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.02,rely=0.53)
        estreet=tk.Entry(hd1,bg='#2f516f').place(relx=0.02,rely=0.57,relwidth=0.63,relheight=0.035)  
    
        city=tk.Label(hd1,text='Preferred Supplier',bg='#243e54',foreground='white',font=('poppins', 14)).place(relx=0.68,rely=0.53)
        ecity=tk.Entry(hd1,bg='#2f516f').place(relx=0.68,rely=0.57,relwidth=0.3,relheight=0.035)

    

    


        sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#5193e6',foreground='white').place(relx=0.02,rely=0.65)

        hd1.place(relx=0,rely=0.3,relwidth=0.9,relheight=0.9)
    

        tk.Frame(frame, bg='#243e54').place(relx=0.02, rely=0.95, relwidth=0.90, relheight=0.8)
        B.mainloop()

    def delete():
        # Get selected item to Delete
        selected_item = treevv.selection()[0]
        treevv.delete(selected_item)

    edit_btn = ttk.Button(hdk, text="Edit", command=edit_product)
    edit_btn.place(relx=0.35,rely=0.8,relheight=0.1,relwidth=0.1)
    del_btn = ttk.Button(hdk, text="Delete", command=delete)
    del_btn.place(relx=0.5,rely=0.8,relheight=0.1,relwidth=0.1)   
    A.mainloop()
    
    
main()    

