"""
Python Essentials — A mid-level developer's reference guide.
No external libraries required; uses only built-in functionality.
Run this file to see everything in action:  python test.py
"""

# ──────────────────────────────────────────────
# 1. Variables & Data Types
# ──────────────────────────────────────────────

name = "Alice"           # str
age = 30                 # int
height = 5.9             # float
is_active = True         # bool
nothing = None           # NoneType
my_list = [1, 2, 3]     # list  (mutable)
my_tuple = (4, 5, 6)    # tuple (immutable)
my_dict = {"a": 1, "b": 2}  # dict  (key-value pairs)
my_set = {7, 8, 9}      # set   (unique values)

print(f"Types: {type(name)}, {type(age)}, {type(height)}")


# ──────────────────────────────────────────────
# 2. String Operations & Formatting
# ──────────────────────────────────────────────

greeting = "Hello, World!"
print(greeting.lower())        # hello, world!
print(greeting.upper())        # HELLO, WORLD!
print(greeting.strip())        # removes whitespace
print(greeting.split(","))     # ['Hello', ' World!']
print(greeting.replace("World", "Python"))

# Formatting (multiple ways — f-strings are preferred)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old")          # f-string
print("My name is {} and I am {} years old".format(name, age))  # .format() (older style — noqa)
print("My name is %s and I am %d years old" % (name, age))     # %-style (legacy format — noqa)

# Multi-line strings
poem = """Roses are red,
Violets are blue,
Python is awesome,
So is this guide."""
print(poem)


# ──────────────────────────────────────────────
# 3. Lists & Tuples
# ──────────────────────────────────────────────

numbers = [10, 20, 30, 40, 50]

# Indexing & slicing
print(numbers[0])    # 10
print(numbers[-1])   # 50 (last element)
print(numbers[1:4])  # [20, 30, 40] — start inclusive, end exclusive
print(numbers[::2])  # [10, 30, 50] — every second element

# Appending & modifying
numbers.append(60)   # add to end
numbers.insert(1, 15)  # insert at index
numbers.extend([70, 80])  # bulk add
popped = numbers.pop()  # remove & return last → 80
removed = numbers.pop(2)  # remove at index 2 → 30
print(f"Numbers: {numbers}")

# Tuples are immutable — used for fixed collections
point = (3, 4)
x, y = point       # unpacking
print(f"Point: ({x}, {y})")


# ──────────────────────────────────────────────
# 4. Dictionaries & Sets
# ──────────────────────────────────────────────

student = {
    "name": "Alice",
    "age": 30,
    "grades": [85, 92, 78],
}

# Accessing with safe fallback
grade_average = student.get("average", None)  # returns None if key missing
student["average"] = grade_average or sum(student["grades"]) / len(student["grades"])

# Iterating
for key, value in student.items():
    print(f"  {key}: {value}")

# Adding & removing entries
student["email"] = "alice@example.com"
del student["age"]

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Union:     {set_a | set_b}")    # {1, 2, 3, 4, 5, 6}
print(f"Intersection:{set_a & set_b}")  # {3, 4}
print(f"Difference:  {set_a - set_b}")   # {1, 2}


# ──────────────────────────────────────────────
# 5. Control Flow
# ──────────────────────────────────────────────

# If / Elif / Else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} → Grade: {grade}")

# Ternary expression (inline if/else)
status = "pass" if score >= 60 else "fail"
print(f"Status: {status}")

# For loops
print("Range loop:", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# Enumerate — index + value
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")

# While loop
count = 0
while count < 3:
    count += 1
print(f"\nWhile loop ran {count} times")

# break / continue
print("Prime numbers up to 20:", end=" ")
for num in range(2, 21):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num, end=" ")
print()


# ──────────────────────────────────────────────
# 6. Comprehensions (List, Dict, Set)
# ──────────────────────────────────────────────

# List comprehension — [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 11)]
evens = [x for x in squares if x % 2 == 0]
print(f"\nSquares:  {squares}")
print(f"Evens:    {evens}")

# Dict comprehension — {key: value for ...}
word_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Word lengths: {word_lengths}")

# Set comprehension — unique results
vowels_in_words = {ch.lower() for word in fruits for ch in word if ch.lower() in "aeiou"}
print(f"Vowels found: {vowels_in_words}")


# ──────────────────────────────────────────────
# 7. Functions
# ──────────────────────────────────────────────

def greet(name, greeting="Hello"):
    """Basic function with default arguments."""
    return f"{greeting}, {name}!"

print(greet("Alice"))       # Hello, Alice!
print(greet("Bob", "Hi"))   # Hi, Bob!


def add_all(*args):
    """Accepts arbitrary positional arguments → tuple."""
    return sum(args)

print(f"Sum: {add_all(1, 2, 3, 4, 5)}")


def describe(**kwargs):
    """Accepts arbitrary keyword arguments → dict."""
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

describe(name="Alice", role="Engineer", city="NYC")


# Lambda (anonymous inline function)
double = lambda x: x * 2
print(f"\nLambda example — double(7): {double(7)}")

# Using map / filter / sorted with lambdas
numbers = [5, 2, 8, 1, 9]
print(f"Filtered (even): {list(filter(lambda x: x % 2 == 0, numbers))}")
squared = list(map(lambda x: x ** 2, numbers))
print(f"Mapped (squared): {squared}")
print(f"Sorted (desc):    {sorted(numbers, reverse=True)}")


# ──────────────────────────────────────────────
# 8. Classes & OOP
# ──────────────────────────────────────────────

