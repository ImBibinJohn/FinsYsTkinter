from multiprocessing.sharedctypes import Value
from pydoc import apropos
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='finsystkinter',
    )
mycursor = mydb.cursor()
jan="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Advertising/Promotional')"
mycursor.execute(jan)
tab1 = mycursor.fetchall()
feb="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Advertising/Promotional')"
mycursor.execute(feb)
tab2 = mycursor.fetchall()
mar="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Advertising/Promotional')"
mycursor.execute(mar)
tab3 = mycursor.fetchall()
apr="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Advertising/Promotional')"
mycursor.execute(apr)
tab4 = mycursor.fetchall()
may="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Advertising/Promotional')"
mycursor.execute(may)
tab5 = mycursor.fetchall()
jun="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Advertising/Promotional')"
mycursor.execute(jun)
tab6 = mycursor.fetchall()
jan1="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Bank Charges')"
mycursor.execute(jan)
tab7 = mycursor.fetchall()
feb1="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Bank Charges')"
mycursor.execute(feb1)
tab8 = mycursor.fetchall()
mar1="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Bank Charges')"
mycursor.execute(mar1)
tab9 = mycursor.fetchall()
apr1="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Bank Charges')"
mycursor.execute(apr1)
tab10 = mycursor.fetchall()
may1="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Bank Charges')"
mycursor.execute(may1)
tab11 = mycursor.fetchall()
jun1="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Bank Charges')"
mycursor.execute(jun)
tab12 = mycursor.fetchall()
jan2="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Business Licenses and Permits')"
mycursor.execute(jan2)
tab13 = mycursor.fetchall()
feb2="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Business Licenses and Permits')"
mycursor.execute(feb2)
tab14 = mycursor.fetchall()
mar2="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Business Licenses and Permits')"
mycursor.execute(mar2)
tab15 = mycursor.fetchall()
apr2="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Business Licenses and Permits')"
mycursor.execute(apr2)
tab16 = mycursor.fetchall()
may2="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Business Licenses and Permits')"
mycursor.execute(may2)
tab17 = mycursor.fetchall()
jun2="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Business Licenses and Permits')"
mycursor.execute(jun2)
tab18 = mycursor.fetchall()
jan3="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Charitable Contributions')"
mycursor.execute(jan3)
tab19 = mycursor.fetchall()
feb3="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Charitable Contributions')"
mycursor.execute(feb3)
tab20 = mycursor.fetchall()
mar3="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Charitable Contributions')"
mycursor.execute(mar3)
tab21 = mycursor.fetchall()
apr3="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Charitable Contributions')"
mycursor.execute(apr3)
tab22 = mycursor.fetchall()
may3="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Charitable Contributions')"
mycursor.execute(may3)
tab23 = mycursor.fetchall()
jun3="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Charitable Contributions')"
mycursor.execute(jun3)
tab24 = mycursor.fetchall()
jan4="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Depreciation Expense')"
mycursor.execute(jan4)
tab25 = mycursor.fetchall()
feb4="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Depreciation Expense')"
mycursor.execute(feb4)
tab26 = mycursor.fetchall()
mar4="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Depreciation Expense')"
mycursor.execute(mar4)
tab27 = mycursor.fetchall()
apr4="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Depreciation Expense')"
mycursor.execute(apr4)
tab28 = mycursor.fetchall()
may4="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Depreciation Expense')"
mycursor.execute(may4)
tab29 = mycursor.fetchall()
jun4="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Depreciation Expense')"
mycursor.execute(jun4)
tab30 = mycursor.fetchall()
jan5="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Continuing Education')"
mycursor.execute(jan5)
tab31 = mycursor.fetchall()
feb5="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Continuing Education')"
mycursor.execute(feb5)
tab32 = mycursor.fetchall()
mar5="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Continuing Education')"
mycursor.execute(mar5)
tab33 = mycursor.fetchall()
apr5="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Continuing Education')"
mycursor.execute(apr5)
tab34 = mycursor.fetchall()
may5="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Continuing Education')"
mycursor.execute(may5)
tab35 = mycursor.fetchall()
jun5="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Continuing Education')"
mycursor.execute(jun5)
tab36 = mycursor.fetchall()
jan6="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Dues and Subscriptions')"
mycursor.execute(jan6)
tab37 = mycursor.fetchall()
feb6="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Dues and Subscriptions')"
mycursor.execute(feb6)
tab38 = mycursor.fetchall()
mar6="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Dues and Subscriptions')"
mycursor.execute(mar6)
tab39 = mycursor.fetchall()
apr6="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Dues and Subscriptions')"
mycursor.execute(apr6)
tab40 = mycursor.fetchall()
may6="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Dues and Subscriptions')"
mycursor.execute(may6)
tab41 = mycursor.fetchall()
jun6="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Dues and Subscriptions')"
mycursor.execute(jun6)
tab42 = mycursor.fetchall()
jan7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Housekeeping Charges')"
mycursor.execute(jan7)
tab43 = mycursor.fetchall()
feb7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Housekeeping Charges')"
mycursor.execute(feb7)
tab44 = mycursor.fetchall()
mar7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Housekeezping Charges')"
mycursor.execute(mar7)
tab45 = mycursor.fetchall()
apr7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Housekeeping Charges')"
mycursor.execute(apr7)
tab46 = mycursor.fetchall()
may7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Housekeeping Charges')"
mycursor.execute(may7)
tab47 = mycursor.fetchall()
jun7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Housekeeping Charges')"
mycursor.execute(jun7)
tab48 = mycursor.fetchall()
jan8="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Insurance Expense')"
mycursor.execute(jan8)
tab49 = mycursor.fetchall()
feb8="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Insurance Expense')"
mycursor.execute(feb8)
tab50 = mycursor.fetchall()
mar8="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Insurance Expense')"
mycursor.execute(mar8)
tab51 = mycursor.fetchall()
apr8="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Insurance Expense')"
mycursor.execute(apr8)
tab52 = mycursor.fetchall()
may8="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Insurance Expense')"
mycursor.execute(may8)
tab53 = mycursor.fetchall()
jun8="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Insurance Expense')"
mycursor.execute(jun8)
tab54 = mycursor.fetchall()
jan9="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Insurance Expense-General Liability Insurance')"
mycursor.execute(jan9)
tab55 = mycursor.fetchall()
feb9="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Insurance Expense-General Liability Insurance')"
mycursor.execute(feb9)
tab56 = mycursor.fetchall()
mar9="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Insurance Expense-General Liability Insurance')"
mycursor.execute(mar9)
tab57 = mycursor.fetchall()
apr9="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Insurance Expense-General Liability Insurance')"
mycursor.execute(apr9)
tab58 = mycursor.fetchall()
may9="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Insurance Expense-General Liability Insurance')"
mycursor.execute(may9)
tab59 = mycursor.fetchall()
jun9="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Insurance Expense-General Liability Insurance')"
mycursor.execute(jun9)
tab60 = mycursor.fetchall()
jan10="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Insurance Expense-Health Insurance')"
mycursor.execute(jan10)
tab61 = mycursor.fetchall()
feb10="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Insurance Expense-Health Insurance')"
mycursor.execute(feb10)
tab62 = mycursor.fetchall()
mar10="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Insurance Expense-Health Insurance')"
mycursor.execute(mar10)
tab63 = mycursor.fetchall()
apr10="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Insurance Expense-Health Insurance')"
mycursor.execute(apr10)
tab64 = mycursor.fetchall()
may10="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Insurance Expense-Health Insurance')"
mycursor.execute(may10)
tab65 = mycursor.fetchall()
jun10="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Insurance Expense-Health Insurance')"
mycursor.execute(jun10)
tab66 = mycursor.fetchall()
jan11="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Insurance Expense-Life and Disability Insurance')"
mycursor.execute(jan11)
tab67 = mycursor.fetchall()
feb11="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Insurance Expense-Life and Disability Insurance')"
mycursor.execute(feb11)
tab68 = mycursor.fetchall()
mar11="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Insurance Expense-Life and Disability Insurance')"
mycursor.execute(mar11)
tab69 = mycursor.fetchall()
apr11="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Insurance Expense-Life and Disability Insurance')"
mycursor.execute(apr11)
tab70 = mycursor.fetchall()
may11="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Insurance Expense-Life and Disability Insurance')"
mycursor.execute(may11)
tab71 = mycursor.fetchall()
jun11="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Insurance Expense-Life and Disability Insurance')"
mycursor.execute(jun11)
tab72 = mycursor.fetchall()
jan12="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Insurance Expense-Professional Liabilitynsurance')"
mycursor.execute(jan12)
tab73 = mycursor.fetchall()
feb12="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Insurance Expense-Professional Liabilitynsurance')"
mycursor.execute(feb12)
tab74 = mycursor.fetchall()
mar12="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Insurance Expense-Professional Liabilitynsurance')"
mycursor.execute(mar12)
tab75 = mycursor.fetchall()
apr12="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Insurance Expense-Professional Liabilitynsurance')"
mycursor.execute(apr12)
tab76 = mycursor.fetchall()
may12="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Insurance Expense-Professional Liabilitynsurance')"
mycursor.execute(may12)
tab77 = mycursor.fetchall()
jun12="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Insurance Expense-Professional Liabilitynsurance')"
mycursor.execute(jun12)
tab78 = mycursor.fetchall()
jan13="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Interest Expense')"
mycursor.execute(jan13)
tab79 = mycursor.fetchall()
feb13="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Interest Expense')"
mycursor.execute(feb13)
tab80 = mycursor.fetchall()
mar13="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Interest Expense')"
mycursor.execute(mar13)
tab81 = mycursor.fetchall()
apr13="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Interest Expense')"
mycursor.execute(apr13)
tab82 = mycursor.fetchall()
may13="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Interest Expense')"
mycursor.execute(may13)
tab83 = mycursor.fetchall()
jun13="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Interest Expense')"
mycursor.execute(jun13)
tab84 = mycursor.fetchall()
jan14="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Meals and entertainment')"
mycursor.execute(jan14)
tab85 = mycursor.fetchall()
feb14="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Meals and entertainment')"
mycursor.execute(feb14)
tab86 = mycursor.fetchall()
mar14="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Meals and entertainment')"
mycursor.execute(mar14)
tab87 = mycursor.fetchall()
apr14="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Meals and entertainment')"
mycursor.execute(apr14)
tab88 = mycursor.fetchall()
may14="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Meals and entertainment')"
mycursor.execute(may14)
tab89 = mycursor.fetchall()
jun14="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Meals and entertainment')"
mycursor.execute(jun14)
tab90 = mycursor.fetchall()
jan15="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Office Supplies')"
mycursor.execute(jan15)
tab91 = mycursor.fetchall()
feb15="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Office Supplies')"
mycursor.execute(feb15)
tab92 = mycursor.fetchall()
mar15="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Office Supplies')"
mycursor.execute(mar15)
tab93 = mycursor.fetchall()
apr15="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Office Supplies')"
mycursor.execute(apr15)
tab94 = mycursor.fetchall()
may15="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Office Supplies')"
mycursor.execute(may15)
tab95 = mycursor.fetchall()
jun15="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Office Supplies')"
mycursor.execute(jun15)
tab96 = mycursor.fetchall()
jan16="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Postage and Delivery')"
mycursor.execute(jan16)
tab97 = mycursor.fetchall()
feb16="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Postage and Delivery')"
mycursor.execute(feb16)
tab98 = mycursor.fetchall()
mar16="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Postage and Delivery')"
mycursor.execute(mar16)
tab99 = mycursor.fetchall()
apr16="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Postage and Delivery')"
mycursor.execute(apr16)
tab100 = mycursor.fetchall()
may16="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Postage and Delivery')"
mycursor.execute(may16)
tab101 = mycursor.fetchall()
jun16="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Postage and Delivery')"
mycursor.execute(jun16)
tab102 = mycursor.fetchall()
jan17="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Printing and Reproduction')"
mycursor.execute(jan17)
tab103 = mycursor.fetchall()
feb17="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Printing and Reproduction')"
mycursor.execute(feb17)
tab104 = mycursor.fetchall()
mar17="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Printing and Reproduction')"
mycursor.execute(mar17)
tab105 = mycursor.fetchall()
apr17="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Printing and Reproduction')"
mycursor.execute(apr17)
tab106 = mycursor.fetchall()
may17="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Printing and Reproduction')"
mycursor.execute(may17)
tab107 = mycursor.fetchall()
jun17="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Printing and Reproduction')"
mycursor.execute(jun17)
tab108 = mycursor.fetchall()
jan18="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Professional Fees')"
mycursor.execute(jan18)
tab109 = mycursor.fetchall()
feb18="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Professional Fees')"
mycursor.execute(feb18)
tab110 = mycursor.fetchall()
mar18="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Professional Fees')"
mycursor.execute(mar18)
tab111 = mycursor.fetchall()
apr18="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Professional Fees')"
mycursor.execute(apr18)
tab112 = mycursor.fetchall()
may18="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Professional Fees')"
mycursor.execute(may18)
tab113 = mycursor.fetchall()
jun18="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Professional Fees')"
mycursor.execute(jun18)
tab114 = mycursor.fetchall()
jan19="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Purchases')"
mycursor.execute(jan19)
tab115 = mycursor.fetchall()
feb19="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Purchases')"
mycursor.execute(feb19)
tab116 = mycursor.fetchall()
mar19="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Purchases')"
mycursor.execute(mar19)
tab117 = mycursor.fetchall()
apr19="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Purchases')"
mycursor.execute(apr19)
tab118 = mycursor.fetchall()
may19="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Purchases')"
mycursor.execute(may19)
tab119 = mycursor.fetchall()
jun19="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Purchases')"
mycursor.execute(jun19)
tab120 = mycursor.fetchall()
jan20="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Rent Expense')"
mycursor.execute(jan20)
tab121 = mycursor.fetchall()
feb20="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Rent Expense')"
mycursor.execute(feb20)
tab122 = mycursor.fetchall()
mar20="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Rent Expense')"
mycursor.execute(mar20)
tab123 = mycursor.fetchall()
apr20="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Rent Expense')"
mycursor.execute(apr20)
tab124 = mycursor.fetchall()
may20="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Rent Expense')"
mycursor.execute(may20)
tab125 = mycursor.fetchall()
jun20="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Rent Expense')"
mycursor.execute(jun20)
tab126 = mycursor.fetchall()
jan21="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Repair and maintenance')"
mycursor.execute(jan21)
tab127 = mycursor.fetchall()
feb21="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Repair and maintenance')"
mycursor.execute(feb21)
tab128 = mycursor.fetchall()
mar21="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Repair and maintenance')"
mycursor.execute(mar21)
tab129 = mycursor.fetchall()
apr21="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Repair and maintenance')"
mycursor.execute(apr21)
tab130 = mycursor.fetchall()
may21="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Repair and maintenance')"
mycursor.execute(may21)
tab131= mycursor.fetchall()
jun21="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Repair and maintenance')"
mycursor.execute(jun21)
tab132 = mycursor.fetchall()
jan22="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Small Tools and Equipment')"
mycursor.execute(jan22)
tab133 = mycursor.fetchall()
feb22="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Small Tools and Equipment')"
mycursor.execute(feb22)
tab134 = mycursor.fetchall()
mar22="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Small Tools and Equipment')"
mycursor.execute(mar22)
tab135 = mycursor.fetchall()
apr22="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Small Tools and Equipment')"
mycursor.execute(apr22)
tab136 = mycursor.fetchall()
may22="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Small Tools and Equipment')"
mycursor.execute(may22)
tab137 = mycursor.fetchall()
jun22="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Small Tools and Equipment')"
mycursor.execute(jun22)
tab138 = mycursor.fetchall()
jan23="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Swachh Bharat Cess Expense')"
mycursor.execute(jan23)
tab139 = mycursor.fetchall()
feb23="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Swachh Bharat Cess Expense')"
mycursor.execute(feb23)
tab140 = mycursor.fetchall()
mar23="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Swachh Bharat Cess Expense')"
mycursor.execute(mar23)
tab141 = mycursor.fetchall()
apr23="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Swachh Bharat Cess Expense')"
mycursor.execute(apr23)
tab142 = mycursor.fetchall()
may23="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Swachh Bharat Cess Expense')"
mycursor.execute(may23)
tab143 = mycursor.fetchall()
jun23="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Swachh Bharat Cess Expense')"
mycursor.execute(jun23)
tab144 = mycursor.fetchall()
jan24="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Taxes - Property')"
mycursor.execute(jan24)
tab145 = mycursor.fetchall()
feb24="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Taxes - Property')"
mycursor.execute(feb24)
tab146 = mycursor.fetchall()
mar24="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Taxes - Property')"
mycursor.execute(mar24)
tab147 = mycursor.fetchall()
apr24="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Taxes - Property')"
mycursor.execute(apr24)
tab148 = mycursor.fetchall()
may24="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Taxes - Property')"
mycursor.execute(may24)
tab149 = mycursor.fetchall()
jun24="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Taxes - Property')"
mycursor.execute(jun24)
tab150 = mycursor.fetchall()
jan25="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Telephone Expense')"
mycursor.execute(jan25)
tab151 = mycursor.fetchall()
feb25="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Telephone Expense')"
mycursor.execute(feb25)
tab152 = mycursor.fetchall()
mar25="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Telephone Expense')"
mycursor.execute(mar25)
tab153 = mycursor.fetchall()
apr25="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Telephone Expense')"
mycursor.execute(apr25)
tab154 = mycursor.fetchall()
may25="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Telephone Expense')"
mycursor.execute(may25)
tab155 = mycursor.fetchall()
jun25="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Telephone Expense')"
mycursor.execute(jun25)
tab156 = mycursor.fetchall()
jan26="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Travel Expense')"
mycursor.execute(jan26)
tab157 = mycursor.fetchall()
feb26="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Travel Expense')"
mycursor.execute(feb26)
tab158 = mycursor.fetchall()
mar26="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Travel Expense')"
mycursor.execute(mar26)
tab159 = mycursor.fetchall()
apr26="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Travel Expense')"
mycursor.execute(apr26)
tab160 = mycursor.fetchall()
may26="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Travel Expense')"
mycursor.execute(may26)
tab161 = mycursor.fetchall()
jun26="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Travel Expense')"
mycursor.execute(jun26)
tab162 = mycursor.fetchall()
jan27="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Uncategorised Expense')"
mycursor.execute(jan27)
tab163 = mycursor.fetchall()
feb27="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Uncategorised Expense')"
mycursor.execute(feb27)
tab164 = mycursor.fetchall()
mar27="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Uncategorised Expense')"
mycursor.execute(mar27)
tab165 = mycursor.fetchall()
apr27="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Uncategorised Expense')"
mycursor.execute(apr27)
tab166 = mycursor.fetchall()
may27="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Uncategorised Expense')"
mycursor.execute(may27)
tab167 = mycursor.fetchall()
jun27="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Uncategorised Expense')"
mycursor.execute(jun27)
tab168 = mycursor.fetchall()
jan28="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Utilities')"
mycursor.execute(jan28)
tab169 = mycursor.fetchall()
feb28="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Utilities')"
mycursor.execute(feb28)
tab170 = mycursor.fetchall()
mar28="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Utilities')"
mycursor.execute(mar28)
tab171 = mycursor.fetchall()
apr28="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Utilities')"
mycursor.execute(apr28)
tab172 = mycursor.fetchall()
may28="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Utilities')"
mycursor.execute(may28)
tab173 = mycursor.fetchall()
jun28="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Utilities')"
mycursor.execute(jun28)
tab174 = mycursor.fetchall()
jan29="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Cash and Cash Equivalents')"
mycursor.execute(jan29)
tab175 = mycursor.fetchall()
feb29="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Cash and Cash Equivalents')"
mycursor.execute(feb29)
tab176 = mycursor.fetchall()
mar29="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Cash and Cash Equivalents')"
mycursor.execute(mar29)
tab177 = mycursor.fetchall()
apr29="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Cash and Cash Equivalents')"
mycursor.execute(apr29)
tab178 = mycursor.fetchall()
may29="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Cash and Cash Equivalents')"
mycursor.execute(may29)
tab179 = mycursor.fetchall()
jun29="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Cash and Cash Equivalents')"
mycursor.execute(jun29)
tab180= mycursor.fetchall()
jan30="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Accounts Receivable (Debtors)')"
mycursor.execute(jan30)
tab181 = mycursor.fetchall()
feb30="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Accounts Receivable (Debtors)')"
mycursor.execute(feb30)
tab182 = mycursor.fetchall()
mar30="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Accounts Receivable (Debtors)')"
mycursor.execute(mar30)
tab183 = mycursor.fetchall()
apr30="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Accounts Receivable (Debtors)')"
mycursor.execute(apr30)
tab184 = mycursor.fetchall()
may30="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Accounts Receivable (Debtors)')"
mycursor.execute(may30)
tab185 = mycursor.fetchall()
jun30="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Accounts Receivable (Debtors)')"
mycursor.execute(jun30)
tab186 = mycursor.fetchall()
jan31="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred CGST')"
mycursor.execute(jan31)
tab187 = mycursor.fetchall()
feb31="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred CGST')"
mycursor.execute(feb31)
tab188 = mycursor.fetchall()
mar31="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred CGST')"
mycursor.execute(mar31)
tab189 = mycursor.fetchall()
apr31="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred CGST')"
mycursor.execute(apr31)
tab190 = mycursor.fetchall()
may31="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred CGST')"
mycursor.execute(may31)
tab191 = mycursor.fetchall()
jun31="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred CGST')"
mycursor.execute(jun31)
tab192= mycursor.fetchall()
jan32="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred GST Input Credit')"
mycursor.execute(jan32)
tab193 = mycursor.fetchall()
feb32="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred GST Input Credit')"
mycursor.execute(feb32)
tab194 = mycursor.fetchall()
mar32="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred GST Input Credit')"
mycursor.execute(mar32)
tab195 = mycursor.fetchall()
apr32="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred GST Input Credit')"
mycursor.execute(apr32)
tab196 = mycursor.fetchall()
may32="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred GST Input Credit')"
mycursor.execute(may32)
tab197= mycursor.fetchall()
jun32="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred GST Input Credit')"
mycursor.execute(jun32)
tab198= mycursor.fetchall()
jan33="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred IGST')"
mycursor.execute(jan33)
tab199 = mycursor.fetchall()
feb33="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred IGST')"
mycursor.execute(feb33)
tab200 = mycursor.fetchall()
mar33="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred IGST')"
mycursor.execute(mar33)
tab201 = mycursor.fetchall()
apr33="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred IGST')"
mycursor.execute(apr33)
tab202 = mycursor.fetchall()
may33="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred IGST')"
mycursor.execute(may33)
tab203= mycursor.fetchall()
jun33="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred IGST')"
mycursor.execute(jun33)
tab204= mycursor.fetchall()
jan34="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred Krishi Kalyan Cess Input Credit')"
mycursor.execute(jan34)
tab205 = mycursor.fetchall()
feb34="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred Krishi Kalyan Cess Input Credit')"
mycursor.execute(feb34)
tab206 = mycursor.fetchall()
mar34="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred Krishi Kalyan Cess Input Credit')"
mycursor.execute(mar34)
tab207 = mycursor.fetchall()
apr34="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred Krishi Kalyan Cess Input Credit')"
mycursor.execute(apr34)
tab208 = mycursor.fetchall()
may34="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred Krishi Kalyan Cess Input Credit')"
mycursor.execute(may34)
tab209= mycursor.fetchall()
jun34="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred Krishi Kalyan Cess Input Credit')"
mycursor.execute(jun34)
tab210= mycursor.fetchall()
jan35="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred Service Tax Input Credit')"
mycursor.execute(jan35)
tab211 = mycursor.fetchall()
feb35="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred Service Tax Input Credit')"
mycursor.execute(feb35)
tab212 = mycursor.fetchall()
mar35="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred Service Tax Input Credit')"
mycursor.execute(mar35)
tab213 = mycursor.fetchall()
apr35="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred Service Tax Input Credit')"
mycursor.execute(apr35)
tab214 = mycursor.fetchall()
may35="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred Service Tax Input Credit')"
mycursor.execute(may35)
tab215= mycursor.fetchall()
jun35="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred Service Tax Input Credit')"
mycursor.execute(jun35)
tab216= mycursor.fetchall()
jan36="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred SGST')"
mycursor.execute(jan36)
tab217 = mycursor.fetchall()
feb36="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred SGST')"
mycursor.execute(feb36)
tab218 = mycursor.fetchall()
mar36="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred SGST')"
mycursor.execute(mar36)
tab219 = mycursor.fetchall()
apr36="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred SGST')"
mycursor.execute(apr36)
tab220 = mycursor.fetchall()
may36="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred SGST')"
mycursor.execute(may36)
tab221= mycursor.fetchall()
jun36="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred SGST')"
mycursor.execute(jun36)
tab222= mycursor.fetchall()
jan37="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Deferred VAT Input Credit')"
mycursor.execute(jan37)
tab223 = mycursor.fetchall()
feb37="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Deferred VAT Input Credit')"
mycursor.execute(feb37)
tab224 = mycursor.fetchall()
mar37="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Deferred VAT Input Credit')"
mycursor.execute(mar37)
tab225 = mycursor.fetchall()
apr37="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Deferred VAT Input Credit')"
mycursor.execute(apr37)
tab226 = mycursor.fetchall()
may37="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Deferred VAT Input Credit')"
mycursor.execute(may37)
tab227= mycursor.fetchall()
jun37="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Deferred VAT Input Credit')"
mycursor.execute(jun37)
tab228= mycursor.fetchall()
jan38="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='GST Refund')"
mycursor.execute(jan38)
tab229 = mycursor.fetchall()
feb38="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='GST Refund')"
mycursor.execute(feb38)
tab230 = mycursor.fetchall()
mar38="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='GST Refund')"
mycursor.execute(mar38)
tab231 = mycursor.fetchall()
apr38="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='GST Refund')"
mycursor.execute(apr38)
tab232 = mycursor.fetchall()
may38="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='GST Refund')"
mycursor.execute(may38)
tab233= mycursor.fetchall()
jun38="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='GST Refund')"
mycursor.execute(jun38)
tab234= mycursor.fetchall()
jan39="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Inventory Asset')"
mycursor.execute(jan39)
tab235 = mycursor.fetchall()
feb39="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Inventory Asset')"
mycursor.execute(feb39)
tab236 = mycursor.fetchall()
mar39="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Inventory Asset')"
mycursor.execute(mar39)
tab237 = mycursor.fetchall()
apr39="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Inventory Asset')"
mycursor.execute(apr39)
tab238 = mycursor.fetchall()
may39="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Inventory Asset')"
mycursor.execute(may39)
tab239= mycursor.fetchall()
jun39="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Inventory Asset')"
mycursor.execute(jun39)
tab240= mycursor.fetchall()
jan40="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Krishi Kalyan Cess Refund')"
mycursor.execute(jan40)
tab241 = mycursor.fetchall()
feb40="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Krishi Kalyan Cess Refund')"
mycursor.execute(feb40)
tab242 = mycursor.fetchall()
mar40="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Krishi Kalyan Cess Refund')"
mycursor.execute(mar40)
tab243 = mycursor.fetchall()
apr40="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Krishi Kalyan Cess Refund')"
mycursor.execute(apr40)
tab244 = mycursor.fetchall()
may40="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Krishi Kalyan Cess Refund')"
mycursor.execute(may40)
tab245= mycursor.fetchall()
jun40="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Krishi Kalyan Cess Refund')"
mycursor.execute(jun40)
tab246= mycursor.fetchall()
jan41="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Prepaid Insurance')"
mycursor.execute(jan41)
tab247 = mycursor.fetchall()
feb41="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Prepaid Insurance')"
mycursor.execute(feb41)
tab248 = mycursor.fetchall()
mar41="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Prepaid Insurance')"
mycursor.execute(mar41)
tab249 = mycursor.fetchall()
apr41="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Prepaid Insurance')"
mycursor.execute(apr41)
tab250 = mycursor.fetchall()
may41="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Prepaid Insurance')"
mycursor.execute(may41)
tab251= mycursor.fetchall()
jun41="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Prepaid Insurance')"
mycursor.execute(jun41)
tab252= mycursor.fetchall()
jan42="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Service Tax Refund')"
mycursor.execute(jan42)
tab253 = mycursor.fetchall()
feb42="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Service Tax Refund')"
mycursor.execute(feb42)
tab254 = mycursor.fetchall()
mar42="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Service Tax Refund')"
mycursor.execute(mar42)
tab255 = mycursor.fetchall()
apr42="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Service Tax Refund')"
mycursor.execute(apr42)
tab256 = mycursor.fetchall()
may42="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Service Tax Refund')"
mycursor.execute(may42)
tab257= mycursor.fetchall()
jun42="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Service Tax Refund')"
mycursor.execute(jun42)
tab258= mycursor.fetchall()
jan43="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='TDS Receivable')"
mycursor.execute(jan43)
tab259 = mycursor.fetchall()
feb43="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='TDS Receivable')"
mycursor.execute(feb43)
tab260 = mycursor.fetchall()
mar43="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='TDS Receivable')"
mycursor.execute(mar43)
tab261 = mycursor.fetchall()
apr43="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='TDS Receivable')"
mycursor.execute(apr43)
tab262= mycursor.fetchall()
may43="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='TDS Receivable')"
mycursor.execute(may43)
tab263= mycursor.fetchall()
jun43="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='TDS Receivable')"
mycursor.execute(jun43)
tab264= mycursor.fetchall()
jan44="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Uncategorised Asset')"
mycursor.execute(jan44)
tab266 = mycursor.fetchall()
feb44="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Uncategorised Asset')"
mycursor.execute(feb44)
tab267 = mycursor.fetchall()
mar44="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Uncategorised Asset')"
mycursor.execute(mar44)
tab268 = mycursor.fetchall()
apr44="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Uncategorised Asset')"
mycursor.execute(apr44)
tab269= mycursor.fetchall()
may44="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Uncategorised Asset')"
mycursor.execute(may44)
tab270= mycursor.fetchall()
jun44="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Uncategorised Asset')"
mycursor.execute(jun44)
tab271= mycursor.fetchall()
jan45="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Undeposited Funds')"
mycursor.execute(jan45)
tab272 = mycursor.fetchall()
feb45="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Undeposited Funds')"
mycursor.execute(feb45)
tab273 = mycursor.fetchall()
mar45="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Undeposited Funds')"
mycursor.execute(mar45)
tab274 = mycursor.fetchall()
apr45="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Undeposited Funds')"
mycursor.execute(apr45)
tab275= mycursor.fetchall()
may45="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Undeposited Funds')"
mycursor.execute(may45)
tab276= mycursor.fetchall()
jun45="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Undeposited Funds')"
mycursor.execute(jun45)
tab277= mycursor.fetchall()
jan46="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Accumulated Depreciation')"
mycursor.execute(jan46)
tab278 = mycursor.fetchall()
feb46="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Accumulated Depreciation')"
mycursor.execute(feb46)
tab279 = mycursor.fetchall()
mar46="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Accumulated Depreciation')"
mycursor.execute(mar46)
tab280 = mycursor.fetchall()
apr46="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Accumulated Depreciation')"
mycursor.execute(apr46)
tab281= mycursor.fetchall()
may46="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Accumulated Depreciation')"
mycursor.execute(may46)
tab282= mycursor.fetchall()
jun46="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Accumulated Depreciation')"
mycursor.execute(jun46)
tab283= mycursor.fetchall()
jan47="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Buildings and Improvements')"
mycursor.execute(jan47)
tab284 = mycursor.fetchall()
feb47="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Buildings and Improvements')"
mycursor.execute(feb47)
tab285 = mycursor.fetchall()
mar47="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Buildings and Improvements')"
mycursor.execute(mar47)
tab286 = mycursor.fetchall()
apr47="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Buildings and Improvements')"
mycursor.execute(apr47)
tab287= mycursor.fetchall()
may47="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Buildings and Improvements')"
mycursor.execute(may47)
tab288= mycursor.fetchall()
jun47="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Buildings and Improvements')"
mycursor.execute(jun47)
tab289= mycursor.fetchall()
jan48="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Furniture and Equipment')"
mycursor.execute(jan48)
tab290 = mycursor.fetchall()
feb48="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Furniture and Equipment')"
mycursor.execute(feb48)
tab291 = mycursor.fetchall()
mar48="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Furniture and Equipment')"
mycursor.execute(mar48)
tab292 = mycursor.fetchall()
apr48="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Furniture and Equipment')"
mycursor.execute(apr48)
tab293= mycursor.fetchall()
may48="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Furniture and Equipment')"
mycursor.execute(may48)
tab294= mycursor.fetchall()
jun48="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Furniture and Equipment')"
mycursor.execute(jun48)
tab295= mycursor.fetchall()
jan49="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Land')"
mycursor.execute(jan49)
tab296 = mycursor.fetchall()
feb49="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Land')"
mycursor.execute(feb49)
tab297 = mycursor.fetchall()
mar49="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Land')"
mycursor.execute(mar49)
tab298 = mycursor.fetchall()
apr49="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Land')"
mycursor.execute(apr49)
tab299= mycursor.fetchall()
may49="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Land')"
mycursor.execute(may49)
tab300= mycursor.fetchall()
jun49="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Land')"
mycursor.execute(jun49)
tab301= mycursor.fetchall()
jan50="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Leasehold Improvements')"
mycursor.execute(jan50)
tab302 = mycursor.fetchall()
feb50="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Leasehold Improvements')"
mycursor.execute(feb50)
tab303 = mycursor.fetchall()
mar50="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Leasehold Improvements')"
mycursor.execute(mar50)
tab304 = mycursor.fetchall()
apr50="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Leasehold Improvements')"
mycursor.execute(apr50)
tab305= mycursor.fetchall()
may50="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Leasehold Improvements')"
mycursor.execute(may50)
tab306= mycursor.fetchall()
jun50="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Leasehold Improvements')"
mycursor.execute(jun50)
tab307= mycursor.fetchall()
jan51="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Vehicles')"
mycursor.execute(jan51)
tab308 = mycursor.fetchall()
feb51="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Vehicles')"
mycursor.execute(feb51)
tab309 = mycursor.fetchall()
mar51="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Vehicles')"
mycursor.execute(mar51)
tab310 = mycursor.fetchall()
apr51="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Vehicles')"
mycursor.execute(apr51)
tab311 = mycursor.fetchall()
may51="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Vehicles')"
mycursor.execute(may51)
tab312 = mycursor.fetchall()
jun51="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Vehicles')"
mycursor.execute(jun51)
tab313 = mycursor.fetchall()
jan52="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='CGST Payable')"
mycursor.execute(jan52)
tab314 = mycursor.fetchall()
feb52="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='CGST Payable')"
mycursor.execute(feb52)
tab315 = mycursor.fetchall()
mar52="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='CGST Payable')"
mycursor.execute(mar52)
tab316 = mycursor.fetchall()
apr52="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='CGST Payable')"
mycursor.execute(apr52)
tab317 = mycursor.fetchall()
may52="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='CGST Payable')"
mycursor.execute(may52)
tab318 = mycursor.fetchall()
jun52="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='CGST Payable')"
mycursor.execute(jun52)
tab319 = mycursor.fetchall()


