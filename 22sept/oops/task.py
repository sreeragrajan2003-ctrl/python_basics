# Inheritance
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_details(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         Employee.__init__(self, name, salary)
#         self.team_size = team_size

#     def display_details(self):
#         print(
#             f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}")


# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         Employee.__init__(self, name, salary)
#         self.programming_language = programming_language

#     def display_details(self):
#         print(
#             f"Name: {self.name}, Salary: {self.salary}, Language: {self.programming_language}")


# manager = Manager("Alice", 80000, 10)
# developer = Developer("Bob", 60000, "Python")

# manager.display_details()
# developer.display_details()

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

# c1 = Circle(5)
# print(f"Circle Area: {c1.area():.1f}")

# s1 = Square(6)
# print(f"Square Area: {s1.area()}")

# r1 = Rectangle(12, 10)
# print(f"Rectangle Area: {r1.area()}")


# Polymorphism
# class guitar:
#     def play_sound(self):
#         print("Guitar music....")


# class piano:
#     def play_sound(self):
#         print("Piano music....")


# class drum:
#     def play_sound(self):
#         print("Drum music....")


# instruments = [guitar(), piano(), drum()]
# for i in instruments:
#     i.play_sound()


# class Dog:
#     def activity(self):
#         print("Dog is barking 🐶")


# class Cat:
#     def activity(self):
#         print("Cat is sleeping 😺")


# class Bird:
#     def activity(self):
#         print("Bird is flying 🐦")


# def animal_activity(animal):
#     animal.activity()


# dog = Dog()
# cat = Cat()
# bird = Bird()

# animal_activity(dog)
# animal_activity(cat)
# animal_activity(bird)


# Abstraction
# from abc import ABC, abstractmethod
# class Payment(ABC):
#     def __init__(self, amount):
#         self.amount = amount

#     @abstractmethod
#     def process_payment(self):
#         pass


# class CashPayment(Payment):
#     def process_payment(self):
#         print(f"Processing cash payment of {self.amount} 💵")


# class CardPayment(Payment):
#     def process_payment(self):
#         print(f"Processing card payment of {self.amount} 💳")


# cash = CashPayment(1000)
# card = CardPayment(2500)

# cash.process_payment()
# card.process_payment()

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

#     def perimeter(self):
#         return 2 * math.pi * self

# Encapsulation
# BankAccount Class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. Remaining Balance: {self.__balance}")

    def check_balance(self):
        print(f"Account Balance: {self.__balance}")
        return self.__balance
# Student Class


class Student:
    def __init__(self, name, roll_number, marks):
        self.__name = name
        self.__roll_number = roll_number
        self.__marks = 0
        self.set_marks(marks)

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        self.__name = name

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")
