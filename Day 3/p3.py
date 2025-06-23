num = int(input("Enter a number: "))
num1 = num
rev = 0
while num1 > 0:
    digit = num1 % 10
    rev = rev * 10 + digit
    num1 = num1 // 10
if num == rev:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")