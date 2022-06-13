# # Firstly import Tkinter Module 
# from tkinter import * 
# from tkinter.ttk import *
# import tkinter as tk
# # Then create a program Tkinter window
# program = Tk()   
# # Photoimage class is created
# # And Image should be in the same folder where there is script saved 
# p1 = PhotoImage(file = 'logo-icon.png')   
# # Icon set for program window
# program.iconphoto(False, p1)   
# # Button creation
# b = Button(program, text = 'Press Me!') 
# b.pack(side = TOP) 
# program.title('iconphoto() method')
# mainloop()



# # importing only those functions
# # which are needed
# from tkinter import *
# from tkinter.ttk import *

# # creating tkinter window
# root = Tk()

# # Adding widgets to the root window
# Label(root, text = 'GeeksforGeeks', font =(
# 'Verdana', 15)).pack(side = TOP, pady = 10)

# # Creating a photoimage object to use image
# photo = PhotoImage(file = r"cogwheel.png")

# # Resizing image to fit on button
# photoimage = photo.subsample(3, 3)

# # here, image option is used to
# # set image on button
# # compound option is used to align
# # image on LEFT side of button
# Button(root, text = 'Click Me !', image = photoimage,
# 					compound = LEFT).pack(side = TOP)

# mainloop()




#Define the working of the button
#Import all the necessary libraries
# from tkinter import *

# #Define the tkinter instance
# win= Toplevel()
# win.title("Rounded Button")

# #Define the size of the tkinter frame
# win.geometry("700x300")

# #Define the working of the button

# def my_command():
#    text.config(text= "You have clicked Me...")

# #Import the image using PhotoImage function
# click_btn= PhotoImage(file='cogwheel.png')

# #Let us create a label for button event
# img_label= Label(image=click_btn)

# #Let us create a dummy button and pass the image
# button= Button(win, image=click_btn,command= my_command,
# borderwidth=0)
# button.pack(pady=30)

# text= Label(win, text= "")
# text.pack(pady=30)


# win.mainloop()




# Importing Tkinter module
# from tkinter import *
# from tkinter.ttk import *

# # Creating master Tkinter window
# master = Tk()

# # Creating object of photoimage class
# # Image should be in the same folder
# # in which script is saved
# p1 = PhotoImage(file = 'cogwheel.png')

# # Setting icon of master window
# master.iconphoto(False, p1)

# # Creating button
# b = Button(master, text = 'Click me !')
# b.pack(side = TOP)

# # Infinite loop can be terminated by
# # keyboard or mouse interrupt
# # or by any predefined function (destroy())
# mainloop()



# import tkinter as tk
# my_w=tk.Tk()
# from PIL import Image,ImageTk
# my_w.geometry('300x100')
# my_w.title('www.plus2net.com')
# my_img = ImageTk.PhotoImage(Image.open("logo-icon.png"))
# b1=tk.Button(my_w,image=my_img)
# b1.grid(row=1,column=1)
# my_w.mainloop()


# import tkinter  as tk 
# from tkinter import ttk
# from PIL import Image,ImageTk
# my_w = tk.Tk()
# my_w.geometry("840x570")  
# #my_img = tk.PhotoImage(file = "D:\\top2.png") 
# my_img2 = ImageTk.PhotoImage(Image.open("logo-icon.png"))

# bg = tk.Label(my_w, image=my_img2)
# bg.place(x=0, y=0, relwidth=1, relheight=1)


        

# my_w.mainloop()