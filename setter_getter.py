class Employee:

    def __init__(self,owner,salary):
        self.name=owner
        self._income=salary
    def get_salary(self,password):
        if password=="admin":
            print(self._income)
        else:
            print("Access denied!!!")
    def set_salary(self,salary,password):
        if password=="admin":
            self._income=salary
            # print(f"New salary-{self._income}")
        else:
            print("Access denied!!!")

emp1=Employee("Rumy",45000)
emp2=Employee("Ehsan",200356)
emp1.get_salary("4556")
emp2.set_salary(70000,"admin")
print(emp2._income)