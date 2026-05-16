# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = 0

if operator == "+":
  result = round((num1 + num2), 3)
elif operator == "-":
  result = round((num1 - num2), 3)
elif operator == "*":
  result = round((num1 * num2), 3)
elif operator == "/":
  result = round((num1 / num2), 3)
else:
  print(f"Please input a valid operator! The {operator} is invalid!")

print(f"Here is the result: {result}")