
from tkinter import *
import tkinter.font as font
import tkinter as tk
root = tk.Tk()
root.title('fynsYs')
root.geometry("700x700")
root['bg']='#2f516a'

headingfont=font.Font(family='Helvitica', size=24,)
inv_heading= Label(root, borderwidth=1, relief="raised",width=60,font=headingfont,bg='#243e55', fg='#fff',height=4)
inv_heading.pack(pady=20)
cashposition=Label(root,text="Today: $ 3556345 USD",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 220, y =50)
cash=Label(root,text="CASH POSITION",font=('Helvitica',25),bg='#243e55',fg='white').place(x = 220, y =110)  
    

#here is for bar chart............

tk.Label(root, text='Bar Chart',font=('Helvitica',24),bg='#2f516a',fg='white').pack()
data = [21, 20, 19, 16, 14, 13, 11, 9, 4, 3]
c_width = 400
c_height = 350
c = tk.Canvas(root, width=1000, height=500, bg= '#243e55')
c.pack()

#experiment with the variables below size to fit your needs

y_stretch = 15
y_gap = 20
x_stretch = 10
x_width = 20
x_gap = 20
for x, y in enumerate(data):
# calculate reactangle coordinates
 x0 = x * x_stretch + x * x_width + x_gap
 y0 = c_height - (y * y_stretch + y_gap)
 x1 = x * x_stretch + x * x_width + x_width + x_gap
 y1 = c_height - y_gap
# Here we draw the bar
 c.create_rectangle(x0, y0, x1, y1, fill="#3a8cb5")
 c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))
root.mainloop()