jan53="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='CST Payable')"
mycursor.execute(jan53)
tab320 = mycursor.fetchall()
feb53="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='CST Payable')"
mycursor.execute(feb53)
tab321 = mycursor.fetchall()
mar53="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='CST Payable')"
mycursor.execute(mar53)
tab322 = mycursor.fetchall()
apr53="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='CST Payable')"
mycursor.execute(apr53)
tab323 = mycursor.fetchall()
may53="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='CST Payable')"
mycursor.execute(may53)
tab324 = mycursor.fetchall()
jun53="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='CST Payable')"
mycursor.execute(jun53)
tab325 = mycursor.fetchall()


jan54="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='CST Suspense')"
mycursor.execute(jan54)
tab326 = mycursor.fetchall()
feb54="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='CST Suspense')"
mycursor.execute(feb54)
tab327 = mycursor.fetchall()
mar54="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='CST Suspense')"
mycursor.execute(mar54)
tab328 = mycursor.fetchall()
apr54="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='CST Suspense')"
mycursor.execute(apr54)
tab329 = mycursor.fetchall()
may54="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='CST Suspense')"
mycursor.execute(may54)
tab330 = mycursor.fetchall()
jun54="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='CST Suspense')"
mycursor.execute(jun54)
tab331 = mycursor.fetchall()


jan55="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='GST Payable')"
mycursor.execute(jan55)
tab332 = mycursor.fetchall()
feb55="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='GST Payable')"
mycursor.execute(feb55)
tab333 = mycursor.fetchall()
mar55="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='GST Payable')"
mycursor.execute(mar55)
tab334 = mycursor.fetchall()
apr55="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='GST Payable')"
mycursor.execute(apr55)
tab335 = mycursor.fetchall()
may55="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='GST Payable')"
mycursor.execute(may55)
tab336 = mycursor.fetchall()
jun55="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='GST Payable')"
mycursor.execute(jun55)
tab337 = mycursor.fetchall()


jan56="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='GST Suspense')"
mycursor.execute(jan56)
tab338 = mycursor.fetchall()
feb56="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='GST Suspense')"
mycursor.execute(feb56)
tab339 = mycursor.fetchall()
mar56="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='GST Suspense')"
mycursor.execute(mar56)
tab340 = mycursor.fetchall()
apr56="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='GST Suspense')"
mycursor.execute(apr56)
tab341 = mycursor.fetchall()
may56="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='GST Suspense')"
mycursor.execute(may56)
tab342 = mycursor.fetchall()
jun56="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='GST Suspense')"
mycursor.execute(jun56)
tab343 = mycursor.fetchall()


jan57="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='IGST Payable')"
mycursor.execute(jan57)
tab344 = mycursor.fetchall()
feb57="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='IGST Payable')"
mycursor.execute(feb57)
tab345 = mycursor.fetchall()
mar57="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='IGST Payable')"
mycursor.execute(mar57)
tab346 = mycursor.fetchall()
apr57="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='IGST Payable')"
mycursor.execute(apr57)
tab347 = mycursor.fetchall()
may57="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='IGST Payable')"
mycursor.execute(may57)
tab348 = mycursor.fetchall()
jun57="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='IGST Payable')"
mycursor.execute(jun57)
tab349 = mycursor.fetchall()


jan58="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input CGST')"
mycursor.execute(jan58)
tab350 = mycursor.fetchall()
feb58="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input CGST')"
mycursor.execute(feb58)
tab351 = mycursor.fetchall()
mar58="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input CGST')"
mycursor.execute(mar58)
tab352 = mycursor.fetchall()
apr58="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input CGST')"
mycursor.execute(apr58)
tab353 = mycursor.fetchall()
may58="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input CGST')"
mycursor.execute(may58)
tab354 = mycursor.fetchall()
jun58="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input CGST')"
mycursor.execute(jun58)
tab355 = mycursor.fetchall()


jan59="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input CGST Tax RCM')"
mycursor.execute(jan59)
tab356 = mycursor.fetchall()
feb59="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input CGST Tax RCM')"
mycursor.execute(feb59)
tab357 = mycursor.fetchall()
mar59="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input CGST Tax RCM')"
mycursor.execute(mar59)
tab358 = mycursor.fetchall()
apr59="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input CGST Tax RCM')"
mycursor.execute(apr59)
tab359 = mycursor.fetchall()
may59="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input CGST Tax RCM')"
mycursor.execute(may59)
tab360 = mycursor.fetchall()
jun59="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input CGST Tax RCM')"
mycursor.execute(jun59)
tab361 = mycursor.fetchall()


jan60="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input IGST Tax RCM')"
mycursor.execute(jan60)
tab362 = mycursor.fetchall()
feb60="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input IGST Tax RCM')"
mycursor.execute(feb60)
tab363 = mycursor.fetchall()
mar60="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input IGST Tax RCM')"
mycursor.execute(mar60)
tab364 = mycursor.fetchall()
apr60="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input IGST Tax RCM')"
mycursor.execute(apr60)
tab365 = mycursor.fetchall()
may60="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input IGST Tax RCM')"
mycursor.execute(may60)
tab366 = mycursor.fetchall()
jun60="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input IGST Tax RCM')"
mycursor.execute(jun60)
tab367 = mycursor.fetchall()


jan61="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input Krishi Kalyan Cess')"
mycursor.execute(jan61)
tab368 = mycursor.fetchall()
feb61="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input Krishi Kalyan Cess')"
mycursor.execute(feb61)
tab369 = mycursor.fetchall()
mar61="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input Krishi Kalyan Cess')"
mycursor.execute(mar61)
tab370 = mycursor.fetchall()
apr61="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input Krishi Kalyan Cess')"
mycursor.execute(apr61)
tab371 = mycursor.fetchall()
may61="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input Krishi Kalyan Cess')"
mycursor.execute(may61)
tab372 = mycursor.fetchall()
jun61="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input Krishi Kalyan Cess')"
mycursor.execute(jun61)
tab373 = mycursor.fetchall()


jan62="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input Krishi Kalyan Cess RCM')"
mycursor.execute(jan62)
tab374 = mycursor.fetchall()
feb62="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input Krishi Kalyan Cess RCM')"
mycursor.execute(feb62)
tab375 = mycursor.fetchall()
mar62="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input Krishi Kalyan Cess RCM')"
mycursor.execute(mar62)
tab376 = mycursor.fetchall()
apr62="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input Krishi Kalyan Cess RCM')"
mycursor.execute(apr62)
tab377 = mycursor.fetchall()
may62="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input Krishi Kalyan Cess RCM')"
mycursor.execute(may62)
tab378 = mycursor.fetchall()
jun62="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input Krishi Kalyan Cess RCM')"
mycursor.execute(jun62)
tab379 = mycursor.fetchall()

jan63="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input Service Tax')"
mycursor.execute(jan63)
tab380 = mycursor.fetchall()
feb63="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input Service Tax')"
mycursor.execute(feb63)
tab381 = mycursor.fetchall()
mar63="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input Service Tax')"
mycursor.execute(mar63)
tab382 = mycursor.fetchall()
apr63="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input Service Tax')"
mycursor.execute(apr63)
tab383 = mycursor.fetchall()
may63="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input Service Tax')"
mycursor.execute(may63)
tab384 = mycursor.fetchall()
jun63="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input Service Tax')"
mycursor.execute(jun63)
tab385 = mycursor.fetchall()

jan64="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input Service Tax RCM')"
mycursor.execute(jan64)
tab386 = mycursor.fetchall()
feb64="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input Service Tax RCM')"
mycursor.execute(feb64)
tab387 = mycursor.fetchall()
mar64="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input Service Tax RCM')"
mycursor.execute(mar64)
tab388 = mycursor.fetchall()
apr64="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input Service Tax RCM')"
mycursor.execute(apr64)
tab389 = mycursor.fetchall()
may64="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input Service Tax RCM')"
mycursor.execute(may64)
tab390 = mycursor.fetchall()
jun64="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input Service Tax RCM')"
mycursor.execute(jun64)
tab391 = mycursor.fetchall()

jan65="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input SGST')"
mycursor.execute(jan65)
tab392 = mycursor.fetchall()
feb65="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input SGST')"
mycursor.execute(feb65)
tab393 = mycursor.fetchall()
mar65="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input SGST')"
mycursor.execute(mar65)
tab394 = mycursor.fetchall()
apr65="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input SGST')"
mycursor.execute(apr65)
tab395 = mycursor.fetchall()
may65="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input SGST')"
mycursor.execute(may65)
tab396 = mycursor.fetchall()
jun65="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input SGST')"
mycursor.execute(jun65)
tab397 = mycursor.fetchall()

jan66="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input SGST Tax RCM')"
mycursor.execute(jan66)
tab398 = mycursor.fetchall()
feb66="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input SGST Tax RCM')"
mycursor.execute(feb66)
tab399 = mycursor.fetchall()
mar66="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input SGST Tax RCM')"
mycursor.execute(mar66)
tab400 = mycursor.fetchall()
apr66="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input SGST Tax RCM')"
mycursor.execute(apr66)
tab401 = mycursor.fetchall()
may66="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input SGST Tax RCM')"
mycursor.execute(may66)
tab402 = mycursor.fetchall()
jun66="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input SGST Tax RCM')"
mycursor.execute(jun66)
tab403 = mycursor.fetchall()

jan67="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input VAT 14%')"
mycursor.execute(jan67)
tab404 = mycursor.fetchall()
feb67="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input VAT 14%')"
mycursor.execute(feb67)
tab405 = mycursor.fetchall()
mar67="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input VAT 14%')"
mycursor.execute(mar67)
tab406 = mycursor.fetchall()
apr67="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input VAT 14%')"
mycursor.execute(apr67)
tab407 = mycursor.fetchall()
may67="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input VAT 14%')"
mycursor.execute(may67)
tab408 = mycursor.fetchall()
jun67="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input VAT 14%')"
mycursor.execute(jun67)
tab409 = mycursor.fetchall()

jan68="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input VAT 4%')"
mycursor.execute(jan68)
tab410 = mycursor.fetchall()
feb68="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input VAT 4%')"
mycursor.execute(feb68)
tab411 = mycursor.fetchall()
mar68="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input VAT 4%')"
mycursor.execute(mar68)
tab412 = mycursor.fetchall()
apr68="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input VAT 4%')"
mycursor.execute(apr68)
tab413 = mycursor.fetchall()
may68="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input VAT 4%')"
mycursor.execute(may68)
tab414 = mycursor.fetchall()
jun68="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input VAT 4%')"
mycursor.execute(jun68)
tab415 = mycursor.fetchall()

jan69="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Input VAT 5%')"
mycursor.execute(jan69)
tab416 = mycursor.fetchall()
feb69="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Input VAT 5%')"
mycursor.execute(feb69)
tab417 = mycursor.fetchall()
mar69="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Input VAT 5%')"
mycursor.execute(mar69)
tab418 = mycursor.fetchall()
apr69="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Input VAT 5%')"
mycursor.execute(apr69)
tab419 = mycursor.fetchall()
may69="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Input VAT 5%')"
mycursor.execute(may69)
tab420 = mycursor.fetchall()
jun69="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Input VAT 5%')"
mycursor.execute(jun69)
tab421 = mycursor.fetchall()

jan70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Krishi Kalyan Cess Payable')"
mycursor.execute(jan70)
tab422 = mycursor.fetchall()
feb70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Krishi Kalyan Cess Payable')"
mycursor.execute(feb70)
tab423 = mycursor.fetchall()
mar70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Krishi Kalyan Cess Payable')"
mycursor.execute(mar70)
tab424 = mycursor.fetchall()
apr70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Krishi Kalyan Cess Payable')"
mycursor.execute(apr70)
tab425 = mycursor.fetchall()
may70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Krishi Kalyan Cess Payable')"
mycursor.execute(may70)
tab426 = mycursor.fetchall()
jun70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Krishi Kalyan Cess Payable')"
mycursor.execute(jun70)
tab427 = mycursor.fetchall()

jan71="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Krishi Kalyan Cess Suspense')"
mycursor.execute(jan71)
tab428 = mycursor.fetchall()
feb71="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Krishi Kalyan Cess Suspense')"
mycursor.execute(feb71)
tab429 = mycursor.fetchall()
mar71="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Krishi Kalyan Cess Suspense')"
mycursor.execute(mar71)
tab430 = mycursor.fetchall()
apr71="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Krishi Kalyan Cess Suspense')"
mycursor.execute(apr71)
tab431 = mycursor.fetchall()
may71="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Krishi Kalyan Cess Suspense')"
mycursor.execute(may71)
tab432 = mycursor.fetchall()
jun71="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Krishi Kalyan Cess Suspense')"
mycursor.execute(jun71)
tab433 = mycursor.fetchall()

jan72="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output CGST')"
mycursor.execute(jan72)
tab434 = mycursor.fetchall()
feb72="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output CGST')"
mycursor.execute(feb72)
tab435 = mycursor.fetchall()
mar72="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output CGST')"
mycursor.execute(mar72)
tab436 = mycursor.fetchall()
apr72="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output CGST')"
mycursor.execute(apr72)
tab437 = mycursor.fetchall()
may72="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output CGST')"
mycursor.execute(may72)
tab438 = mycursor.fetchall()
jun72="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output CGST')"
mycursor.execute(jun72)
tab439 = mycursor.fetchall()

