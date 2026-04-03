def greet(name):
    print(f"Hello, {name}!")

greet("World")
greet(69)
print("\n")


# Function with a return value
def add(a,b):
    return a + b

result = add(5,10)
print(result)
print("\n")


# Function with Logic
def result_check(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(result_check(95))
print(result_check(85))
print("\n")


# Function involving words (Text Handling)
name = "Dinesh"
print(name.upper())
print(name.lower())
print(len(name))
print("\n")

# Function with loop
mark = [90, 85, 78, 92, 8]

for m in mark:
    print(result_check(m))

# FUnction with spliting the words
sentence = "Hello World, welcome to Python programming"
words = sentence.split()
print(words)
print(len(words))
print("\n")


# Task1 : Square of a number
# Task2 : Upper case of a list of words
# Task3 : Count the number of words in a sentence

# Task1

def square(num):
    return num * num
print(square(5))
print("\n")

# Task2
names = ["dinesh", "kumar", "ai"]

upper_names = [name.upper() for name in names]
print(upper_names)
print()

# Task3
sentence = "python is very powerful"
print(len(sentence.split()))