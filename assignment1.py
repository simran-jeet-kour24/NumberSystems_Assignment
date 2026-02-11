# Problem 1: Decimal to Binary, Octal, Hexadecimal

# taking decimal number as input
num = int(input("Enter a decimal number: "))

print("Binary   :", bin(num))   # binary representation
print("Octal    :", oct(num))   # octal representation
print("Hexa     :", hex(num))   # hexadecimal representation
 


# Problem 2: Binary/Octal/Hexadecimal → Decimal

# Taking input from user as a string

num_str = input("Enter a number (binary/octal/hex): ")
num = int(num_str, 0)   
print("Decimal :", num)


 