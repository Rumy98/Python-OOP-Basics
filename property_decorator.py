class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._sal=salary

    @property
    def salary(self):
        return self._sal
    @salary.setter
    def salary(self,new_salary):
        self._sal=new_salary


emp1=Employee("rahim",4000)
print(emp1._sal)
print(emp1.salary)
emp1._sal=70000
print(emp1._sal)