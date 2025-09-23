# ss vehicle:
#     def start(self):
#         print("vehicle starts....")


# class car(vehicle):
#     pass


# cla
# c1 = car()
# c1.start()
roman_values = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
roman = "MCMXCIV"
prev_value = 0
total = 0
for char in reversed(roman):
    value = roman_values[char]
    if value < prev_value:
        total -= value
    else:
        total += value
    prev_value = value
print(f"Total: {total}")
