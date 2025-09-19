# BONUS TASK
# import random
# def roll_dice(face):
#     return random.randint(1, face)
# total = 0
# out = []
# while True:
#     print("Dice roller\n1. Roll dice of 6 faces\n2. Roll dice of 20 faces\n3. Roll multiple dices\n4. Exit")
#     select = int(input("Enter operation: "))
#     if select == 1:
#         result = roll_dice(6)
#         print(f"🎲 You rolled: {result}")
#     elif select == 2:
#         result = roll_dice(20)
#         print(f"🎲 You rolled: {result}")
#     elif select == 3:
#         num = int(input("Enter no of dice: "))
#         for i in range(num):
#             result = roll_dice(6)
#             total += result
#             out.append(str(result))
#         print(f"{'🎲' * num} You rolled:{",".join(out)}")
#         print(f"Total: {total}")


# STRETCH TASK
# from datetime import date, datetime
# birthstones = {
#     1: "Garnet",
#     2: "Amethyst",
#     3: "Aquamarine",
#     4: "Diamond",
#     5: "Emerald",
#     6: "Pearl",
#     7: "Ruby",
#     8: "Peridot",
#     9: "Sapphire",
#     10: "Opal",
#     11: "Topaz",
#     12: "Turquoise"
# }

# zodiac_animals = [
#     "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
#     "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
# ]

# bday = input("Enter your birthday(YYYY-MM-DD): ")
# birthday = datetime.strptime(bday, "%Y-%m-%d").date()
# week = birthday.strftime("%A")
# today = date.today()
# no_days = (today-birthday).days
# years = no_days//365
# months = (no_days % 365)//30
# days = (no_days % 365) % 30
# next_birthday = date(today.year, birthday.month, birthday.day)
# if next_birthday < today:
#     next_birthday = date(today.year+1, birthday.month, birthday.day)
# days_to_next = (next_birthday-today).days
# chinese_zodiac = zodiac_animals[(birthday.year-1900) % 12]
# birth_stone = birthstones[birthday.month]
# print("\n🎂 Birthday Facts:")
# print(f"- You were born on a {week}")
# print(f"- You are {years} years, {months} months, and {days} days old")
# print(f"- You have lived for {no_days:,} days")
# print(f"- Your next birthday is in {days_to_next} days")
# print(f"- You were born in the year of the {chinese_zodiac} (Chinese zodiac)")
# print(f"- Your birthstone is {birth_stone}")
