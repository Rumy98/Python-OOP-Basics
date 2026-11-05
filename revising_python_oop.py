class Person:
 def __init__(self,name,age=18):
  self.name=name
  self.age=age
 def greet(self):
    print("Hello, my name is ",self.name )

p1=Person("John")
p2=Person("Rumy",28) 
p1.greet()
print(p1.age)
p2.greet()
print(p2.age)