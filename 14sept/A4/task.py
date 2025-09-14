number = int(input("Enter the number: "))
if number <= 1:
    print("No prime number")
else:
    for i in range(2, number+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)


word = input("Enter the string: ")
vowels = 0
consanants = 0
for i in word:
    if i.isalpha():
        if i in "aeiou":
            vowels += 1
        else:
            consanants += 1
print(f"No of vowels= {vowels} \nNo of consanants= {consanants}")
