# LargeSmall.py - This program calculates the largest and smallest of three integer values.
# Declare and initialize variables here

firstNumber = input("type first number here")
secondNumber = input("type second number here")
thirdNumber = input("type third number here")

largest = None
smallest = None
third = None

if firstNumber >secondNumber:
    if firstNumber > secondNumber:
        if firstNumber > thirdNumber:
            largest = firstNumber
elif secondNumber > thirdNumber:
             if secondNumber > firstNumber:
                 largest = thirdNumber
else:
      largest = thirdNumber

if firstNumber < secondNumber:
    if firstNumber < thirdNumber:
        smallest = firstNumber
elif secondNumber < thirdNumber:
      if secondNumber < firstNumber:
           largest = thirdNumber
else:

    print("The largest value is " + str(largest))
    print("The smallest value is " + str(smallest))
