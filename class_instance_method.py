class Employee:
    company_name="ABC"
    def __init__(self,owner,salary):
        self.name=owner
        self.income=salary
    def display_info(self):
        print(f"Employee Name: {self.name}& Salary:{self.income}")
    @classmethod
    def change_company_name(cls,name):
        cls.name=name

emp1=Employee("Ehsan",30000)
emp1.display_info()
emp2=Employee("Rumy",45000)
Employee.change_company_name("Bomb")
emp2.display_info()