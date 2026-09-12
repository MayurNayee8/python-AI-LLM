'''
class - blue print or templat or strcuture that defnines the object

object - instance of class

syntac:

class ClassName:

// propoerties (var) and mathods (unctions)
functions in class are methods

inside class there is constructor
constructor is speciacla type of functions that runs auto when you create 
object of class

if function inside class then self keyword mandatory
def display(self)

'''

class Employee:
    name:str
    age:int
    gender:str
    salary:float
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        
        
    def display_emp(self):
        print("name", self.name)
        print("age", self.age)
        print("gender", self.gender)
        print("salary", self.salary)
    

obj = Employee("maysup",33, "male", 14.8)
obj.display_emp()

obj1 = Employee("Sup", 34, "female", 6.9)
obj1.display_emp()


class Department(Employee):
    department:str
    def __init__(self, name, age, gender, salary, department):
        super().__init__(name, age, gender, salary)
        self.department =department
    def update(self):
        self.display_emp()
        print("employee department is", self.department)

dp = Department("Sup", 34, "female", 6.9, "IT")
dp.update()
#developer as clasd 
'''
developer as class
skilss as list

assign some values by using obj and if 
'''

class Developer:
    skills:list
    def __init__(self, skills):
        self.skills = skills

    def display_skills(self):
        print("skills are: ", self.skills)

devSkills = Developer(['Playwright', 'Jmeter', 'Python', 32, 'testing'])
devSkills.display_skills()


        