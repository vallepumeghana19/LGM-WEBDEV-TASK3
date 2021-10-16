from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class course_ui:
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

        ### TITLE BAR##
        title = Label(self.root,text="Manage Course Details", font=("goudy old style",20,"bold"),bg='#033054',fg='white')
        title.place(x=10,y=15,width=1180,height=35)

        ### CONTENT SECTION ##
        ### Widgets##
        label1 = Label(self.root,text="Course Name", font=("goudy old style",15,"bold"),bg='white')
        label1.place(x=10,y=70)
        label2 = Label(self.root,text="Duration", font=("goudy old style",15,"bold"),bg='white')
        label2.place(x=10,y=110) 
        label3 = Label(self.root,text="Charges", font=("goudy old style",15,"bold"),bg='white')
        label3.place(x=10,y=150)
        label4 = Label(self.root,text="Description", font=("goudy old style",15,"bold"),bg='white')
        label4.place(x=10,y=190)
        ### Entries##
        self.entry1 = Entry(self.root,textvariable=self.var1, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry1.place(x=150,y=70,width=200)
        self.entry2 = Entry(self.root,textvariable=self.var2, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry2.place(x=150,y=110,width=200) 
        self.entry3 = Entry(self.root,textvariable=self.var3, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry3.place(x=150,y=150,width=200)
        self.entry4 = Text(self.root, font=("goudy old style",15,"bold"),bg='#FFFCC2')
        self.entry4.place(x=150,y=190,width=462,height=100)
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
        self.search_label = Label(self.root,text="Course Name",font=('goudy old style',15,"bold"),bg='white')
        self.search_label.place(x=720,y=70)
        self.search_entry = Entry(self.root,textvariable=self.var4,font=("goudy old style",15,'bold'),bg='#FFFCC2')
        self.search_entry.place(x=870,y=70,width=180)
        self.search_btn = Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search)
        self.search_btn.place(x=1070,y=70,width=120,height=28)
        ### Course Details Display Section##
        self.frame2 = Frame(self.root,bd=2,relief=RIDGE)
        self.frame2.place(x=720,y=110,width=470,height=340)
        scrollY = Scrollbar(self.frame2,orient=VERTICAL)
        scrollX = Scrollbar(self.frame2,orient=HORIZONTAL)
        
        self.course_info = ttk.Treeview(self.frame2,columns=('cid','name','duration','charges','description'),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        
        scrollY.pack(side=RIGHT,fill=Y)    ##setting scrolls
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.config(command=self.course_info.yview)
        scrollX.config(command=self.course_info.xview)

        self.course_info.heading('cid',text='Course Id')  ##setting column heading text
        self.course_info.heading('name',text='Name')
        self.course_info.heading('duration',text='Duration')
        self.course_info.heading('charges',text='Charges')
        self.course_info.heading('description',text='Description')
        self.course_info["show"] ='headings'
        self.course_info.column('cid',width=70)  ##setting each column width
        self.course_info.column('name',width=100)
        self.course_info.column('duration',width=100)
        self.course_info.column('charges',width=100)
        self.course_info.column('description',width=150)
        self.course_info.pack(fill=BOTH,expand=1)
        self.course_info.bind("<ButtonRelease-1>",self.GetData)
        self.Display()
    
    ### METHOD T0 ADD A NEW COURSE
    def  Save(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var1.get() == '':
                    messagebox.showerror("Error","Please Enter Course Name",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Course WHERE Name=?",(self.var1.get(),))
                    data =obj.fetchone()
                    if data!=None:
                        messagebox.showerror("Error","Course Name already exists",parent=self.root)
                    else:
                        obj.execute("INSERT INTO Course(Name,Duration,Charges,Description) values(?,?,?,?)",(self.var1.get(),self.var2.get(),self.var3.get(),self.entry4.get("1.0",END)))
                        obj1.commit()
                        messagebox.showinfo("Success","Course Added successfully",parent=self.root)
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
                self.course_info.delete(*self.course_info.get_children())
                obj.execute("SELECT * FROM Course")
                items = obj.fetchall()
                for data in items:
                    self.course_info.insert("",END,values=data)
            except:
                messagebox.showerror("Error","An Error occured while displaying details",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)
    

    def GetData(self,eve):
        self.entry1.config(state='readonly')
        obj = self.course_info.focus()  ##for row which gets focusssed/clicked by user
        data = self.course_info.item(obj)
        row = data['values'] ##Retrieving the data collected from focussed row
        ### Setting the selelected values over the entry labels
        self.var1.set(row[1])
        self.var2.set(row[2]) 
        self.var3.set(row[3]) 
        self.entry4.delete("1.0",END)
        self.entry4.insert(END,row[4])

    ### METHOD TO UPDATE DETAILS OF ANY COURSE##
    def  Modify(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var1.get() == '':
                    messagebox.showerror("Error","Please Enter Course Name",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Course WHERE Name=?",(self.var1.get(),))
                    data =obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","Select Course from list",parent=self.root)
                    else:
                        obj.execute("UPDATE Course SET Duration=?,Charges=?,Description=? WHERE Name=?",(self.var2.get(),self.var3.get(),self.entry4.get("1.0",END),self.var1.get()))
                        obj1.commit()
                        messagebox.showinfo("Success","Course Details Updated Successfully",parent=self.root)
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
        self.var4.set("")
        self.entry4.delete("1.0",END)
        self.entry1.config(state=NORMAL)
        self.Display()

    ###METHOD TO REMOVE DATA OF A COURSE
    def Erase(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var1.get()=='':
                    messagebox.showerror("Error","Please Enter Course Name",parent=self.root)
                else:
                    obj.execute("SELECT * FROM  Course WHERE Name=?",(self.var1.get(),))
                    data = obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","Please select a course from list to delete",parent=self.root)
                    else:
                        ans=messagebox.askyesno("Confirm","Do you really want to delete this course detail?",parent=self.root)
                        if ans==True:
                            obj.execute("DELETE FROM Course WHERE Name=?",(self.var1.get(),))
                            obj1.commit()
                            messagebox.showinfo("Success","Course Deleted Successfully",parent=self.root)
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
                self.course_info.delete(*self.course_info.get_children())
                obj.execute(F"SELECT * FROM Course WHERE Name LIKE '%{self.var4.get()}%'")
                items = obj.fetchall()
                for data in items:
                    self.course_info.insert("",END,values=data)
            except:
                messagebox.showerror("Error","An Error occured while displaying details",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)    
                            


if __name__=="__main__" :

    obj1 = Tk()
    obj2 = course_ui(obj1)
    obj1.mainloop()
