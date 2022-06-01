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
jun7="SELECT ROUND(SUM(grandtotal),3) FROM app1_expences WHERE paymmethod='cash'AND monthname(paymdate)='June' AND(category1='Insurance Expense')"
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
query13="SELECT ROUND(SUM(grandtotal),3) FROM `app1_expences` WHERE paymmethod='cash' AND category1='Insurance Expense-Life and Disability IInsurance Expense-Professional Liabilitynsurance' "
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



label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=395,y=160)

label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=523,y=160)

label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=653,y=160)
label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=783,y=160)
label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=913,y=160)
label=Label(form_frame,text="[MONTH]",bg='#243e55' ,fg="white",font=('Arial',15))
label.place(x=1043,y=160)
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
tot2.set(tab8)
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
tot9.set(tab7)
tot10=tk.StringVar()
tot10.set(tab8)
tot11=tk.StringVar()
tot11.set(tab7)
tot12=tk.StringVar()
tot12.set(tab8)
tot13=tk.StringVar()
tot13.set(tab7)
tot14=tk.StringVar()
tot14.set(tab8)
tot15=tk.StringVar()
tot15.set(tab7)
tot15=tk.StringVar()
tot15.set(tab8)
tot16=tk.StringVar()
tot16.set(tab7)
tot17=tk.StringVar()
tot17.set(tab8)
tot18=tk.StringVar()
tot18.set(tab9)
tot19=tk.StringVar()
tot19.set(tab10)
tot20=tk.StringVar()
tot20.set(tab11)
tot21=tk.StringVar()
tot21.set(tab12)
tot22=tk.StringVar()
tot22.set(tab13)
tot23=tk.StringVar()
tot23.set(tab14)
tot24=tk.StringVar()
tot24.set(tab15)
tot25=tk.StringVar()
tot25.set(tab16)
tot26=tk.StringVar()
tot26.set(tab17)
tot27=tk.StringVar()
tot27.set(tab18)
tot28=tk.StringVar()
tot28.set(tab19)
tot29=tk.StringVar()
tot29.set(tab20)
tot30=tk.StringVar()
tot30.set(tab21)
tot31=tk.StringVar()
tot31.set(tab22)
tot32=tk.StringVar()
tot32.set(tab23)
tot33=tk.StringVar()
tot33.set(tab24)
tot34=tk.StringVar()
tot34.set(tab25)
tot35=tk.StringVar()
tot35.set(tab26)
tot36=tk.StringVar()
tot36.set(tab27)
tot37=tk.StringVar()
tot37.set(tab28)
tot38=tk.StringVar()
tot38.set(tab29)
tot39=tk.StringVar()
tot39.set(tab30)
tot40=tk.StringVar()
tot40.set(tab31)
tot41=tk.StringVar()
tot41.set(tab32)


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
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1375,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total6,fg='white',width=16,justify='center').place(x=1155,y=1375,height=40)

r16=Label(form_frame,text="Dues and Subscriptions",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r16.place(x=80,y=1469)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=1465,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=1465,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=1465,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=1465,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=1465,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1465,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total7,fg='white',width=16,justify='center').place(x=1155,y=1465,height=40)

r17=Label(form_frame,text="Housekeeping Charges",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r17.place(x=80,y=1555)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=1555,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=1555,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=1555,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=1555,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=1555,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1555,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total8,fg='white',width=16,justify='center').place(x=1155,y=1555,height=40)

