class Employee:
    companyName="Opza"
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,newSalary):
        self._salary=newSalary
emp1=Employee("Rahim",500)
print(emp1.salary)
print(emp1.salary)
emp1.salary=70000
print(emp1._salary)