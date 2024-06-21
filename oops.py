

# Define the base class Swimming
class Swimming:
    def swim(self):
        print("Swimming")

# Define the base class Flying
class Flying:
    def fly(self):
        print("Flying")

# Define the derived class Duck
class Duck(Swimming, Flying):
    pass

# Instantiate an object of Duck
my_duck = Duck()

# Call both the swim() and fly() methods
my_duck.swim()
my_duck.fly()
########################################################################


# Define the base class LivingBeing
class LivingBeing:
    def live(self):
        print("Living")

# Define the derived class Animal
class Animal(LivingBeing):
    def breathe(self):
        print("Breathing")

# Define the derived class Human
class Human(Animal):
    def speak(self):
        print("Speaking")

# Instantiate an object of Human
my_human = Human()

# Call all three methods
my_human.live()
my_human.breathe()
my_human.speak()
############################################33333

# Define the base class Shape
class Shape:
    def area(self):
        return 0

# Define the derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)

# Define the derived class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Instantiate objects of both Circle and Rectangle
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

# Call their area() methods
print(f"Circle area: {my_circle.area()}")
print(f"Rectangle area: {my_rectangle.area()}")
########################################################################

# Define the base class Vehicle
class Vehicle:
    def drive(self):
        print("Driving")

# Define the derived class Car
class Car(Vehicle):
    def carry_passengers(self):
        print("Carrying passengers")

# Define the derived class Truck
class Truck(Vehicle):
    def carry_cargo(self):
        print("Carrying cargo")

# Define the derived class PickupTruck
class PickupTruck(Car, Truck):
    pass

# Instantiate an object of PickupTruck
my_pickup_truck = PickupTruck()

# Call the methods
my_pickup_truck.drive()
my_pickup_truck.carry_passengers()
my_pickup_truck.carry_cargo()
###################################################33333333


