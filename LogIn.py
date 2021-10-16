from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from tkinter import messagebox,ttk
import sqlite3
import os

class login_ui:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='#021e2f')

        ###Required Variables##
        self.var1 = StringVar()
        self.var2 = StringVar()

        #### BACKGROUND SECTION##
        ### Background Colors##
        self.label_left = Label(self.root,bg='#08a3D2')
        self.label_left.place(x=0,y=0,width=600,relheight=1)
        self.label_right = Label(self.root,bg='#031f3c')
        self.label_right.place(x=600,y=0,relwidth=1,relheight=1)
        ###Frames##
        frame1 = Frame(self.root,bg='white')
        frame1.place(x=250,y=100,width=800,height=500)
        title = Label(frame1,text='LOGIN HERE',font=("times new roman",30,"bold"),bg='white',fg='#08A3D2')
        title.place(x=250,y=50)
        ###Labels###
        label1 = Label(frame1,text='EMAIL ADDRESS',font=("times new roman",18,"bold"),bg='white',fg='gray')
        label1.place(x=250,y=150)
        label2 = Label(frame1,text='PASSWORD',font=("times new roman",18,"bold"),bg='white',fg='gray')
        label2.place(x=250,y=250)


        ###Entries###
        self.entry1 = Entry(frame1,textvariable=self.var1,font=("times new roman",15),bg='lightgray')
        self.entry1.place(x=250,y=180,width=350,height=35)
        self.entry2 = Entry(frame1,textvariable=self.var2,font=("times new roman",15),bg='lightgray')
        self.entry2.place(x=250,y=280,width=350,height=35)

        ###Button##
        button1 = Button(frame1,cursor='hand2',command=self.RegisterWindow,text='Register New Account?',font=("times new roman",14),bg="white",bd=0,fg='#B00857')
        button1.place(x=250,y=320)
        button2 = Button(frame1,cursor='hand2',command=self.Login,text='Login',font=("times new roman",20,"bold"),fg="white",bg='#B00857')
        button2.place(x=250,y=380,width=150,height=40)
        button3 = Button(frame1,cursor='hand2',command=self.ForgetPwd,text='Forget Password?',font=("times new roman",14,),fg='red',bg='white',bd=0)
        button3.place(x=465,y=320)

        ### CLOCK SECTION##
        self.label3 = Label(self.root,text="\nAnalog Clock",compound=BOTTOM,fg='white',font=("Book Antiqua",25,'bold'),bg='#081923')
        self.label3.place(x=90,y=120,width=350,height=450)
        self.Working()

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


    def Working(self):
        h  = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        
        hr = (h/12)*360
        min = (m/60)*360
        sec = (s/60)*360
        
        self.clock_image(hr,min,sec)
        self.img=ImageTk.PhotoImage(file="Images/clock_new.png")
        self.label3.config(image=self.img)
        self.label3.after(200,self.Working)

    ### METHODS FOR FUNCTIONALITY##
    def Login(self):
        if self.var1.get()=='' or self.var2.get()=='':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                obj1 = sqlite3.connect("Database.db")
                obj = obj1.cursor()
                try:
                    obj.execute("SELECT * FROM Register WHERE Email=?",(self.var1.get(),))
                    data = obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","Email Id does not exist",parent=self.root)
                    else:
                        obj.execute("SELECT * FROM Register WHERE Email=? and Pwd=?",(self.var1.get(),self.var2.get()))
                        data = obj.fetchone()
                        if data!=None:
                            messagebox.showinfo("Success","Welcome",parent=self.root)
                            self.DashboardWindow()
                        else:
                             messagebox.showerror("Error","Incorrect Password",parent=self.root)
                except:
                    messagebox.showerror("Error","Error while fetching details",parent=self.root)

            except:
                messagebox.showerror("Error","Error while processing",parent=self.root)


    def RegisterWindow(self):
        self.root.destroy()
        os.system("python Register.py")

    def DashboardWindow(self):
        self.root.destroy()
        os.system("python Dashboard.py")

    def ForgetPwd(self):
        if self.var1.get()=='':
            messagebox.showerror("Error","Please enter the  email to reset password",parent=self.root)
        else:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                obj.execute("SELECT * FROM Register WHERE  Email=?",(self.var1.get(),))
                data = obj.fetchone()
                if data==None:
                    messagebox.showerror("Error","Please enter the valid email to reset password",parent=self.root)
                else:

                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+450+150")
                    self.root2.grab_set()
                    self.root2.config(bg='white')
                    self.title2 = Label(self.root2,text='Forget password',font=('times new roman',20,"bold"),bg='white',fg='red')
                    self.title2.place(x=0,y=10,relwidth=1)
                    self.var5 = StringVar()
                    self.var6 = StringVar()
                    self.var7 = StringVar()

                    ###Labels###
                    label5 = Label(self.root2,text='Security Question',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
                    label5.place(x=50,y=100)
                    label6 = Label(self.root2,text='Answer',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
                    label6.place(x=50,y=180)
                    label7 = Label(self.root2,text='New Password',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
                    label7.place(x=50,y=260)


                    ###Entries###
                    self.entry5 = ttk.Combobox(self.root2,textvariable=self.var5,font=("times new roman",13),justify=CENTER,values=("Your First Pet Name","Your Birth Place","Your Best Friend Name"),state='readonly')
                    self.entry5.set("Select")
                    self.entry5.place(x=50,y=130,width=250)
                    self.entry6 = Entry(self.root2,textvariable=self.var6,font=("times new roman",15),bg='lightgray')
                    self.entry6.place(x=50,y=210,width=250)
                    self.entry7 = Entry(self.root2,textvariable=self.var7,font=("times new roman",15),bg='lightgray')
                    self.entry7.place(x=50,y=290,width=250)

                    ##button##
                    button_pwd = Button(self.root2,text='Reset Password',command=self.NewPwd,bg='green',fg='white',font=("times new roman",15,"bold"))
                    button_pwd.place(x=80,y=340)
                    
            except:
                messagebox.showerror("Error","Error while procesing",parent=self.root)


    def NewPwd(self):
        obj1 = sqlite3.connect("Database.db")
        obj = obj1.cursor()
        try:
            if self.var5.get()=="Select":
                messagebox.showerror("Error","Please select a security question",parent=self.root)
            elif self.var6.get()=="":
                messagebox.showerror("Error","Please enter the answer for security question",parent=self.root)
            elif self.var7.get()=='':
                messagebox.showerror("Error","Please enter the new password to update",parent=self.root)
            else:
                obj.execute("SELECT * FROM Register WHERE Ques=? and Email=?",(self.var5.get(),self.var1.get()))
                data = obj.fetchone()
                if data==None:
                    messagebox.showerror("Error","Incorrect Security Question",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Register WHERE Ans=? and Email=?",(self.var6.get(),self.var1.get()))
                    data = obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","Incorrect Answer for Security Question",parent=self.root)
                    else:
                        obj.execute("UPDATE Register SET Pwd=? WHERE Email=?",(self.var7.get(),self.var1.get()))
                        obj1.commit()
                        messagebox.showinfo("Success","Password Updated Successfully")
                        self.Reset()
                        self.root2.destroy()

        except:
            messagebox.showerror("Error","Error while processing",parent=self.root)

    def Reset(self):
        self.var1.set("")
        self.var2.set("")
        self.var5.set("Select")
        self.var6.set("")
        self.var7.set("")



obj = Tk()
obj2 = login_ui(obj)
obj.mainloop()
