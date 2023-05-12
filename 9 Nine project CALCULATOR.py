from replit import clear
from art import logo


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multioly(num1, num2):
    return num1 * num2


def devide(num1, num2):
    return num1 / num2


def sqrt(num1, num2):
    return num1 ** num2


operations = {
    '+': add,
    '-': subtract,
    '*': multioly,
    '/': devide,
    '**': sqrt
}


def calcutalor():
  print(logo)

  num_one = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  should_end = False

  while not should_end:
    #First operation
    operations_symbol = input("Pick the operation from the line above: ")
    num_two = float(input("What's the second number?: "))
    calculating_function = operations[operations_symbol]
    answer = calculating_function(num_one, num_two)

    print(f"{num_one} {operations_symbol} {num_two} = {answer}")

    #Next operations
    if input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: "
    ) == 'y':
      num_one = answer
    else:
      should_end = True
      clear()
      calcutalor()


calcutalor()
