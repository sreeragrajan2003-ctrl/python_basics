# FOUNDATION TASK
# sum = 0


# def digit_sum(num):
#     if num == 1:
#         return 1
#     else:
#         sum = digit_sum(num-1)+num
#         return sum


# num = int(input("Enter the number: "))
# print(f"Sum={digit_sum(num)}")


# STRTCH TASK
# def pattern(n):
#     if n == 0:
#         return
#     pattern(n - 1)
#     print("*" * n)


# num = int(input("Enter number: "))
# pattern(num)


# CHALLENGE TASK
# def febbonacci(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return (febbonacci(num-1))+(febbonacci(num-2))


# num = int(input("Enter number: "))
# for i in range(1, num+1):
#     print(febbonacci(i), end=",")

# BONUS TASK
# def palindrome(word):
#     if len(word) <= 1:
#         return True
#     if word[0] != word[-1]:
#         return False
#     return palindrome(word[1:-1])


# word = input("Enter the word: ")
# if palindrome(word):
#     print("palindrome")
# else:
#     print("not palindrome")
