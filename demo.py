
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")


print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")

# For loop examples
print("\n=== For Loop Examples ===")

# 1. Basic for loop with range
print("1. Basic for loop with range:")
for i in range(5):
    print(f"Count: {i}")

# 2. For loop with list
print("\n2. For loop with list:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# 3. For loop with enumerate (get index and value)
print("\n3. For loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 4. For loop with dictionary
print("\n4. For loop with dictionary:")
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# 5. For loop with string
print("\n5. For loop with string:")
for char in "Python":
    print(f"Character: {char}")

# 6. For loop with step
print("\n6. For loop with step:")
for i in range(0, 10, 2):
    print(f"Even number: {i}")

# 7. Nested for loop
print("\n7. Nested for loop:")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row

