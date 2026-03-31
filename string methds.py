# 1. Convert to uppercase
print("hello world".upper())  # 'HELLO WORLD'

# 2. Convert to lowercase
print("Python Programming".lower())  # 'python programming'

# 3. Capitalize first letter
print("hello python learners".capitalize())  # 'Hello python learners'

# 4. Title case
print("welcome to python".title())  # 'Welcome To Python'

# 5. Remove leading and trailing spaces
print(" Python String Functions ".strip())  # 'Python String Functions'

# 6. Remove only trailing spaces
print("Hello World ".rstrip())  # 'Hello World'

# 7. Remove only leading spaces
print(" Learn Python".lstrip())  # 'Learn Python'

# 8. Split into list
print("apple banana grape".split())  # ['apple', 'banana', 'grape']

# 9. Join list with space
print(" ".join(['Python', 'is', 'fun']))  # 'Python is fun'

# 10. Join list with hyphen
print("-".join(['A', 'B', 'C']))  # 'A-B-C'

# 11. Index of first occurrence
print("I love Python programming".index("Python"))  # 7

# 12. Last occurrence of 'o'
print("Hello World".rindex("o"))  # 7

# 13. Replace Java with Python
print("I love Java".replace("Java", "Python"))  # 'I love Python'

# 14. Startswith check
print("Hello World".startswith("Hello"))  # True

# 15. Endswith check
print("example.txt".endswith(".txt"))  # True

# 16. Count occurrences of 'o'
print("Hello, how are you?".count("o"))  # 3

# 17. Index of 'r'
print("programming".index("r"))  # 1

# 18. Index of 'z' (will raise ValueError)
# print("Python".index("z"))  # ValueError: substring not found

# 19. Last occurrence of 'e'
print("experience".rindex("e"))  # 8

# 20. First occurrence of 'e'
print("experience".index("e"))  # 0

# 21. Only alphabets?
print("Python".isalpha())  # True

# 22. Only digits?
print("12345".isdigit())  # True

# 23. Alphanumeric?
print("Python123".isalnum())  # True

# 24. Only spaces?
print(" ".isspace())  # True

# 25. Numeric check
print("12345".isnumeric())  # True

# 26. Using format()
print("{} is {}!".format("Python", "fun"))  # 'Python is fun!'

# 27. Partition at '-'
print("python-programming-language".partition("-"))
# ('python', '-', 'programming-language')

# 28. rpartition from right
print("one-two-three".rpartition("-"))
# ('one-two', '-', 'three')

# 29. Casefold to lowercase
print("PYTHON".casefold())  # 'python'

# 30. zfill to pad with zeros
print("42".zfill(5))  # '00042'

# 31. Is uppercase?
print("HELLO".isupper())  # True

# 32. Is lowercase?
print("hello".islower())  # True

# 33. Title case check
print("Python Programming".istitle())  # True

# 34. Sort characters alphabetically
print("".join(sorted("banana")))  # 'aaabnn'

# 35. Length of string
print(len("Data Science"))