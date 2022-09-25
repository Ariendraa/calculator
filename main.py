import os


os.system("cls")
print("Welcome")

while True:
    firstNumber = float(input("Enter a number: "))
    operation = input("What you choose? Addition, subtraction, division, multiplication?: ")
    secondNumber = float(input("Enter the another number: "))

    if operation == "addition" or operation == "+":
        print(f"The result is: {firstNumber + secondNumber}")
    elif operation == "subtraction" or operation == "-":
        print(f"The result is: {firstNumber - secondNumber}")
    elif operation == "division" or operation == "/":
        print(f"The result is: {firstNumber / secondNumber}")
    elif operation == "multiplication" or operation == "*":
        print(f"The result is: {firstNumber * secondNumber}")

    isContinue = input("\nDo you want to do it again? y/n: ")
    if isContinue == "n":
        print("\nEnd of program :)\n")
        break
