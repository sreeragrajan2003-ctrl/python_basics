for i in range(1, 20, 2):
    print(i)
j = 1
while j < 20:
    print(j)
    j += 2

while True:
    code = input("Enter the secret code: ")
    if code == "python":
        print("Access granted!")
        break
    else:
        print("Invalid code! Try again.")


import random
time = 1
value = random.randrange(1, 11)
while True:
    number = int(input("Guess the number (1-10): "))
    if number == value:
        print(f"Correct! You won in {time} tries.")
        break
    elif number < value:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    time += 1


number = int(input("Enter number:"))
for j in range(1, number+1):
    for i in range(1, 11):
        print(f"{j} x {i} = {number*i}")


#extra
#factorial calulator
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number+1):
    factorial = factorial*i
print(f"factorial of the number is {factorial}")

#divisible of a number with in hundred
number = int(input("Enter a number: "))
for i in range(1, 101):
    if i % number == 0:
        print(i)


#Ask the user for a number n and print numbers from n down to 1 using a loop.
number = int(input("Enter a number: "))
for i in range(number, 0, -1):
    print(i)

#prints numbers from 1 to 20, but skips the even numbers using   
for i in range(1, 20):
    if i % 2 == 0:
        continue
    else:
        print(i)
