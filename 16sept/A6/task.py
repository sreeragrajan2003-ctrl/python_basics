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
# students = {}

# while True:
#     show_menu()
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter student name: ")
#         grade = float(input("Enter grade (0-100): "))
#         students[name] = grade
#         print(f"{name}'s grade has been added/updated.")

#     elif choice == "2":
#         if not students:
#             print("No students yet.")
#         else:
#             print("\nAll Students and Grades:")
#             for name, grade in students.items():
#                 print(f"{name}: {grade}")

#     elif choice == "3":
#         if not students:
#             print("No grades available.")
#         else:
#             average = sum(students.values()) / len(students)
#             print(f"Average Grade: {average:.2f}")

#     elif choice == "4":
#         if not students:
#             print("No students to compare.")
#         else:
#             highest_student = max(students, key=students.get)
#             lowest_student = min(students, key=students.get)
#             print(
#                 f"Highest scorer: {highest_student} ({students[highest_student]})")
#             print(
#                 f"Lowest scorer: {lowest_student} ({students[lowest_student]})")

#     elif choice == "5":
#         print("Exiting Student Grade Tracker.")
#         break

#     else:
#         print("Invalid choice. Try again.")


# contacts = {
#     "Alice Johnson": {"phone": "555-0123", "email": "alice@email.com", "address": "123 Main St"},
#     "Bob Smith": {"phone": "555-0456", "email": "bob@email.com", "address": "456 Oak Ave"}
# }
while True:
    print("\n--- Contact Book ---")
    print("1. Show all contacts")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Add new contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":  # show all contacts
        for name in sorted(contacts):
            info = contacts[name]
            print(
                f"\n{name}\n Phone: {info['phone']}\n Email: {info['email']}\n Address: {info['address']}")

    elif choice == "2":  # search
        name = input("Enter name to search: ")
        if name in contacts:
            info = contacts[name]
            print(
                f"\n{name}\n Phone: {info['phone']}\n Email: {info['email']}\n Address: {info['address']}")
        else:
            print("Not found")

    elif choice == "3":  # edit
        name = input("Enter name to edit: ")
        if name in contacts:
            phone = input("New phone: ")
            email = input("New email: ")
            address = input("New address: ")
            contacts[name] = {"phone": phone,
                              "email": email, "address": address}
            print("Updated!")
        else:
            print("Not found")

    elif choice == "4":  # add new
        name = input("Enter new name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
