class Student:
    def __init__(self,n):
        self.name=n
    def say_hi(self):
        print(f"Hi, {self.name}")

a=Student("Rumy")

a.say_hi()
