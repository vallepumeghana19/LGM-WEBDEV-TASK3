import sqlite3
obj1 = sqlite3.connect("Database.db")
obj = obj1.cursor()

### For Course Section##
def AddCourse():
    obj.execute("CREATE TABLE  IF NOT EXISTS Course(CourseId INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Duration text,Charges text, Description text)")
    obj1.commit()

def AddStudent():
    obj.execute("CREATE TABLE IF NOT EXISTS Student(Roll INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,DOB text,Contact text,Admission text,Course text,State text,City text,Pin text,Address text)")
    obj1.commit()

def AddResult():
     obj.execute("CREATE TABLE  IF NOT EXISTS Result(Rid INTEGER PRIMARY KEY AUTOINCREMENT,Roll text,Name text,Course text,Marks_ob text,Full_marks text,Percentage text)")
     obj1.commit()

def Register():
    obj.execute("CREATE TABLE IF NOT EXISTS Register(Empid INTEGER PRIMARY KEY AUTOINCREMENT,FName text,LName text,Email text,Contact text,Ques text,Ans text,Pwd text)")

AddCourse()
AddStudent()
AddResult()
Register()   
