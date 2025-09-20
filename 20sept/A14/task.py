# FOUNDATION TASK
# class vehicle:
#     def start(self):
#         print("vehicle strating.....")


# class car(vehicle):
#     def start(self):
#         print("Car: Vroom Vroom!")


# class bike(vehicle):
#     def start(self):
#         print("Bike: Brum Brum!")


# v1 = vehicle()
# v1.start()
# c1 = car()
# c1.start()
# b1 = bike()
# b1.start()

import math

# Base class

# STRETCH TASK
# class Shape:
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2


# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth


# # --- Testing ---
# c1 = Circle(5)
# print(f"Circle Area: {c1.area():.1f}")

# s1 = Square(6)
# print(f"Square Area: {s1.area()}")

# r1 = Rectangle(12, 10)
# print(f"Rectangle Area: {r1.area()}")

# CHALLENGE TASK
# Base class
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def work(self):
#         pass


# class Developer(Employee):
#     def work(self):
#         return "Writing code..."


# class Manager(Employee):
#     def work(self):
#         return "Managing project..."


# employee = [Developer("Ravi", 70000), Manager("Suku", 60000)]
# for emp1 in employee:
#     print(f"Employee: {emp1.name}")
#     print(f"Position: {emp1.__class__.__name__}")
#     print(f"Work: {emp1.work()}")
