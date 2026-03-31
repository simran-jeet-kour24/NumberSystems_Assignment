# 1. String Reverse
def reverse_string():
    s = input("Enter string: ")
    print("Reversed String:", s[::-1])

reverse_string()


# 2. Number Reverse
def reverse_number():
    n = int(input("Enter number: "))
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print("Reversed Number:", rev)

reverse_number()


# 3. Count Characters
def count_characters():
    s = input("Enter string: ")
    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    print("Character Count:", count)

count_characters()


# 4. Sum of Digits
def sum_of_digits():
    n = int(input("Enter number: "))
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    print("Sum of Digits:", total)

sum_of_digits()


# 5. Palindrome
def palindrome():
    s = input("Enter string: ")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome()


# 6. Prime Number
def prime():
    n = int(input("Enter number: "))
    if n <= 1:
        print("Not Prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime Number")

prime()


# 7. Right Triangle
def right_triangle():
    n = int(input("Enter rows: "))
    for i in range(1, n + 1):
        print("*" * i)

right_triangle()


# 8. Inverted Triangle
def inverted_triangle():
    n = int(input("Enter rows: "))
    for i in range(n, 0, -1):
        print("*" * i)

inverted_triangle()


# 9. While Loop
def while_loop():
    i = 1
    while i <= 5:
        print(i)
        i += 1

while_loop()


# 10. For Loop
def for_loop():
    for i in range(1, 6):
        print(i)

for_loop()


# 11. Division
def division():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)

division()