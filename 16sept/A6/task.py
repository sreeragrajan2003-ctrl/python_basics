# animals_sound = {"dog": "bark",
#                  "cat": "meow",
#                  "cow": "moo",
#                  "duck": "quack",
#                  "lion": "roar"
#                  }
# for animals, sounds in animals_sound.items():
#     print(f"{animals} says {sounds}")


# fruits = {"apple": 5, "banana": 3}
# print("Original dictionary:", fruits)

# fruits["orange"] = 8
# print("After adding orange:", fruits)

# fruits["apple"] = 10
# print("After updating apple:", fruits)


# def show_menu():
#     print("\nStudent Grade Tracker")
#     print("1. Add/Update student")
#     print("2. Show all students")
#     print("3. Show average grade")
#     print("4. Show highest and lowest scorer")
#     print("5. Exit")


# Dictionary to store student: grade
# student_grade = {}
# while True:
#     print("Grade tracker\n1. Add/update student details\n2. Display details\n3. Average grade\n4. Highest and lowest grade\n5. Exit")
#     selector = int(input("Enter the operation: "))
#     if selector == 1:
#         student = input("Name of student: ")
#         grade = int(input("Enter grade out of 100: "))
#         student_grade[student] = grade
#         print(f"{student} details added\n")
#     elif selector == 2:
#         if len(student_grade) == 0:
#             print("No student details added\n")
#         else:
#             print(f"Students: {student_grade}\n")
#     elif selector == 3:
#         if len(student_grade) == 0:
#             print("No student details added\n")
#         else:
#             average = sum(student_grade.values())/len(student_grade)
#             print(f"Average: {average}\n")
#     elif selector == 4:
#         if len(student_grade) == 0:
#             print("No student details added\n")
#         else:
#             highest = max(student_grade, key=student_grade.get)
#             lowest = min(student_grade, key=student_grade.get)
#             print(f"Highest student:{highest} {student_grade[highest]}")
#             print(f"Lowest student:{lowest} {student_grade[lowest]}\n")
#     else:
#         break

# contacts = {}
# while True:
#     print("Contact book: \n 1. Display contacts \n 2. Update contact\n 3. Add contact\n 4. Search contact\n 5. Exit")
#     selector = int(input("Enter the operation: "))
#     if selector == 1:
#         if len(contacts) == 0:
#             print("No contacts")
#         else:
#             for name in sorted(contacts):
#                 info = contacts[name]
#                 print(
#                     f"{name}\nPhone: {info["phone"]}\nEmail: {info["email"]}\nAddress: {info["address"]}\n")
#     elif selector == 2:
#         if len(contacts) == 0:
#             print("No contacts")
#         else:
#             name = input("Enter name: ")
#             if name in contacts:
#                 info = contacts[name]
#                 phone = input("Enter number: ")
#                 email = input("Enter email: ")
#                 address = input("Enter address")
#                 info["phone"] = phone
#                 info["email"] = email
#                 info["address"] = address
#                 print("contact updated")
#             else:
#                 print("No such names in contact")
#     elif selector == 3:
#         name = input("Enter name: ")
#         phone = input("Enter number: ")
#         email = input("Enter email: ")
#         address = input("Enter address: ")
#         contacts[name] = {"phone": phone, "email": email, "address": address}
#         print("Contact Added")
#     elif selector == 4:
#         name = input("Enter name to search: ")
#         if name in contacts:
#             info = contacts[name]
#             print(
#                 f"{name}\nPhone: {info["phone"]}\nEmail: {info["email"]}\nAddress: {info["address"]}")
#         else:
#             print("No such names in contact")
#     elif selector == 5:
#         print("Bye.....")
#         break
#     else:
#         print("Invalid input")
