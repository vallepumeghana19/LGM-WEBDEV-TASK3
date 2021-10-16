from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from Course import course_ui
from Student import student_ui
from Result import result_ui
from View import view_ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tkinter import messagebox
from datetime import *
import time
from math import *
import sqlite3
import os
class ui:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')

        self.logo_img = ImageTk.PhotoImage(file='Images/logo_p.png')
        ### TITLE BAR##
        title = Label(self.root,text="Student Result Management System", image=self.logo_img,compound=LEFT,padx=10,font=("goudy old style",20,"bold"),bg='#033054',fg='white')
        title.place(x=0,y=0,relwidth=1,height=50)

        ### MENU BAR##
        frame1 = LabelFrame(self.root,text="Menus",font=("Times New Roman",15),bg="white")
        frame1.place(x=10,y=70,width=1340,height=80)
        button1 = Button(frame1,text="Course",font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor='hand2',command=self.add_course)
        button1.place(x=20,y=5,width=200,height=40)
        button2 = Button(frame1,text="Student",font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor='hand2',command=self.add_student)
        button2.place(x=240,y=5,width=200,height=40)
        button3 = Button(frame1,text="Result",font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor='hand2',command=self.add_result)
        button3.place(x=460,y=5,width=200,height=40)
        button4 = Button(frame1,text="View Student Results",font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor='hand2',command=self.view_result)
        button4.place(x=680,y=5,width=200,height=40)
        button5 =Button(frame1,text="Log Out",command=self.log_out,font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor='hand2')
        button5.place(x=900,y=5,width=200,height=40)
        button6 = Button(frame1,text="Exit",command=self.exit_,font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor='hand2')
        button6.place(x=1120,y=5,width=200,height=40)

        ### CONTENT WINDOW##
        ### Background Image##
        self.bg_img = Image.open('Images/bg.png')
        self.bg_img = self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        bg_label = Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)
        ### Details##
        self.label1 = Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bg='#e43b06',fg='white',bd=10,relief=RIDGE)
        self.label1.place(x=400,y=530,width=300,height=100)
        self.label2 = Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bg='#0676ad',fg='white',bd=10,relief=RIDGE)
        self.label2.place(x=710,y=530,width=300,height=100)
        self.label3 = Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bg='#038074',fg='white',bd=10,relief=RIDGE)
        self.label3.place(x=1020,y=530,width=300,height=100)

        ### CLOCK SECTION##
        self.label4 = Label(self.root,text="\nAnalog Clock",compound=BOTTOM,fg='white',font=("Book Antiqua",25,'bold'),bg='#081923')
        self.label4.place(x=10,y=170,width=350,height=450)
        self.Working()

    

        ### FOOTER SECTION##
        footer = Label(self.root,text="SRMS - Student Result Management System\n Contact us for any Technical Issue : +91 7814396214",font=('goudy old style',12),bg='#262626',fg='white')
        footer.pack(side=BOTTOM,fill=X)
        self.update_details()


    def Working(self):
        h  = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        
        hr = (h/12)*360
        min = (m/60)*360
        sec = (s/60)*360
        
        self.clock_image(hr,min,sec)
        self.img=ImageTk.PhotoImage(file="Images/clock_new.png")
        self.label4.config(image=self.img)
        self.label4.after(200,self.Working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw = ImageDraw.Draw(clock)
        ### For Clock Image##
        bg = Image.open("Images/c.png")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        ###For Hour Line Image ##
        draw.line((200,200,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='#DF005E',width=4)
        ###For Minute Line Image ##
        draw.line((200,200,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill='white',width=3)
        ###For Second Line Image ##
        draw.line((200,200,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill='yellow',width=2)
        ### Center circle##
        draw.ellipse((195,195,210,210),fill='#1AD5D5')
        clock.save("Images/clock_new.png")

        
       
        


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.obj = course_ui(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.obj = student_ui(self.new_win)
    
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.obj = result_ui(self.new_win)

    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.obj = view_ui(self.new_win)

    def log_out(self):
        op = messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python LogIn.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()

    def update_details(self):
        try:
            obj1 = sqlite3.connect("Database.db") 
            obj = obj1.cursor()
            try:
            
                obj.execute("SELECT * FROM Course")
                items1 = obj.fetchall()
                l1   = str(len(items1))
                self.str1 = "Total Courses\n["+l1+']'
                self.label1.config(text=self.str1)
                

                obj.execute("SELECT * FROM Student")
                items2 = obj.fetchall()
                l2   = str(len(items2))
                self.str2 = "Total Students\n["+l2+']'
                self.label2.config(text=self.str2)
                

                obj.execute("SELECT * FROM Result")
                items3 = obj.fetchall()
                l3   = str(len(items3))
                self.str3 = "Total Results\n["+l3+']'
                self.label3.config(text=self.str3)
                
                self.label1.after(200,self.update_details)
            except:
                messagebox.showerror("Error","An Error occured while displaying details",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)
    
        
            


if __name__=="__main__" :

    obj1 = Tk()
    obj2 = ui(obj1)
    obj1.mainloop()
