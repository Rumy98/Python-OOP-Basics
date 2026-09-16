class Car():
    def __init__(self):
        Car.model=""
        Car.brand=""

car1=Car()
car1.brand="Toyota"
car1.model="Corolla"
print(car1.brand)
print(car1.model)
print("---------------------")
car2=Car()
car2.brand="Honda"
car2.model="Civic"
print(car2.brand, car2.model)