jan73="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output CGST Tax RCM')"
mycursor.execute(jan73)
tab440 = mycursor.fetchall()
feb73="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output CGST Tax RCM')"
mycursor.execute(feb73)
tab441 = mycursor.fetchall()
mar73="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output CGST Tax RCM')"
mycursor.execute(mar73)
tab442 = mycursor.fetchall()
apr73="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output CGST Tax RCM')"
mycursor.execute(apr73)
tab443 = mycursor.fetchall()
may73="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output CGST Tax RCM')"
mycursor.execute(may73)
tab444 = mycursor.fetchall()
jun73="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output CGST Tax RCM')"
mycursor.execute(jun73)
tab445 = mycursor.fetchall()

jan74="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output CGST 2%')"
mycursor.execute(jan74)
tab446 = mycursor.fetchall()
feb74="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output CGST 2%')"
mycursor.execute(feb74)
tab447 = mycursor.fetchall()
mar74="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output CGST 2%')"
mycursor.execute(mar74)
tab448 = mycursor.fetchall()
apr74="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output CGST 2%')"
mycursor.execute(apr74)
tab449 = mycursor.fetchall()
may74="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output CGST 2%')"
mycursor.execute(may74)
tab450 = mycursor.fetchall()
jun74="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output CGST 2%')"
mycursor.execute(jun74)
tab451 = mycursor.fetchall()

jan75="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output IGST')"
mycursor.execute(jan75)
tab452 = mycursor.fetchall()
feb75="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output IGST')"
mycursor.execute(feb75)
tab453 = mycursor.fetchall()
mar75="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output IGST')"
mycursor.execute(mar75)
tab454 = mycursor.fetchall()
apr75="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output IGST')"
mycursor.execute(apr75)
tab455 = mycursor.fetchall()
may75="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output IGST')"
mycursor.execute(may75)
tab456 = mycursor.fetchall()
jun75="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output IGST')"
mycursor.execute(jun75)
tab457 = mycursor.fetchall()

jan76="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output IGST Tax RCM')"
mycursor.execute(jan76)
tab458 = mycursor.fetchall()
feb76="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output IGST Tax RCM')"
mycursor.execute(feb76)
tab459 = mycursor.fetchall()
mar76="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output IGST Tax RCM')"
mycursor.execute(mar76)
tab460 = mycursor.fetchall()
apr76="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output IGST Tax RCM')"
mycursor.execute(apr76)
tab461 = mycursor.fetchall()
may76="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output IGST Tax RCM')"
mycursor.execute(may76)
tab462 = mycursor.fetchall()
jun76="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output IGST Tax RCM')"
mycursor.execute(jun76)
tab463 = mycursor.fetchall()

jan77="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output Krishi Kalyan Cess RCM')"
mycursor.execute(jan77)
tab464 = mycursor.fetchall()
feb77="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output Krishi Kalyan Cess RCM')"
mycursor.execute(feb77)
tab465 = mycursor.fetchall()
mar77="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output Krishi Kalyan Cess RCM')"
mycursor.execute(mar77)
tab466 = mycursor.fetchall()
apr77="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output Krishi Kalyan Cess RCM')"
mycursor.execute(apr77)
tab467 = mycursor.fetchall()
may77="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output Krishi Kalyan Cess RCM')"
mycursor.execute(may77)
tab468 = mycursor.fetchall()
jun77="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output Krishi Kalyan Cess RCM')"
mycursor.execute(jun77)
tab469 = mycursor.fetchall()

jan78="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output SGST')"
mycursor.execute(jan78)
tab470 = mycursor.fetchall()
feb78="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output SGST')"
mycursor.execute(feb78)
tab471 = mycursor.fetchall()
mar78="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output SGST')"
mycursor.execute(mar78)
tab472 = mycursor.fetchall()
apr78="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output SGST')"
mycursor.execute(apr78)
tab473 = mycursor.fetchall()
may78="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output SGST')"
mycursor.execute(may78)
tab474 = mycursor.fetchall()
jun78="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output SGST')"
mycursor.execute(jun78)
tab475 = mycursor.fetchall()

jan79="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output SGST Tax RCM')"
mycursor.execute(jan79)
tab476 = mycursor.fetchall()
feb79="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output SGST Tax RCM')"
mycursor.execute(feb79)
tab477 = mycursor.fetchall()
mar79="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output SGST Tax RCM')"
mycursor.execute(mar79)
tab478 = mycursor.fetchall()
apr79="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output SGST Tax RCM')"
mycursor.execute(apr79)
tab479 = mycursor.fetchall()
may79="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output SGST Tax RCM')"
mycursor.execute(may79)
tab480 = mycursor.fetchall()
jun79="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output SGST Tax RCM')"
mycursor.execute(jun79)
tab481 = mycursor.fetchall()

jan80="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output VAT 14%')"
mycursor.execute(jan80)
tab482 = mycursor.fetchall()
feb80="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output VAT 14%')"
mycursor.execute(feb80)
tab483 = mycursor.fetchall()
mar80="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output VAT 14%')"
mycursor.execute(mar80)
tab484 = mycursor.fetchall()
apr80="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output VAT 14%')"
mycursor.execute(apr80)
tab485 = mycursor.fetchall()
may80="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output VAT 14%')"
mycursor.execute(may80)
tab486 = mycursor.fetchall()
jun80="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output VAT 14%')"
mycursor.execute(jun80)
tab487 = mycursor.fetchall()

jan81="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output VAT 4%')"
mycursor.execute(jan81)
tab488 = mycursor.fetchall()
feb81="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output VAT 4%')"
mycursor.execute(feb81)
tab489 = mycursor.fetchall()
mar81="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output VAT 4%')"
mycursor.execute(mar81)
tab490 = mycursor.fetchall()
apr81="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output VAT 4%')"
mycursor.execute(apr81)
tab491 = mycursor.fetchall()
may81="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output VAT 4%')"
mycursor.execute(may81)
tab492 = mycursor.fetchall()
jun81="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output VAT 4%')"
mycursor.execute(jun81)
tab493 = mycursor.fetchall()

jan82="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Output VAT 5%')"
mycursor.execute(jan82)
tab494 = mycursor.fetchall()
feb82="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Output VAT 5%')"
mycursor.execute(feb82)
tab495 = mycursor.fetchall()
mar82="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Output VAT 5%')"
mycursor.execute(mar82)
tab496 = mycursor.fetchall()
apr82="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Output VAT 5%')"
mycursor.execute(apr82)
tab497 = mycursor.fetchall()
may82="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Output VAT 5%')"
mycursor.execute(may82)
tab498 = mycursor.fetchall()
jun82="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Output VAT 5%')"
mycursor.execute(jun82)
tab499 = mycursor.fetchall()
jan83="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Service Tax Payable')"
mycursor.execute(jan83)
tab500 = mycursor.fetchall()
feb83="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Service Tax Payable')"
mycursor.execute(feb83)
tab501 = mycursor.fetchall()
mar83="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Service Tax Payable')"
mycursor.execute(mar83)
tab502 = mycursor.fetchall()
apr83="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Service Tax Payable')"
mycursor.execute(apr83)
tab503 = mycursor.fetchall()
may83="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Service Tax Payable')"
mycursor.execute(may83)
tab504 = mycursor.fetchall()
jun83="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Service Tax Payable')"
mycursor.execute(jun83)
tab505 = mycursor.fetchall()

jan84="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Service Tax  Suspense')"
mycursor.execute(jan84)
tab506 = mycursor.fetchall()
feb84="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Service Tax  Suspense')"
mycursor.execute(feb84)
tab507 = mycursor.fetchall()
mar84="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Service Tax  Suspense')"
mycursor.execute(mar84)
tab508 = mycursor.fetchall()
apr84="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Service Tax  Suspense')"
mycursor.execute(apr84)
tab509 = mycursor.fetchall()
may84="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Service Tax  Suspense')"
mycursor.execute(may84)
tab510 = mycursor.fetchall()
jun84="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Service Tax  Suspense')"
mycursor.execute(jun84)
tab511 = mycursor.fetchall()

jan85="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='SGST Payable')"
mycursor.execute(jan85)
tab512 = mycursor.fetchall()
feb85="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='SGST Payable')"
mycursor.execute(feb85)
tab513 = mycursor.fetchall()
mar85="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='SGST Payable')"
mycursor.execute(mar85)
tab514 = mycursor.fetchall()
apr85="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='SGST Payable')"
mycursor.execute(apr85)
tab515 = mycursor.fetchall()
may85="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='SGST Payable')"
mycursor.execute(may85)
tab516 = mycursor.fetchall()
jun85="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='SGST Payable')"
mycursor.execute(jun85)
tab517 = mycursor.fetchall()

jan86="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Swachh Bharat Cess Payable')"
mycursor.execute(jan86)
tab518 = mycursor.fetchall()
feb86="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Swachh Bharat Cess Payable')"
mycursor.execute(feb86)
tab519 = mycursor.fetchall()
mar86="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Swachh Bharat Cess Payable')"
mycursor.execute(mar86)
tab520 = mycursor.fetchall()
apr86="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Swachh Bharat Cess Payable')"
mycursor.execute(apr86)
tab521 = mycursor.fetchall()
may86="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Swachh Bharat Cess Payable')"
mycursor.execute(may86)
tab522 = mycursor.fetchall()
jun86="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Swachh Bharat Cess Payable')"
mycursor.execute(jun86)
tab523 = mycursor.fetchall()

jan87="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Swachh Bharat Cess Suspense')"
mycursor.execute(jan87)
tab524 = mycursor.fetchall()
feb87="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Swachh Bharat Cess Suspense')"
mycursor.execute(feb87)
tab525 = mycursor.fetchall()
mar87="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Swachh Bharat Cess Suspense')"
mycursor.execute(mar87)
tab526 = mycursor.fetchall()
apr87="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Swachh Bharat Cess Suspense')"
mycursor.execute(apr87)
tab527 = mycursor.fetchall()
may87="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Swachh Bharat Cess Suspense')"
mycursor.execute(may87)
tab528 = mycursor.fetchall()
jun87="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Swachh Bharat Cess Suspense')"
mycursor.execute(jun87)
tab529 = mycursor.fetchall()

jan88="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='TDS Payable')"
mycursor.execute(jan88)
tab530 = mycursor.fetchall()
feb88="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='TDS Payable')"
mycursor.execute(feb88)
tab531 = mycursor.fetchall()
mar88="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='TDS Payable')"
mycursor.execute(mar88)
tab532 = mycursor.fetchall()
apr88="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='TDS Payable')"
mycursor.execute(apr88)
tab533 = mycursor.fetchall()
may88="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='TDS Payable')"
mycursor.execute(may88)
tab534 = mycursor.fetchall()
jun88="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='TDS Payable')"
mycursor.execute(jun88)
tab535 = mycursor.fetchall()

jan89="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='VAT Suspense')"
mycursor.execute(jan89)
tab536 = mycursor.fetchall()
feb89="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='VAT Suspense')"
mycursor.execute(feb89)
tab537 = mycursor.fetchall()
mar89="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='VAT Suspense')"
mycursor.execute(mar89)
tab538 = mycursor.fetchall()
apr89="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='VAT Suspense')"
mycursor.execute(apr89)
tab539 = mycursor.fetchall()
may89="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='VAT Suspense')"
mycursor.execute(may89)
tab540 = mycursor.fetchall()
jun89="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='VAT Suspense')"
mycursor.execute(jun89)
tab541 = mycursor.fetchall()

jan90="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Opening Balance Equity')"
mycursor.execute(jan90)
tab542 = mycursor.fetchall()
feb90="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Opening Balance Equity')"
mycursor.execute(feb90)
tab543 = mycursor.fetchall()
mar90="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Opening Balance Equity')"
mycursor.execute(mar90)
tab544 = mycursor.fetchall()
apr90="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Opening Balance Equity')"
mycursor.execute(apr90)
tab545 = mycursor.fetchall()
may90="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Opening Balance Equity')"
mycursor.execute(may90)
tab546 = mycursor.fetchall()
jun90="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Opening Balance Equity')"
mycursor.execute(jun90)
tab547 = mycursor.fetchall()

jan91="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Retained Earnings')"
mycursor.execute(jan91)
tab548 = mycursor.fetchall()
feb91="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Retained Earnings')"
mycursor.execute(feb91)
tab549 = mycursor.fetchall()
mar91="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Retained Earnings')"
mycursor.execute(mar91)
tab550 = mycursor.fetchall()
apr91="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Retained Earnings')"
mycursor.execute(apr91)
tab551 = mycursor.fetchall()
may91="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Retained Earnings')"
mycursor.execute(may91)
tab552 = mycursor.fetchall()
jun91="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Retained Earnings')"
mycursor.execute(jun91)
tab553 = mycursor.fetchall()

jan92="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Billable Expense Income')"
mycursor.execute(jan92)
tab554 = mycursor.fetchall()
feb92="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Billable Expense Income')"
mycursor.execute(feb92)
tab555 = mycursor.fetchall()
mar92="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Billable Expense Income')"
mycursor.execute(mar92)
tab556 = mycursor.fetchall()
apr92="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Billable Expense Income')"
mycursor.execute(apr92)
tab557 = mycursor.fetchall()
may92="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Billable Expense Income')"
mycursor.execute(may92)
tab558 = mycursor.fetchall()
jun92="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Billable Expense Income')"
mycursor.execute(jun92)
tab559 = mycursor.fetchall()

jan93="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Consulting Income')"
mycursor.execute(jan93)
tab560 = mycursor.fetchall()
feb93="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Consulting Income')"
mycursor.execute(feb93)
tab561 = mycursor.fetchall()
mar93="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Consulting Income')"
mycursor.execute(mar93)
tab562 = mycursor.fetchall()
apr93="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Consulting Income')"
mycursor.execute(apr93)
tab563 = mycursor.fetchall()
may93="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Consulting Income')"
mycursor.execute(may93)
tab564 = mycursor.fetchall()
jun93="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Consulting Income')"
mycursor.execute(jun93)
tab565 = mycursor.fetchall()

jan94="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Product Sales')"
mycursor.execute(jan94)
tab566 = mycursor.fetchall()
feb94="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Product Sales')"
mycursor.execute(feb94)
tab567 = mycursor.fetchall()
mar94="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Product Sales')"
mycursor.execute(mar94)
tab568 = mycursor.fetchall()
apr94="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Product Sales')"
mycursor.execute(apr94)
tab569 = mycursor.fetchall()
may94="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Product Sales')"
mycursor.execute(may94)
tab570 = mycursor.fetchall()
jun94="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Product Sales')"
mycursor.execute(jun94)
tab571 = mycursor.fetchall()

jan95="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Sales')"
mycursor.execute(jan95)
tab572 = mycursor.fetchall()
feb95="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Sales')"
mycursor.execute(feb95)
tab573 = mycursor.fetchall()
mar95="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Sales')"
mycursor.execute(mar95)
tab574 = mycursor.fetchall()
apr95="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Sales')"
mycursor.execute(apr95)
tab575 = mycursor.fetchall()
may95="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Sales')"
mycursor.execute(may95)
tab576 = mycursor.fetchall()
jun95="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Sales')"
mycursor.execute(jun95)
tab577 = mycursor.fetchall()

jan96="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Sales - Hardware')"
mycursor.execute(jan96)
tab578 = mycursor.fetchall()
feb96="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Sales - Hardware')"
mycursor.execute(feb96)
tab579 = mycursor.fetchall()
mar96="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Sales - Hardware')"
mycursor.execute(mar96)
tab580 = mycursor.fetchall()
apr96="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Sales - Hardware')"
mycursor.execute(apr96)
tab581 = mycursor.fetchall()
may96="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Sales - Hardware')"
mycursor.execute(may96)
tab582 = mycursor.fetchall()
jun96="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Sales - Hardware')"
mycursor.execute(jun96)
tab583 = mycursor.fetchall()

jan97="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Sales - Software')"
mycursor.execute(jan97)
tab584 = mycursor.fetchall()
feb97="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Sales - Software')"
mycursor.execute(feb97)
tab585 = mycursor.fetchall()
mar97="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Sales - Software')"
mycursor.execute(mar97)
tab586 = mycursor.fetchall()
apr97="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Sales - Software')"
mycursor.execute(apr97)
tab587 = mycursor.fetchall()
may97="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Sales - Software')"
mycursor.execute(may97)
tab588 = mycursor.fetchall()
jun97="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Sales - Software')"
mycursor.execute(jun97)
tab589 = mycursor.fetchall()

jan98="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Sales - Support and Maintenance')"
mycursor.execute(jan98)
tab590 = mycursor.fetchall()
feb98="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Sales - Support and Maintenance')"
mycursor.execute(feb98)
tab591 = mycursor.fetchall()
mar98="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Sales - Support and Maintenance')"
mycursor.execute(mar98)
tab592 = mycursor.fetchall()
apr98="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Sales - Support and Maintenance')"
mycursor.execute(apr98)
tab593 = mycursor.fetchall()
may98="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Sales - Support and Maintenance')"
mycursor.execute(may98)
tab594 = mycursor.fetchall()
jun98="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Sales - Support and Maintenance')"
mycursor.execute(jun98)
tab595 = mycursor.fetchall()

jan99="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Sales  Discounts')"
mycursor.execute(jan99)
tab596 = mycursor.fetchall()
feb99="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Sales  Discounts')"
mycursor.execute(feb99)
tab597 = mycursor.fetchall()
mar99="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Sales  Discounts')"
mycursor.execute(mar99)
tab598 = mycursor.fetchall()
apr99="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Sales  Discounts')"
mycursor.execute(apr99)
tab599 = mycursor.fetchall()
may99="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Sales  Discounts')"
mycursor.execute(may99)
tab600 = mycursor.fetchall()
jun99="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Sales  Discounts')"
mycursor.execute(jun99)
tab601 = mycursor.fetchall()

jan100="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Sales  of Product Income')"
mycursor.execute(jan100)
tab602 = mycursor.fetchall()
feb100="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Sales  of Product Income')"
mycursor.execute(feb100)
tab603 = mycursor.fetchall()
mar100="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Sales  of Product Income')"
mycursor.execute(mar100)
tab604 = mycursor.fetchall()
apr100="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Sales  of Product Income')"
mycursor.execute(apr100)
tab605 = mycursor.fetchall()
may100="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Sales  of Product Income')"
mycursor.execute(may100)
tab606 = mycursor.fetchall()
jun100="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Sales  of Product Income')"
mycursor.execute(jun100)
tab607 = mycursor.fetchall()

jan101="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Uncategorised Income')"
mycursor.execute(jan101)
tab608 = mycursor.fetchall()
feb101="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Uncategorised Income')"
mycursor.execute(feb101)
tab609 = mycursor.fetchall()
mar101="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Uncategorised Income')"
mycursor.execute(mar101)
tab610 = mycursor.fetchall()
apr101="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Uncategorised Income')"
mycursor.execute(apr101)
tab611 = mycursor.fetchall()
may101="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Uncategorised Income')"
mycursor.execute(may101)
tab612 = mycursor.fetchall()
jun101="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Uncategorised Income')"
mycursor.execute(jun101)
tab613 = mycursor.fetchall()

jan102="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Cost of sales')"
mycursor.execute(jan102)
tab614 = mycursor.fetchall()
feb102="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Cost of sales')"
mycursor.execute(feb102)
tab615 = mycursor.fetchall()
mar102="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Cost of sales')"
mycursor.execute(mar102)
tab616 = mycursor.fetchall()
apr102="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Cost of sales')"
mycursor.execute(apr102)
tab617 = mycursor.fetchall()
may102="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Cost of sales')"
mycursor.execute(may102)
tab618 = mycursor.fetchall()
jun102="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Cost of sales')"
mycursor.execute(jun102)
tab619 = mycursor.fetchall()

jan103="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Equipment Rental for Jobs')"
mycursor.execute(jan103)
tab620 = mycursor.fetchall()
feb103="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Equipment Rental for Jobs')"
mycursor.execute(feb103)
tab621 = mycursor.fetchall()
mar103="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Equipment Rental for Jobs')"
mycursor.execute(mar103)
tab622 = mycursor.fetchall()
apr103="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Equipment Rental for Jobs')"
mycursor.execute(apr103)
tab623 = mycursor.fetchall()
may103="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Equipment Rental for Jobs')"
mycursor.execute(may103)
tab624 = mycursor.fetchall()
jun103="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Equipment Rental for Jobs')"
mycursor.execute(jun103)
tab625 = mycursor.fetchall()

jan104="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='January' AND(category1='Freight and Shipping Costs')"
mycursor.execute(jan104)
tab626 = mycursor.fetchall()
feb104="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='February' AND(category1='Freight and Shipping Costs')"
mycursor.execute(feb104)
tab627 = mycursor.fetchall()
mar70="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='March' AND(category1='Freight and Shipping Costs')"
mycursor.execute(mar70)
tab628 = mycursor.fetchall()
apr104="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='April' AND(category1='Freight and Shipping Costs')"
mycursor.execute(apr104)
tab629 = mycursor.fetchall()
may104="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='May' AND(category1='Freight and Shipping Costs')"
mycursor.execute(may104)
tab630 = mycursor.fetchall()
jun104="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Freight and Shipping Costs')"
mycursor.execute(jun104)
tab631 = mycursor.fetchall()





