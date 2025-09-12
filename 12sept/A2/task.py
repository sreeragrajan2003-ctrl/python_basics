number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
elif number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")


response = input("Do you love coding? (yes/no): ")
if response.lower() == "yes":
    print("You are going to enjoy this journey!")
elif response.lower() == "no":
    print("Dont worry lets grow together.")
else:
    print("Lets make ourself better.")


number1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+,-,*,/): ")
number2 = int(input("Enter the second number: "))
if operator == "+":
    result = number1+number2
elif operator == "-":
    result = number1-number2
elif operator == "*":
    result = number1*number2
elif operator == "/":
    if number2 != 0:
        result = number1/number2
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operator"
print(f"Result: {result}")    


field = input("Which is your favourite field? ")
person = input("Who is the person you admire most in this field? ")
why = input("Why do you like them? ")

print(
    f"You are a person who loves {field}, and your favorite person in this field is {person.title()}. You admire them because of their {why}."
)


#calculator with modulus
number1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+,-,*,/,%): ")
number2 = int(input("Enter the second number: "))
if operator == "+":
    result = number1+number2
elif operator == "-":
    result = number1-number2
elif operator == "*":
    result = number1*number2
elif operator == "/":
    if number2 != 0:
        result = number1/number2
    else:
        result = "Cannot divide by zero."
elif operator == "%":
    result = number1 % number2
else:
    result = "Invalid operator"
print(f"Result: {result}")

#extra personality
field = input("Which is your favourite field? ").lower()
person = input("Who is the person you admire most in this field? ")
why = input("Why do you like them? ")
if field == "science":
    message = f"You love {field}, and admire {person.title()} for their {why}. You're curious and love discovering new things!"
elif field == "sports":
    message = f"You love {field}, and admire {person.title()} for their {why}. You're energetic and enjoy challenges!"
elif field == "music":
    message = f"You love {field}, and admire {person.title()} for their {why}. You have a creative and expressive personality!"
else:
    message = f"You love {field}, and admire {person.title()} for their {why}. That's a unique passion!"

print(message)
