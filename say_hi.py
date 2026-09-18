class Student:
    def say_hi(self):
        print(f"Hi, {self.name}")

a=Student()
a.name="Rumy"
b=Student()
b.say_hi()
a.say_hi()