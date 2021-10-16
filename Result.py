from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class result_ui:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg='white')

        ###REQUIRED VARIABLES##
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.list = []
        self.FetchRoll()

         ### TITLE BAR##
        title = Label(self.root,text="Add Student Result", font=("goudy old style",20,"bold"),bg='orange',fg='#262626')
        title.place(x=10,y=15,width=1180,height=50)

        ### CONTENT SECTION##
        ### Labels##
        label1 = Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg='white')
        label1.place(x=50,y=100)
        label2 = Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg='white')
        label2.place(x=50,y=160)
        label3 = Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg='white')
        label3.place(x=50,y=220)
        label4 = Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg='white')
        label4.place(x=50,y=280)
        label5 = Label(self.root,text="Total Marks",font=("goudy old style",20,"bold"),bg='white')
        label5.place(x=50,y=340)

        ### Entries##
        self.entry1 = ttk.Combobox(self.root,textvariable=self.var1,values=self.list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.entry1.place(x=280,y=100,width=200)
        self.entry1.set("Select")
        self.search_btn = Button(self.root,text="Search",font=("goudy old style",15,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search)
        self.search_btn.place(x=500,y=100,width=100,height=28)

        self.entry2 = Entry(self.root,textvariable=self.var2,state='readonly', font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry2.place(x=280,y=160,width=320)
        self.entry3 = Entry(self.root,textvariable=self.var3,state='readonly', font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry3.place(x=280,y=220,width=320) 
        self.entry4 = Entry(self.root,textvariable=self.var4, font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry4.place(x=280,y=280,width=320)
        self.entry5 = Entry(self.root,textvariable=self.var5, font=("goudy old style",20,"bold"),bg='#FFFCC2')
        self.entry5.place(x=280,y=340,width=320)


        ### Background-Image##
        self.bg_img = Image.open('Images/result.jpg')
        self.bg_img = self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        bg_label = Label(self.root,image=self.bg_img).place(x=650,y=100)

        ### Buttons##
        self.button1 = Button(self.root,text="Submit",font=("Times New Roman",15),bg='lightgreen',activebackground='lightgreen',cursor='hand2',command=self.Submit)
        self.button1.place(x=300,y=420,width=120,height=35)
        self.button1 = Button(self.root,command=self.Clear,text="Clear",font=("Times New Roman",15),bg='lightgray',activebackground='white',cursor='hand2')
        self.button1.place(x=430,y=420,width=120,height=35)

    ### METHODS FOR HANDLING EVENTS##
    ### Function to fetch roll number data from student table
    def FetchRoll(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                obj.execute("SELECT Roll FROM Student")
                items = obj.fetchall()
                if len(items)>0:
                    for data in items:
                        self.list.append(data)
            except:
                messagebox.showerror("Error","Error while fetching the details",parent=self.root)

        except:
            messagebox.showerror("Error","Error while processing",parent=self.root)                      


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


    ### Function for handling events of Submit button
    def  Submit(self):
        try:
            obj1 = sqlite3.connect("Database.db")
            obj = obj1.cursor()
            try:
                if self.var2.get() == '':
                    messagebox.showerror("Error","Please First Search Student Record",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Result WHERE Name=? AND Course=?",(self.var2.get(),self.var3.get()))
                    data =obj.fetchone()
                    if data!=None:
                        messagebox.showerror("Error","Result already exists",parent=self.root)
                    else:
                        per = (int(self.var4.get())*100)/(int(self.var5.get()))
                        obj.execute("INSERT INTO Result(Roll,Name,Course,Marks_ob,Full_marks,percentage) values(?,?,?,?,?,?)",(self.var1.get(),self.var2.get(),self.var3.get(),self.var4.get(),self.var5.get(),str(per)))
                        obj1.commit()
                        messagebox.showinfo("Success","Result Added successfully",parent=self.root)
                        
            except:
                messagebox.showerror("Error","An Error occurred while adding details",parent=self.root)
        except:
                messagebox.showerror("Error","An Error occurred while processing",parent=self.root)
        
    ### Function for handling event of clear button
    def Clear(self):
        self.var1.set("Select")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("")
        

if __name__=="__main__" :

    obj1 = Tk()
    obj2 = result_ui(obj1)
    obj1.mainloop()
