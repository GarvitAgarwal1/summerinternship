name = input("Enter the name of student: ")
cl = int(input("Enter the class of student: "))
marks1 = int(input("Enter the marks in maths: "))
marks2 = int(input("Enter the marks in science: "))
marks3 = int(input("Enter the marks in english: "))
marks4 = int(input("Enter the marks in hindi: "))
marks5 = int(input("Enter the marks in french: "))

total = marks1+marks2+marks3+marks4+marks5
percentage = (total/500)*100
print(f"Your name: {name}\nYour class: {cl}\nPercentage: {percentage}")
if percentage>=60:
    print("Your Grade: A")
elif percentage>=50 and percentage<60:
    print("Your Grade: B")
elif percentage>=40 and percentage<50:
    print("Your Grade: C")
elif percentage>=33 and percentage<40:
    print("Your Grade: D")
else:
    print("You are Fail.")