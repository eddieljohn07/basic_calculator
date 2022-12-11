import math

def calculator():
  firstNum = float(input("First Number: "))
  answer = firstNum
  operation = input("What operation would you like? (+, -, *, /, power, square root, =): ")
  while operation != "=":
    if operation == "+":
      answer = firstNum + float(input("Second Number: "))
    elif operation == "-":
      answer = firstNum - float(input("Second Number: "))
