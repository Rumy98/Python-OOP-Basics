class Department:
    def __init__(self,name):
        self.name=name
class University:
    def __init__(self,name):
        self.name=name
        self.departments=[]
    def add_dept(self,department):
        self.departments.append(department)
    def show_dept(self):
        return [department.name for department in self.departments]  
uni1=University("IUB")
dep1=Department("CSE")
dep2=Department("AI")
uni1.add_dept(dep2)
uni1.add_dept(dep1)
print(uni1.show_dept())