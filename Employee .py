#Parent Class
class Person:
    
    
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        

#child class
class Employee( Person ):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self,name,idnumber)
        
a = Employee("Junaira", 12,500000, "Senior Software Engeenier")

a.display()
print(a.salary)
print(a.post)