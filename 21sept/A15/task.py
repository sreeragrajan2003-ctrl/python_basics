# FOUNDATION TASK
# class smartdevice:
#     def power_on(self):
#         print("Turning on device....")


# class smartphone(smartdevice):
#     def power_on(self):
#         print("Smartphone: Booting mobile OS...")


# class smartwatch(smartdevice):
#     def power_on(self):
#         print("Smartwatch: Starting wearable system...")


# v1 = smartdevice()
# v1.power_on()
# c1 = smartphone()
# c1.power_on()
# b1 = smartwatch()
# b1.power_on()


# STRTCH TASK
# from abc import ABC, abstractmethod


# class paymentmethod(ABC):
#     def __init__(self, amount=0):
#         self.amount = amount

#     @abstractmethod
#     def process_payment(self):
#         pass


# class upi(paymentmethod):
#     def process_payment(self):
#         print(f"UPI: Processing payment of {self.amount}")


# class cash(paymentmethod):
#     def process_payment(self):
#         print(f"Cash: Processing payment of {self.amount}")


# class credit_card(paymentmethod):
#     def process_payment(self):
#         print(f"Credit card: Processing payment of {self.amount}")


# payment = [cash(), credit_card(), upi()]
# method_names = ["Cash", "Credit card", "UPI"]
# for method, name in zip(payment, method_names):
#     amount = int(input(f"Enter amount for {name}: "))
#     method.amount = amount
#     method.process_payment()


# CHALLENGE TASK
# class contentcreater:
#     def __init__(self, name, followers):
#         self.name = name
#         self.__followers = followers

#     def create_content(self):
#         pass


# class youtuber(contentcreater):
#     def create_content(self):
#         return "Recording and editing videos..."


# class blogger(contentcreater):
#     def create_content(self):
#         return "Writing and publishing articles..."


# employee = [blogger("Ravi", 70000), youtuber("Suku", 60000)]
# for emp1 in employee:
#     print(f"Employee: {emp1.name}")
#     print(f"Position: {emp1.__class__.__name__}")
#     print(f"Work: {emp1.create_content()}")