# def fetchdata():
query="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Advertising/Promotional' "
mycursor.execute(query)
table = mycursor.fetchall()
query1="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Bank Charges' "
mycursor.execute(query1)
table1 = mycursor.fetchall()
query2="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Business Licenses and Permits' "
mycursor.execute(query2)
table2 = mycursor.fetchall()
query3="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Charitable Contributions' "
mycursor.execute(query3)
table3 = mycursor.fetchall()
query4="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Computer and Internet Expense' "
mycursor.execute(query4)
table4 = mycursor.fetchall()
query5="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Continuing Education' "
mycursor.execute(query5)
table5 = mycursor.fetchall()
query6="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Depreciation Expense' "
mycursor.execute(query6)
table6 = mycursor.fetchall()
query7="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Dues and Subscriptions' "
mycursor.execute(query7)
table7 = mycursor.fetchall()
query8="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Housekeeping Charges' "
mycursor.execute(query8)
table8 = mycursor.fetchall()
query9="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Expense' "
mycursor.execute(query9)
table9 = mycursor.fetchall()
query10="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Expense-General Liability Insurance' "
mycursor.execute(query10)
table10 = mycursor.fetchall()
query11="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Expense-Health Insurance' "
mycursor.execute(query11)
table11 = mycursor.fetchall()
query12="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Expense-Life and Disability Insurance' "
mycursor.execute(query12)
table12 = mycursor.fetchall()
query13="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Expense-Professional Liabilitynsurance' "
mycursor.execute(query13)
table13 = mycursor.fetchall()
query14="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Interest Expense' "
mycursor.execute(query14)
table14 = mycursor.fetchall()
query15="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Meals and entertainment' "
mycursor.execute(query15)
table15 = mycursor.fetchall()
query16="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Office Supplies' "
mycursor.execute(query16)
table16 = mycursor.fetchall()
query17="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Postage and Delivery' "
mycursor.execute(query17)
table17 = mycursor.fetchall()
query18="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Printing and Reproduction' "
mycursor.execute(query18)
table18 = mycursor.fetchall()
query19="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Professional Fees' "
mycursor.execute(query19)
table19 = mycursor.fetchall()
query20="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Purchases' "
mycursor.execute(query20)
table20 = mycursor.fetchall()
query21="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Rent Expense' "
mycursor.execute(query21)
table21 = mycursor.fetchall()
query22="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Repair and maintenance' "
mycursor.execute(query22)
table22 = mycursor.fetchall()
query23="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Small Tools and Equipment' "
mycursor.execute(query23)
table23 = mycursor.fetchall()
query24="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Swachh Bharat Cess Expense' "
mycursor.execute(query24)
table24 = mycursor.fetchall()
query25="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Taxes - Property' "
mycursor.execute(query25)
table25 = mycursor.fetchall()
query26="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Telephone Expense' "
mycursor.execute(query26)
table26 = mycursor.fetchall()
query27="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Travel Expense' "
mycursor.execute(query27)
table27 = mycursor.fetchall()
query28="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Uncategorised Expense' "
mycursor.execute(query28)
table28 = mycursor.fetchall()
query29="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Utilities' "
mycursor.execute(query29)
table29 = mycursor.fetchall()
query30="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Cash and cash equivalents' "
mycursor.execute(query30)
table30 = mycursor.fetchall()
query31="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Accounts Receivable (Debtors)' "
mycursor.execute(query31)
table31 = mycursor.fetchall()
query32="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred CGST' "
mycursor.execute(query32)
table32 = mycursor.fetchall()
query33="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred GST Input Credit' "
mycursor.execute(query33)
table33 = mycursor.fetchall()
query34="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred IGST' "
mycursor.execute(query34)
table34 = mycursor.fetchall()
query35="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
mycursor.execute(query35)
table35 = mycursor.fetchall()
query36="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Service Tax Input Credit' "
mycursor.execute(query36)
table36 = mycursor.fetchall()
query37="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred SGST' "
mycursor.execute(query37)
table37 = mycursor.fetchall()
query38="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred VAT Input Credit' "
mycursor.execute(query38)
table38 = mycursor.fetchall()
query39="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='GST Refund' "
mycursor.execute(query39)
table39 = mycursor.fetchall()
query40="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Inventory Asset' "
mycursor.execute(query40)
table40 = mycursor.fetchall()
query41="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Krishi Kalyan Cess Refund' "
mycursor.execute(query41)
table41 = mycursor.fetchall()
query42="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Prepaid Insurance' "
mycursor.execute(query42)
table42 = mycursor.fetchall()
query43="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Service Tax Refund' "
mycursor.execute(query43)
table43 = mycursor.fetchall()
query44="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='TDS Receivable' "
mycursor.execute(query44)
table44 = mycursor.fetchall()
query45="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Uncategorised Asset' "
mycursor.execute(query45)
table45 = mycursor.fetchall()
query46="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Undeposited Funds' "
mycursor.execute(query46)
table46 = mycursor.fetchall()
query47="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Accumulated Depreciation' "
mycursor.execute(query47)
table47 = mycursor.fetchall()
query48="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Buildings and Improvements' "
mycursor.execute(query48)
table48 = mycursor.fetchall()
query49="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Furniture and Equipment' "
mycursor.execute(query49)
table49 = mycursor.fetchall()
query50="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Land' "
mycursor.execute(query50)
table50 = mycursor.fetchall()
query51="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Leasehold Improvements' "
mycursor.execute(query51)
table51 = mycursor.fetchall()
query52="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Vehicles' "
mycursor.execute(query52)
table52 = mycursor.fetchall()
query53="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='CGST Payable' "
mycursor.execute(query53)
table53 = mycursor.fetchall()
query54="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='CST Payable' "
mycursor.execute(query54)
table54 = mycursor.fetchall()
query55="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='CST Suspense' "
mycursor.execute(query55)
table55 = mycursor.fetchall()
query56="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='GST Payable' "
mycursor.execute(query56)
table56 = mycursor.fetchall()
query57="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='GST Suspense' "
mycursor.execute(query57)
table57 = mycursor.fetchall()
query58="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='IGST Payable' "
mycursor.execute(query58)
table58 = mycursor.fetchall()
query59="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input CGST' "
mycursor.execute(query59)
table59 = mycursor.fetchall()
query60="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input CGST Tax RCM' "
mycursor.execute(query60)
table60 = mycursor.fetchall()
query61="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input IGST' "
mycursor.execute(query61)
table61 = mycursor.fetchall()
query62="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input IGST Tax RCM' "
mycursor.execute(query62)
table62 = mycursor.fetchall()
query63="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input Krishi Kalyan Cess' "
mycursor.execute(query63)
table63 = mycursor.fetchall()
query64="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input Krishi Kalyan Cess RCM' "
mycursor.execute(query64)
table64 = mycursor.fetchall()
query65="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input Service Tax' "
mycursor.execute(query65)
table65 = mycursor.fetchall()
query66="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input Service Tax RCM' "
mycursor.execute(query66)
table66 = mycursor.fetchall()
query67="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input SGST' "
mycursor.execute(query67)
table67 = mycursor.fetchall()
query68="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input SGST Tax RCM' "
mycursor.execute(query68)
table68 = mycursor.fetchall()
query69="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input VAT 14%' "
mycursor.execute(query69)
table69 = mycursor.fetchall()
query70="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input VAT 4%' "
mycursor.execute(query70)
table70 = mycursor.fetchall()
query71="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Input VAT 5%' "
mycursor.execute(query71)
table71 = mycursor.fetchall()
query72="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Krishi Kalyan Cess Payable' "
mycursor.execute(query72)
table72 = mycursor.fetchall()
query73="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Krishi Kalyan Cess Suspense' "
mycursor.execute(query73)
table73 = mycursor.fetchall()
query74="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output CGST' "
mycursor.execute(query74)
table74 = mycursor.fetchall()
query75="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output CGST Tax RCM' "
mycursor.execute(query75)
table75 = mycursor.fetchall()
query76="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output CST 2%' "
mycursor.execute(query76)
table76 = mycursor.fetchall()
query77="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output IGST' "
mycursor.execute(query77)
table77 = mycursor.fetchall()
query78="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output IGST Tax RCM' "
mycursor.execute(query78)
table78 = mycursor.fetchall()
query79="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output Krishi Kalyan Cess' "
mycursor.execute(query79)
table79 = mycursor.fetchall()
query80="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output Krishi Kalyan Cess RCM' "
mycursor.execute(query80)
table80 = mycursor.fetchall()
query81="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output Service Tax' "
mycursor.execute(query81)
table81 = mycursor.fetchall()
query82="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output Service Tax RCM' "
mycursor.execute(query82)
table82 = mycursor.fetchall()
query83="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output SGST' "
mycursor.execute(query83)
table83 = mycursor.fetchall()
query84="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output SGST Tax RCM' "
mycursor.execute(query84)
table84 = mycursor.fetchall()
query85="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output VAT 14%' "
mycursor.execute(query85)
table85 = mycursor.fetchall()
query86="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output VAT 4%' "
mycursor.execute(query86)
table86 = mycursor.fetchall()
query87="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Output VAT 5%' "
mycursor.execute(query87)
table87 = mycursor.fetchall()
query88="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Service Tax Payable' "
mycursor.execute(query88)
table88 = mycursor.fetchall()
query89="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Service Tax Suspense' "
mycursor.execute(query89)
table89 = mycursor.fetchall()
query90="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='SGST Payable' "
mycursor.execute(query90)
table90 = mycursor.fetchall()
query91="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Swachh Bharat Cess Payable' "
mycursor.execute(query91)
table91 = mycursor.fetchall()
query92="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Swachh Bharat Cess Suspense' "
mycursor.execute(query92)
table92 = mycursor.fetchall()
query93="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='TDS Payable' "
mycursor.execute(query93)
table93 = mycursor.fetchall()
query94="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='VAT Suspense' "
mycursor.execute(query94)
table94 = mycursor.fetchall()
query95="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Opening Balance Equity' "
mycursor.execute(query95)
table95 = mycursor.fetchall()
query96="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Retained Earnings' "
mycursor.execute(query96)
table96 = mycursor.fetchall()
query97="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Billable Expense Income' "
mycursor.execute(query97)
table97 = mycursor.fetchall()
query98="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Consulting Income' "
mycursor.execute(query98)
table98 = mycursor.fetchall()
query99="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Product Sales' "
mycursor.execute(query99)
table99 = mycursor.fetchall()
query100="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Sales' "
mycursor.execute(query100)
table100 = mycursor.fetchall()
query101="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Sales - Hardware' "
mycursor.execute(query101)
table101 = mycursor.fetchall()
query102="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Sales - Software' "
mycursor.execute(query102)
table102 = mycursor.fetchall()
query103="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Sales - Support and Maintenance' "
mycursor.execute(query103)
table103 = mycursor.fetchall()
query104="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Sales Discounts' "
mycursor.execute(query104)
table104 = mycursor.fetchall()
query105="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Sales of Product Income' "
mycursor.execute(query105)
table105 = mycursor.fetchall()
query106="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Uncategorised Income' "
mycursor.execute(query106)
table106 = mycursor.fetchall()

query107="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Cost of sales' "
mycursor.execute(query107)
table107 = mycursor.fetchall()
query108="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Equipment Rental for Jobs' "
mycursor.execute(query108)
table108 = mycursor.fetchall()
query109="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Freight and Shipping Costs' "
mycursor.execute(query109)
table109 = mycursor.fetchall()
query110="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Merchant Account Fees' "
mycursor.execute(query110)
table110 = mycursor.fetchall()
query111="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Purchases - Hardware for Resale' "
mycursor.execute(query111)
table111 = mycursor.fetchall()
query112="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Purchases - Software for Resale' "
mycursor.execute(query112)
table112 = mycursor.fetchall()
query113="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Subcontracted Services' "
mycursor.execute(query113)
table113 = mycursor.fetchall()
query114="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Tools and Craft Supplies' "
mycursor.execute(query114)
table114 = mycursor.fetchall()
query115="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Finance Charge Income' "
mycursor.execute(query115)
table115 = mycursor.fetchall()
query116="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Proceeds Received' "
mycursor.execute(query116)
table116 = mycursor.fetchall()
query117="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Interest Income' "
mycursor.execute(query117)
table117 = mycursor.fetchall()
query118="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Proceeds from Sale of Assets' "
mycursor.execute(query118)
table118 = mycursor.fetchall()
query119="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Shipping and Delivery Income' "
mycursor.execute(query119)
table119 = mycursor.fetchall()
query120="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Ask My Accountant' "
mycursor.execute(query120)
table120 = mycursor.fetchall()
query121="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='CGST write-off' "
mycursor.execute(query121)
table121 = mycursor.fetchall()
query122="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='GST write-off' "
mycursor.execute(query122)
table122 = mycursor.fetchall()
query123="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='IGST write-off' "
mycursor.execute(query123)
table123 = mycursor.fetchall()
query124="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Miscellaneous Expense' "
mycursor.execute(query124)
table124 = mycursor.fetchall()
query125="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Political Contributions' "
mycursor.execute(query125)
table125 = mycursor.fetchall()
query126="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='SGST write-off' "
mycursor.execute(query126)
table126 = mycursor.fetchall()
query127="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Tax write-of' "
mycursor.execute(query127)
table127 = mycursor.fetchall()
query128="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Vehicle Expenses' "
mycursor.execute(query128)
table128 = mycursor.fetchall()
# query129="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='' "
# mycursor.execute(query129)
# table129 = mycursor.fetchall()
# query130="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='' "
# mycursor.execute(query130)
# table130 = mycursor.fetchall()
# query131="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query131)
# table131 = mycursor.fetchall()
# query132="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query132)
# table132 = mycursor.fetchall()
# query133="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query133)
# table133 = mycursor.fetchall()
# query134="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query134)
# table134 = mycursor.fetchall()
# query135="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query135)
# table135 = mycursor.fetchall()
# query136="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query136)
# table136 = mycursor.fetchall()
# query137="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query137)
# table137 = mycursor.fetchall()
# query138="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query138)
# table138 = mycursor.fetchall()
# query139="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query139)
# table139 = mycursor.fetchall()
# query140="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query140)
# table140 = mycursor.fetchall()
# query141="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query141)
# table141 = mycursor.fetchall()
# query142="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query142)
# table142 = mycursor.fetchall()
# query143="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query143)
# table143 = mycursor.fetchall()
# query144="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query144)
# table144 = mycursor.fetchall()
# query145="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query145)
# table145 = mycursor.fetchall()
# query146="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query146)
# table146 = mycursor.fetchall()
# query147="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query147)
# table147 = mycursor.fetchall()
# query148="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query148)
# table148 = mycursor.fetchall()
# query149="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query149)
# table149 = mycursor.fetchall()
# query150="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Deferred Krishi Kalyan Cess Input Credit' "
# mycursor.execute(query150)
# table150 = mycursor.fetchall()


mycursor.close()
mydb.close()

window = tk.Tk()
window.title("finsYs")
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
window.geometry("%dx%d" %(width,height))
window['bg']='#2f516a'
wrappen=ttk.LabelFrame(window)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=13500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((40,40),window=heading_frame,anchor="nw")
headingfont=font.Font(family='Arial', size=25,)
addcustomer_heading= tk.Label(heading_frame, text="CASH FLOW ANALYZER",fg='#fff',bg='#243e55',height=2,bd=1,relief="raised",font=headingfont,width=76)
addcustomer_heading.pack()

#form fields
sub_headingfont=font.Font(family='Times New Roman', size=26)
form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
mycanvas.create_window((40,140),window=form_frame,anchor="nw")



label=Label(form_frame,text="JANUARY",bg='#243e55' ,fg="white",font=('Arial',13))
label.place(x=396,y=160)

label=Label(form_frame,text="FEBRUARY",bg='#243e55' ,fg="white",font=('Arial',13))
label.place(x=523,y=160)

label=Label(form_frame,text="MARCH",bg='#243e55' ,fg="white",font=('Arial',13))
label.place(x=656,y=160)
label=Label(form_frame,text="APRIL",bg='#243e55' ,fg="white",font=('Arial',13))
label.place(x=788,y=160)
label=Label(form_frame,text="MAY",bg='#243e55' ,fg="white",font=('Arial',13))
label.place(x=918,y=160)
label=Label(form_frame,text="JUNE",bg='#243e55' ,fg="white",font=('Arial',13))
label.place(x=1047,y=160)
label=Label(form_frame,text="TOTAL",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=1173,y=160)

menu= StringVar()
menu.set("Filter By")
drop= OptionMenu(form_frame, menu,"Date","Month","Month range")
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))
drop.place(x=1250,y=50,)
wrappen.pack(fill='both',expand='yes',)
# sub_frame1=Frame(mycanvas,width=120,height=37,bg='#2f516a')
# mycanvas.create_window((420,370),window=sub_frame1,anchor="nw")
# l1=Label(sub_frame1,text=table,bg='#243e55' ,fg="white",font=('Arial',16))
# l1.place(x=10,y=10)
# total=font.Font(family="Helvetica",26,"bold")

total=tk.StringVar()
total.set(table)
total1=tk.StringVar()
total1.set(table1)
total2=tk.StringVar()
total2.set(table2)
total3=tk.StringVar()
total3.set(table3)
total4=tk.StringVar()
total4.set(table4)
total5=tk.StringVar()
total5.set(table5)
total6=tk.StringVar()
total6.set(table6)
total7=tk.StringVar()
total7.set(table7)
total8=tk.StringVar()
total8.set(table8)
total9=tk.StringVar()
total9.set(table9)
total10=tk.StringVar()
total10.set(table10)
total11=tk.StringVar()
total11.set(table11)
total12=tk.StringVar()
total12.set(table12)
total13=tk.StringVar()
total13.set(table13)
total14=tk.StringVar()
total14.set(table14)
total15=tk.StringVar()
total15.set(table15)
total16=tk.StringVar()
total16.set(table16)
total17=tk.StringVar()
total17.set(table17)
total18=tk.StringVar()
total18.set(table18)
total19=tk.StringVar()
total19.set(table19)
total20=tk.StringVar()
total20.set(table20)
total21=tk.StringVar()
total21.set(table21)
total22=tk.StringVar()
total22.set(table22)
total23=tk.StringVar()
total23.set(table23)
total24=tk.StringVar()
total24.set(table24)
total25=tk.StringVar()
total25.set(table25)
total26=tk.StringVar()
total26.set(table26)
total27=tk.StringVar()
total27.set(table27)
total28=tk.StringVar()
total28.set(table28)
total29=tk.StringVar()
total29.set(table29)
total30=tk.StringVar()
total30.set(table30)
total31=tk.StringVar()
total31.set(table31)
total32=tk.StringVar()
total32.set(table32)
total33=tk.StringVar()
total33.set(table33)
total34=tk.StringVar()
total34.set(table34)
total35=tk.StringVar()
total35.set(table35)
total36=tk.StringVar()
total36.set(table36)
total37=tk.StringVar()
total37.set(table37)
total38=tk.StringVar()
total38.set(table38)
total39=tk.StringVar()
total39.set(table39)
total40=tk.StringVar()
total40.set(table40)
total41=tk.StringVar()
total41.set(table41)
total42=tk.StringVar()
total42.set(table42)
total43=tk.StringVar()
total43.set(table43)
total44=tk.StringVar()
total44.set(table44)
total45=tk.StringVar()
total45.set(table45)
total46=tk.StringVar()
total46.set(table46)
total47=tk.StringVar()
total47.set(table47)
total48=tk.StringVar()
total48.set(table48)
total49=tk.StringVar()
total49.set(table49)
total50=tk.StringVar()
total50.set(table50)
total51=tk.StringVar()
total51.set(table51)
total52=tk.StringVar()
total52.set(table52)
total53=tk.StringVar()
total53.set(table53)
total54=tk.StringVar()
total54.set(table54)
total55=tk.StringVar()
total55.set(table55)
total56=tk.StringVar()
total56.set(table56)
total57=tk.StringVar()
total57.set(table57)
total58=tk.StringVar()
total58.set(table58)
total59=tk.StringVar()
total59.set(table59)
total60=tk.StringVar()
total60.set(table60)
total61=tk.StringVar()
total61.set(table61)
total62=tk.StringVar()
total62.set(table62)
total63=tk.StringVar()
total63.set(table63)
total64=tk.StringVar()
total64.set(table64)
total65=tk.StringVar()
total65.set(table65)
total66=tk.StringVar()
total66.set(table66)
total67=tk.StringVar()
total67.set(table67)
total68=tk.StringVar()
total68.set(table68)
total69=tk.StringVar()
total69.set(table69)
total70=tk.StringVar()
total70.set(table70)
total71=tk.StringVar()
total71.set(table71)
total72=tk.StringVar()
total72.set(table72)
total73=tk.StringVar()
total73.set(table73)
total74=tk.StringVar()
total74.set(table74)
total75=tk.StringVar()
total75.set(table75)
total76=tk.StringVar()
total76.set(table76)
total77=tk.StringVar()
total77.set(table77)
total78=tk.StringVar()
total78.set(table78)
total79=tk.StringVar()
total79.set(table79)
total80=tk.StringVar()
total80.set(table80)
total81=tk.StringVar()
total81.set(table81)
total82=tk.StringVar()
total82.set(table82)
total83=tk.StringVar()
total83.set(table83)
total84=tk.StringVar()
total84.set(table84)
total85=tk.StringVar()
total85.set(table85)
total86=tk.StringVar()
total86.set(table86)
total87=tk.StringVar()
total87.set(table87)
total88=tk.StringVar()
total88.set(table88)
total89=tk.StringVar()
total89.set(table89)
total90=tk.StringVar()
total90.set(table90)
total91=tk.StringVar()
total91.set(table91)
total92=tk.StringVar()
total92.set(table92)
total93=tk.StringVar()
total93.set(table93)
total94=tk.StringVar()
total94.set(table94)
total95=tk.StringVar()
total95.set(table95)
total96=tk.StringVar()
total96.set(table96)
total97=tk.StringVar()
total97.set(table97)
total98=tk.StringVar()
total98.set(table98)
total99=tk.StringVar()
total99.set(table99)
total100=tk.StringVar()
total100.set(table100)
total101=tk.StringVar()
total101.set(table101)
total102=tk.StringVar()
total102.set(table102)
total103=tk.StringVar()
total103.set(table103)
total104=tk.StringVar()
total104.set(table104)
total105=tk.StringVar()
total105.set(table105)
total106=tk.StringVar()
total106.set(table106)
total107=tk.StringVar()
total107.set(table107)
total108=tk.StringVar()
total108.set(table108)
total109=tk.StringVar()
total109.set(table109)
total110=tk.StringVar()
total110.set(table110)
total111=tk.StringVar()
total111.set(table111)
total112=tk.StringVar()
total112.set(table112)
total113=tk.StringVar()
total113.set(table113)
total114=tk.StringVar()
total114.set(table114)
total115=tk.StringVar()
total115.set(table115)
total116=tk.StringVar()
total116.set(table116)
total117=tk.StringVar()
total117.set(table117)
total118=tk.StringVar()
total118.set(table118)
total119=tk.StringVar()
total119.set(table119)
total120=tk.StringVar()
total120.set(table120)
total121=tk.StringVar()
total121.set(table121)
total122=tk.StringVar()
total122.set(table122)
total123=tk.StringVar()
total123.set(table123)
total124=tk.StringVar()
total124.set(table124)
total125=tk.StringVar()
total125.set(table125)
total126=tk.StringVar()
total126.set(table126)
total127=tk.StringVar()
total127.set(table127)
total128=tk.StringVar()
total128.set(table128)


