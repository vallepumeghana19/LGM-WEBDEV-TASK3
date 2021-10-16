from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class register_ui:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')

        ### Required Variables##
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6 = StringVar()
        self.var7 = StringVar()
        self.var8 = StringVar()
        self.var9 = IntVar()
        
        ### Background Image##
        self.bg_img = ImageTk.PhotoImage(file='Images/b2.jpg')
        bg_label = Label(self.root,image=self.bg_img)
        bg_label.place(x=250,y=0,relwidth=1,relheight=1)

        ###Side Image##
        self.side_img = ImageTk.PhotoImage(file='Images/side.png')
        side_label = Label(self.root,image=self.side_img)
        side_label.place(x=80,y=100,width=400,height=500)

        ###CONTENT SECTION##
        ### Registeration Frame##
        frame1 = Frame(self.root,bg='white')
        frame1.place(x=480,y=100,width=700,height=500)

        title = Label(frame1,text='REGISTER HERE',font=('Times New Roman',20,'bold'),bg='white',fg='green')
        title.place(x=50,y=30)

        ###  Labels## 
        label1 = Label(frame1,text='First Name',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label1.place(x=50,y=100)
        label2 = Label(frame1,text='Last Name',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label2.place(x=370,y=100)
        label3 = Label(frame1,text='Contact No.',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label3.place(x=50,y=170)
        label4 = Label(frame1,text='Email.',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label4.place(x=370,y=170)
        label5 = Label(frame1,text='Security Question',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label5.place(x=50,y=240)
        label6 = Label(frame1,text='Answer',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label6.place(x=370,y=240)
        label7 = Label(frame1,text='Password',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label7.place(x=50,y=310)
        label8 = Label(frame1,text='Confirm Password',font=('Times New Roman',15,'bold'),bg='white',fg='grey')
        label8.place(x=370,y=310)





        ###  Entries##
        self.entry1 = Entry(frame1,textvariable=self.var1,font=("times new roman",15),bg='lightgray')
        self.entry1.place(x=50,y=130,width=250)
        self.entry2 = Entry(frame1,textvariable=self.var2,font=("times new roman",15),bg='lightgray')
        self.entry2.place(x=370,y=130,width=250)
        self.entry3 = Entry(frame1,textvariable=self.var3,font=("times new roman",15),bg='lightgray')
        self.entry3.place(x=50,y=200,width=250)
        self.entry4 = Entry(frame1,textvariable=self.var4,font=("times new roman",15),bg='lightgray')
        self.entry4.place(x=370,y=200,width=250)
        self.entry5 = ttk.Combobox(frame1,textvariable=self.var5,font=("times new roman",13),justify=CENTER,values=("Your First Pet Name","Your Birth Place","Your Best Friend Name"),state='readonly')
        self.entry5.set("Select")
        self.entry5.place(x=50,y=270,width=250)
        self.entry6 = Entry(frame1,textvariable=self.var6,font=("times new roman",15),bg='lightgray')
        self.entry6.place(x=370,y=270,width=250)
        self.entry7 = Entry(frame1,textvariable=self.var7,font=("times new roman",15),bg='lightgray')
        self.entry7.place(x=50,y=340,width=250)
        self.entry8 = Entry(frame1,textvariable=self.var8,font=("times new roman",15),bg='lightgray')
        self.entry8.place(x=370,y=340,width=250)

        ### Terms##
        self.chk = Checkbutton(frame1,variable=self.var9,text="I Agree the Terms and Conditions",onvalue=1,offvalue=0,bg='white',font=("times new roman",12))
        self.chk.place(x=50,y=380)

        ### Submission#
        self.btn_image = ImageTk.PhotoImage(file='Images/register.png')
        button1 = Button(frame1,image=self.btn_image,bd=0,cursor='hand2',command=self.Register)
        button1.place(x=50,y=420)
        button2 = Button(self.root,text='Sign In',command=self.LogInWindow,font=("Times New Roman",20),bd=0,cursor='hand2')
        button2.place(x=200,y=460,width=180)

    ### METHODS FOR FUNCTIONALITY##
    def Register(self):
        if self.var1.get()=='' or self.var3.get()=='' or self.var4.get()=='' or self.var5.get()=='Select' or self.var6.get()=='' or self.var7.get()=='' or self.var8.get()=='':
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var7.get()!=self.var8.get():
            messagebox.showerror("Error","Password and Confirm Password shoud be same",parent=self.root)
        elif self.var9.get()==0:
            messagebox.showerror("Error","Please Agree our terms and conditions",parent=self.root)
        else:
            try:

                obj1 = sqlite3.connect("Database.db")
                obj  = obj1.cursor()
            except:
                messagebox.showerror("Error","Error in processing",parent=self.root)
            try:
                obj.execute("SELECT * FROM Register WHERE Email=?",(self.var4.get(),))
                data = obj.fetchone()
                if data!=None:
                    messagebox.showerror("Error","User with this Email already Exists",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Register WHERE Contact=?",(self.var3.get(),))
                    data = obj.fetchone()
                    if data!=None:
                        messagebox.showerror("Error","User with this Contact No. already Exists",parent=self.root)
                    else:
                        obj.execute("INSERT INTO Register(FName,LName,Email,Contact,Ques,Ans,Pwd) values(?,?,?,?,?,?,?)",(self.var1.get(),self.var2.get(),self.var4.get(),self.var3.get(),self.var5.get(),self.var6.get(),self.var7.get()))
                        obj1.commit()
                        messagebox.showinfo("Message","Registeration Successful")
                        self.Clear()
                        
            except:
                messagebox.showerror("Error","Unable to register",parent=self.root)

    def Clear(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("Select")
        self.var6.set("")
        self.var7.set("")
        self.var8.set("")

    def LogInWindow(self):
        self.root.destroy()
        os.system("python LogIn.py")
            


obj1=Tk()
obj2 = register_ui(obj1)
obj1.mainloop()
