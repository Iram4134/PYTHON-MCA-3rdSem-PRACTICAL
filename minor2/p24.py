n1=int (input("Enter first number:"))
n2=int (input("Enter second number:"))

try:
   result=n1/n2
   print("The result is", result)
except ZeroDivisionError:
   print("Error: Division by zero is not allowed.")