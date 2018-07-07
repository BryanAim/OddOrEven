# Ask the user for a number. Depending on whether the number is even or odd, print
#     out the appropriate message to the user.

inputNumber = int(input("Enter a number: "))
inputNumber %= 2
if inputNumber == 0:
    print("That's an Even number!")
else:
    print("That's an Odd number!")