from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter.font import Font
from PIL import Image,ImageTk
# setting root window:

class MainFrame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.titlefont = Font(family = "Verdana",size=12,weight="bold",slant ="roman")
        container=tk.Frame(bg="#243e55")
        container.place(x=0,y=0,width=1355,height=160)
        # container.grid(row=0,column=1,sticky="nesw")
        
        self.id=tk.StringVar()
        # self.id.set("Mister Smith")
        
        self.listing = {}
        
        for p in (WelcomePage, PageOne):
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky = "nsew")
            self.listing[page_name]=frame
        
        self.up_frame('WelcomePage')
    
    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()
    
    F2 = LabelFrame(container, font=('times new roman', 15, 'bold'), bd=0, fg="Black", bg="#243e55")
    F2.place(x=100, y=0, width=500, height=1100)
    load = Image.open("logo-icon.png")
    render = ImageTk.PhotoImage(load)
    img = Label(F2,image=render,bg="#243e55")
    img.image = render
    img.place(x=0,y=0)   

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        
        
        
        label = tk.Label(self,text="" + controller.id.get(), font=controller.titlefont,bg="#243e55")
        label.pack()
        
        bou = tk.Button(self,text = "Next",command=lambda: controller.up_frame("PageOne"),bg="#243e55")
        bou.pack()
        
        
        
        
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        
        label = tk.Label(self,text="" + controller.id.get(), font=controller.titlefont,bg="#243e55")
        label.pack()
        
        bou = tk.Button(self,text = "back to main",command=lambda: controller.up_frame("WelcomePage"),bg="#243e55")
        bou.pack()
    
    
        
            
if __name__ == '__main__':
    app = MainFrame()
    width=app.winfo_screenwidth()
    height=app.winfo_screenheight()
    app.geometry("%dx%d" %(width,height))
    app.configure(bg="#2f516f")
    app.mainloop()
        
    
        
                
    
    
# root = Tk()
# root.title('FinsYs')
# width=root.winfo_screenwidth()
# height=root.winfo_screenheight()
# root.geometry("%dx%d" %(width,height))
# root.configure(bg="#2f516f")

# label1 = Label(root,bg="#fff")
# label1.place(x=0,y=0,width="1355", height="200")




# root.mainloop()