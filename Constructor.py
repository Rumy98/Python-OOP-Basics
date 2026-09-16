class Car:
    # def __init__(self):
    #     self.brand="" 
    #     self.model=""
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand

    def __init__(self,brand="HP",model="Ryzen"):
        self.model=model
        self.brand=brand


car1=Car("Toyota","Corolla")
car1.brand="Toyota"
car1.model="Corolla"
print(car1.brand,car1.model)

car2=Car()
print(car2.brand,car2.model)