from tkinter import *
from PIL import Image,ImageTk
from Update import update_ui
from tkinter import ttk,messagebox
import sqlite3
class view_ui:
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
        self.var_id=''
        self.list = []
        self.FetchData()

        ### TITLE BAR##
        title = Label(self.root,text="View Student Result", font=("goudy old style",20,"bold"),bg='orange',fg='#262626')
        title.place(x=10,y=15,width=1180,height=50)

        ### CONTENT SECTION##
        ### Serach Panel##
        label1 = Label(self.root,text="Search by Roll No.",font=("goudy old style",20,"bold"),bg='white')
        label1.place(x=300,y=102)
        self.entry1 = ttk.Combobox(self.root,textvariable=self.var1,values=self.list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.entry1.place(x=530,y=103,width=250,height=35)
        self.entry1.set("Select")
        self.button1 = Button(self.root,text="Search",command=self.Search,font=("goudy old style",15,'bold'),bg='#03a9f4',fg='white',cursor='hand2')
        self.button1.place(x=800,y=100,width=120,height=35)
        self.button2 = Button(self.root,text="Clear",command=self.Clear,font=("goudy old style",15,'bold'),bg='gray',fg='white',cursor='hand2')
        self.button2.place(x=950,y=100,width=120,height=35)

        ###Display Section##
        label2 = Label(self.root,text="Roll No.",font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        label2.place(x=150,y=230,width=150,height=50)
        label3 = Label(self.root,text="Name",font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        label3.place(x=300,y=230,width=150,height=50)
        label4 = Label(self.root,text="Course",font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        label4.place(x=450,y=230,width=150,height=50)
        label5 = Label(self.root,text="Marks obtained",font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        label5.place(x=600,y=230,width=200,height=50)
        label6 = Label(self.root,text="Total Marks",font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        label6.place(x=800,y=230,width=170,height=50)
        label7 = Label(self.root,text="Percentage",font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        label7.place(x=970,y=230,width=170,height=50)

        self.roll = Label(self.root,font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name = Label(self.root,font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course = Label(self.root,font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks_ob = Label(self.root,font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        self.marks_ob.place(x=600,y=280,width=200,height=50)
        self.full_marks = Label(self.root,font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        self.full_marks.place(x=800,y=280,width=170,height=50)
        self.per = Label(self.root,font=("goudy old style",17,"bold"),bg='white',bd=2,relief=GROOVE)
        self.per.place(x=970,y=280,width=170,height=50)
        self.button3 = Button(self.root,text="Delete",font=("goudy old style",15,'bold'),bg='#f44336',fg='white',cursor='hand2',command=self.Delete)
        self.button3.place(x=450,y=375,width=150,height=35)
        self.button3 = Button(self.root,text="Update",command=self.Update,font=("goudy old style",15,'bold'),bg='#4caf50',fg='white',cursor='hand2')
        self.button3.place(x=650,y=375,width=150,height=35)
    
    ### METHODS FOR FUNCTIONALITY##
    ### Function to handle events of search button##
    def Search(self):
        try:
            obj1 = sqlite3.connect("Database.db") 
            obj = obj1.cursor()
            try:
                if self.var1.get()=="":
                    messagebox.showerror("Error","Please Enter Roll Number to search",parent=self.root)
                else:
                    obj.execute("SELECT * FROM Result WHERE Roll=?",(self.var1.get(),))
                    data = obj.fetchone()
                    if data==None:
                        messagebox.showerror("Error","No record found",parent=self.root)
                    else:
                        self.var_id = data[0]
                        self.roll.config(text=data[1])
                        self.name.config(text=data[2])
                        self.course.config(text=data[3])
                        self.marks_ob.config(text=data[4])
                        self.full_marks.config(text=data[5])
                        self.per.config(text=data[6])

            except:
                messagebox.showerror("Error","An Error occured while displaying details",parent=self.root)       
        except:
            messagebox.showerror("Error","An Error occurred while processing",parent=self.root)    


    ### Function to fetch data by roll number
    def FetchData(self):
        obj1 = sqlite3.connect("Database.db")
        obj = obj1.cursor()
        try:
            obj.execute("SELECT Roll FROM Result")
            items = obj.fetchall()
            if len(items)>0:
                for data in items:
                    self.list.append(data)
            else:
                self.list.clear()
                
           
        except:
            print("An error in fetching data")

    ### Function for handling events of clear button
    def Clear(self):
        self.var1.set("Select")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_id=""
        self.list=[]

    ### Method for handling details of update button
    def Update(self):
        self.new_win = Toplevel(self.root)
        self.obj = update_ui(self.new_win)

    ### Method for handling details of delete button
    def Delete(self):
        obj1 = sqlite3.connect("Database.db")
        obj = obj1.cursor()
        try:
            if self.var_id=='':
                messagebox.showerror("Error","Please select record to delete",parent=self.root)
            else:
                 ans=messagebox.askyesno("Confirm","Do you really want to delete this result detail?",parent=self.root)
                 if ans==True:
                    obj.execute("DELETE FROM Result WHERE Rid=?",(self.var_id,))
                    obj1.commit()
                    messagebox.showinfo("Message","Result deleted successfully",parent=self.root)
                    self.Clear()
                    self.FetchData()
        except:
            messagebox.showerror("Error","Error in deleting result",parent=self.root)
        




    


if __name__=="__main__" :

    obj1 = Tk()
    obj2 = view_ui(obj1)
    obj1.mainloop()
