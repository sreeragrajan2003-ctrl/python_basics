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


# CHALLENGE TASK
# import string
# import random
# character = string.ascii_letters
# password = []


# def password_gen(length, upper, number, symbol, similar):
#     character = string.ascii_letters
#     if upper:
#         character += string.ascii_uppercase
#     if number:
#         character += string.digits
#     if symbol:
#         character += string.punctuation
#     if similar:
#         for i in "o01l":
#             character = character.replace(i, "")

#     for i in range(length):
#         password.append(random.choice(character))
#     return "".join(password)


# analysis = {}


# def password_strength(password, length):
#     print("Password Analysis:")
#     if length >= 12:
#         print(f"Length:{length}: Strong")
#     else:
#         print(f"Length:{length}: Weak")
#     analysis["upper"] = any(c.isupper() for c in password)
#     analysis["number"] = any(c.isdigit() for c in password)
#     analysis["symbol"] = any(c.isupper() for c in password)
#     analysis["upper"] = any(c in string.punctuation for c in password)
#     if length >= 12 and analysis["upper"] and analysis["number"] and analysis["symbol"]:
#         analysis["overall"] = "Strong"
#     elif length >= 8:
#         analysis["overall"] = "Medium"
#     else:
#         analysis["overall"] = "Weak"
#     if analysis["upper"]:
#         print("✅ Uppercase: Yes")
#     else:
#         print("❌ Uppercase: No")
#     if analysis["symbol"]:
#         print("✅ Symbols: Yes")
#     else:
#         print("❌ Symbols: No")
#     if analysis["number"]:
#         print("✅ Number: Yes")
#     else:
#         print("❌ Number: No")
#     print(f"🔒 Overall strength:{analysis['overall']}")


# print("Advanced Password Generator")
# length = int(input("Enter password length: "))
# upper = input("Include uppercase letters? (y/n): ").lower() == "y"
# number = input("Include numbers? (y/n): ").lower() == "y"
# symbol = input("Include symbols? (y/n): ").lower() == "y"
# similar = input("Exclude similar characters (0,O,l,1)? (y/n): ") == "y"
# password = password_gen(length, upper, number, symbol, similar)
# print(f"Generated pasword: {password}")
# password_strength(password, length)

# Bonus Task
# import random
# import datetime


# weather_conditions = {
#     "Sunny ☀️": 9,
#     "Rainy 🌧️": 6,
#     "Cloudy ⛅": 7,
#     "Snowy ❄️": 8,
#     "Stormy 🌪️": 4
# }

# quotes = [
#     "The best time to plant a tree was 20 years ago. The second best time is now.",
#     "Keep your face always toward the sunshine—and shadows will fall behind you.",
#     "It does not matter how slowly you go as long as you do not stop.",
#     "The harder you work for something, the greater you’ll feel when you achieve it.",
#     "Dream bigger. Do bigger."
# ]

# file_name = "favorites.txt"


# def get_greeting():
#     hour = datetime.datetime.now().hour
#     if 5 <= hour < 12:
#         return "Good morning 🌅", 2
#     elif 12 <= hour < 18:
#         return "Good afternoon ☀️", 1
#     elif 18 <= hour < 22:
#         return "Good evening 🌆", 1
#     else:
#         return "Good night 🌙", 0


# def generate_weather_and_quote():
#     weather = random.choice(list(weather_conditions.keys()))
#     weather_score = weather_conditions[weather]
#     quote = random.choice(quotes)
#     luck = random.randint(1, 10)
#     return weather, weather_score, quote, luck


# def save_quote_to_file(quote):
#     with open(file_name, "a") as f:
#         f.write(quote + "\n")


# def view_saved_quotes():
#     try:
#         with open(file_name, "r") as f:
#             print("\n⭐ Favorite Quotes:")
#             print(f.read())
#     except FileNotFoundError:
#         print("\nNo favorite quotes yet.")


# while True:
#     greeting, time_bonus = get_greeting()
#     weather, weather_score, quote, luck = generate_weather_and_quote()
#     total_mood = (weather_score + time_bonus + luck) * 5

#     print("\nDaily Inspiration Generator")
#     print(f"{greeting}")
#     print(f"Today's weather mood: {weather}")
#     print(f"🌟 Quote: {quote}")

#     print("\nMood calculation:")
#     print(f"Weather score: {weather_score}/10")
#     print(f"Time bonus: +{time_bonus}")
#     print(f"Random luck: {luck}/10")
#     print(f"Total mood score: {total_mood}/100")

#     print("\nOptions:")
#     print("1. Get another quote")
#     print("2. Save this quote")
#     print("3. View quote history")
#     print("4. Exit")

#     choice = input("Choose option: ")
#     if choice == "1":
#         continue
#     elif choice == "2":
#         save_quote_to_file(quote)
#         print("Quote saved! ⭐")
#     elif choice == "3":
#         view_saved_quotes()
#     elif choice == "4":
#         print("Goodbye 👋 Stay inspired!")
#         break
#     else:
#         print("Invalid choice, try again.")
