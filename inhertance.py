from employee import Employee
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