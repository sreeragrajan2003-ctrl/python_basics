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


# def save_contacts():
#     with open("contacts.txt", "w") as f:
#         for name, info in contacts.items():
#             f.write(f"{name}: {info}\n")
#     with open("contacts.txt", "r") as f:
#         print(f.read())


# contacts = {}
# while True:
#     print("Contact book: \n 1. Display contacts \n 2. Delete contact\n 3. Add contact\n 4. Search contact\n 5. Exit")
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
#             name = input("Enter name to delete: ")
#             if name in contacts:
#                 del contacts[name]
#                 save_contacts()
#             else:
#                 print("No such names in contact")
#     elif selector == 3:
#         name = input("Enter name: ")
#         phone = input("Enter number: ")
#         email = input("Enter email: ")
#         address = input("Enter address: ")
#         contacts[name] = {"phone": phone, "email": email, "address": address}
#         print("Contact Added")
#         save_contacts()
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
def file_details():
    with open("report.txt", "w") as file:
        for exp in expenses:
            file.write(
                f"{exp['date']}\n{exp['category']}\n{exp['amount']}\n{exp['description']}\n")
    with open("report.txt", "r") as file:
        print(file.read())


expenses = []


while True:
    print("Expense tracker\n1. Add expense\n2. View all expense\n3. Category summary\n4. Monthly summary")
    operator = int(input("Select operation: "))
    if operator == 1:
        date = input("Enter date (yyyy/mm/dd): ")
        category = input("Enter category: ")
        amount = int(input("Enter the amount: "))
        description = input("Enter description")
        expenses.append({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description}
        )
        print("Contact added")
        file_details()
    elif operator == 2:
        for exp in expenses:
            print(
                f"date:{exp["date"]}\ncategory:{exp["category"]}\namount:{exp["amount"]}\ndescription:{exp["description"]}")
    elif operator == 3:
        category_sum = {}
        for exp in expenses:
            cat = exp["category"]
            amt = exp["amount"]
            category_sum[cat] = amt+category_sum.get(cat, 0)
        for cat, amt in category_sum.items():
            print(f"Category: {cat}\nAmount: {amt}")
    elif operator == 4:
        monthly = 0
        for exp in expenses:
            monthly += exp["amount"]
        print(f"Monthly expense: {monthly}")
    else:
        print("invalid input!")
