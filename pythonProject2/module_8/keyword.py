class Car:
    class_name = "Car"
    def __init__(self, make = "", model = ""):
        self.speed = 0
        self.make = make
        self.model = model

car1 = Car("Toyota", "BMW")
car2 = Car("Jaguar","XF")
print(car1.make)
print(car2.speed)

# self is a reference used to refer to the current instance (similar to this in Java)
# self is the mechanism by which Python knows which object's instance variables to access/modify
# This reference is sent implicitly to each class method but must be received explicitly