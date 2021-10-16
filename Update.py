from tkinter import *
from PIL import Image,ImageTk

from tkinter import ttk,messagebox
import sqlite3
class update_ui:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("700x550+280+210")
        self.root.config(bg='white')

        ### REQUIRED VARIABLES##
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.list = []
        self.FetchRoll()

        title = Label(self.root,text="Update Student Result", font=("goudy old style",20,"bold"),bg='#03a9f4',fg='#262626')
        title.place(x=10,y=15,width=680,height=50)

        ### CONTENT SECTION##
        ### Labels##
        label1 = Label(self.root,text="Enter the details to update:", font=("goudy old style",19,"bold"),bg='white')
        label1.place(x=10,y=80,height=25)
        label2 = Label(self.root,text="Select Student",font=("goudy old style",19,"bold"),bg='white')
        label2.place(x=10,y=140)
        label3 = Label(self.root,text="Name",font=("goudy old style",19,"bold"),bg='white')
        label3.place(x=10,y=200)
        label4 = Label(self.root,text="Course",font=("goudy old style",19,"bold"),bg='white')
        label4.place(x=10,y=260)
        label5 = Label(self.root,text="Marks Obtained",font=("goudy old style",19,"bold"),bg='white')
        label5.place(x=10,y=320)
        label6 = Label(self.root,text="Total Marks",font=("goudy old style",19,"bold"),bg='white')
        label6.place(x=10,y=380)

        ### ENTRIES##
        self.entry1 = ttk.Combobox(self.root,textvariable=self.var1,values=self.list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.entry1.place(x=280,y=140,width=200,height=28)
        self.entry1.set("Select")
        self.search_btn = Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search)
        self.search_btn.place(x=500,y=140,width=100,height=28)

        self.entry2 = Entry(self.root,textvariable=self.var2,state='readonly', font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry2.place(x=280,y=200,width=320)
        self.entry3 = Entry(self.root,textvariable=self.var3,state='readonly', font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry3.place(x=280,y=260,width=320) 
        self.entry4 = Entry(self.root,textvariable=self.var4, font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry4.place(x=280,y=320,width=320)
        self.entry5 = Entry(self.root,textvariable=self.var5, font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry5.place(x=280,y=380,width=320)

        ### Update button##
        self.button1 = Button(self.root,text="Update",font=("goudy old style",15,'bold'),bg='#f44336',fg='white',cursor='hand2',command=self.Update)
        self.button1.place(x=230,y=470,width=200,height=32)


    ### METHODS FOR FUNCTIONALITY##
    ###Function to add functionality to search button##
    def Search(self):
        try:
            obj1 = sqlite3.connect("Database.db") 
            obj = obj1.cursor()
            try:
                
                obj.execute("SELECT Name,Course FROM Student WHERE Roll=?",(self.var1.get(),))
                data = obj.fetchone()
                if data!=None:
                    self.var2.set(data[0])
                    self.var3.set(data[1])
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)
            except:
                messagebox.showerror("Error","An Error occured while searching data",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)    


    ### Function to fetch roll number data from student table
    def FetchRoll(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                obj.execute("SELECT Roll FROM Result")
                items = obj.fetchall()
                if len(items)>0:
                    for data in items:
                        self.list.append(data)
            except:
                messagebox.showerror("Error","Error while fetching the details",parent=self.root)

        except:
            messagebox.showerror("Error","Error while processing",parent=self.root)                      


    ### Method to handle events of update button###
    def Update(self):
        obj1 = sqlite3.connect("Database.db")
        obj = obj1.cursor()
        try:
            if self.var1.get()=='Select':
                messagebox.showerror("Error","Please select Roll Number to update",parent=self.root)
            else:
                obj.execute("UPDATE Result SET Marks_ob=?, Full_Marks=? WHERE Roll=?",(self.var4.get(),self.var5.get(),self.var1.get()))
                obj1.commit()
                messagebox.showinfo("Message","Result details updated successfully",parent=self.root)
            
        except:
            messagebox.showerror("Error","Error in updating details",parent=self.root)
        






if __name__=="__main__" :

    obj1 = Tk()
    obj2 = update_ui(obj1)
    obj1.mainloop()
