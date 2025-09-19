# thoughts = input("Enter your thoughts: ")
# with open("diary.txt", "w") as file:
#     file.write(thoughts)
#     print("Your thoughts have been saved to diary.txt")
# with open("diary.txt", "r") as file:
#     print(file.read())

# with open("score.txt", "w") as file:
#     file.write("Alice: 95\nBob: 87 \nCarol: 92")
# scores = {}
# with open("score.txt", "r") as file:
#     for line in file:
#         name, score = line.strip().split(":")
#         scores[name] = score
# print("Current high score: ")
# for i, (name, score) in enumerate(sorted(scores.items(), reverse=True), 1):
#     print(f"{i}. {name}: {score}")
# new_name = input("Enter new name: ")
# new_score = int(input("Enter score: "))
# scores[new_name] = new_score
# print("Updated high score: ")
# for i, (name, score) in enumerate(sorted(scores.items(), reverse=True), 1):
#     print(f"{i}. {name}: {score}")
# with open("score.txt", "w") as file:
#     for name, score in scores.items():
#         file.write(f"{name}:{score}\n")
# with open("score.txt", "r") as file:
#     print(file.read())


# expenses = []

# def file_details():
#     # Write expenses to file
#     with open("report.txt", "w") as file:
#         for exp in expenses:
#             file.write(f"{exp['date']}|{exp['category']}|{exp['amount']}|{exp['description']}\n")

#     # Read and print file content
#     with open("report.txt", "r") as file:
#         print(file.read())

# while True:
#     print("\nExpense tracker")
#     print("1. Add expense\n2. View all expenses\n3. Category summary\n4. Monthly summary\n5. Exit")
#     operator = int(input("Select operation: "))

#     if operator == 1:
#         date = input("Enter date (yyyy/mm/dd): ")
#         category = input("Enter category: ")
#         amount = float(input("Enter the amount: "))
#         description = input("Enter description: ")
#         expenses.append({
#             "date": date,
#             "category": category,
#             "amount": amount,
#             "description": description
#         })
#         print("Expense added")
#         file_details()

#     elif operator == 2:
#         if not expenses:
#             print("No expenses recorded.")
#         else:
#             for exp in expenses:
#                 print(
#                     f"Date: {exp['date']}\nCategory: {exp['category']}\nAmount: {exp['amount']}\nDescription: {exp['description']}\n"
#                 )

#     elif operator == 3:
#         if not expenses:
#             print("No expenses recorded.")
#         else:
#             category_sum = {}
#             for exp in expenses:
#                 cat = exp["category"]
#                 amt = exp["amount"]
#                 category_sum[cat] = amt + category_sum.get(cat, 0)
#             print("Category Summary:")
#             for cat, amt in category_sum.items():
#                 print(f"{cat}: ${amt:.2f}")

#     elif operator == 4:
#         if not expenses:
#             print("No expenses recorded.")
#         else:
#             monthly = sum(exp["amount"] for exp in expenses)
#             print(f"Monthly expense: ${monthly:.2f}")

#     elif operator == 5:
#         print("Bye!")
#         break

#     else:
#         print("Invalid input!")


contacts = {}


def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, info in contacts.items():
            file.write(
                f"{name}|{info['phone']}|{info['email']}|{info['address']}\n")


while True:
    print("Contact book: \n 1. Display contacts \n 2. Delete contact\n 3. Add contact\n 4. Search contact\n 5. Exit")
    selector = int(input("Enter the operation: "))

    if selector == 1:
        if len(contacts) == 0:
            print("No contacts")
        else:
            for name in sorted(contacts):
                info = contacts[name]
                print(
                    f"{name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n")

    elif selector == 2:
        if len(contacts) == 0:
            print("No contacts")
        else:
            name = input("Enter name to delete: ")
            if name in contacts:
                del contacts[name]
                save_contacts()  # Save after deletion
                print("Contact deleted.")
            else:
                print("No such name in contact")

    elif selector == 3:
        name = input("Enter name: ")
        phone = input("Enter number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_contacts()  # Save after adding
        print("Contact added.")

    elif selector == 4:
        name = input("Enter name to search: ")
        if name in contacts:
            info = contacts[name]
            print(
                f"{name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
        else:
            print("No such name in contact")

    elif selector == 5:
        print("Bye.....")
        break

    else:
        print("Invalid input")
