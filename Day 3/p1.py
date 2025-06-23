print("----- Dictionary -----")
student = {"name": "Ravi","age": 21,"branch": "CSE"}
print("Student Dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
student["college"] = "SKIT"
student["age"] = 22
print("Updated Dictionary:", student)
print("----- Tuple -----")
colors = ("red", "green", "blue", "green")
print("Colors Tuple:", colors)
print("First color:", colors[0])
print("Count of 'green':", colors.count("green"))
print("Index of 'blue':", colors.index("blue"))
print("----- Set -----")
fruits = {"apple", "banana", "apple", "mango", "orange"}
print("Fruits Set:", fruits)
fruits.add("grape")
fruits.discard("banana")
print("Updated Set:", fruits)