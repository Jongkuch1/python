# Assignment 1: Vehicle Class with Inheritance
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print(f"{self.brand} {self.model} is starting...")
    
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        super().__init__(brand, model, year)
        self.wingspan = wingspan
    
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length = length
    
    def move(self):
        print("Sailing ⛵")

# Activity 2: Polymorphism Demo
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(f"{vehicle.brand} {vehicle.model}:", end=" ")
        vehicle.move()

# Create objects and test
car = Car("Toyota", "Camry", 2023, 4)
plane = Plane("Boeing", "747", 2022, 68.4)
boat = Boat("Yamaha", "242X", 2023, 24)

vehicles = [car, plane, boat]
demonstrate_movement(vehicles)