tot1=tk.StringVar()
tot1.set(tab1)
tot2=tk.StringVar()
tot2.set(tab2)
tot3=tk.StringVar()
tot3.set(tab3)
tot4=tk.StringVar()
tot4.set(tab4)
tot5=tk.StringVar()
tot5.set(tab5)
tot6=tk.StringVar()
tot6.set(tab6)
tot7=tk.StringVar()
tot7.set(tab7)
tot8=tk.StringVar()
tot8.set(tab8)
tot9=tk.StringVar()
tot9.set(tab9)
tot10=tk.StringVar()
tot10.set(tab10)
tot11=tk.StringVar()
tot11.set(tab11)
tot12=tk.StringVar()
tot12.set(tab12)
tot13=tk.StringVar()
tot13.set(tab13)
tot14=tk.StringVar()
tot14.set(tab14)
tot15=tk.StringVar()
tot15.set(tab15)
tot16=tk.StringVar()
tot16.set(tab16)
tot17=tk.StringVar()
tot17.set(tab17)
tot18=tk.StringVar()
tot18.set(tab18)
tot19=tk.StringVar()
tot19.set(tab19)
tot20=tk.StringVar()
tot20.set(tab20)
tot21=tk.StringVar()
tot21.set(tab21)
tot22=tk.StringVar()
tot22.set(tab22)
tot23=tk.StringVar()
tot23.set(tab23)
tot24=tk.StringVar()
tot24.set(tab24)
tot25=tk.StringVar()
tot25.set(tab25)
tot26=tk.StringVar()
tot26.set(tab26)
tot27=tk.StringVar()
tot27.set(tab27)
tot28=tk.StringVar()
tot28.set(tab28)
tot29=tk.StringVar()
tot29.set(tab29)
tot30=tk.StringVar()
tot30.set(tab30)
tot31=tk.StringVar()
tot31.set(tab31)
tot32=tk.StringVar()
tot32.set(tab32)
tot33=tk.StringVar()
tot33.set(tab33)
tot34=tk.StringVar()
tot34.set(tab34)
tot35=tk.StringVar()
tot35.set(tab35)
tot36=tk.StringVar()
tot36.set(tab36)
tot37=tk.StringVar()
tot37.set(tab37)
tot38=tk.StringVar()
tot38.set(tab38)
tot39=tk.StringVar()
tot39.set(tab39)
tot40=tk.StringVar()
tot40.set(tab40)
tot41=tk.StringVar()
tot41.set(tab41)
tot42=tk.StringVar()
tot42.set(tab42)
tot43=tk.StringVar()
tot43.set(tab43)
tot44=tk.StringVar()
tot44.set(tab44)
tot45=tk.StringVar()
tot45.set(tab45)
tot46=tk.StringVar()
tot46.set(tab46)
tot47=tk.StringVar()
tot47.set(tab47)
tot48=tk.StringVar()
tot48.set(tab48)
tot49=tk.StringVar()
tot49.set(tab49)
tot50=tk.StringVar()
tot50.set(tab50)
tot51=tk.StringVar()
tot51.set(tab51)
tot52=tk.StringVar()
tot52.set(tab52)
tot53=tk.StringVar()
tot53.set(tab53)
tot54=tk.StringVar()
tot54.set(tab54)
tot55=tk.StringVar()
tot55.set(tab55)
tot56=tk.StringVar()
tot56.set(tab56)
tot57=tk.StringVar()
tot57.set(tab57)
tot58=tk.StringVar()
tot58.set(tab58)
tot59=tk.StringVar()
tot59.set(tab59)
tot60=tk.StringVar()
tot60.set(tab60)
tot61=tk.StringVar()
tot61.set(tab61)
tot62=tk.StringVar()
tot62.set(tab62)
tot63=tk.StringVar()
tot63.set(tab63)
tot64=tk.StringVar()
tot64.set(tab64)
tot65=tk.StringVar()
tot65.set(tab65)
tot66=tk.StringVar()
tot66.set(tab66)
tot67=tk.StringVar()
tot67.set(tab67)
tot68=tk.StringVar()
tot68.set(tab68)
tot69=tk.StringVar()
tot69.set(tab69)
tot70=tk.StringVar()
tot70.set(tab70)
tot71=tk.StringVar()
tot71.set(tab71)
tot72=tk.StringVar()
tot72.set(tab72)
tot73=tk.StringVar()
tot73.set(tab73)
tot74=tk.StringVar()
tot74.set(tab74)
tot75=tk.StringVar()
tot75.set(tab75)
tot76=tk.StringVar()
tot76.set(tab76)
tot77=tk.StringVar()
tot77.set(tab77)
tot78=tk.StringVar()
tot78.set(tab78)
tot79=tk.StringVar()
tot79.set(tab79)
tot80=tk.StringVar()
tot80.set(tab80)
tot81=tk.StringVar()
tot81.set(tab81)
tot82=tk.StringVar()
tot82.set(tab82)
tot83=tk.StringVar()
tot83.set(tab83)
tot84=tk.StringVar()
tot84.set(tab84)
tot85=tk.StringVar()
tot85.set(tab85)
tot86=tk.StringVar()
tot86.set(tab86)
tot87=tk.StringVar()
tot87.set(tab87)
tot88=tk.StringVar()
tot88.set(tab88)
tot89=tk.StringVar()
tot89.set(tab89)
tot90=tk.StringVar()
tot90.set(tab90)
tot91=tk.StringVar()
tot91.set(tab91)
tot92=tk.StringVar()
tot92.set(tab92)
tot93=tk.StringVar()
tot93.set(tab93)
tot94=tk.StringVar()
tot94.set(tab94)
tot95=tk.StringVar()
tot95.set(tab95)
tot96=tk.StringVar()
tot96.set(tab96)
tot97=tk.StringVar()
tot97.set(tab97)
tot98=tk.StringVar()
tot98.set(tab98)
tot99=tk.StringVar()
tot99.set(tab99)
tot100=tk.StringVar()
tot100.set(tab100)
tot101=tk.StringVar()
tot101.set(tab101)
tot102=tk.StringVar()
tot102.set(tab102)
tot103=tk.StringVar()
tot103.set(tab103)
tot104=tk.StringVar()
tot104.set(tab104)
tot105=tk.StringVar()
tot105.set(tab105)
tot106=tk.StringVar()
tot106.set(tab106)
tot107=tk.StringVar()
tot107.set(tab107)
tot108=tk.StringVar()
tot108.set(tab108)
tot109=tk.StringVar()
tot109.set(tab109)
tot110=tk.StringVar()
tot110.set(tab110)
tot111=tk.StringVar()
tot111.set(tab111)
tot112=tk.StringVar()
tot112.set(tab112)
tot113=tk.StringVar()
tot113.set(tab113)
tot114=tk.StringVar()
tot114.set(tab114)
tot115=tk.StringVar()
tot115.set(tab115)
tot116=tk.StringVar()
tot116.set(tab116)
tot117=tk.StringVar()
tot117.set(tab117)
tot118=tk.StringVar()
tot118.set(tab118)
tot119=tk.StringVar()
tot119.set(tab119)
tot120=tk.StringVar()
tot120.set(tab120)
tot121=tk.StringVar()
tot121.set(tab121)
tot122=tk.StringVar()
tot122.set(tab122)
tot123=tk.StringVar()
tot123.set(tab123)
tot124=tk.StringVar()
tot124.set(tab124)
tot125=tk.StringVar()
tot125.set(tab125)
tot126=tk.StringVar()
tot126.set(tab126)
tot127=tk.StringVar()
tot127.set(tab127)
tot128=tk.StringVar()
tot128.set(tab128)
tot129=tk.StringVar()
tot129.set(tab129)
tot130=tk.StringVar()
tot130.set(tab130)
tot131=tk.StringVar()
tot131.set(tab131)
tot132=tk.StringVar()
tot132.set(tab132)
tot133=tk.StringVar()
tot133.set(tab133)
tot134=tk.StringVar()
tot134.set(tab134)
tot135=tk.StringVar()
tot135.set(tab135)
tot136=tk.StringVar()
tot136.set(tab136)
tot137=tk.StringVar()
tot137.set(tab137)
tot138=tk.StringVar()
tot138.set(tab138)
tot139=tk.StringVar()
tot139.set(tab139)
tot140=tk.StringVar()
tot140.set(tab140)
tot141=tk.StringVar()
tot141.set(tab141)
tot142=tk.StringVar()
tot142.set(tab142)
tot143=tk.StringVar()
tot143.set(tab143)
tot144=tk.StringVar()
tot144.set(tab144)
tot145=tk.StringVar()
tot145.set(tab145)
tot146=tk.StringVar()
tot146.set(tab146)
tot147=tk.StringVar()
tot147.set(tab147)
tot148=tk.StringVar()
tot148.set(tab148)
tot149=tk.StringVar()
tot149.set(tab149)
tot150=tk.StringVar()
tot150.set(tab150)
tot151=tk.StringVar()
tot151.set(tab151)
tot152=tk.StringVar()
tot152.set(tab152)
tot153=tk.StringVar()
tot153.set(tab153)
tot154=tk.StringVar()
tot154.set(tab154)
tot155=tk.StringVar()
tot155.set(tab155)
tot156=tk.StringVar()
tot156.set(tab156)
tot157=tk.StringVar()
tot157.set(tab157)
tot158=tk.StringVar()
tot158.set(tab158)
tot159=tk.StringVar()
tot159.set(tab159)
tot160=tk.StringVar()
tot160.set(tab160)
tot161=tk.StringVar()
tot161.set(tab161)
tot162=tk.StringVar()
tot162.set(tab162)
tot163=tk.StringVar()
tot163.set(tab163)
tot164=tk.StringVar()
tot164.set(tab164)
tot165=tk.StringVar()
tot165.set(tab165)
tot166=tk.StringVar()
tot166.set(tab166)
tot167=tk.StringVar()
tot167.set(tab167)
tot168=tk.StringVar()
tot168.set(tab168)
tot169=tk.StringVar()
tot169.set(tab169)
tot170=tk.StringVar()
tot170.set(tab170)
tot171=tk.StringVar()
tot171.set(tab171)
tot172=tk.StringVar()
tot172.set(tab172)
tot173=tk.StringVar()
tot173.set(tab173)
tot174=tk.StringVar()
tot174.set(tab174)
tot175=tk.StringVar()
tot175.set(tab175)
tot176=tk.StringVar()
tot176.set(tab176)
tot177=tk.StringVar()
tot177.set(tab177)
tot178=tk.StringVar()
tot178.set(tab178)
tot179=tk.StringVar()
tot179.set(tab179)
tot180=tk.StringVar()
tot180.set(tab180)
tot181=tk.StringVar()
tot181.set(tab181)
tot182=tk.StringVar()
tot182.set(tab182)
tot183=tk.StringVar()
tot183.set(tab183)
tot184=tk.StringVar()
tot184.set(tab184)
tot185=tk.StringVar()
tot185.set(tab185)
tot186=tk.StringVar()
tot186.set(tab186)
tot187=tk.StringVar()
tot187.set(tab187)
tot188=tk.StringVar()
tot188.set(tab188)
tot189=tk.StringVar()
tot189.set(tab189)
tot190=tk.StringVar()
tot190.set(tab190)
tot191=tk.StringVar()
tot191.set(tab191)
tot192=tk.StringVar()
tot192.set(tab192)
tot193=tk.StringVar()
tot193.set(tab193)
tot194=tk.StringVar()
tot194.set(tab194)
tot195=tk.StringVar()
tot195.set(tab195)
tot196=tk.StringVar()
tot196.set(tab196)
tot197=tk.StringVar()
tot197.set(tab197)
tot198=tk.StringVar()
tot198.set(tab198)
tot199=tk.StringVar()
tot199.set(tab199)
tot200=tk.StringVar()
tot200.set(tab200)
tot201=tk.StringVar()
tot201.set(tab201)
tot202=tk.StringVar()
tot202.set(tab202)
tot203=tk.StringVar()
tot203.set(tab203)
tot204=tk.StringVar()
tot204.set(tab204)
tot205=tk.StringVar()
tot205.set(tab205)
tot206=tk.StringVar()
tot206.set(tab206)
tot207=tk.StringVar()
tot207.set(tab207)
tot208=tk.StringVar()
tot208.set(tab208)
tot209=tk.StringVar()
tot209.set(tab209)
tot210=tk.StringVar()
tot210.set(tab210)
tot211=tk.StringVar()
tot211.set(tab211)
tot212=tk.StringVar()
tot212.set(tab212)
tot213=tk.StringVar()
tot213.set(tab213)
tot214=tk.StringVar()
tot214.set(tab214)
tot215=tk.StringVar()
tot215.set(tab215)
tot216=tk.StringVar()
tot216.set(tab216)
tot217=tk.StringVar()
tot217.set(tab217)
tot218=tk.StringVar()
tot218.set(tab218)
tot219=tk.StringVar()
tot219.set(tab219)
tot220=tk.StringVar()
tot220.set(tab220)
tot221=tk.StringVar()
tot221.set(tab221)
tot222=tk.StringVar()
tot222.set(tab222)
tot223=tk.StringVar()
tot223.set(tab223)
tot224=tk.StringVar()
tot224.set(tab224)
tot225=tk.StringVar()
tot225.set(tab225)
tot226=tk.StringVar()
tot226.set(tab226)
tot227=tk.StringVar()
tot227.set(tab227)
tot228=tk.StringVar()
tot228.set(tab228)
tot229=tk.StringVar()
tot229.set(tab229)
tot230=tk.StringVar()
tot230.set(tab230)
tot231=tk.StringVar()
tot231.set(tab231)
tot232=tk.StringVar()
tot232.set(tab232)
tot233=tk.StringVar()
tot233.set(tab233)
tot234=tk.StringVar()
tot234.set(tab234)
tot235=tk.StringVar()
tot235.set(tab235)
tot236=tk.StringVar()
tot236.set(tab236)
tot237=tk.StringVar()
tot237.set(tab237)
tot238=tk.StringVar()
tot238.set(tab238)
tot239=tk.StringVar()
tot239.set(tab239)
tot240=tk.StringVar()
tot240.set(tab240)
tot241=tk.StringVar()
tot241.set(tab241)
tot242=tk.StringVar()
tot242.set(tab242)
tot243=tk.StringVar()
tot243.set(tab243)
tot244=tk.StringVar()
tot244.set(tab244)
tot245=tk.StringVar()
tot245.set(tab245)
tot246=tk.StringVar()
tot246.set(tab246)
tot247=tk.StringVar()
tot247.set(tab247)
tot248=tk.StringVar()
tot248.set(tab248)
tot249=tk.StringVar()
tot249.set(tab249)
tot250=tk.StringVar()
tot250.set(tab250)
tot251=tk.StringVar()
tot251.set(tab251)
tot252=tk.StringVar()
tot252.set(tab252)
tot253=tk.StringVar()
tot253.set(tab253)
tot254=tk.StringVar()
tot254.set(tab254)
tot255=tk.StringVar()
tot255.set(tab255)
tot256=tk.StringVar()
tot256.set(tab256)
tot257=tk.StringVar()
tot257.set(tab257)
tot258=tk.StringVar()
tot258.set(tab258)
tot259=tk.StringVar()
tot259.set(tab259)
tot260=tk.StringVar()
tot260.set(tab260)
tot261=tk.StringVar()
tot261.set(tab261)
tot262=tk.StringVar()
tot262.set(tab262)
tot263=tk.StringVar()
tot263.set(tab263)
tot264=tk.StringVar()
tot264.set(tab264)
tot266=tk.StringVar()
tot266.set(tab266)
tot267=tk.StringVar()
tot267.set(tab267)
tot268=tk.StringVar()
tot268.set(tab268)
tot269=tk.StringVar()
tot269.set(tab269)
tot270=tk.StringVar()
tot270.set(tab270)
tot271=tk.StringVar()
tot271.set(tab271)
tot272=tk.StringVar()
tot272.set(tab272)
tot273=tk.StringVar()
tot273.set(tab273)
tot274=tk.StringVar()
tot274.set(tab274)
tot275=tk.StringVar()
tot275.set(tab275)
tot276=tk.StringVar()
tot276.set(tab276)
tot277=tk.StringVar()
tot277.set(tab277)
tot278=tk.StringVar()
tot278.set(tab278)
tot279=tk.StringVar()
tot279.set(tab279)
tot280=tk.StringVar()
tot280.set(tab280)
tot281=tk.StringVar()
tot281.set(tab281)
tot282=tk.StringVar()
tot282.set(tab282)
tot283=tk.StringVar()
tot283.set(tab283)
tot284=tk.StringVar()
tot284.set(tab284)
tot285=tk.StringVar()
tot285.set(tab285)
tot286=tk.StringVar()
tot286.set(tab286)
tot287=tk.StringVar()
tot287.set(tab287)
tot288=tk.StringVar()
tot288.set(tab288)
tot289=tk.StringVar()
tot289.set(tab289)
tot290=tk.StringVar()
tot290.set(tab290)
tot291=tk.StringVar()
tot291.set(tab291)
tot292=tk.StringVar()
tot292.set(tab292)
tot293=tk.StringVar()
tot293.set(tab293)
tot294=tk.StringVar()
tot294.set(tab294)
tot295=tk.StringVar()
tot295.set(tab295)
tot296=tk.StringVar()
tot296.set(tab296)
tot297=tk.StringVar()
tot297.set(tab297)
tot298=tk.StringVar()
tot298.set(tab298)
tot299=tk.StringVar()
tot299.set(tab299)
tot300=tk.StringVar()
tot300.set(tab300)
tot301=tk.StringVar()
tot301.set(tab301)
tot302=tk.StringVar()
tot302.set(tab302)
tot303=tk.StringVar()
tot303.set(tab303)
tot304=tk.StringVar()
tot304.set(tab304)
tot305=tk.StringVar()
tot305.set(tab305)
tot306=tk.StringVar()
tot306.set(tab306)
tot307=tk.StringVar()
tot307.set(tab307)
tot308=tk.StringVar()
tot308.set(tab308)
tot309=tk.StringVar()
tot309.set(tab309)
tot310=tk.StringVar()
tot310.set(tab310)
tot311=tk.StringVar()
tot311.set(tab311)
tot312=tk.StringVar()
tot312.set(tab312)
tot313=tk.StringVar()
tot313.set(tab313)
tot314=tk.StringVar()
tot314.set(tab314)
tot315=tk.StringVar()
tot315.set(tab315)
tot316=tk.StringVar()
tot316.set(tab316)
tot317=tk.StringVar()
tot317.set(tab317)
tot318=tk.StringVar()
tot318.set(tab318)
tot319=tk.StringVar()
tot319.set(tab319)
tot320=tk.StringVar()
tot320.set(tab320)
tot321=tk.StringVar()
tot321.set(tab321)
tot322=tk.StringVar()
tot322.set(tab322)
tot323=tk.StringVar()
tot323.set(tab323)
tot324=tk.StringVar()
tot324.set(tab324)
tot325=tk.StringVar()
tot325.set(tab325)
tot326=tk.StringVar()
tot326.set(tab326)
tot327=tk.StringVar()
tot327.set(tab327)
tot328=tk.StringVar()
tot328.set(tab328)
tot329=tk.StringVar()
tot329.set(tab329)
tot330=tk.StringVar()
tot330.set(tab330)
tot331=tk.StringVar()
tot331.set(tab331)
tot332=tk.StringVar()
tot332.set(tab332)
tot333=tk.StringVar()
tot333.set(tab333)
tot334=tk.StringVar()
tot334.set(tab334)
tot335=tk.StringVar()
tot335.set(tab335)
tot336=tk.StringVar()
tot336.set(tab336)
tot337=tk.StringVar()
tot337.set(tab337)
tot338=tk.StringVar()
tot338.set(tab338)
tot339=tk.StringVar()
tot339.set(tab339)
tot340=tk.StringVar()
tot340.set(tab340)
tot341=tk.StringVar()
tot341.set(tab341)

tot342=tk.StringVar()
tot342.set(tab342)
tot343=tk.StringVar()
tot343.set(tab343)
tot344=tk.StringVar()
tot344.set(tab344)
tot345=tk.StringVar()
tot345.set(tab345)
tot346=tk.StringVar()
tot346.set(tab346)
tot347=tk.StringVar()
tot347.set(tab347)
tot348=tk.StringVar()
tot348.set(tab348)
tot349=tk.StringVar()
tot349.set(tab349)
tot350=tk.StringVar()
tot350.set(tab350)
tot351=tk.StringVar()
tot351.set(tab351)
tot352=tk.StringVar()
tot352.set(tab352)
tot353=tk.StringVar()
tot353.set(tab353)
tot354=tk.StringVar()
tot354.set(tab354)
tot355=tk.StringVar()
tot355.set(tab355)
tot356=tk.StringVar()
tot356.set(tab356)
tot357=tk.StringVar()
tot357.set(tab357)
tot358=tk.StringVar()
tot358.set(tab358)
tot359=tk.StringVar()
tot359.set(tab359)
tot360=tk.StringVar()
tot360.set(tab360)
tot361=tk.StringVar()
tot361.set(tab361)
tot362=tk.StringVar()
tot362.set(tab362)
tot363=tk.StringVar()
tot363.set(tab363)
tot364=tk.StringVar()
tot364.set(tab364)
tot365=tk.StringVar()
tot365.set(tab365)
tot366=tk.StringVar()
tot366.set(tab366)
tot367=tk.StringVar()
tot367.set(tab367)
tot368=tk.StringVar()
tot368.set(tab368)
tot369=tk.StringVar()
tot369.set(tab369)
tot370=tk.StringVar()
tot370.set(tab370)
tot371=tk.StringVar()
tot371.set(tab371)
tot372=tk.StringVar()
tot372.set(tab372)
tot373=tk.StringVar()
tot373.set(tab373)
tot374=tk.StringVar()
tot374.set(tab374)
tot375=tk.StringVar()
tot375.set(tab375)
tot376=tk.StringVar()
tot376.set(tab376)
tot377=tk.StringVar()
tot377.set(tab377)
tot378=tk.StringVar()
tot378.set(tab378)
tot379=tk.StringVar()
tot379.set(tab379)
tot380=tk.StringVar()
tot380.set(tab380)
tot381=tk.StringVar()
tot381.set(tab381)
tot382=tk.StringVar()
tot382.set(tab382)
tot383=tk.StringVar()
tot383.set(tab383)
tot384=tk.StringVar()
tot384.set(tab384)
tot385=tk.StringVar()
tot385.set(tab385)
tot386=tk.StringVar()
tot386.set(tab386)
tot387=tk.StringVar()
tot387.set(tab387)
tot388=tk.StringVar()
tot388.set(tab388)
tot389=tk.StringVar()
tot389.set(tab389)
tot390=tk.StringVar()
tot390.set(tab390)
tot391=tk.StringVar()
tot391.set(tab391)
tot392=tk.StringVar()
tot392.set(tab392)
tot393=tk.StringVar()
tot393.set(tab393)
tot394=tk.StringVar()
tot394.set(tab394)
tot395=tk.StringVar()
tot395.set(tab395)
tot396=tk.StringVar()
tot396.set(tab396)
tot397=tk.StringVar()
tot397.set(tab397)
tot398=tk.StringVar()
tot398.set(tab398)
tot399=tk.StringVar()
tot399.set(tab399)
tot400=tk.StringVar()
tot400.set(tab400)
tot401=tk.StringVar()
tot401.set(tab401)
tot402=tk.StringVar()
tot402.set(tab402)
tot403=tk.StringVar()
tot403.set(tab403)
tot404=tk.StringVar()
tot404.set(tab404)
tot405=tk.StringVar()
tot405.set(tab405)
tot406=tk.StringVar()
tot406.set(tab406)
tot407=tk.StringVar()
tot407.set(tab407)
tot408=tk.StringVar()
tot408.set(tab408)
tot409=tk.StringVar()
tot409.set(tab409)
tot410=tk.StringVar()
tot410.set(tab410)
tot411=tk.StringVar()
tot411.set(tab411)
tot412=tk.StringVar()
tot412.set(tab412)
tot413=tk.StringVar()
tot413.set(tab413)
tot414=tk.StringVar()
tot414.set(tab414)
tot415=tk.StringVar()
tot415.set(tab415)
tot416=tk.StringVar()
tot416.set(tab416)
tot417=tk.StringVar()
tot417.set(tab417)
tot418=tk.StringVar()
tot418.set(tab418)
tot419=tk.StringVar()
tot419.set(tab419)
tot420=tk.StringVar()
tot420.set(tab420)
tot421=tk.StringVar()
tot421.set(tab421)
tot422=tk.StringVar()
tot422.set(tab422)
tot423=tk.StringVar()
tot423.set(tab423)
tot424=tk.StringVar()
tot424.set(tab424)
tot425=tk.StringVar()
tot425.set(tab425)
tot426=tk.StringVar()
tot426.set(tab426)
tot427=tk.StringVar()
tot427.set(tab427)
tot428=tk.StringVar()
tot428.set(tab428)
tot429=tk.StringVar()
tot429.set(tab429)
tot430=tk.StringVar()
tot430.set(tab430)
tot431=tk.StringVar()
tot431.set(tab431)
tot432=tk.StringVar()
tot432.set(tab432)
tot433=tk.StringVar()
tot433.set(tab433)
tot434=tk.StringVar()
tot434.set(tab434)
tot435=tk.StringVar()
tot435.set(tab435)
tot436=tk.StringVar()
tot436.set(tab436)
tot437=tk.StringVar()
tot437.set(tab437)
tot438=tk.StringVar()
tot438.set(tab438)
tot439=tk.StringVar()
tot439.set(tab439)
tot440=tk.StringVar()
tot440.set(tab440)
tot441=tk.StringVar()
tot441.set(tab441)
tot442=tk.StringVar()
tot442.set(tab442)
tot443=tk.StringVar()
tot443.set(tab443)
tot444=tk.StringVar()
tot444.set(tab444)
tot445=tk.StringVar()
tot445.set(tab445)
tot446=tk.StringVar()
tot446.set(tab446)
tot447=tk.StringVar()
tot447.set(tab447)
tot448=tk.StringVar()
tot448.set(tab448)
tot449=tk.StringVar()
tot449.set(tab449)
tot450=tk.StringVar()
tot450.set(tab450)
tot451=tk.StringVar()
tot451.set(tab451)
tot452=tk.StringVar()
tot452.set(tab452)
tot453=tk.StringVar()
tot453.set(tab453)
tot454=tk.StringVar()
tot454.set(tab454)
tot455=tk.StringVar()
tot455.set(tab455)
tot456=tk.StringVar()
tot456.set(tab456)
tot457=tk.StringVar()
tot457.set(tab457)
tot458=tk.StringVar()
tot458.set(tab458)
tot459=tk.StringVar()
tot459.set(tab459)
tot460=tk.StringVar()
tot460.set(tab460)
tot461=tk.StringVar()
tot461.set(tab461)
tot462=tk.StringVar()
tot462.set(tab462)
tot463=tk.StringVar()
tot463.set(tab463)
tot464=tk.StringVar()
tot464.set(tab464)
tot465=tk.StringVar()
tot465.set(tab465)
tot466=tk.StringVar()
tot466.set(tab466)
tot467=tk.StringVar()
tot467.set(tab467)
tot468=tk.StringVar()
tot468.set(tab468)
tot469=tk.StringVar()
tot469.set(tab469)
tot470=tk.StringVar()
tot470.set(tab470)
tot471=tk.StringVar()
tot471.set(tab471)
tot472=tk.StringVar()
tot472.set(tab472)
tot473=tk.StringVar()
tot473.set(tab473)
tot474=tk.StringVar()
tot474.set(tab474)
tot475=tk.StringVar()
tot475.set(tab475)
tot476=tk.StringVar()
tot476.set(tab476)
tot477=tk.StringVar()
tot477.set(tab477)
tot478=tk.StringVar()
tot478.set(tab478)
tot479=tk.StringVar()
tot479.set(tab479)
tot480=tk.StringVar()
tot480.set(tab480)
tot481=tk.StringVar()
tot481.set(tab481)
tot482=tk.StringVar()
tot482.set(tab482)
tot483=tk.StringVar()
tot483.set(tab483)
tot484=tk.StringVar()
tot484.set(tab484)
tot485=tk.StringVar()
tot485.set(tab485)
tot486=tk.StringVar()
tot486.set(tab486)
tot487=tk.StringVar()
tot487.set(tab487)
tot488=tk.StringVar()
tot488.set(tab488)
tot489=tk.StringVar()
tot489.set(tab489)
tot490=tk.StringVar()
tot490.set(tab490)
tot491=tk.StringVar()
tot491.set(tab491)
tot492=tk.StringVar()
tot492.set(tab492)
tot493=tk.StringVar()
tot493.set(tab493)
tot494=tk.StringVar()
tot494.set(tab494)
tot495=tk.StringVar()
tot495.set(tab495)
tot496=tk.StringVar()
tot496.set(tab496)
tot497=tk.StringVar()
tot497.set(tab497)
tot498=tk.StringVar()
tot498.set(tab498)
tot499=tk.StringVar()
tot499.set(tab499)
tot500=tk.StringVar()
tot500.set(tab500)
tot501=tk.StringVar()
tot501.set(tab501)
tot502=tk.StringVar()
tot502.set(tab502)
tot503=tk.StringVar()
tot503.set(tab503)
tot504=tk.StringVar()
tot504.set(tab504)
tot505=tk.StringVar()
tot505.set(tab505)
tot506=tk.StringVar()
tot506.set(tab506)
tot507=tk.StringVar()
tot507.set(tab507)
tot508=tk.StringVar()
tot508.set(tab508)
tot509=tk.StringVar()
tot509.set(tab509)
tot510=tk.StringVar()
tot510.set(tab510)
tot511=tk.StringVar()
tot511.set(tab511)
tot512=tk.StringVar()
tot512.set(tab512)
tot513=tk.StringVar()
tot513.set(tab513)
tot514=tk.StringVar()
tot514.set(tab514)
tot515=tk.StringVar()
tot515.set(tab515)
tot516=tk.StringVar()
tot516.set(tab516)
tot517=tk.StringVar()
tot517.set(tab517)
tot518=tk.StringVar()
tot518.set(tab518)
tot519=tk.StringVar()
tot519.set(tab519)
tot520=tk.StringVar()
tot520.set(tab520)
tot521=tk.StringVar()
tot521.set(tab521)
tot522=tk.StringVar()
tot522.set(tab522)
tot523=tk.StringVar()
tot523.set(tab523)
tot524=tk.StringVar()
tot524.set(tab524)
tot525=tk.StringVar()
tot525.set(tab525)
tot526=tk.StringVar()
tot526.set(tab526)
tot527=tk.StringVar()
tot527.set(tab527)
tot528=tk.StringVar()
tot528.set(tab528)
tot529=tk.StringVar()
tot529.set(tab529)
tot530=tk.StringVar()
tot530.set(tab530)
tot531=tk.StringVar()
tot531.set(tab531)
tot532=tk.StringVar()
tot532.set(tab532)
tot533=tk.StringVar()
tot533.set(tab533)
tot534=tk.StringVar()
tot534.set(tab534)
tot535=tk.StringVar()
tot535.set(tab535)
tot536=tk.StringVar()
tot536.set(tab536)
tot537=tk.StringVar()
tot537.set(tab537)
tot538=tk.StringVar()
tot538.set(tab538)
tot539=tk.StringVar()
tot539.set(tab539)
tot540=tk.StringVar()
tot540.set(tab540)
tot541=tk.StringVar()
tot541.set(tab541)
tot542=tk.StringVar()
tot542.set(tab542)
tot543=tk.StringVar()
tot543.set(tab543)
tot544=tk.StringVar()
tot544.set(tab544)
tot545=tk.StringVar()
tot545.set(tab545)
tot546=tk.StringVar()
tot546.set(tab546)
tot547=tk.StringVar()
tot547.set(tab547)
tot548=tk.StringVar()
tot548.set(tab548)
tot549=tk.StringVar()
tot549.set(tab549)
tot550=tk.StringVar()
tot550.set(tab550)
tot551=tk.StringVar()
tot551.set(tab551)
tot552=tk.StringVar()
tot552.set(tab552)
tot553=tk.StringVar()
tot553.set(tab553)