r18=Label(form_frame,text="Insurance Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r18.place(x=80,y=1649)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=1645,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=1645,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=1645,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=1645,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=1645,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1645,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total9,fg='white',width=16,justify='center').place(x=1155,y=1645,height=40)

r19=Label(form_frame,text="Insurance Expense-General\nLiability Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r19.place(x=80,y=1739)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=1735,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=1735,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=1735,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=1735,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=1735,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1735,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total10,fg='white',width=16,justify='center').place(x=1155,y=1735,height=40)

r20=Label(form_frame,text="Insurance Expense-Health\nInsurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r20.place(x=80,y=1825)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=1825,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=1825,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=1825,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=1825,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=1825,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1825,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total11,fg='white',width=16,justify='center').place(x=1155,y=1825,height=40)


r21=Label(form_frame,text="Insurance Expense-Life\nand Disability Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r21.place(x=80,y=1919)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=1919,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=1919,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=1919,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=1919,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=1919,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=1919,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total12,fg='white',width=16,justify='center').place(x=1155,y=1919,height=40)

r22=Label(form_frame,text="Insurance Expense-Professional\nLiability",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r22.place(x=80,y=2009)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2009,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2009,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2009,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2009,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2009,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2009,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total13,fg='white',width=16,justify='center').place(x=1155,y=2009,height=40)

r23=Label(form_frame,text="Interest Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r23.place(x=80,y=2099)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2099,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2099,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2099,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2099,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2099,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2099,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total14,fg='white',width=16,justify='center').place(x=1155,y=2099,height=40)

r24=Label(form_frame,text="Meals and entertainment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r24.place(x=80,y=2189)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2189,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2189,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2189,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2189,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2189,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2189,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total15,fg='white',width=16,justify='center').place(x=1155,y=2189,height=40)

r25=Label(form_frame,text="Office Supplies",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r25.place(x=80,y=2279)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2279,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2279,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2279,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2279,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2279,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2279,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total16,fg='white',width=16,justify='center').place(x=1155,y=2279,height=40)

r26=Label(form_frame,text="Postage and Delivery",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r26.place(x=80,y=2369)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2369,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2369,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2369,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2369,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2369,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2369,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total17,fg='white',width=16,justify='center').place(x=1155,y=2369,height=40)

r27=Label(form_frame,text="Printing and Reproduction",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r27.place(x=80,y=2459)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2455,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2455,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2455,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2455,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2455,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2455,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total18,fg='white',width=16,justify='center').place(x=1155,y=2455,height=40)

r28=Label(form_frame,text="Professional Fees",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r28.place(x=80,y=2549)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2549,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2549,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2549,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2549,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2549,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2549,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total19,fg='white',width=16,justify='center').place(x=1155,y=2549,height=40)

r29=Label(form_frame,text="Purchases",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r29.place(x=80,y=2639)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2639,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2639,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2639,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2639,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2639,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2639,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total20,fg='white',width=16,justify='center').place(x=1155,y=2639,height=40)



r30=Label(form_frame,text="Rent Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r30.place(x=80,y=2729)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2729,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2729,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2729,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2729,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2729,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2729,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total21,fg='white',width=16,justify='center').place(x=1155,y=2729,height=40)

r31=Label(form_frame,text="Repair and maintenance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r31.place(x=80,y=2819)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2819,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2819,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2819,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2819,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2819,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2819,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total22,fg='white',width=16,justify='center').place(x=1155,y=2819,height=40)

r32=Label(form_frame,text="Small Tools and Equipment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r32.place(x=80,y=2909)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2909,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2909,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2909,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2909,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2909,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2909,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total23,fg='white',width=16,justify='center').place(x=1155,y=2909,height=40)

r33=Label(form_frame,text="Swachh Bharat Cess Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r33.place(x=80,y=2999)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=2999,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=2999,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=2999,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=2999,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=2999,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=2999,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total24,fg='white',width=16,justify='center').place(x=1155,y=2999,height=40)

r34=Label(form_frame,text="Taxes - Property",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r34.place(x=80,y=3089)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3089,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3089,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3089,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3089,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3089,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3089,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total25,fg='white',width=16,justify='center').place(x=1155,y=3089,height=40)

r35=Label(form_frame,text="Telephone Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r35.place(x=80,y=3179)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3179,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3179,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3179,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3179,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3179,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3179,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total26,fg='white',width=16,justify='center').place(x=1155,y=3179,height=40)

r36=Label(form_frame,text="Travel Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r36.place(x=80,y=3267)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3267,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3267,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3267,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3267,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3267,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3267,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total27,fg='white',width=16,justify='center').place(x=1155,y=3267,height=40)

r37=Label(form_frame,text="Uncategorised Expense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r37.place(x=80,y=3357)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3357,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3357,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3357,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3357,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3357,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3357,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total28,fg='white',width=16,justify='center').place(x=1155,y=3357,height=40)

r38=Label(form_frame,text="Utilities",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r38.place(x=80,y=3447)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3447,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3447,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3447,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3447,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3447,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3447,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total29,fg='white',width=16,justify='center').place(x=1155,y=3447,height=40)

r39=Label(form_frame,text="Cash and cash\n equivalents",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r39.place(x=80,y=3537)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3537,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3537,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3537,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3537,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3537,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3537,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total30,fg='white',width=16,justify='center').place(x=1155,y=3537,height=40)

r40=Label(form_frame,text="Accounts Receivable \n(Debtors)",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r40.place(x=80,y=3627)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3627,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3627,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3627,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3627,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3627,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3627,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total31,fg='white',width=16,justify='center').place(x=1155,y=3627,height=40)


r41=Label(form_frame,text="Deferred CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r41.place(x=80,y=3717)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3717,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3717,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3717,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3717,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3717,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3717,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total32,fg='white',width=16,justify='center').place(x=1155,y=3717,height=40)

r42=Label(form_frame,text="Deferred GST\n Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r42.place(x=80,y=3807)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3807,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3807,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3807,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3807,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3807,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3807,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total33,fg='white',width=16,justify='center').place(x=1155,y=3807,height=40)

r43=Label(form_frame,text="Deferred IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r43.place(x=80,y=3897)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3897,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3897,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3897,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3897,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3897,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3897,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total34,fg='white',width=16,justify='center').place(x=1155,y=3897,height=40)

r44=Label(form_frame,text="Deferred Krishi Kalyan \nCess Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r44.place(x=80,y=3987)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=3987,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=3987,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=3987,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=3987,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=3987,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=3987,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total35,fg='white',width=16,justify='center').place(x=1155,y=3987,height=40)

r45=Label(form_frame,text="Deferred Service \nTax Input Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r45.place(x=80,y=4077)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4077,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4077,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4077,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4077,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4077,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4077,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total36,fg='white',width=16,justify='center').place(x=1155,y=4077,height=40)

r46=Label(form_frame,text="Deferred SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r46.place(x=80,y=4167)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4167,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4167,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4167,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4167,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4167,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4167,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total37,fg='white',width=16,justify='center').place(x=1155,y=4167,height=40)

r47=Label(form_frame,text="Deferred VAT \nInput Credit",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r47.place(x=80,y=4257)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4257,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4257,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4257,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4257,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4257,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4257,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total38,fg='white',width=16,justify='center').place(x=1155,y=4257,height=40)

r48=Label(form_frame,text="GST Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r48.place(x=80,y=4347)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4347,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4347,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4347,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4347,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4347,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4347,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total39,fg='white',width=16,justify='center').place(x=1155,y=4347,height=40)

r49=Label(form_frame,text="Inventory Asset",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r49.place(x=80,y=4437)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4437,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4437,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4437,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4437,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4437,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4437,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total40,fg='white',width=16,justify='center').place(x=1155,y=4437,height=40)

r50=Label(form_frame,text="Krishi Kalyan \nCess Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r50.place(x=80,y=4527)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4527,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4527,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4527,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4527,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4527,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4527,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total41,fg='white',width=16,justify='center').place(x=1155,y=4527,height=40)

r51=Label(form_frame,text="Prepaid Insurance",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r51.place(x=80,y=4617)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4617,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4617,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4617,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4617,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4617,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4617,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total42,fg='white',width=16,justify='center').place(x=1155,y=4617,height=40)

r52=Label(form_frame,text="Service Tax Refund",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r52.place(x=80,y=4707)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4707,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4707,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4707,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4707,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4707,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4707,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total43,fg='white',width=16,justify='center').place(x=1155,y=4707,height=40)

r53=Label(form_frame,text="TDS Receivable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r53.place(x=80,y=4797)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4797,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4797,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4797,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4797,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4797,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4797,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total44,fg='white',width=16,justify='center').place(x=1155,y=4797,height=40)


r54=Label(form_frame,text="Uncategorised Asset",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r54.place(x=80,y=4887)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4887,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4887,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4887,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4887,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4887,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4887,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total45,fg='white',width=16,justify='center').place(x=1155,y=4887,height=40)


r55=Label(form_frame,text="Undeposited Funds",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r55.place(x=80,y=4977)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=4977,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=4977,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=4977,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=4977,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=4977,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=4977,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total46,fg='white',width=16,justify='center').place(x=1155,y=4977,height=40)



r56=Label(form_frame,text="Accumulated Depreciation",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r56.place(x=80,y=5067)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5067,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5067,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5067,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5067,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5067,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5067,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total47,fg='white',width=16,justify='center').place(x=1155,y=5067,height=40)



r57=Label(form_frame,text="Buildings and\n Improvements",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r57.place(x=80,y=5157)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5157,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5157,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5157,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5157,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5157,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5157,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total48,fg='white',width=16,justify='center').place(x=1155,y=5157,height=40)



r58=Label(form_frame,text="Furniture and \nEquipment",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r58.place(x=80,y=5247)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5247,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5247,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5247,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5247,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5247,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5247,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total49,fg='white',width=16,justify='center').place(x=1155,y=5247,height=40)


r59=Label(form_frame,text="Land",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r59.place(x=80,y=5337)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5337,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5337,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5337,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5337,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5337,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5337,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total50,fg='white',width=16,justify='center').place(x=1155,y=5337,height=40)

r60=Label(form_frame,text="Leasehold Improvements",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r60.place(x=80,y=5427)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5427,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5427,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5427,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5427,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5427,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5427,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total51,fg='white',width=16,justify='center').place(x=1155,y=5427,height=40)

r61=Label(form_frame,text="Vehicles",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r61.place(x=80,y=5517)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5517,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5517,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5517,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5517,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5517,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5517,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total52,fg='white',width=16,justify='center').place(x=1155,y=5517,height=40)

r62=Label(form_frame,text="CGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r62.place(x=80,y=5607)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5607,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5607,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5607,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5607,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5607,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5607,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total53,fg='white',width=16,justify='center').place(x=1155,y=5607,height=40)

r63=Label(form_frame,text="CST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r63.place(x=80,y=5697)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5697,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5697,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5697,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5697,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5697,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5697,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total54,fg='white',width=16,justify='center').place(x=1155,y=5697,height=40)


r64=Label(form_frame,text="CST Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r64.place(x=80,y=5787)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5787,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5787,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5787,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5787,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5787,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5787,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total55,fg='white',width=16,justify='center').place(x=1155,y=5787,height=40)


r65=Label(form_frame,text="GST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r65.place(x=80,y=5877)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5877,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5877,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5877,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5877,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5877,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5877,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total56,fg='white',width=16,justify='center').place(x=1155,y=5877,height=40)


r66=Label(form_frame,text="GST Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r66.place(x=80,y=5967)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=5967,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=5967,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=5967,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=5967,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=5967,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=5967,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total57,fg='white',width=16,justify='center').place(x=1155,y=5967,height=40)


r67=Label(form_frame,text="IGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r67.place(x=80,y=6057)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6057,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6057,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6057,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6057,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6057,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6057,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total58,fg='white',width=16,justify='center').place(x=1155,y=6057,height=40)


r68=Label(form_frame,text="Input CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r68.place(x=80,y=6147)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6147,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6147,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6147,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6147,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6147,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6147,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total59,fg='white',width=16,justify='center').place(x=1155,y=6147,height=40)


r69=Label(form_frame,text="Input CGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r69.place(x=80,y=6237)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6237,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6237,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6237,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6237,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6237,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6237,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total60,fg='white',width=16,justify='center').place(x=1155,y=6237,height=40)


r70=Label(form_frame,text="Input IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r70.place(x=80,y=6327)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6327,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6327,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6327,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6327,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6327,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6327,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total61,fg='white',width=16,justify='center').place(x=1155,y=6327,height=40)


r71=Label(form_frame,text="Input IGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r71.place(x=80,y=6417)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6417,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6417,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6417,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6417,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6417,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6417,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total62,fg='white',width=16,justify='center').place(x=1155,y=6417,height=40)


r72=Label(form_frame,text="Input Krishi \nKalyan Cess",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r72.place(x=80,y=6507)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6507,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6507,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6507,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6507,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6507,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6507,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total63,fg='white',width=16,justify='center').place(x=1155,y=6507,height=40)

r73=Label(form_frame,text="Input Krishi Kalyan\n Cess RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r73.place(x=80,y=6597)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6597,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6597,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6597,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6597,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6597,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6597,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total64,fg='white',width=16,justify='center').place(x=1155,y=6597,height=40)

r74=Label(form_frame,text="Input Service Tax",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r74.place(x=80,y=6687)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6687,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6687,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6687,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6687,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6687,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6687,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total65,fg='white',width=16,justify='center').place(x=1155,y=6687,height=40)


r75=Label(form_frame,text="Input Service Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r75.place(x=80,y=6777)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6777,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6777,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6777,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6777,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6777,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6777,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total66,fg='white',width=16,justify='center').place(x=1155,y=6777,height=40)


r76=Label(form_frame,text="Input SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r76.place(x=80,y=6867)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6867,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6867,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6867,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6867,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6867,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6867,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total67,fg='white',width=16,justify='center').place(x=1155,y=6867,height=40)


r77=Label(form_frame,text="Input SGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r77.place(x=80,y=6957)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=6957,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=6957,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=6957,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=6957,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=6957,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=6957,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total68,fg='white',width=16,justify='center').place(x=1155,y=6957,height=40)


r78=Label(form_frame,text="Input VAT 14%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r78.place(x=80,y=7047)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7047,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7047,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7047,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7047,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7047,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7047,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total69,fg='white',width=16,justify='center').place(x=1155,y=7047,height=40)

r79=Label(form_frame,text="Input VAT 4%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r79.place(x=80,y=7137)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7137,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7137,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7137,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7137,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7137,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7137,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total70,fg='white',width=16,justify='center').place(x=1155,y=7137,height=40)

r80=Label(form_frame,text="Input VAT 5%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r80.place(x=80,y=7227)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7227,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7227,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7227,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7227,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7227,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7227,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total71,fg='white',width=16,justify='center').place(x=1155,y=7227,height=40)

r81=Label(form_frame,text="Krishi Kalyan Cess Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r81.place(x=80,y=7317)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7317,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7317,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7317,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7317,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7317,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7317,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total72,fg='white',width=16,justify='center').place(x=1155,y=7317,height=40)

r82=Label(form_frame,text="Krishi Kalyan Cess Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r82.place(x=80,y=7407)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7407,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7407,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7407,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7407,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7407,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7407,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total73,fg='white',width=16,justify='center').place(x=1155,y=7407,height=40)

r83=Label(form_frame,text="Output CGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r83.place(x=80,y=7497)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7497,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7497,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7497,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7497,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7497,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7497,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total74,fg='white',width=16,justify='center').place(x=1155,y=7497,height=40)

r84=Label(form_frame,text="Output CGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r84.place(x=80,y=7587)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7587,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7587,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7587,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7587,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7587,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7587,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total75,fg='white',width=16,justify='center').place(x=1155,y=7587,height=40)

r85=Label(form_frame,text="Output CST 2%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r85.place(x=80,y=7677)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7677,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7677,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7677,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7677,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7677,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7677,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total76,fg='white',width=16,justify='center').place(x=1155,y=7677,height=40)

r86=Label(form_frame,text="Output IGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r86.place(x=80,y=7767)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7767,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7767,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7767,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7767,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7767,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7767,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total77,fg='white',width=16,justify='center').place(x=1155,y=7767,height=40)

r87=Label(form_frame,text="Output IGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r87.place(x=80,y=7857)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7857,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7857,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7857,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7857,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7857,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7857,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total78,fg='white',width=16,justify='center').place(x=1155,y=7857,height=40)

r88=Label(form_frame,text="Output Krishi Kalyan Cess",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r88.place(x=80,y=7947)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=7947,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=7947,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=7947,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=7947,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=7947,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=7947,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total79,fg='white',width=16,justify='center').place(x=1155,y=7947,height=40)

r89=Label(form_frame,text="Output Krishi \nKalyan Cess RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r89.place(x=80,y=8037)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8037,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8037,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8037,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8037,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8037,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8037,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total80,fg='white',width=16,justify='center').place(x=1155,y=8037,height=40)

r90=Label(form_frame,text="Output Service Tax",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r90.place(x=80,y=8127)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8127,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8127,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8127,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8127,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8127,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8127,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total81,fg='white',width=16,justify='center').place(x=1155,y=8127,height=40)

r91=Label(form_frame,text="Output Service Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r91.place(x=80,y=8217)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8217,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8217,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8217,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8217,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8217,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8217,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total82,fg='white',width=16,justify='center').place(x=1155,y=8217,height=40)

r92=Label(form_frame,text="Output SGST",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r92.place(x=80,y=8307)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8307,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8307,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8307,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8307,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8307,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8307,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total83,fg='white',width=16,justify='center').place(x=1155,y=8307,height=40)

r93=Label(form_frame,text="Output SGST Tax RCM",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r93.place(x=80,y=8397)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8397,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8397,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8397,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8397,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8397,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8397,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total84,fg='white',width=16,justify='center').place(x=1155,y=8397,height=40)


r94=Label(form_frame,text="Output VAT 14%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r94.place(x=80,y=8487)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8487,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8487,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8487,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8487,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8487,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8487,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total85,fg='white',width=16,justify='center').place(x=1155,y=8487,height=40)

r95=Label(form_frame,text="Output VAT 4%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r95.place(x=80,y=8577)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8577,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8577,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8577,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8577,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8577,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8577,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total86,fg='white',width=16,justify='center').place(x=1155,y=8577,height=40)

r96=Label(form_frame,text="Output VAT 5%",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r96.place(x=80,y=8667)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8667,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8667,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8667,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8667,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8667,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8667,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total87,fg='white',width=16,justify='center').place(x=1155,y=8667,height=40)

r97=Label(form_frame,text="Service Tax Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r97.place(x=80,y=8757)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8757,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8757,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8757,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8757,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8757,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8757,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total88,fg='white',width=16,justify='center').place(x=1155,y=8757,height=40)

r98=Label(form_frame,text="Service Tax Suspense",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r98.place(x=80,y=8847)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8847,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8847,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8847,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8847,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8847,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8847,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total89,fg='white',width=16,justify='center').place(x=1155,y=8847,height=40)

r99=Label(form_frame,text="SGST Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r99.place(x=80,y=8937)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=8937,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=8937,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=8937,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=8937,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=8937,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=8937,height=40)
input7=Entry(form_frame,bg='#2f516a',textvariable=total89,fg='white',width=16,justify='center').place(x=1155,y=8937,height=40)

r100=Label(form_frame,text="Swachh Bharat\n Cess Payable",bg='#243e55' ,fg="white",font=('Arial',16),justify='left')
r100.place(x=80,y=9027)

input1=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=395,y=9027,height=40)
input2=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=515,y=9027,height=40)
input3=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=645,y=9027,height=40)
input4=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=775,y=9027,height=40)
input5=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=895,y=9027,height=40)
input6=Entry(form_frame,bg='#2f516a',fg='white',width=16,justify='center').place(x=1025,y=9027,height=40)
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
