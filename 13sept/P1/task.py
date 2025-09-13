# Write a function to get the sum of the digits in the given number.
number = (input("Enter a number:"))
digit_sum = 0
for i in range(len(number)):
    digit_sum += int(number[i])
print(f"sum={digit_sum}")

#reverse a number
number = (input("Enter a number:"))
number = number[::-1]
print(f"reversed number= {number}")

#factorial
number = int(input("Enter a number:"))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print(f"Factorial= {factorial}")

#palindrome
number = (input("Enter a number:"))
number_reversed = number[::-1]
if number == number_reversed:
    print("Palindrome")
else:
    print(" Not a palindrome")

#No of digits
number = (input("Enter a number:"))
print(f"No of digits in given number= {len(number)}")

#multiplication table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} X {i} = {number*i} ")

#prime
number = int(input("Enter the number: "))
if number <= 1:
    print("Not a prime number")
else:
    
    is_prime = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Number is prime")
    else:
        print("Not a prime number")
#extra
number = int(input("Enter the number: "))
if number <= 1:
    print("Not a prime number")
else:
    for number in range(2, number+1):

        is_prime = True
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number)

#amstrongnumber = int(input("Enter a number: "))
length = len(str(number))
temp = number
result = 0
while temp > 0:
    digit = temp % 10
    result += digit**length
    temp //= 10
if result == number:
    print("Armstrong")
else:
    print("Not a armstrong number")

#reverse a string
word = (input("Enter a word:"))
word = word[::-1]
print(f"reversed word= {word}")

#palindrome string
word = (input("Enter a word:"))
word_reversed = word[::-1]
if word == word_reversed:
    print("Palindrome")
else:
    print(" Not a palindrome")

#vowels
word = input("Enter a word: ").lower()
length = len(word)
count = 0
for i in range(length):
    if word[i] in "aeiou":
        count += 1
print(f"There are {count} vowels")

#coverting case
word = input("Enter a word: ")
converted = word.swapcase()
print(f"Converted= {converted}")

#Count Alphabets, Digits, and Special Characters
word = input("Enter Anything: ")
alphabets = 0
number = 0
special = 0
for i in word:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        number += 1
    else:
        special += 1
print(f"Alphabets= {alphabets}\nNumbers= {number} \nSpecial={special}")

# Write a program to find the largest digit in the given number.
digit = int(input("Enter a number"))
big=0
while digit > 0:
    num = digit % 10
    if num > big:
        big = num
    digit //=10
print(f"Biggest= {big}")

# Fibonacci Series
number = int(input("Enter the count: "))
a = 0
b = 1
for i in range(number):
    print(a)
    a, b = b, a+b
