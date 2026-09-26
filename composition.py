class Engine:
    def __init__(self,power):
        self.power=power
class Car:
    def __init__(self,brand,power):
        self.name=brand
        self.engine=Engine(power)
    def show_details(self):
        print(f"{self.name} has engine of power {self.engine.power}")
car1=Car("BMW",500)
car1.show_details()