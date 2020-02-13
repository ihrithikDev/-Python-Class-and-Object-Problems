# class and Object Problem

'''
    Problem 2 : 
    Define a class Employee with instance variables empid, name, slary.
    Also define instance member variables. Define function to show employee data
''' 

class Employee:
    def __init__(self,empid,name,salary):
        self.empid = empid
        self.name = name 
        self.salary = salary
    def showEmployee(self):
        print(" ======= Employee Data ======= ")
        print("Employee Name : {} \n Employee ID : {} \n Salary : {}".format(self.name,self.empid,self.salary))


e = Employee(45,"Ritik", 5000)
e.showEmployee()