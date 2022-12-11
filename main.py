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
    elif operation == "*":
      answer = firstNum * float(input("Second Number: "))
    elif operation == "/":
      answer = float(firstNum) / float(input("Second Number: "))
    elif operation == "power":
      answer = math.pow(firstNum, float(input("Second Number: ")))
    elif operation == "square root":
      answer = math.sqrt(firstNum)
    firstNum = answer
    operation = input("Enter the operator (+, -, *, /, power, square root, =): ")
  return answer
