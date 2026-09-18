class Student:
    def set_name(self,n):
        self.name=n
    def say_hi(self):
        print(f"Hi, {self.name}")

a=Student()
a.set_name("Rumy")
b=Student()
a.say_hi()