class Animal:
    """Base class with inheritance."""

    species = "Unknown"  # class-level attribute (shared across instances)

    def __init__(self, name: str, age: int):
        self.name = name      # instance attribute — public
        self._age = age       # conventionally protected

    def speak(self) -> str:
        return f"{self.name} makes a sound"

    @property
    def age(self):            # getter (can also have setter/deleter)
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def __str__(self):        # human-readable string representation
        return f"Animal({self.name}, {self._age})"

    def __repr__(self):       # developer-facing representation
        return f"Animal(name={self.name!r}, age={self.age})"


class Dog(Animal):           # inheritance — Dog IS-A Animal
    species = "Canine"

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)   # call parent constructor
        self.breed = breed

    def speak(self) -> str:          # method override (polymorphism)
        return f"{self.name} says Woof!"


class Cat(Animal):
    species = "Feline"

    def speak(self) -> str:
        return f"{self.name} says Meow!"


# Instantiation & polymorphism
animals = [Dog("Rex", 5, "Labrador"), Cat("Whiskers", 3)]
for animal in animals:
    print(f"  {animal} → {animal.speak()}")

dog = Dog("Buddy", 4, "Poodle")
print(f"\nDog repr: {dog!r}")
print(f"Dog str:  {dog!s}")
print(f"Dog age getter: {dog.age}")
# dog.age = -1  # raises ValueError — demonstrates property setter


# ──────────────────────────────────────────────
# 9. Error Handling (Exceptions)
# ──────────────────────────────────────────────

def divide(a, b):
    """Demonstrates try / except / else / finally."""
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"  Cannot divide {a} by zero → {e}")
        return None
    except TypeError as e:
        print(f"  Invalid types → {e}")
        return None
    else:
        # runs only if no exception occurred
        print(f"  {a} / {b} = {result}")
        return result
    finally:
        # always runs — great for cleanup
        print(f"  Division attempt finished (a={a}, b={b})")


print("\nError handling:")
divide(10, 2)
divide(10, 0)
divide("10", 2)

# Raising custom exceptions
def validate_age(age):
    if age < 0:
        raise ValueError(f"Invalid age: {age}")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"\nCaught ValueError: {e}")


# ──────────────────────────────────────────────
# 10. File I/O (Read & Write)
# ──────────────────────────────────────────────

OUTPUT_FILE = "output_demo.txt"

# Writing a file — uses context manager (with statement) for safety
print(f"\nWriting to {OUTPUT_FILE}…")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("Hello from Python!\n")
    f.write("Line 2\n")
    f.writelines(["Line 3\n", "Line 4\n"])

# Reading a file
print(f"Contents of {OUTPUT_FILE}:")
with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Reading line by line
print("Reading line by line:")
with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        print(f"  → {line.strip()}")

# Appending to a file
with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    f.write("Appended line\n")


# ──────────────────────────────────────────────
# 11. Context Managers (Custom __enter__ / __exit__)
# ──────────────────────────────────────────────

class Timer:
    """A simple context manager to measure elapsed time."""

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"\nElapsed: {elapsed:.4f} seconds")
        # Returning False lets exceptions propagate; True swallows them.
        return False

with Timer():
    import time
    time.sleep(0.1)  # simulate work


# ──────────────────────────────────────────────
# 12. Generators (Lazy Evaluation)
# ──────────────────────────────────────────────

def fibonacci(n):
    """Yields the first n Fibonacci numbers — generator function."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(f"\nFirst 10 Fibonacci numbers: {list(fibonacci(10))}")

# Generator expression (similar to list comprehension but lazy)
squares_gen = (x**2 for x in range(10))
print(f"Next square from generator: {next(squares_gen)}")


# ──────────────────────────────────────────────
# 13. Modules & Imports (stdlib only)
# ──────────────────────────────────────────────

import datetime
import json
import math
import os
import random
import sys

print("\nStdlib examples:")
print(f"  Current dir:      {os.getcwd()}")
print(f"  Python version:   {'.'.join(map(str, sys.version_info[:3]))}")
json_str = '{"x": 42}'
print(f"  JSON parse:       {json.loads(json_str)}")
print(f"  Now:              {datetime.datetime.now(tz=datetime.timezone.utc)}")
print(f"  Pi to 4 decimal:  {math.pi:.4f}")
print(f"  Random int:       {random.randint(1, 100)}")


# ──────────────────────────────────────────────
# 14. Operator Quick Reference
# ──────────────────────────────────────────────

a, b = 10, 3
print(f"\nOperators — a={a}, b={b}:")
print(f"  +   {a} + {b} = {a + b}")        # addition
print(f"  -   {a} - {b} = {a - b}")        # subtraction
print(f"  *   {a} * {b} = {a * b}")        # multiplication
print(f"  /   {a} / {b} = {a / b:.2f}")    # float division
print(f"  //  {a} // {b} = {a // b}")      # integer division
print(f"  %   {a} % {b} = {a % b}")        # modulo
print(f"  **  {a} ** {b} = {a ** b}")      # exponentiation
print(f"  ==  {a} == {b}: {a == b}")       # equality
print(f"  !=  {a} != {b}: {a != b}")       # not equal
and_result = False
or_result = True
not_result = True
eq_comparison = [] == None
print(f"  and True and False: {and_result}")
print(f"  or  True or False:  {or_result}")
print(f"  not not True:       {not_result}")
print(f"  [] == None:         {eq_comparison}")   # identity comparison


# ──────────────────────────────────────────────
# Done!
# ──────────────────────────────────────────────

print("\n" + "=" * 40)
print("All concepts demonstrated successfully.")
print("=" * 40)
