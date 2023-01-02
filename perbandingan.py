# function to compare two numbers
def compare(x, y):
  if x > y:
    print(f"{x} is greater than {y}")
  elif x < y:
    print(f"{x} is less than {y}")
  else:
    print(f"{x} is equal to {y}")

# main program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
compare(num1, num2)
