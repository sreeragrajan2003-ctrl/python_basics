# try:
#     print("Safe calculator")
#     first = int(input("Enter First number: "))
#     second = int(input("Enter second number: "))
#     result = first/second
#     print(f"Result: {result}")
# except ValueError:
#     print("Enter valid number")
# except ZeroDivisionError:
#     print("Cannot divisible by zero")


# con = True
# while con == True:
#     try:
#         text = input("Enter the text name with .txt: ")
#         with open(text, "r") as file:
#             print(file.read())
#     except FileNotFoundError:
#         print(f"File \"{text}\" not found")
#         select = input("Would you like to open new file (y/n)?").lower()
#         if select == "y":
#             con == True
#         else:
#             break


# def average_grade(average):
#     if average >= 90:
#         return "A"
#     elif average >= 80:
#         return "B"
#     elif average >= 70:
#         return "C"
#     elif average >= 60:
#         return "D"
#     else:
#         return "Fail"


# grades = []
# try:
#     length = int(input("Enter the no of grades: "))
#     for i in range(length):
#         while True:
#             try:
#                 grade = int(input(f"Enter the grade no {i+1} (0-100):"))
#                 if grade <= 100:
#                     grades.append(grade)
#                 else:
#                     print("Enter grade between 0-100")
#             except ValueError:
#                 print("Give valid value")
#     for i in range(length):
#         print(f"Grade {i+1}: {grades[i]}")
#     average = sum(grades)/len(grades)
#     print(f"Average= {average}")
#     letter_grade = average_grade(average)
#     print(f"Letter grade= {letter_grade}")
# except ValueError:
#     print("Enter valid value")


contacts = []
while True:
    print("Contact manage\n1. Add contacts\n2. View contacts\n3. Search contact")
    try:
        op = int(input("Enter the operation: "))
    except ValueError:
        continue
    if op == 1:
        try:
            name = input('Enter the name: ')
            flag = True
            while True:
                number = input("Enter the mobile number: ")
                if number.isdigit():
                    break
                else:
                    print("Enter proper number")

            email = input("Enter email")

            contacts.append({"name": name, "phone": number, "email": email})
            if "." or "@" not in email:
                print("Not proper email still saved")
            else:
                print("Contact saved")
        except ValueError:
            print("Enter valid value")
    elif op == 2:
        for con in contacts:
            print(
                f"name:{con["name"]}\nPhone:{con["phone"]}\nemail:{con["email"]}\n")
    elif op == 3:
        search = input("Enter the name: ")
        for con in contacts:
            if con["name"] == search:
                print(
                    f"name:{con["name"]}\nPhone:{con["phone"]}\nemail:{con["email"]}\n")
                break
            else:
                print("no such contact")
    else:
        print("Invalid input")
