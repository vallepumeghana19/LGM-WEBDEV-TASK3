from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class student_ui:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')

        ### REQUIRED VARIABLES##
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6 = StringVar()
        self.var7 = StringVar()
        self.var8 = StringVar()
        self.var9 = StringVar()
        self.var10 = StringVar()
        self.var11 = StringVar()
        self.var12 = StringVar()

        ### TITLE BAR##
        title = Label(self.root,text="Manage Student Details", font=("goudy old style",20,"bold"),bg='#033054',fg='white')
        title.place(x=10,y=15,width=1180,height=35)

        ### CONTENT SECTION ##
        ### Widgets##
        ### Column1##
        label1 = Label(self.root,text="Roll No.", font=("goudy old style",15,"bold"),bg='white')
        label1.place(x=10,y=70)
        label2 = Label(self.root,text="Name", font=("goudy old style",15,"bold"),bg='white')
        label2.place(x=10,y=110) 
        label3 = Label(self.root,text="Email", font=("goudy old style",15,"bold"),bg='white')
        label3.place(x=10,y=150)
        label4 = Label(self.root,text="Gender", font=("goudy old style",15,"bold"),bg='white')
        label4.place(x=10,y=190)
        label5 = Label(self.root,text="State", font=("goudy old style",15,"bold"),bg='white')
        label5.place(x=10,y=230)
        label6 = Label(self.root,text="Address", font=("goudy old style",15,"bold"),bg='white')
        label6.place(x=10,y=270)
        ###Column2##
        label7 = Label(self.root,text="D.O.B(dd-mm-yyyy)", font=("goudy old style",15,"bold"),bg='white')
        label7.place(x=350,y=70)
        label8 = Label(self.root,text="Contact No.", font=("goudy old style",15,"bold"),bg='white')
        label8.place(x=350,y=110) 
        label9 = Label(self.root,text="Admission Date", font=("goudy old style",15,"bold"),bg='white')
        label9.place(x=350,y=150)
        label10 = Label(self.root,text="Select Course", font=("goudy old style",15,"bold"),bg='white')
        label10.place(x=350,y=190)
        label11 = Label(self.root,text="City", font=("goudy old style",15,"bold"),bg='white')
        label11.place(x=290,y=230)
        label12 = Label(self.root,text="Pin Code", font=("goudy old style",15,"bold"),bg='white')
        label12.place(x=510,y=230)




        ### Entries##
        self.list=[]
        self.fetch_course()
        ### Column1##
        self.entry1 = Entry(self.root,textvariable=self.var1, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry1.place(x=120,y=70,width=200)
        self.entry2 = Entry(self.root,textvariable=self.var2, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry2.place(x=120,y=110,width=200) 
        self.entry3 = Entry(self.root,textvariable=self.var3, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry3.place(x=120,y=150,width=200)
        self.entry4 = ttk.Combobox(self.root,textvariable=self.var4,values=("Male","Female","Others"),font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.entry4.place(x=120,y=190,width=200)
        self.entry4.set("Select")
        self.entry5 = Entry(self.root,textvariable=self.var5, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry5.place(x=120,y=230,width=150)
        self.entry6 = Text(self.root, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry6.place(x=120,y=270,width=590,height=100)
        ### Column2#
        self.entry7 = Entry(self.root,textvariable=self.var6, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry7.place(x=530,y=70,width=180)
        self.entry8 = Entry(self.root,textvariable=self.var7, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry8.place(x=530,y=110,width=180) 
        self.entry9 = Entry(self.root,textvariable=self.var8, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry9.place(x=530,y=150,width=180)
        self.entry10 = ttk.Combobox(self.root,textvariable=self.var9,values=self.list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.entry10.place(x=530,y=190,width=180)
        self.entry10.set("Select")
        self.entry11 = Entry(self.root,textvariable=self.var10, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry11.place(x=345,y=230,width=150)
        self.entry12 = Entry(self.root,textvariable=self.var11, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry12.place(x=600,y=230,width=110)

        
        ### Buttons##
        self.button1 = Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg='#2196f3',fg='white',command=self.Save)
        self.button1.place(x=150,y=400,width=110,height=40)
        self.button2 = Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg='#4caf50',fg='white',command=self.Modify)
        self.button2.place(x=270,y=400,width=110,height=40)
        self.button3 = Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg='#f44336',fg='white',command=self.Erase)
        self.button3.place(x=390,y=400,width=110,height=40)
        self.button4 = Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg='#607d8b',fg='white',command=self.Remove)
        self.button4.place(x=510,y=400,width=110,height=40)
        ### Search Panel##
        self.search_label = Label(self.root,text="Search | Roll No.",font=('goudy old style',15,"bold"),bg='white')
        self.search_label.place(x=730,y=70)
        self.search_entry = Entry(self.root,textvariable=self.var12,font=("goudy old style",15,'bold'),bg='#FFFCC2')
        self.search_entry.place(x=890,y=70,width=180)
        self.search_btn = Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search)
        self.search_btn.place(x=1085,y=68,width=105,height=28)
        ### Course Details Display Section##
        self.frame2 = Frame(self.root,bd=2,relief=RIDGE)
        self.frame2.place(x=730,y=110,width=650,height=340)
        scrollY = Scrollbar(self.frame2,orient=VERTICAL)
        scrollX = Scrollbar(self.frame2,orient=HORIZONTAL)
        
        self.student_info = ttk.Treeview(self.frame2,columns=('roll','name','email','gender','dob','contact','admission','course','state','city','pin','address'),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        
        scrollY.pack(side=RIGHT,fill=Y)    ##setting scrolls
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.config(command=self.student_info.yview)
        scrollX.config(command=self.student_info.xview)

        self.student_info.heading('roll',text='Roll No.')  ##setting column heading text
        self.student_info.heading('name',text='Name')
        self.student_info.heading('email',text='Email')
        self.student_info.heading('gender',text='Gender')
        self.student_info.heading('dob',text='D.O.B')
        self.student_info.heading('contact',text='Contact No.')
        self.student_info.heading('admission',text='Admission Date')
        self.student_info.heading('course',text='Course Name')
        self.student_info.heading('state',text='State')
        self.student_info.heading('city',text='City')
        self.student_info.heading('pin',text='Pin Code')
        self.student_info.heading('address',text='Address')
        self.student_info["show"] ='headings'
        self.student_info.column('roll',width=100)  ##setting each column width
        self.student_info.column('name',width=150)
        self.student_info.column('email',width=180)
        self.student_info.column('gender',width=70)
        self.student_info.column('dob',width=150)
        self.student_info.column('contact',width=150)
        self.student_info.column('admission',width=150)
        self.student_info.column('course',width=100)
        self.student_info.column('state',width=100)
        self.student_info.column('city',width=100)
        self.student_info.column('pin',width=130)
        self.student_info.column('address',width=300)
        self.student_info.pack(fill=BOTH,expand=1)
        self.student_info.bind("<ButtonRelease-1>",self.GetData)
        self.Display()
    
    ### METHOD T0 ADD NEW STUDENT DETAILS
    def  Save(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var1.get() == '':
                    messagebox.showerror("Error","Please Enter Roll Number",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Student WHERE Roll=?",(self.var1.get(),))
                    data =obj.fetchone()
                    if data!=None:
                        messagebox.showerror("Error","Roll Number already present",parent=self.root)
                    else:
                        obj.execute("INSERT INTO Student(Roll,Name,Email,Gender,DOB,Contact,Admission,Course,State,City,Pin,Address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(self.var1.get(),self.var2.get(),self.var3.get(),self.var4.get(),self.var6.get(),self.var7.get(),self.var8.get(),self.var9.get(),self.var5.get(),self.var10.get(),self.var11.get(),self.entry6.get("1.0",END)))
                        obj1.commit()
                        messagebox.showinfo("Success","Student Details Added successfully",parent=self.root)
                        self.Display()
            except:
                messagebox.showerror("Error","An Error occurred while adding details",parent=self.root)
        except:
                messagebox.showerror("Error","An Error occurred while processing",parent=self.root)

    ### METHOD TO DISPLAY DATA IN DISPLAY PANEL##
    def Display(self):
        try:
            obj1 = sqlite3.connect("Database.db") 
            obj = obj1.cursor()
            try:
                self.student_info.delete(*self.student_info.get_children())
                obj.execute("SELECT * FROM Student")
                items = obj.fetchall()
                for data in items:
                    self.student_info.insert("",END,values=data)
            except:
                messagebox.showerror("Error","An Error occured while displaying details",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)
    

    def GetData(self,eve):
        self.entry1.config(state='readonly')
        obj = self.student_info.focus()  ##for row which gets focusssed/clicked by user
        data = self.student_info.item(obj)
        row = data['values'] ##Retrieving the data collected from focussed row
        ### Setting the selelected values over the entry labels
        self.var1.set(row[0])
        self.var2.set(row[1]) 
        self.var3.set(row[2])
        self.var4.set(row[3])
        self.var5.set(row[8])
        self.var6.set(row[4])
        self.var7.set(row[5])
        self.var8.set(row[6])
        self.var9.set(row[7])
        self.var10.set(row[9])
        self.var11.set(row[10]) 
        self.entry6.delete("1.0",END)
        self.entry6.insert(END,row[11])

    ### METHOD TO UPDATE STUDENT DETAILS##
    def  Modify(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var1.get() == '':
                    messagebox.showerror("Error","Please Enter Roll Number",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Student WHERE Roll=?",(self.var1.get(),))
                    data =obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","Select Student from list",parent=self.root)
                    else:
                        obj.execute("UPDATE Student SET Name=?,Email=?,Gender=?,DOB=?,Contact=?,Admission=?,Course=?,State=?,City=?,Pin=?,Address=? WHERE Roll=?",(self.var2.get(),self.var3.get(),self.var4.get(),self.var6.get(),self.var7.get(),self.var8.get(),self.var9.get(),self.var5.get(),self.var10.get(),self.var11.get(),self.entry6.get("1.0",END),self.var1.get()))
                        obj1.commit()
                        messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                        self.Display()
            except:
                messagebox.showerror("Error","An Error occurred while updating details",parent=self.root)
        except:
                messagebox.showerror("Error","An Error occurred while processing",parent=self.root)


    ### METHOD TO CLEAR ALL FIELDS##
    def Remove(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("Select")
        self.var6.set("")
        self.var7.set("")
        self.var8.set("")
        self.var9.set("Select")
        self.var5.set("")
        self.var10.set("")
        self.var11.set("")
        self.entry6.delete("1.0",END)
        self.Display()
        self.entry1.config(state=NORMAL)
        self.var12.set("")

    ###METHOD TO REMOVE STUDENT DATA
    def Erase(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var1.get()=='':
                    messagebox.showerror("Error","Please Enter Roll Number",parent=self.root)
                else:
                    obj.execute("SELECT * FROM  Student WHERE Roll=?",(self.var1.get(),))
                    data = obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","Please select student from list to delete",parent=self.root)
                    else:
                        ans=messagebox.askyesno("Confirm","Do you really want to delete this student detail?",parent=self.root)
                        if ans==True:
                            obj.execute("DELETE FROM Student WHERE Roll=?",(self.var1.get(),))
                            obj1.commit()
                            messagebox.showinfo("Success","Student details Deleted Successfully",parent=self.root)
                            self.Display()
                        else:
                            messagebox.showinfo("Message","Operation Cancelled Successfully",parent=self.root)
            except:
                messagebox.showerror("Error","Error while deleting the course",parent=self.root)
        except:
            messagebox.showerror("Error","Error while processing",parent=self.root)

    ### METHOD FOR HANDLING SEARCH OPERATION##
    def Search(self):
        try:
            obj1 = sqlite3.connect("Database.db") 
            obj = obj1.cursor()
            try:
                if self.var12.get()=="":
                    messagebox.showerror("Error","Please Enter Roll Number to search",parent=self.root)
                else:
                    self.student_info.delete(*self.student_info.get_children())
                    obj.execute("SELECT * FROM Student WHERE Roll=?",(self.var12.get(),))
                    data = obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","No record found",parent=self.root)
                    else:
                        self.student_info.delete(*self.student_info.get_children())
                        self.student_info.insert("",END,values=data)
            except:
                messagebox.showerror("Error","An Error occured while displaying details",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)    

    ### FUNCTION TO FETCH COURSE NAMES FROM COURSE TABLE##
    def fetch_course(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                obj.execute("SELECT Name FROM Course")
                items = obj.fetchall()
                if len(items)>0:
                    for data in items:
                        self.list.append(data)
            except:
                messagebox.showerror("Error","Error while fetching the details",parent=self.root)

        except:
            messagebox.showerror("Error","Error while processing",parent=self.root)                      



if __name__=="__main__" :

    obj1 = Tk()
    obj2 = student_ui(obj1)
    obj1.mainloop()
