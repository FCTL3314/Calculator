

def main():
    user_choice = int(input('1. Plus\n2.Minus\n3.Multiply\n4.Divide\nChoose the desired action: '))
    if user_choice == 1:
        print(plus(float(input('Enter the first number: ')), float(input('Enter the second number: '))))
    elif user_choice == 2:
        print(minus(float(input('Enter the first number: ')), float(input('Enter the second number: '))))
    elif user_choice == 3:
        print(multiply(float(input('Enter the first number: ')), float(input('Enter the second number: '))))
    elif user_choice == 4:
        print(divide(float(input('Enter the first number: ')), float(input('Enter the second number: '))))


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


main()
