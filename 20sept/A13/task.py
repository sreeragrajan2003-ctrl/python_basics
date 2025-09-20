# FOUNDATION TASK
# class book:
#     def __init__(self, title, author, date):
#         self.title = title
#         self.author = author
#         self.date = date

#     def display(self):
#         print(
#             f"Book Summary:\nTitle: {self.title}\nAuthor: {self.author}\nPublished: {self.date}")


# book_name = input("Enter book name: ")
# book_author = input("Enter author name: ")
# book_year = input("Enter year published: ")
# book_1 = book(book_name, book_author, book_year)
# book_1.display()


# STRETCH TASK
# class student:
#     def __init__(self, name, roll, mark):
#         self.name = name
#         self.roll = roll
#         self.mark = mark

#     def display(self):
#         print(
#             f"Student: {self.name}\nRoll No: {self.roll}\nMarks: {self.mark}")
#         if self.mark > 40:
#             print("Status: ✅ Passed")
#         else:
#             print("Status: ❌ Failed")


# name, roll, mark = input("Enter the name,roll,mark(out of 100): ").split(",")
# student_1 = student(name, roll, int(mark))
# student_1.display()


# CHALLENGE TASK
class account:
    def __init__(self, current_balance, operation, amount):
        self.current_balance = current_balance
        self.operation = operation
        self.amount = amount

    def process(self):
        if self.operation == "credit":
            self.new_balance = self.current_balance+self.amount
            print(
                f"Depositing ₹{self.amount}...\nNew Balance: ₹{self.new_balance}")
            return self.new_balance
        elif self.operation == "debit":
            if self.amount > self.current_balance:
                print("❌ Error: Insufficient funds")
                return self.current_balance
            else:
                self.new_balance = self.current_balance-self.amount
                print(
                    f"Depositing ₹{self.amount}...\nNew Balance: ₹{self.new_balance}")
                return self.new_balance


current_balance = int(input("Enter current balance: "))
while True:

    operation = input("credit or debit or exit: ").lower()

    if operation == "exit":
        print("exiting....")
        break
    elif operation not in ["credit", "debit"]:
        print("Give credit debit or exit")
        continue
    try:
        amount = int(input("amount: "))
    except ValueError:
        print("Error! Enter a valid amount")
    print(f"Welcome to Python Bank!\nBalance: ₹{current_balance}")
    acc_1 = account(current_balance, operation, amount)
    new_balance = acc_1.process()
    current_balance = new_balance
