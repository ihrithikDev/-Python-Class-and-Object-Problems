# class and Object Problem

'''
    Problem 1 : 
    Define a class Student with instance variables rollno, name, semester, branch.
    Also define instance member function for user input data to set values of instance variables and
    Display student data
''' 

class Student:
    def __init__(self,rollno,name,semester,branch):
        self.rollno = rollno
        self.name = name 
        self.semester = semester
        self.branch = branch
    def getStudentData(self):
        self.rollno = input("Enter Roll No : ")
        self.name = input("Your Name : ")
        self.semester = input("Enter Semester : ")
        self.branch = input("Enter branch name : ")
    def showStudentData(self):
        print("Your name is {},  Your Roll no is {}, semeter {} and branch is {}".format(self.name,self.rollno,self.semester,self.branch))


s = Student(12,"Ritik Sharma", "V", "Computer Science & Engineering")
s.getStudentData()
s.showStudentData()