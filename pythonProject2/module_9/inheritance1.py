# class Vehicle:
#     def __init__(self):
#         self.velocity = 5
#
#     def stop(self):
#         self.velocity = 0
#
# class Car(Vehicle):
#     def __init__(self, make_model, mpg):
#         self.make_model = make_model
#         self.mpg = mpg
#
# car = Car("Toyota Camry", 27.5)
# # print(car.make_model)
# # print(car.mpg)
# # print(car.velocity) # error since there is no velocity in class Car
# car.stop() # use the stop() method in class Vehicle
# print(car.velocity)

# super is a way of accessing the parents attributes or methods from inside the child
class Vehicle:
    def __init__(self):
        self.velocity = 5

    def stop(self):
        self.velocity = 0

class Car(Vehicle):
    def __init__(self, make_model, mpg):
        super().__init__() # the Vehicle constructor was called using super()
        self.make_model = make_model
        self.mpg = mpg

car = Car("Toyota Camry", 27.5)
# print(car.make_model)
# print(car.mpg)
print(car.velocity) # error since there is no velocity in class Car
car.stop() # use the stop() method in class Vehicle
print(car.velocity)
# print(car.mpg)