r1=Label(form_frame,text="Beginning Cash\nBalance",bg='#243e55' ,fg="white",font=('Arial',16))
r1.place(x=70,y=220)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=225,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=225,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=225,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=225,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=225,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=225,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1155,y=225,height=40)

r2=Label(form_frame,text="Cash Inflows (Income):",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r2.place(x=70,y=300)

r3=Label(form_frame,text="Accts. Rec. \nCollections",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r3.place(x=80,y=370)
input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=375,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=375,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=375,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=375,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=375,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=375,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1155,y=375,height=40)


r4=Label(form_frame,text="Loan Proceeds",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r4.place(x=80,y=459)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=456,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=456,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=456,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=456,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=456,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=456,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1155,y=456,height=40)


r5=Label(form_frame,text="Sales & Reciepts",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r5.place(x=80,y=539)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=536,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=536,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=536,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=536,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=536,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=536,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1155,y=536,height=40)


r6=Label(form_frame,text="Other :",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r6.place(x=80,y=619)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=610,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=610,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=610,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=610,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=610,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=610,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1155,y=610,height=40)


r7=Label(form_frame,text="Total Cash\nInflows",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r7.place(x=80,y=699)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=690,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=690,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=690,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=690,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=690,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=690,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1155,y=690,height=40)

r8=Label(form_frame,text="Cash Outflow(Expenses):",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r8.place(x=80,y=769)

r9=Label(form_frame,text="Advertising\nPromotional",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r9.place(x=80,y=849)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot1,fg='white',width=16,justify='center').place(x=395,y=855,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot2,fg='white',width=16,justify='center').place(x=515,y=855,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot3,fg='white',width=16,justify='center').place(x=645,y=855,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot4,fg='white',width=16,justify='center').place(x=775,y=855,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot5,fg='white',width=16,justify='center').place(x=895,y=855,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot6,fg='white',width=16,justify='center').place(x=1025,y=855,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total,fg='white',width=16,justify='center').place(x=1155,y=855,height=40)


r10=Label(form_frame,text="Bank Charges",bg='#243e55',fg="white",font=('Arial',16),justify='left')
r10.place(x=80,y=939)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot7,fg='white',width=16,justify='center').place(x=395,y=935,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot8,fg='white',width=16,justify='center').place(x=515,y=935,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot9,fg='white',width=16,justify='center').place(x=645,y=935,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot10,fg='white',width=16,justify='center').place(x=775,y=935,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot11,fg='white',width=16,justify='center').place(x=895,y=935,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot12,fg='white',width=16,justify='center').place(x=1025,y=935,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total1,fg='white',width=16,justify='center').place(x=1155,y=935,height=40)

r11=Label(form_frame,text="Business Licenses \nand Permits",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r11.place(x=80,y=1019)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot13,fg='white',width=16,justify='center').place(x=395,y=1025,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot14,fg='white',width=16,justify='center').place(x=515,y=1025,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot15,fg='white',width=16,justify='center').place(x=645,y=1025,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot16,fg='white',width=16,justify='center').place(x=775,y=1025,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot17,fg='white',width=16,justify='center').place(x=895,y=1025,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot18,fg='white',width=16,justify='center').place(x=1025,y=1025,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total2,fg='white',width=16,justify='center').place(x=1155,y=1025,height=40)

r12=Label(form_frame,text="Charitable Contributions",bg='#243e55',fg="white",font=('Arial',16),justify='left')
r12.place(x=80,y=1119)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot19,fg='white',width=16,justify='center').place(x=395,y=1115,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot20,fg='white',width=16,justify='center').place(x=515,y=1115,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot21,fg='white',width=16,justify='center').place(x=645,y=1115,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot22,fg='white',width=16,justify='center').place(x=775,y=1115,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot23,fg='white',width=16,justify='center').place(x=895,y=1115,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot24,fg='white',width=16,justify='center').place(x=1025,y=1115,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total3,fg='white',width=16,justify='center').place(x=1155,y=1115,height=40)

