# transactions = [

#     {"id": 1, "amount": 250, "type": "credit"},

#     {"id": 2, "amount": 100, "type": "debit"},

#     {"id": 3, "amount": 50, "type": "debit"},

#     {"id": 4, "amount": 400, "type": "credit"},

#     {"id": 5, "amount": 75, "type": "debit"},

#     {"id": 6, "amount": 600, "type": "credit"},

#     {"id": 7, "amount": 120, "type": "debit"},

#     {"id": 8, "amount": 90, "type": "debit"},

#     {"id": 9, "amount": 1000, "type": "credit"},

#     {"id": 10, "amount": 200, "type": "credit"},

#     {"id": 11, "amount": 40, "type": "debit"},

#     {"id": 12, "amount": 300, "type": "credit"},

#     {"id": 13, "amount": 500, "type": "credit"},

#     {"id": 14, "amount": 60, "type": "debit"},

#     {"id": 15, "amount": 350, "type": "credit"},

#     {"id": 16, "amount": 80, "type": "debit"},

#     {"id": 17, "amount": 450},

#     {"id": 18, "amount": 220, "type": "debit"},

#     {"id": 19, "amount": 700, "type": "credit"},

#     {"id": 20, "amount": 150, "type": "debit"},

# ]


# def balance_account(transactions, current_balance=0):
#     for transaction in transactions:
#         if transaction.get('type') == "credit":
#             current_balance += int(transaction["amount"])
#         elif transaction.get('type') == "debit":
#             current_balance -= int(transaction["amount"])
#     print(f"Current balance: {current_balance}")


# def top_credit(transactions):
#     highest = {}
#     for transaction in transactions:
#         if transaction.get('type') == "credit":
#             amount = transaction["amount"]
#             if amount > highest.get("amount", 0):
#                 highest = transaction
#     print(f"Highest credit is {highest}")


# balance_account(transactions, 0)
# top_credit(transactions)

students = [['Harry', 37.21], ['Berry', 37.21], [
    'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
student = []
for name, grade in students:
    student.append({"name": name, "grade": grade})

print(student)
for student in student:
    print(student)
