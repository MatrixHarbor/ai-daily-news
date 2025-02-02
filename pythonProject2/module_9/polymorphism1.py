# class Hybrid:
#     def start(self):
#         print("Meep, meep!")
#
# class Car:
#     def start(self):
#         print("Vroom!")
#
# class Truck:
#     def start(self):
#         print("Rawr!")
#
# def start_vehicle(vehicle):
#     vehicle.start()
#
# hybrid = Hybrid()
# car = Car()
# truck = Truck()
#
# for vehicle in [hybrid, car, truck]:
#     start_vehicle(vehicle)

# import sys
# print(sys.version)
# class Animal:
#     def bark(self):
#         print("Woof!")
# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name
#
# pooch = Dog("Coach")
# pooch.bark()

class A:
    def __init__(self, x=10):
        self.x = x

class B(A):
    def __init__(self, x=20):
        self.x = x
        super().__init__()

    def print_x(self):
        print(self.x)

class C(B):
    def __init__(self, x=40):
        self.x = x
        super().__init__()

c = C(1)
c.print_x()