r13=Label(form_frame,text="Computer and \nInternet Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r13.place(x=80,y=1199)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot25,fg='white',width=16,justify='center').place(x=395,y=1205,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot26,fg='white',width=16,justify='center').place(x=515,y=1205,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot27,fg='white',width=16,justify='center').place(x=645,y=1205,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot28,fg='white',width=16,justify='center').place(x=775,y=1205,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot29,fg='white',width=16,justify='center').place(x=895,y=1205,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot30,fg='white',width=16,justify='center').place(x=1025,y=1205,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total4,fg='white',width=16,justify='center').place(x=1155,y=1205,height=40)

r14=Label(form_frame,text="Continuing Education",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r14.place(x=80,y=1289)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot31,fg='white',width=16,justify='center').place(x=395,y=1285,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot32,fg='white',width=16,justify='center').place(x=515,y=1285,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot33,fg='white',width=16,justify='center').place(x=645,y=1285,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot34,fg='white',width=16,justify='center').place(x=775,y=1285,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot35,fg='white',width=16,justify='center').place(x=895,y=1285,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot36,fg='white',width=16,justify='center').place(x=1025,y=1285,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total5,fg='white',width=16,justify='center').place(x=1155,y=1285,height=40)

r15=Label(form_frame,text="Depreciation Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r15.place(x=80,y=1379)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot37,fg='white',width=16,justify='center').place(x=395,y=1375,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot38,fg='white',width=16,justify='center').place(x=515,y=1375,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot39,fg='white',width=16,justify='center').place(x=645,y=1375,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot40,fg='white',width=16,justify='center').place(x=775,y=1375,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot41,fg='white',width=16,justify='center').place(x=895,y=1375,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot42,fg='white',width=16,justify='center').place(x=1025,y=1375,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total6,fg='white',width=16,justify='center').place(x=1155,y=1375,height=40)

r16=Label(form_frame,text="Dues and Subscriptions",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r16.place(x=80,y=1469)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot43,fg='white',width=16,justify='center').place(x=395,y=1465,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot44,fg='white',width=16,justify='center').place(x=515,y=1465,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot45,fg='white',width=16,justify='center').place(x=645,y=1465,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot46,fg='white',width=16,justify='center').place(x=775,y=1465,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot47,fg='white',width=16,justify='center').place(x=895,y=1465,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot48,fg='white',width=16,justify='center').place(x=1025,y=1465,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total7,fg='white',width=16,justify='center').place(x=1155,y=1465,height=40)

r17=Label(form_frame,text="Housekeeping Charges",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r17.place(x=80,y=1555)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot49,fg='white',width=16,justify='center').place(x=395,y=1555,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot50,fg='white',width=16,justify='center').place(x=515,y=1555,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot51,fg='white',width=16,justify='center').place(x=645,y=1555,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot52,fg='white',width=16,justify='center').place(x=775,y=1555,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot53,fg='white',width=16,justify='center').place(x=895,y=1555,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot54,fg='white',width=16,justify='center').place(x=1025,y=1555,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total8,fg='white',width=16,justify='center').place(x=1155,y=1555,height=40)

r18=Label(form_frame,text="Insurance Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r18.place(x=80,y=1649)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot55,fg='white',width=16,justify='center').place(x=395,y=1645,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot56,fg='white',width=16,justify='center').place(x=515,y=1645,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot57,fg='white',width=16,justify='center').place(x=645,y=1645,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot58,fg='white',width=16,justify='center').place(x=775,y=1645,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot59,fg='white',width=16,justify='center').place(x=895,y=1645,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot60,fg='white',width=16,justify='center').place(x=1025,y=1645,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total9,fg='white',width=16,justify='center').place(x=1155,y=1645,height=40)

r19=Label(form_frame,text="Insurance Expense-General\nLiability Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r19.place(x=80,y=1739)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot61,fg='white',width=16,justify='center').place(x=395,y=1735,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot62,fg='white',width=16,justify='center').place(x=515,y=1735,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot63,fg='white',width=16,justify='center').place(x=645,y=1735,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot64,fg='white',width=16,justify='center').place(x=775,y=1735,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot65,fg='white',width=16,justify='center').place(x=895,y=1735,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot66,fg='white',width=16,justify='center').place(x=1025,y=1735,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total10,fg='white',width=16,justify='center').place(x=1155,y=1735,height=40)

r20=Label(form_frame,text="Insurance Expense-Health\nInsurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r20.place(x=80,y=1825)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot67,fg='white',width=16,justify='center').place(x=395,y=1825,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot68,fg='white',width=16,justify='center').place(x=515,y=1825,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot69,fg='white',width=16,justify='center').place(x=645,y=1825,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot70,fg='white',width=16,justify='center').place(x=775,y=1825,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot71,fg='white',width=16,justify='center').place(x=895,y=1825,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot72,fg='white',width=16,justify='center').place(x=1025,y=1825,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total11,fg='white',width=16,justify='center').place(x=1155,y=1825,height=40)


r21=Label(form_frame,text="Insurance Expense-Life\nand Disability Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r21.place(x=80,y=1919)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot73,fg='white',width=16,justify='center').place(x=395,y=1919,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot74,fg='white',width=16,justify='center').place(x=515,y=1919,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot75,fg='white',width=16,justify='center').place(x=645,y=1919,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot76,fg='white',width=16,justify='center').place(x=775,y=1919,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot77,fg='white',width=16,justify='center').place(x=895,y=1919,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot78,fg='white',width=16,justify='center').place(x=1025,y=1919,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total12,fg='white',width=16,justify='center').place(x=1155,y=1919,height=40)

r22=Label(form_frame,text="Insurance Expense-Professional\nLiability",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r22.place(x=80,y=2009)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot79,fg='white',width=16,justify='center').place(x=395,y=2009,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot80,fg='white',width=16,justify='center').place(x=515,y=2009,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot81,fg='white',width=16,justify='center').place(x=645,y=2009,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot82,fg='white',width=16,justify='center').place(x=775,y=2009,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot83,fg='white',width=16,justify='center').place(x=895,y=2009,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot84,fg='white',width=16,justify='center').place(x=1025,y=2009,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total13,fg='white',width=16,justify='center').place(x=1155,y=2009,height=40)

r23=Label(form_frame,text="Interest Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r23.place(x=80,y=2099)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot85,fg='white',width=16,justify='center').place(x=395,y=2099,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot86,fg='white',width=16,justify='center').place(x=515,y=2099,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot87,fg='white',width=16,justify='center').place(x=645,y=2099,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot88,fg='white',width=16,justify='center').place(x=775,y=2099,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot89,fg='white',width=16,justify='center').place(x=895,y=2099,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot90,fg='white',width=16,justify='center').place(x=1025,y=2099,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total14,fg='white',width=16,justify='center').place(x=1155,y=2099,height=40)

r24=Label(form_frame,text="Meals and entertainment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r24.place(x=80,y=2189)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot91,fg='white',width=16,justify='center').place(x=395,y=2189,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot92,fg='white',width=16,justify='center').place(x=515,y=2189,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot93,fg='white',width=16,justify='center').place(x=645,y=2189,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot94,fg='white',width=16,justify='center').place(x=775,y=2189,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot95,fg='white',width=16,justify='center').place(x=895,y=2189,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot96,fg='white',width=16,justify='center').place(x=1025,y=2189,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total15,fg='white',width=16,justify='center').place(x=1155,y=2189,height=40)

r25=Label(form_frame,text="Office Supplies",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r25.place(x=80,y=2279)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot97,fg='white',width=16,justify='center').place(x=395,y=2279,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot98,fg='white',width=16,justify='center').place(x=515,y=2279,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot99,fg='white',width=16,justify='center').place(x=645,y=2279,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot100,fg='white',width=16,justify='center').place(x=775,y=2279,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot101,fg='white',width=16,justify='center').place(x=895,y=2279,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot102,fg='white',width=16,justify='center').place(x=1025,y=2279,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total16,fg='white',width=16,justify='center').place(x=1155,y=2279,height=40)

r26=Label(form_frame,text="Postage and Delivery",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r26.place(x=80,y=2369)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot103,fg='white',width=16,justify='center').place(x=395,y=2369,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot104,fg='white',width=16,justify='center').place(x=515,y=2369,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot105,fg='white',width=16,justify='center').place(x=645,y=2369,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot106,fg='white',width=16,justify='center').place(x=775,y=2369,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot107,fg='white',width=16,justify='center').place(x=895,y=2369,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot108,fg='white',width=16,justify='center').place(x=1025,y=2369,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total17,fg='white',width=16,justify='center').place(x=1155,y=2369,height=40)

r27=Label(form_frame,text="Printing and Reproduction",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r27.place(x=80,y=2459)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot109,fg='white',width=16,justify='center').place(x=395,y=2455,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot110,fg='white',width=16,justify='center').place(x=515,y=2455,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot111,fg='white',width=16,justify='center').place(x=645,y=2455,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot112,fg='white',width=16,justify='center').place(x=775,y=2455,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot113,fg='white',width=16,justify='center').place(x=895,y=2455,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot114,fg='white',width=16,justify='center').place(x=1025,y=2455,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total18,fg='white',width=16,justify='center').place(x=1155,y=2455,height=40)

r28=Label(form_frame,text="Professional Fees",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r28.place(x=80,y=2549)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot115,fg='white',width=16,justify='center').place(x=395,y=2549,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot116,fg='white',width=16,justify='center').place(x=515,y=2549,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot117,fg='white',width=16,justify='center').place(x=645,y=2549,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot118,fg='white',width=16,justify='center').place(x=775,y=2549,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot119,fg='white',width=16,justify='center').place(x=895,y=2549,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot120,fg='white',width=16,justify='center').place(x=1025,y=2549,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total19,fg='white',width=16,justify='center').place(x=1155,y=2549,height=40)

r29=Label(form_frame,text="Purchases",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r29.place(x=80,y=2639)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot121,fg='white',width=16,justify='center').place(x=395,y=2639,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot122,fg='white',width=16,justify='center').place(x=515,y=2639,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot123,fg='white',width=16,justify='center').place(x=645,y=2639,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot124,fg='white',width=16,justify='center').place(x=775,y=2639,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot125,fg='white',width=16,justify='center').place(x=895,y=2639,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot126,fg='white',width=16,justify='center').place(x=1025,y=2639,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total20,fg='white',width=16,justify='center').place(x=1155,y=2639,height=40)



r30=Label(form_frame,text="Rent Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r30.place(x=80,y=2729)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot127,fg='white',width=16,justify='center').place(x=395,y=2729,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot128,fg='white',width=16,justify='center').place(x=515,y=2729,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot129,fg='white',width=16,justify='center').place(x=645,y=2729,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot130,fg='white',width=16,justify='center').place(x=775,y=2729,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot131,fg='white',width=16,justify='center').place(x=895,y=2729,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot132,fg='white',width=16,justify='center').place(x=1025,y=2729,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total21,fg='white',width=16,justify='center').place(x=1155,y=2729,height=40)

r31=Label(form_frame,text="Repair and maintenance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r31.place(x=80,y=2819)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot133,fg='white',width=16,justify='center').place(x=395,y=2819,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot134,fg='white',width=16,justify='center').place(x=515,y=2819,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot135,fg='white',width=16,justify='center').place(x=645,y=2819,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot136,fg='white',width=16,justify='center').place(x=775,y=2819,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot137,fg='white',width=16,justify='center').place(x=895,y=2819,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot138,fg='white',width=16,justify='center').place(x=1025,y=2819,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total22,fg='white',width=16,justify='center').place(x=1155,y=2819,height=40)

r32=Label(form_frame,text="Small Tools and Equipment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r32.place(x=80,y=2909)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot139,fg='white',width=16,justify='center').place(x=395,y=2909,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot140,fg='white',width=16,justify='center').place(x=515,y=2909,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot141,fg='white',width=16,justify='center').place(x=645,y=2909,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot142,fg='white',width=16,justify='center').place(x=775,y=2909,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot143,fg='white',width=16,justify='center').place(x=895,y=2909,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot144,fg='white',width=16,justify='center').place(x=1025,y=2909,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total23,fg='white',width=16,justify='center').place(x=1155,y=2909,height=40)

r33=Label(form_frame,text="Swachh Bharat Cess Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r33.place(x=80,y=2999)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot145,fg='white',width=16,justify='center').place(x=395,y=2999,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot146,fg='white',width=16,justify='center').place(x=515,y=2999,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot147,fg='white',width=16,justify='center').place(x=645,y=2999,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot148,fg='white',width=16,justify='center').place(x=775,y=2999,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot149,fg='white',width=16,justify='center').place(x=895,y=2999,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot150,fg='white',width=16,justify='center').place(x=1025,y=2999,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total24,fg='white',width=16,justify='center').place(x=1155,y=2999,height=40)

r34=Label(form_frame,text="Taxes - Property",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r34.place(x=80,y=3089)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot151,fg='white',width=16,justify='center').place(x=395,y=3089,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot152,fg='white',width=16,justify='center').place(x=515,y=3089,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot153,fg='white',width=16,justify='center').place(x=645,y=3089,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot154,fg='white',width=16,justify='center').place(x=775,y=3089,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot155,fg='white',width=16,justify='center').place(x=895,y=3089,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot156,fg='white',width=16,justify='center').place(x=1025,y=3089,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total25,fg='white',width=16,justify='center').place(x=1155,y=3089,height=40)

r35=Label(form_frame,text="Telephone Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r35.place(x=80,y=3179)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot157,fg='white',width=16,justify='center').place(x=395,y=3179,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot158,fg='white',width=16,justify='center').place(x=515,y=3179,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot159,fg='white',width=16,justify='center').place(x=645,y=3179,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot160,fg='white',width=16,justify='center').place(x=775,y=3179,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot161,fg='white',width=16,justify='center').place(x=895,y=3179,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot162,fg='white',width=16,justify='center').place(x=1025,y=3179,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total26,fg='white',width=16,justify='center').place(x=1155,y=3179,height=40)

r36=Label(form_frame,text="Travel Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r36.place(x=80,y=3267)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot163,fg='white',width=16,justify='center').place(x=395,y=3267,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot164,fg='white',width=16,justify='center').place(x=515,y=3267,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot165,fg='white',width=16,justify='center').place(x=645,y=3267,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot166,fg='white',width=16,justify='center').place(x=775,y=3267,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot167,fg='white',width=16,justify='center').place(x=895,y=3267,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot168,fg='white',width=16,justify='center').place(x=1025,y=3267,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total27,fg='white',width=16,justify='center').place(x=1155,y=3267,height=40)

r37=Label(form_frame,text="Uncategorised Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r37.place(x=80,y=3357)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot169,fg='white',width=16,justify='center').place(x=395,y=3357,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot170,fg='white',width=16,justify='center').place(x=515,y=3357,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot171,fg='white',width=16,justify='center').place(x=645,y=3357,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot172,fg='white',width=16,justify='center').place(x=775,y=3357,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot173,fg='white',width=16,justify='center').place(x=895,y=3357,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot174,fg='white',width=16,justify='center').place(x=1025,y=3357,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total28,fg='white',width=16,justify='center').place(x=1155,y=3357,height=40)

r38=Label(form_frame,text="Utilities",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r38.place(x=80,y=3447)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot175,fg='white',width=16,justify='center').place(x=395,y=3447,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot176,fg='white',width=16,justify='center').place(x=515,y=3447,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot177,fg='white',width=16,justify='center').place(x=645,y=3447,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot178,fg='white',width=16,justify='center').place(x=775,y=3447,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot179,fg='white',width=16,justify='center').place(x=895,y=3447,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot180,fg='white',width=16,justify='center').place(x=1025,y=3447,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total29,fg='white',width=16,justify='center').place(x=1155,y=3447,height=40)

r39=Label(form_frame,text="Cash and cash\n equivalents",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r39.place(x=80,y=3537)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot181,fg='white',width=16,justify='center').place(x=395,y=3537,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot182,fg='white',width=16,justify='center').place(x=515,y=3537,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot183,fg='white',width=16,justify='center').place(x=645,y=3537,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot184,fg='white',width=16,justify='center').place(x=775,y=3537,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot185,fg='white',width=16,justify='center').place(x=895,y=3537,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot186,fg='white',width=16,justify='center').place(x=1025,y=3537,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total30,fg='white',width=16,justify='center').place(x=1155,y=3537,height=40)

r40=Label(form_frame,text="Accounts Receivable \n(Debtors)",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r40.place(x=80,y=3627)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot187,fg='white',width=16,justify='center').place(x=395,y=3627,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot188,fg='white',width=16,justify='center').place(x=515,y=3627,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot189,fg='white',width=16,justify='center').place(x=645,y=3627,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot190,fg='white',width=16,justify='center').place(x=775,y=3627,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot191,fg='white',width=16,justify='center').place(x=895,y=3627,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot192,fg='white',width=16,justify='center').place(x=1025,y=3627,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total31,fg='white',width=16,justify='center').place(x=1155,y=3627,height=40)


r41=Label(form_frame,text="Deferred CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r41.place(x=80,y=3717)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot193,fg='white',width=16,justify='center').place(x=395,y=3717,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot194,fg='white',width=16,justify='center').place(x=515,y=3717,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot195,fg='white',width=16,justify='center').place(x=645,y=3717,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot196,fg='white',width=16,justify='center').place(x=775,y=3717,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot197,fg='white',width=16,justify='center').place(x=895,y=3717,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot198,fg='white',width=16,justify='center').place(x=1025,y=3717,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total32,fg='white',width=16,justify='center').place(x=1155,y=3717,height=40)

r42=Label(form_frame,text="Deferred GST\n Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r42.place(x=80,y=3807)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot199,fg='white',width=16,justify='center').place(x=395,y=3807,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot200,fg='white',width=16,justify='center').place(x=515,y=3807,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot201,fg='white',width=16,justify='center').place(x=645,y=3807,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot202,fg='white',width=16,justify='center').place(x=775,y=3807,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot203,fg='white',width=16,justify='center').place(x=895,y=3807,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot204,fg='white',width=16,justify='center').place(x=1025,y=3807,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total33,fg='white',width=16,justify='center').place(x=1155,y=3807,height=40)

r43=Label(form_frame,text="Deferred IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r43.place(x=80,y=3897)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot205,fg='white',width=16,justify='center').place(x=395,y=3897,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot206,fg='white',width=16,justify='center').place(x=515,y=3897,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot207,fg='white',width=16,justify='center').place(x=645,y=3897,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot208,fg='white',width=16,justify='center').place(x=775,y=3897,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot209,fg='white',width=16,justify='center').place(x=895,y=3897,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot210,fg='white',width=16,justify='center').place(x=1025,y=3897,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total34,fg='white',width=16,justify='center').place(x=1155,y=3897,height=40)

r44=Label(form_frame,text="Deferred Krishi Kalyan \nCess Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r44.place(x=80,y=3987)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot211,fg='white',width=16,justify='center').place(x=395,y=3987,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot212,fg='white',width=16,justify='center').place(x=515,y=3987,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot213,fg='white',width=16,justify='center').place(x=645,y=3987,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot214,fg='white',width=16,justify='center').place(x=775,y=3987,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot215,fg='white',width=16,justify='center').place(x=895,y=3987,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot216,fg='white',width=16,justify='center').place(x=1025,y=3987,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total35,fg='white',width=16,justify='center').place(x=1155,y=3987,height=40)

r45=Label(form_frame,text="Deferred Service \nTax Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r45.place(x=80,y=4077)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot217,fg='white',width=16,justify='center').place(x=395,y=4077,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot218,fg='white',width=16,justify='center').place(x=515,y=4077,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot219,fg='white',width=16,justify='center').place(x=645,y=4077,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot220,fg='white',width=16,justify='center').place(x=775,y=4077,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot221,fg='white',width=16,justify='center').place(x=895,y=4077,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot222,fg='white',width=16,justify='center').place(x=1025,y=4077,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total36,fg='white',width=16,justify='center').place(x=1155,y=4077,height=40)

r46=Label(form_frame,text="Deferred SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r46.place(x=80,y=4167)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot223,fg='white',width=16,justify='center').place(x=395,y=4167,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot224,fg='white',width=16,justify='center').place(x=515,y=4167,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot225,fg='white',width=16,justify='center').place(x=645,y=4167,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot226,fg='white',width=16,justify='center').place(x=775,y=4167,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot227,fg='white',width=16,justify='center').place(x=895,y=4167,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot228,fg='white',width=16,justify='center').place(x=1025,y=4167,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total37,fg='white',width=16,justify='center').place(x=1155,y=4167,height=40)

r47=Label(form_frame,text="Deferred VAT \nInput Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r47.place(x=80,y=4257)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot229,fg='white',width=16,justify='center').place(x=395,y=4257,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot230,fg='white',width=16,justify='center').place(x=515,y=4257,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot231,fg='white',width=16,justify='center').place(x=645,y=4257,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot232,fg='white',width=16,justify='center').place(x=775,y=4257,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot233,fg='white',width=16,justify='center').place(x=895,y=4257,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot234,fg='white',width=16,justify='center').place(x=1025,y=4257,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total38,fg='white',width=16,justify='center').place(x=1155,y=4257,height=40)

r48=Label(form_frame,text="GST Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r48.place(x=80,y=4347)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot235,fg='white',width=16,justify='center').place(x=395,y=4347,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot236,fg='white',width=16,justify='center').place(x=515,y=4347,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot237,fg='white',width=16,justify='center').place(x=645,y=4347,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot238,fg='white',width=16,justify='center').place(x=775,y=4347,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot239,fg='white',width=16,justify='center').place(x=895,y=4347,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot240,fg='white',width=16,justify='center').place(x=1025,y=4347,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total39,fg='white',width=16,justify='center').place(x=1155,y=4347,height=40)

r49=Label(form_frame,text="Inventory Asset",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r49.place(x=80,y=4437)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot241,fg='white',width=16,justify='center').place(x=395,y=4437,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot242,fg='white',width=16,justify='center').place(x=515,y=4437,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot243,fg='white',width=16,justify='center').place(x=645,y=4437,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot244,fg='white',width=16,justify='center').place(x=775,y=4437,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot245,fg='white',width=16,justify='center').place(x=895,y=4437,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot246,fg='white',width=16,justify='center').place(x=1025,y=4437,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total40,fg='white',width=16,justify='center').place(x=1155,y=4437,height=40)

r50=Label(form_frame,text="Krishi Kalyan \nCess Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r50.place(x=80,y=4527)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot247,fg='white',width=16,justify='center').place(x=395,y=4527,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot248,fg='white',width=16,justify='center').place(x=515,y=4527,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot249,fg='white',width=16,justify='center').place(x=645,y=4527,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot250,fg='white',width=16,justify='center').place(x=775,y=4527,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot251,fg='white',width=16,justify='center').place(x=895,y=4527,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot252,fg='white',width=16,justify='center').place(x=1025,y=4527,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total41,fg='white',width=16,justify='center').place(x=1155,y=4527,height=40)

r51=Label(form_frame,text="Prepaid Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r51.place(x=80,y=4617)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot253,fg='white',width=16,justify='center').place(x=395,y=4617,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot254,fg='white',width=16,justify='center').place(x=515,y=4617,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot255,fg='white',width=16,justify='center').place(x=645,y=4617,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot257,fg='white',width=16,justify='center').place(x=775,y=4617,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot258,fg='white',width=16,justify='center').place(x=895,y=4617,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot258,fg='white',width=16,justify='center').place(x=1025,y=4617,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total42,fg='white',width=16,justify='center').place(x=1155,y=4617,height=40)

r52=Label(form_frame,text="Service Tax Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r52.place(x=80,y=4707)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot259,fg='white',width=16,justify='center').place(x=395,y=4707,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot260,fg='white',width=16,justify='center').place(x=515,y=4707,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot261,fg='white',width=16,justify='center').place(x=645,y=4707,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot262,fg='white',width=16,justify='center').place(x=775,y=4707,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot263,fg='white',width=16,justify='center').place(x=895,y=4707,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot264,fg='white',width=16,justify='center').place(x=1025,y=4707,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total43,fg='white',width=16,justify='center').place(x=1155,y=4707,height=40)

r53=Label(form_frame,text="TDS Receivable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r53.place(x=80,y=4797)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot266,fg='white',width=16,justify='center').place(x=395,y=4797,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot267,fg='white',width=16,justify='center').place(x=515,y=4797,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot268,fg='white',width=16,justify='center').place(x=645,y=4797,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot269,fg='white',width=16,justify='center').place(x=775,y=4797,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot270,fg='white',width=16,justify='center').place(x=895,y=4797,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot271,fg='white',width=16,justify='center').place(x=1025,y=4797,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total44,fg='white',width=16,justify='center').place(x=1155,y=4797,height=40)


r54=Label(form_frame,text="Uncategorised Asset",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r54.place(x=80,y=4887)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot272,fg='white',width=16,justify='center').place(x=395,y=4887,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot273,fg='white',width=16,justify='center').place(x=515,y=4887,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot274,fg='white',width=16,justify='center').place(x=645,y=4887,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot275,fg='white',width=16,justify='center').place(x=775,y=4887,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot276,fg='white',width=16,justify='center').place(x=895,y=4887,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot277,fg='white',width=16,justify='center').place(x=1025,y=4887,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total45,fg='white',width=16,justify='center').place(x=1155,y=4887,height=40)


r55=Label(form_frame,text="Undeposited Funds",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r55.place(x=80,y=4977)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot278,fg='white',width=16,justify='center').place(x=395,y=4977,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot279,fg='white',width=16,justify='center').place(x=515,y=4977,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot280,fg='white',width=16,justify='center').place(x=645,y=4977,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot281,fg='white',width=16,justify='center').place(x=775,y=4977,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot282,fg='white',width=16,justify='center').place(x=895,y=4977,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot283,fg='white',width=16,justify='center').place(x=1025,y=4977,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total46,fg='white',width=16,justify='center').place(x=1155,y=4977,height=40)



r56=Label(form_frame,text="Accumulated Depreciation",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r56.place(x=80,y=5067)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot284,fg='white',width=16,justify='center').place(x=395,y=5067,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot285,fg='white',width=16,justify='center').place(x=515,y=5067,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot286,fg='white',width=16,justify='center').place(x=645,y=5067,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot287,fg='white',width=16,justify='center').place(x=775,y=5067,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot288,fg='white',width=16,justify='center').place(x=895,y=5067,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot289,fg='white',width=16,justify='center').place(x=1025,y=5067,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total47,fg='white',width=16,justify='center').place(x=1155,y=5067,height=40)



r57=Label(form_frame,text="Buildings and\n Improvements",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r57.place(x=80,y=5157)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot290,fg='white',width=16,justify='center').place(x=395,y=5157,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot291,fg='white',width=16,justify='center').place(x=515,y=5157,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot292,fg='white',width=16,justify='center').place(x=645,y=5157,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot293,fg='white',width=16,justify='center').place(x=775,y=5157,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot294,fg='white',width=16,justify='center').place(x=895,y=5157,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot295,fg='white',width=16,justify='center').place(x=1025,y=5157,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total48,fg='white',width=16,justify='center').place(x=1155,y=5157,height=40)



r58=Label(form_frame,text="Furniture and \nEquipment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r58.place(x=80,y=5247)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot296,fg='white',width=16,justify='center').place(x=395,y=5247,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot297,fg='white',width=16,justify='center').place(x=515,y=5247,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot298,fg='white',width=16,justify='center').place(x=645,y=5247,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot299,fg='white',width=16,justify='center').place(x=775,y=5247,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot300,fg='white',width=16,justify='center').place(x=895,y=5247,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot301,fg='white',width=16,justify='center').place(x=1025,y=5247,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total49,fg='white',width=16,justify='center').place(x=1155,y=5247,height=40)


r59=Label(form_frame,text="Land",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r59.place(x=80,y=5337)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot302,fg='white',width=16,justify='center').place(x=395,y=5337,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot303,fg='white',width=16,justify='center').place(x=515,y=5337,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot304,fg='white',width=16,justify='center').place(x=645,y=5337,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot305,fg='white',width=16,justify='center').place(x=775,y=5337,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot306,fg='white',width=16,justify='center').place(x=895,y=5337,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot307,fg='white',width=16,justify='center').place(x=1025,y=5337,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total50,fg='white',width=16,justify='center').place(x=1155,y=5337,height=40)

r60=Label(form_frame,text="Leasehold Improvements",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r60.place(x=80,y=5427)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot308,fg='white',width=16,justify='center').place(x=395,y=5427,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot309,fg='white',width=16,justify='center').place(x=515,y=5427,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot310,fg='white',width=16,justify='center').place(x=645,y=5427,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot311,fg='white',width=16,justify='center').place(x=775,y=5427,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot312,fg='white',width=16,justify='center').place(x=895,y=5427,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot313,fg='white',width=16,justify='center').place(x=1025,y=5427,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total51,fg='white',width=16,justify='center').place(x=1155,y=5427,height=40)

r61=Label(form_frame,text="Vehicles",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r61.place(x=80,y=5517)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot314,fg='white',width=16,justify='center').place(x=395,y=5517,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot315,fg='white',width=16,justify='center').place(x=515,y=5517,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot316,fg='white',width=16,justify='center').place(x=645,y=5517,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot317,fg='white',width=16,justify='center').place(x=775,y=5517,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot318,fg='white',width=16,justify='center').place(x=895,y=5517,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot319,fg='white',width=16,justify='center').place(x=1025,y=5517,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total52,fg='white',width=16,justify='center').place(x=1155,y=5517,height=40)

r62=Label(form_frame,text="CGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r62.place(x=80,y=5607)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot320,fg='white',width=16,justify='center').place(x=395,y=5607,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot321,fg='white',width=16,justify='center').place(x=515,y=5607,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot322,fg='white',width=16,justify='center').place(x=645,y=5607,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot323,fg='white',width=16,justify='center').place(x=775,y=5607,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot324,fg='white',width=16,justify='center').place(x=895,y=5607,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot325,fg='white',width=16,justify='center').place(x=1025,y=5607,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total53,fg='white',width=16,justify='center').place(x=1155,y=5607,height=40)

r63=Label(form_frame,text="CST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r63.place(x=80,y=5697)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot326,fg='white',width=16,justify='center').place(x=395,y=5697,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot327,fg='white',width=16,justify='center').place(x=515,y=5697,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot328,fg='white',width=16,justify='center').place(x=645,y=5697,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot329,fg='white',width=16,justify='center').place(x=775,y=5697,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot330,fg='white',width=16,justify='center').place(x=895,y=5697,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot331,fg='white',width=16,justify='center').place(x=1025,y=5697,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total54,fg='white',width=16,justify='center').place(x=1155,y=5697,height=40)


r64=Label(form_frame,text="CST Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r64.place(x=80,y=5787)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot332,fg='white',width=16,justify='center').place(x=395,y=5787,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot333,fg='white',width=16,justify='center').place(x=515,y=5787,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot334,fg='white',width=16,justify='center').place(x=645,y=5787,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot335,fg='white',width=16,justify='center').place(x=775,y=5787,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot336,fg='white',width=16,justify='center').place(x=895,y=5787,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot337,fg='white',width=16,justify='center').place(x=1025,y=5787,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total55,fg='white',width=16,justify='center').place(x=1155,y=5787,height=40)


r65=Label(form_frame,text="GST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r65.place(x=80,y=5877)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot338,fg='white',width=16,justify='center').place(x=395,y=5877,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot339,fg='white',width=16,justify='center').place(x=515,y=5877,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot340,fg='white',width=16,justify='center').place(x=645,y=5877,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot341,fg='white',width=16,justify='center').place(x=775,y=5877,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot342,fg='white',width=16,justify='center').place(x=895,y=5877,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot343,fg='white',width=16,justify='center').place(x=1025,y=5877,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total56,fg='white',width=16,justify='center').place(x=1155,y=5877,height=40)


r66=Label(form_frame,text="GST Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r66.place(x=80,y=5967)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot344,fg='white',width=16,justify='center').place(x=395,y=5967,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot345,fg='white',width=16,justify='center').place(x=515,y=5967,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot346,fg='white',width=16,justify='center').place(x=645,y=5967,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot347,fg='white',width=16,justify='center').place(x=775,y=5967,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot348,fg='white',width=16,justify='center').place(x=895,y=5967,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot349,fg='white',width=16,justify='center').place(x=1025,y=5967,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total57,fg='white',width=16,justify='center').place(x=1155,y=5967,height=40)


r67=Label(form_frame,text="IGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r67.place(x=80,y=6057)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot350,fg='white',width=16,justify='center').place(x=395,y=6057,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot351,fg='white',width=16,justify='center').place(x=515,y=6057,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot352,fg='white',width=16,justify='center').place(x=645,y=6057,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot353,fg='white',width=16,justify='center').place(x=775,y=6057,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot354,fg='white',width=16,justify='center').place(x=895,y=6057,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot355,fg='white',width=16,justify='center').place(x=1025,y=6057,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total58,fg='white',width=16,justify='center').place(x=1155,y=6057,height=40)


r68=Label(form_frame,text="Input CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r68.place(x=80,y=6147)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot356,fg='white',width=16,justify='center').place(x=395,y=6147,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot357,fg='white',width=16,justify='center').place(x=515,y=6147,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot358,fg='white',width=16,justify='center').place(x=645,y=6147,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot359,fg='white',width=16,justify='center').place(x=775,y=6147,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot360,fg='white',width=16,justify='center').place(x=895,y=6147,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot361,fg='white',width=16,justify='center').place(x=1025,y=6147,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total59,fg='white',width=16,justify='center').place(x=1155,y=6147,height=40)


r69=Label(form_frame,text="Input CGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r69.place(x=80,y=6237)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot362,fg='white',width=16,justify='center').place(x=395,y=6237,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot363,fg='white',width=16,justify='center').place(x=515,y=6237,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot364,fg='white',width=16,justify='center').place(x=645,y=6237,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot365,fg='white',width=16,justify='center').place(x=775,y=6237,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot366,fg='white',width=16,justify='center').place(x=895,y=6237,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot367,fg='white',width=16,justify='center').place(x=1025,y=6237,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total60,fg='white',width=16,justify='center').place(x=1155,y=6237,height=40)


r70=Label(form_frame,text="Input IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r70.place(x=80,y=6327)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot368,fg='white',width=16,justify='center').place(x=395,y=6327,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot369,fg='white',width=16,justify='center').place(x=515,y=6327,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot370,fg='white',width=16,justify='center').place(x=645,y=6327,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot371,fg='white',width=16,justify='center').place(x=775,y=6327,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot372,fg='white',width=16,justify='center').place(x=895,y=6327,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot373,fg='white',width=16,justify='center').place(x=1025,y=6327,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total61,fg='white',width=16,justify='center').place(x=1155,y=6327,height=40)


r71=Label(form_frame,text="Input IGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r71.place(x=80,y=6417)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot374,fg='white',width=16,justify='center').place(x=395,y=6417,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot375,fg='white',width=16,justify='center').place(x=515,y=6417,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot376,fg='white',width=16,justify='center').place(x=645,y=6417,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot377,fg='white',width=16,justify='center').place(x=775,y=6417,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot378,fg='white',width=16,justify='center').place(x=895,y=6417,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot379,fg='white',width=16,justify='center').place(x=1025,y=6417,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total62,fg='white',width=16,justify='center').place(x=1155,y=6417,height=40)


r72=Label(form_frame,text="Input Krishi \nKalyan Cess",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r72.place(x=80,y=6507)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot380,fg='white',width=16,justify='center').place(x=395,y=6507,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot381,fg='white',width=16,justify='center').place(x=515,y=6507,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot382,fg='white',width=16,justify='center').place(x=645,y=6507,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot383,fg='white',width=16,justify='center').place(x=775,y=6507,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot384,fg='white',width=16,justify='center').place(x=895,y=6507,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot385,fg='white',width=16,justify='center').place(x=1025,y=6507,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total63,fg='white',width=16,justify='center').place(x=1155,y=6507,height=40)

r73=Label(form_frame,text="Input Krishi Kalyan\n Cess RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r73.place(x=80,y=6597)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot386,fg='white',width=16,justify='center').place(x=395,y=6597,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot387,fg='white',width=16,justify='center').place(x=515,y=6597,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot388,fg='white',width=16,justify='center').place(x=645,y=6597,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot389,fg='white',width=16,justify='center').place(x=775,y=6597,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot390,fg='white',width=16,justify='center').place(x=895,y=6597,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot391,fg='white',width=16,justify='center').place(x=1025,y=6597,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total64,fg='white',width=16,justify='center').place(x=1155,y=6597,height=40)

r74=Label(form_frame,text="Input Service Tax",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r74.place(x=80,y=6687)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot392,fg='white',width=16,justify='center').place(x=395,y=6687,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot393,fg='white',width=16,justify='center').place(x=515,y=6687,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot394,fg='white',width=16,justify='center').place(x=645,y=6687,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot395,fg='white',width=16,justify='center').place(x=775,y=6687,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot396,fg='white',width=16,justify='center').place(x=895,y=6687,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot397,fg='white',width=16,justify='center').place(x=1025,y=6687,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total65,fg='white',width=16,justify='center').place(x=1155,y=6687,height=40)


r75=Label(form_frame,text="Input Service Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r75.place(x=80,y=6777)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot398,fg='white',width=16,justify='center').place(x=395,y=6777,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot399,fg='white',width=16,justify='center').place(x=515,y=6777,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot400,fg='white',width=16,justify='center').place(x=645,y=6777,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot401,fg='white',width=16,justify='center').place(x=775,y=6777,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot402,fg='white',width=16,justify='center').place(x=895,y=6777,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot403,fg='white',width=16,justify='center').place(x=1025,y=6777,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total66,fg='white',width=16,justify='center').place(x=1155,y=6777,height=40)


r76=Label(form_frame,text="Input SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r76.place(x=80,y=6867)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot404,fg='white',width=16,justify='center').place(x=395,y=6867,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot405,fg='white',width=16,justify='center').place(x=515,y=6867,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot406,fg='white',width=16,justify='center').place(x=645,y=6867,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot407,fg='white',width=16,justify='center').place(x=775,y=6867,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot408,fg='white',width=16,justify='center').place(x=895,y=6867,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot409,fg='white',width=16,justify='center').place(x=1025,y=6867,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total67,fg='white',width=16,justify='center').place(x=1155,y=6867,height=40)


r77=Label(form_frame,text="Input SGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r77.place(x=80,y=6957)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot410,fg='white',width=16,justify='center').place(x=395,y=6957,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot411,fg='white',width=16,justify='center').place(x=515,y=6957,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot412,fg='white',width=16,justify='center').place(x=645,y=6957,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot413,fg='white',width=16,justify='center').place(x=775,y=6957,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot414,fg='white',width=16,justify='center').place(x=895,y=6957,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot415,fg='white',width=16,justify='center').place(x=1025,y=6957,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total68,fg='white',width=16,justify='center').place(x=1155,y=6957,height=40)


r78=Label(form_frame,text="Input VAT 14%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r78.place(x=80,y=7047)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot416,fg='white',width=16,justify='center').place(x=395,y=7047,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot417,fg='white',width=16,justify='center').place(x=515,y=7047,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot418,fg='white',width=16,justify='center').place(x=645,y=7047,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot419,fg='white',width=16,justify='center').place(x=775,y=7047,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot420,fg='white',width=16,justify='center').place(x=895,y=7047,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot421,fg='white',width=16,justify='center').place(x=1025,y=7047,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total69,fg='white',width=16,justify='center').place(x=1155,y=7047,height=40)

r79=Label(form_frame,text="Input VAT 4%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r79.place(x=80,y=7137)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot422,fg='white',width=16,justify='center').place(x=395,y=7137,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot423,fg='white',width=16,justify='center').place(x=515,y=7137,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot424,fg='white',width=16,justify='center').place(x=645,y=7137,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot425,fg='white',width=16,justify='center').place(x=775,y=7137,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot426,fg='white',width=16,justify='center').place(x=895,y=7137,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot427,fg='white',width=16,justify='center').place(x=1025,y=7137,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total70,fg='white',width=16,justify='center').place(x=1155,y=7137,height=40)

r80=Label(form_frame,text="Input VAT 5%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r80.place(x=80,y=7227)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot428,fg='white',width=16,justify='center').place(x=395,y=7227,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot429,fg='white',width=16,justify='center').place(x=515,y=7227,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot430,fg='white',width=16,justify='center').place(x=645,y=7227,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot431,fg='white',width=16,justify='center').place(x=775,y=7227,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot432,fg='white',width=16,justify='center').place(x=895,y=7227,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot433,fg='white',width=16,justify='center').place(x=1025,y=7227,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total71,fg='white',width=16,justify='center').place(x=1155,y=7227,height=40)

r81=Label(form_frame,text="Krishi Kalyan Cess Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r81.place(x=80,y=7317)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot434,fg='white',width=16,justify='center').place(x=395,y=7317,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot435,fg='white',width=16,justify='center').place(x=515,y=7317,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot436,fg='white',width=16,justify='center').place(x=645,y=7317,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot437,fg='white',width=16,justify='center').place(x=775,y=7317,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot438,fg='white',width=16,justify='center').place(x=895,y=7317,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot439,fg='white',width=16,justify='center').place(x=1025,y=7317,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total72,fg='white',width=16,justify='center').place(x=1155,y=7317,height=40)

r82=Label(form_frame,text="Krishi Kalyan Cess Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r82.place(x=80,y=7407)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot440,fg='white',width=16,justify='center').place(x=395,y=7407,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot441,fg='white',width=16,justify='center').place(x=515,y=7407,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot442,fg='white',width=16,justify='center').place(x=645,y=7407,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot443,fg='white',width=16,justify='center').place(x=775,y=7407,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot444,fg='white',width=16,justify='center').place(x=895,y=7407,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot445,fg='white',width=16,justify='center').place(x=1025,y=7407,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total73,fg='white',width=16,justify='center').place(x=1155,y=7407,height=40)

r83=Label(form_frame,text="Output CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r83.place(x=80,y=7497)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot446,fg='white',width=16,justify='center').place(x=395,y=7497,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot447,fg='white',width=16,justify='center').place(x=515,y=7497,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot448,fg='white',width=16,justify='center').place(x=645,y=7497,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot449,fg='white',width=16,justify='center').place(x=775,y=7497,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot450,fg='white',width=16,justify='center').place(x=895,y=7497,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot451,fg='white',width=16,justify='center').place(x=1025,y=7497,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total74,fg='white',width=16,justify='center').place(x=1155,y=7497,height=40)

r84=Label(form_frame,text="Output CGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r84.place(x=80,y=7587)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot452,fg='white',width=16,justify='center').place(x=395,y=7587,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot453,fg='white',width=16,justify='center').place(x=515,y=7587,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot454,fg='white',width=16,justify='center').place(x=645,y=7587,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot455,fg='white',width=16,justify='center').place(x=775,y=7587,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot456,fg='white',width=16,justify='center').place(x=895,y=7587,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot457,fg='white',width=16,justify='center').place(x=1025,y=7587,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total75,fg='white',width=16,justify='center').place(x=1155,y=7587,height=40)

r85=Label(form_frame,text="Output CST 2%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r85.place(x=80,y=7677)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot458,fg='white',width=16,justify='center').place(x=395,y=7677,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot459,fg='white',width=16,justify='center').place(x=515,y=7677,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot460,fg='white',width=16,justify='center').place(x=645,y=7677,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot461,fg='white',width=16,justify='center').place(x=775,y=7677,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot462,fg='white',width=16,justify='center').place(x=895,y=7677,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot463,fg='white',width=16,justify='center').place(x=1025,y=7677,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total76,fg='white',width=16,justify='center').place(x=1155,y=7677,height=40)

r86=Label(form_frame,text="Output IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r86.place(x=80,y=7767)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot464,fg='white',width=16,justify='center').place(x=395,y=7767,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot465,fg='white',width=16,justify='center').place(x=515,y=7767,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot466,fg='white',width=16,justify='center').place(x=645,y=7767,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot467,fg='white',width=16,justify='center').place(x=775,y=7767,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot468,fg='white',width=16,justify='center').place(x=895,y=7767,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot469,fg='white',width=16,justify='center').place(x=1025,y=7767,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total77,fg='white',width=16,justify='center').place(x=1155,y=7767,height=40)

r87=Label(form_frame,text="Output IGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r87.place(x=80,y=7857)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot470,fg='white',width=16,justify='center').place(x=395,y=7857,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot471,fg='white',width=16,justify='center').place(x=515,y=7857,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot472,fg='white',width=16,justify='center').place(x=645,y=7857,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot473,fg='white',width=16,justify='center').place(x=775,y=7857,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot474,fg='white',width=16,justify='center').place(x=895,y=7857,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot475,fg='white',width=16,justify='center').place(x=1025,y=7857,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total78,fg='white',width=16,justify='center').place(x=1155,y=7857,height=40)

r88=Label(form_frame,text="Output Krishi Kalyan Cess",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r88.place(x=80,y=7947)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot476,fg='white',width=16,justify='center').place(x=395,y=7947,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot477,fg='white',width=16,justify='center').place(x=515,y=7947,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot478,fg='white',width=16,justify='center').place(x=645,y=7947,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot479,fg='white',width=16,justify='center').place(x=775,y=7947,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot480,fg='white',width=16,justify='center').place(x=895,y=7947,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot481,fg='white',width=16,justify='center').place(x=1025,y=7947,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total79,fg='white',width=16,justify='center').place(x=1155,y=7947,height=40)

r89=Label(form_frame,text="Output Krishi \nKalyan Cess RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r89.place(x=80,y=8037)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot482,fg='white',width=16,justify='center').place(x=395,y=8037,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot483,fg='white',width=16,justify='center').place(x=515,y=8037,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot484,fg='white',width=16,justify='center').place(x=645,y=8037,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot485,fg='white',width=16,justify='center').place(x=775,y=8037,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot486,fg='white',width=16,justify='center').place(x=895,y=8037,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot487,fg='white',width=16,justify='center').place(x=1025,y=8037,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total80,fg='white',width=16,justify='center').place(x=1155,y=8037,height=40)

r90=Label(form_frame,text="Output Service Tax",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r90.place(x=80,y=8127)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot488,fg='white',width=16,justify='center').place(x=395,y=8127,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot489,fg='white',width=16,justify='center').place(x=515,y=8127,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot490,fg='white',width=16,justify='center').place(x=645,y=8127,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot491,fg='white',width=16,justify='center').place(x=775,y=8127,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot492,fg='white',width=16,justify='center').place(x=895,y=8127,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot493,fg='white',width=16,justify='center').place(x=1025,y=8127,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total81,fg='white',width=16,justify='center').place(x=1155,y=8127,height=40)

r91=Label(form_frame,text="Output Service Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r91.place(x=80,y=8217)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot494,fg='white',width=16,justify='center').place(x=395,y=8217,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot495,fg='white',width=16,justify='center').place(x=515,y=8217,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot496,fg='white',width=16,justify='center').place(x=645,y=8217,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot497,fg='white',width=16,justify='center').place(x=775,y=8217,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot498,fg='white',width=16,justify='center').place(x=895,y=8217,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot499,fg='white',width=16,justify='center').place(x=1025,y=8217,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total82,fg='white',width=16,justify='center').place(x=1155,y=8217,height=40)

r92=Label(form_frame,text="Output SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r92.place(x=80,y=8307)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot500,fg='white',width=16,justify='center').place(x=395,y=8307,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot501,fg='white',width=16,justify='center').place(x=515,y=8307,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot502,fg='white',width=16,justify='center').place(x=645,y=8307,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot503,fg='white',width=16,justify='center').place(x=775,y=8307,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot504,fg='white',width=16,justify='center').place(x=895,y=8307,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot505,fg='white',width=16,justify='center').place(x=1025,y=8307,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total83,fg='white',width=16,justify='center').place(x=1155,y=8307,height=40)

r93=Label(form_frame,text="Output SGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r93.place(x=80,y=8397)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot506,fg='white',width=16,justify='center').place(x=395,y=8397,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot507,fg='white',width=16,justify='center').place(x=515,y=8397,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot508,fg='white',width=16,justify='center').place(x=645,y=8397,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot509,fg='white',width=16,justify='center').place(x=775,y=8397,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot510,fg='white',width=16,justify='center').place(x=895,y=8397,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot511,fg='white',width=16,justify='center').place(x=1025,y=8397,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total84,fg='white',width=16,justify='center').place(x=1155,y=8397,height=40)


r94=Label(form_frame,text="Output VAT 14%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r94.place(x=80,y=8487)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot512,fg='white',width=16,justify='center').place(x=395,y=8487,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot513,fg='white',width=16,justify='center').place(x=515,y=8487,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot514,fg='white',width=16,justify='center').place(x=645,y=8487,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot515,fg='white',width=16,justify='center').place(x=775,y=8487,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot516,fg='white',width=16,justify='center').place(x=895,y=8487,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot517,fg='white',width=16,justify='center').place(x=1025,y=8487,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total85,fg='white',width=16,justify='center').place(x=1155,y=8487,height=40)

r95=Label(form_frame,text="Output VAT 4%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r95.place(x=80,y=8577)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot518,fg='white',width=16,justify='center').place(x=395,y=8577,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot519,fg='white',width=16,justify='center').place(x=515,y=8577,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot520,fg='white',width=16,justify='center').place(x=645,y=8577,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot521,fg='white',width=16,justify='center').place(x=775,y=8577,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot522,fg='white',width=16,justify='center').place(x=895,y=8577,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot523,fg='white',width=16,justify='center').place(x=1025,y=8577,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total86,fg='white',width=16,justify='center').place(x=1155,y=8577,height=40)

r96=Label(form_frame,text="Output VAT 5%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r96.place(x=80,y=8667)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot524,fg='white',width=16,justify='center').place(x=395,y=8667,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot525,fg='white',width=16,justify='center').place(x=515,y=8667,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot526,fg='white',width=16,justify='center').place(x=645,y=8667,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot527,fg='white',width=16,justify='center').place(x=775,y=8667,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot528,fg='white',width=16,justify='center').place(x=895,y=8667,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot529,fg='white',width=16,justify='center').place(x=1025,y=8667,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total87,fg='white',width=16,justify='center').place(x=1155,y=8667,height=40)

r97=Label(form_frame,text="Service Tax Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r97.place(x=80,y=8757)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot530,fg='white',width=16,justify='center').place(x=395,y=8757,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot531,fg='white',width=16,justify='center').place(x=515,y=8757,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot532,fg='white',width=16,justify='center').place(x=645,y=8757,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot533,fg='white',width=16,justify='center').place(x=775,y=8757,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot534,fg='white',width=16,justify='center').place(x=895,y=8757,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot535,fg='white',width=16,justify='center').place(x=1025,y=8757,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total88,fg='white',width=16,justify='center').place(x=1155,y=8757,height=40)

r98=Label(form_frame,text="Service Tax Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r98.place(x=80,y=8847)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot536,fg='white',width=16,justify='center').place(x=395,y=8847,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot537,fg='white',width=16,justify='center').place(x=515,y=8847,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot538,fg='white',width=16,justify='center').place(x=645,y=8847,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot539,fg='white',width=16,justify='center').place(x=775,y=8847,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot540,fg='white',width=16,justify='center').place(x=895,y=8847,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot541,fg='white',width=16,justify='center').place(x=1025,y=8847,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total89,fg='white',width=16,justify='center').place(x=1155,y=8847,height=40)

r99=Label(form_frame,text="SGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r99.place(x=80,y=8937)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot542,fg='white',width=16,justify='center').place(x=395,y=8937,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot543,fg='white',width=16,justify='center').place(x=515,y=8937,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot544,fg='white',width=16,justify='center').place(x=645,y=8937,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot545,fg='white',width=16,justify='center').place(x=775,y=8937,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot546,fg='white',width=16,justify='center').place(x=895,y=8937,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot547,fg='white',width=16,justify='center').place(x=1025,y=8937,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total89,fg='white',width=16,justify='center').place(x=1155,y=8937,height=40)

r100=Label(form_frame,text="Swachh Bharat\n Cess Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r100.place(x=80,y=9027)

input1=Entry(form_frame,bg='#2f516a',textvariable=tot548,fg='white',width=16,justify='center').place(x=395,y=9027,height=40)
input2=Entry(form_frame,bg='#2f516a',textvariable=tot549,fg='white',width=16,justify='center').place(x=515,y=9027,height=40)
input3=Entry(form_frame,bg='#2f516a',textvariable=tot550,fg='white',width=16,justify='center').place(x=645,y=9027,height=40)
input4=Entry(form_frame,bg='#2f516a',textvariable=tot551,fg='white',width=16,justify='center').place(x=775,y=9027,height=40)
input5=Entry(form_frame,bg='#2f516a',textvariable=tot552,fg='white',width=16,justify='center').place(x=895,y=9027,height=40)
input6=Entry(form_frame,bg='#2f516a',textvariable=tot553,fg='white',width=16,justify='center').place(x=1025,y=9027,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total91,fg='white',width=16,justify='center').place(x=1155,y=9027,height=40)

r101=Label(form_frame,text="Swachh Bharat\n Cess Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r101.place(x=80,y=9117)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9117,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9117,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9117,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9117,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9117,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9117,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total92,fg='white',width=16,justify='center').place(x=1155,y=9117,height=40)

r102=Label(form_frame,text="TDS Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r102.place(x=80,y=9207)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9207,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9207,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9207,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9207,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9207,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9207,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total93,fg='white',width=16,justify='center').place(x=1155,y=9207,height=40)

r103=Label(form_frame,text="VAT Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r103.place(x=80,y=9297)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9297,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9297,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9297,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9297,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9297,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9297,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total94,fg='white',width=16,justify='center').place(x=1155,y=9297,height=40)

r104=Label(form_frame,text="Opening Balance Equity",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r104.place(x=80,y=9387)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9387,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9387,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9387,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9387,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9387,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9387,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total95,fg='white',width=16,justify='center').place(x=1155,y=9387,height=40)

r105=Label(form_frame,text="Retained Earnings",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r105.place(x=80,y=9477)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9477,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9477,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9477,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9477,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9477,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9477,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total96,fg='white',width=16,justify='center').place(x=1155,y=9477,height=40)

r106=Label(form_frame,text="Billable Expense Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r106.place(x=80,y=9567)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9567,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9567,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9567,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9567,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9567,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9567,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total97,fg='white',width=16,justify='center').place(x=1155,y=9567,height=40)

r107=Label(form_frame,text="Consulting Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r107.place(x=80,y=9657)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9657,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9657,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9657,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9657,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9657,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9657,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total98,fg='white',width=16,justify='center').place(x=1155,y=9657,height=40)

r108=Label(form_frame,text="Product Sales",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r108.place(x=80,y=9747)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9747,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9747,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9747,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9747,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9747,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9747,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total99,fg='white',width=16,justify='center').place(x=1155,y=9747,height=40)

r109=Label(form_frame,text="Sales",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r109.place(x=80,y=9837)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9837,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9837,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9837,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9837,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9837,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9837,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total100,fg='white',width=16,justify='center').place(x=1155,y=9837,height=40)

r110=Label(form_frame,text="Sales - Hardware",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r110.place(x=80,y=9927)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9927,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9927,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9927,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9927,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9927,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9927,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total101,fg='white',width=16,justify='center').place(x=1155,y=9927,height=40)

r111=Label(form_frame,text="Sales - Software",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r111.place(x=80,y=10017)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10017,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10017,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10017,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10017,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10017,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10017,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total102,fg='white',width=16,justify='center').place(x=1155,y=10017,height=40)

r112=Label(form_frame,text="Sales - Support\n and Maintenance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r112.place(x=80,y=10107)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10107,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10107,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10107,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10107,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10107,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10107,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total103,fg='white',width=16,justify='center').place(x=1155,y=10107,height=40)

r113=Label(form_frame,text="Sales Discounts",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r113.place(x=80,y=10197)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10197,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10197,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10197,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10197,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10197,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10197,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total104,fg='white',width=16,justify='center').place(x=1155,y=10197,height=40)

r114=Label(form_frame,text="Sales of Product Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r114.place(x=80,y=10287)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10287,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10287,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10287,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10287,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10287,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10287,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total105,fg='white',width=16,justify='center').place(x=1155,y=10287,height=40)

r115=Label(form_frame,text="Uncategorised Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r115.place(x=80,y=10377)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10377,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10377,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10377,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10377,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10377,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10377,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total106,fg='white',width=16,justify='center').place(x=1155,y=10377,height=40)

r116=Label(form_frame,text="Cost of sales",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r116.place(x=80,y=10467)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10467,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10467,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10467,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10467,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10467,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10467,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total107,fg='white',width=16,justify='center').place(x=1155,y=10467,height=40)

r117=Label(form_frame,text="Equipment \nRental for Jobs",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r117.place(x=80,y=10557)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10557,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10557,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10557,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10557,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10557,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10557,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total108,fg='white',width=16,justify='center').place(x=1155,y=10557,height=40)

r118=Label(form_frame,text="Freight and Shipping Costs",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r118.place(x=80,y=10647)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10647,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10647,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10647,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10647,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10647,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10647,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total109,fg='white',width=16,justify='center').place(x=1155,y=10647,height=40)

r119=Label(form_frame,text="Merchant Account Fees",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r119.place(x=80,y=10737)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10737,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10737,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10737,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10737,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10737,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10737,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total110,fg='white',width=16,justify='center').place(x=1155,y=10737,height=40)

r120=Label(form_frame,text="Purchases - Hardware \nfor Resale",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r120.place(x=80,y=10827)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10827,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10827,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10827,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10827,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10827,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10827,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total111,fg='white',width=16,justify='center').place(x=1155,y=10827,height=40)

r121=Label(form_frame,text="Purchases - Software\n for Resale",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r121.place(x=80,y=10917)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=10917,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=10917,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=10917,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=10917,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=10917,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=10917,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total112,fg='white',width=16,justify='center').place(x=1155,y=10917,height=40)

r122=Label(form_frame,text="Subcontracted Services",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r122.place(x=80,y=11007)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11007,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11007,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11007,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11007,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11007,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11007,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total113,fg='white',width=16,justify='center').place(x=1155,y=11007,height=40)

r123=Label(form_frame,text="Tools and Craft Supplies",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r123.place(x=80,y=11097)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11097,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11097,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11097,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11097,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11097,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11097,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total114,fg='white',width=16,justify='center').place(x=1155,y=11097,height=40)

r124=Label(form_frame,text="Finance Charge Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r124.place(x=80,y=11187)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11187,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11187,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11187,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11187,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11187,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11187,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total115,fg='white',width=16,justify='center').place(x=1155,y=11187,height=40)


r125=Label(form_frame,text="Insurance Proceeds Received",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r125.place(x=80,y=11277)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11277,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11277,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11277,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11277,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11277,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11277,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total116,fg='white',width=16,justify='center').place(x=1155,y=11277,height=40)



r126=Label(form_frame,text="Interest Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r126.place(x=80,y=11367)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11367,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11367,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11367,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11367,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11367,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11367,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total117,fg='white',width=16,justify='center').place(x=1155,y=11367,height=40)


r127=Label(form_frame,text="Proceeds from \nSale of Assets",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r127.place(x=80,y=11457)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11457,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11457,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11457,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11457,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11457,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11457,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total118,fg='white',width=16,justify='center').place(x=1155,y=11457,height=40)


r128=Label(form_frame,text="Shipping and \nDelivery Income",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r128.place(x=80,y=11547)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11547,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11547,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11547,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11547,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11547,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11547,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total119,fg='white',width=16,justify='center').place(x=1155,y=11547,height=40)


r129=Label(form_frame,text="Ask My Accountant",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r129.place(x=80,y=11637)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11637,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11637,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11637,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11637,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11637,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11637,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total120,fg='white',width=16,justify='center').place(x=1155,y=11637,height=40)


r130=Label(form_frame,text="CGST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r130.place(x=80,y=11727)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11727,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11727,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11727,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11727,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11727,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11727,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total121,fg='white',width=16,justify='center').place(x=1155,y=11727,height=40)


r131=Label(form_frame,text="GST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r131.place(x=80,y=11817)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11817,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11817,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11817,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11817,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11817,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11817,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total122,fg='white',width=16,justify='center').place(x=1155,y=11817,height=40)


r132=Label(form_frame,text="IGST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r132.place(x=80,y=11907)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11907,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11907,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11907,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11907,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11907,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11907,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total123,fg='white',width=16,justify='center').place(x=1155,y=11907,height=40)


r133=Label(form_frame,text="Miscellaneous Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r133.place(x=80,y=11997)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=11997,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=11997,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=11997,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=11997,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=11997,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=11997,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total124,fg='white',width=16,justify='center').place(x=1155,y=11997,height=40)


r134=Label(form_frame,text="Political Contributions",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r134.place(x=80,y=12087)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=12087,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=12087,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=12087,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=12087,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=12087,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=12087,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total125,fg='white',width=16,justify='center').place(x=1155,y=12087,height=40)


r135=Label(form_frame,text="SGST write-off",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r135.place(x=80,y=12177)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=12177,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=12177,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=12177,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=12177,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=12177,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=12177,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total126,fg='white',width=16,justify='center').place(x=1155,y=12177,height=40)


r136=Label(form_frame,text="Tax write-of",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r136.place(x=80,y=12267)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=12267,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=12267,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=12267,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=12267,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=12267,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=12267,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total127,fg='white',width=16,justify='center').place(x=1155,y=12267,height=40)


r137=Label(form_frame,text="Vehicle Expenses",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r137.place(x=80,y=12357)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=12357,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=12357,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=12357,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=12357,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=12357,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=12357,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total128,fg='white',width=16,justify='center').place(x=1155,y=12357,height=40)


r138=Label(form_frame,text="Other Cash Out Flows:",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r138.place(x=80,y=12447)

r139=Label(form_frame,text="Capital\nPurchases",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r139.place(x=80,y=12537)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12537,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12537,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12537,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12537,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12537,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12537,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12537,height=40)

r140=Label(form_frame,text="Loan Principal",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r140.place(x=80,y=12627)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12627,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12627,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12627,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12627,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12627,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12627,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12627,height=40)

r141=Label(form_frame,text="Owner's Draw",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r141.place(x=80,y=12717)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12717,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12717,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12717,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12717,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12717,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12717,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12717,height=40)

r142=Label(form_frame,text="Other:",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r142.place(x=80,y=12807)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12807,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12807,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12807,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12807,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12807,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12807,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12807,height=40)

r143=Label(form_frame,text="Subtotal",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r143.place(x=80,y=12897)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12897,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12897,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12897,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12897,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12897,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12897,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12897,height=40)

r144=Label(form_frame,text="Total Cash\nOutflows",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r144.place(x=80,y=12987)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=12989,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=12989,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=12989,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=12989,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=12989,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=12989,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=12989,height=40)

r145=Label(form_frame,text="Ending Cash\nBalance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r145.place(x=80,y=13077)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=395,y=13079,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=515,y=13079,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=645,y=13079,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=775,y=13079,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=895,y=13079,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1025,y=13079,height=40)
input7=Entry(form_frame,bg='#2f516a',fg='white',width=16).place(x=1155,y=13079,height=40)

window.mainloop()
