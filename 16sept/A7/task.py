import random
import string


def temparature(farent_temp):
    return (farent_temp - 32)*(5/9)


farent_heat = int(input("Enter temparature in farent heat: "))
celcius = temparature(farent_heat)
print(f"{farent_heat}°F is {celcius:.1f}°C")


def calculations(length, width):
    perimeter = (length+width)*2
    area = length*width
    return perimeter, area


length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))
perimeter, area = calculations(length, width)
print(
    f"Rectangle Calculations\nLength= {length}\nWidth= {width}\nPerimeter={perimeter}\nArea={area}")


def addition(first_number, second_number):
    return first_number+second_number


def subtraction(first_number, second_number):
    return first_number-second_number


def multiplication(first_number, second_number):
    return first_number*second_number


def division(first_number, second_number):
    return first_number/second_number


print(f"Simple Calculator\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Divion")
operator = int(input("Choose operator: "))
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
if operator == 1:
    print(f"Answer= {addition(first_number, second_number)}")
elif operator == 2:
    print(f"Answer= {subtraction(first_number, second_number)}")
elif operator == 3:
    print(f"Answer= {multiplication(first_number, second_number)}")
elif operator == 4:
    if second_number == 0:
        print("Error!Division by zero")
    else:
        print(f"Answer= {division(first_number, second_number)}")
else:
    print("Invalid option")


def generate_password(length, is_number, is_symbol):
    characters = string.ascii_letters
    if is_number:
        characters += string.digits
    if is_symbol:
        characters += string.punctuation
    password = ""
    for i in range(length):
        password += ''.join(random.choice(characters))
    return password


def check_password(password, is_number, is_symbol):
    if len(password) >= 12 and is_number and is_symbol:
        print("Password strength: Strong")
    elif len(password) >= 8 and (is_number or is_symbol):
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")


print("Password gnerator")
length = int(input("Enter length of password: "))
is_number = input("Includes numbers?(y/n): ").lower() == "y"
is_symbol = input("Includes symbols?(y/n): ").lower() == "y"
password = generate_password(length, is_number, is_symbol)
print(f"Password: {password}")
check_password(password, is_number, is_symbol)


def reverse(itr):
    return itr[::-1]


str1 = input("Enter value to be reversed: ")


print("Original string:", str1)


print("Reverse string:", reverse(str1))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Input a number to compute the factorial: "))
print(factorial(n))


def square(number):
    for i in range(1, number+1):
        print(f"{i}^2= {i**2}")


number = int(input("Enter range: "))
square(number)
