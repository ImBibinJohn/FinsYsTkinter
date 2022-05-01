
from tkinter import *
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox as MessageBox
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from requests import get
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql

def bankrecon():
    
    import bankrecon
    

window = Tk()
window.geometry('320x150')
menubar = Menu(window)
Sale = Menu(menubar, tearoff=False)
Sale.add_command(label="Online Banking")
Sale.add_command(label="Offline Banking")
Sale.add_command(label="Bank Reconcilation", command=bankrecon)
menubar.add_cascade(label="Banking", menu=Sale)

def salesrecords():
    
    import salesrecords
    

Sale = Menu(menubar, tearoff=False)
Sale.add_command(label="Sales Records",command=salesrecords)
Sale.add_command(label="Invoices")
Sale.add_command(label="Customers")
Sale.add_command(label="Product and Services")
menubar.add_cascade(label="Sales", menu=Sale)
window.config(menu=menubar)
window.mainloop() 