import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import os
import pandas as pd
import webbrowser
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cursor=mydata.cursor()

off=tk.Tk()
off.title('OFFLINE BANKING')
off.geometry('1500x1000')
off['bg'] = '#2f516f'
mycanvas=tk.Canvas(off,width=1800,height=1200)
mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
yscrollbar =ttk.Scrollbar(off,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill=Y)
mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
frame=tk.Frame(mycanvas)
frame['bg']='#2f516f'
mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1200)
fra1=tk.Frame(frame,bg='#243e54')
tk.Label(fra1,text='ADD TRANSACTIONS',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
fra1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
fra2=tk.Frame(frame,bg='#243e54')

#image...
s=(400,390)
im=Image.open('trans.png').resize(s)
img=ImageTk.PhotoImage(im,master=off)
imgg=tk.Label(fra2,image=img,bg='#243e54')
imgg.place(relx=0.05,rely=0.1,relheight=0.8,relwidth=0.4)

tk.Label(fra2,text='Upload Your Bank Transactions',font=('Times New Roman',30),bg='#243e54').place(relx=0.5,rely=0.1)
tk.Label(fra2,text='1. Sign in to your bank account.',font=('Times New Roman',20),bg='#243e54').place(relx=0.53,rely=0.2)
tk.Label(fra2,text='2. Download transactions.',font=('Times New Roman',20),bg='#243e54').place(relx=0.53,rely=0.26)
tk.Label(fra2,text='3. Upload the file to Fin sYs.',font=('Times New Roman',20),bg='#243e54').place(relx=0.53,rely=0.32)

#downloading excel sheet
def download():
    webbrowser.open('https://view.officeapps.live.com/op/view.aspx?src=http%3A%2F%2Ffinsys.live%2Fstatic%2Fassets%2FExcel%2FTransaxtions.xlsx&wdOrigin=BROWSELINK')
tk.Button(fra2,text='Download Excel Sheet',font=('Times New Roman',16),bg='#243e54',command=download).place(relx=0.6,rely=0.42,relwidth=0.3)

#uploaded statements
def statements():
    st=tk.Tk()
    st.title('STATEMENTS')
    st.geometry('1500x1000')
    st['bg'] = '#2f516f'
    stframe=tk.Frame(st,bg='#243e54')
    tk.Label(stframe,text='BANK STATEMENTS',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    stframe.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    sthframe=tk.Frame(st,bg='#243e54')

      #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='black',fieldbackground='#243e54')
    style.map('Treeview',background=[('selected','green')])
    stattree = ttk.Treeview(sthframe, height=7, columns=(1,2,3,4,5), show='headings') 
    stattree.heading(1, text='ID')
    stattree.heading(2, text='DATE')#headings
    stattree.heading(3, text='DESCRIPTION')
    stattree.heading(4, text='DEBIT')
    stattree.heading(5, text='CREDIT')

    sthframe.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.7)
    st.mainloop()
tk.Button(fra2,text='Uploaded Statements',font=('Times New Roman',16),bg='#243e54',command=statements).place(relx=0.6,rely=0.52,relwidth=0.3)

#excel file entering
def open_file():
    global b
    file_path = filedialog.askopenfilename(filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))
    a=os.path.basename(file_path)
    b=os.path.abspath(file_path)
    #d=os.path.dirname(os.path.abspath(file_path))
    tk.Label(fra2,text=a,font=('Times New Roman',14),bg='#243e54').place(relx=0.5,rely=0.72,relwidth=0.2)

#excel datas to database    
def upload():
    cid=2 
    df = pd.read_excel(b)  
    for index,row in df.iterrows():
        ff="INSERT INTO bankstatements (cid,name,date,description,debit,credit) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(ff,[cid, row[0], row[1], row[2], row[3], row[4]])
        mydata.commit()

tk.Button(fra2,text = "Select Excel File",font=('Times New Roman',16),command=open_file,bg='#243e54').place(relx=0.5,rely=0.65,relwidth=0.2)
tk.Button(fra2,text='Upload',font=('Times New Roman',16),bg='#243e54',command=upload).place(relx=0.73,rely=0.65,relwidth=0.2)
fra2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
off.mainloop()