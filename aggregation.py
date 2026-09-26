class Laptop:
    def __init__(self,brand):
        self.brand=brand
class Student:
    def __init__(self,name,laptop_obj):
        self.name=name
        self.laptop_v=laptop_obj
    def show_student_laptop_info(self):
        print(f"{self.name} uses the {self.laptop_v.brand} laptop")
lap1=Laptop("HP")
st1=Student("Rumy",lap1)
st1.show_student_laptop_info()