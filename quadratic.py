"""
    * Author - Indrajeet
   * Date - 04-06-2021
   * Time - 12:25 PM
   * Title - Print the roots of the equation a*x*x + b*x + c
"""

import math


def quad(num1, num2, num3):
    delta = num2 * num2 - 4 * num1 * num3
    print(abs(delta))
    root1 = (-num2 + math.sqrt(abs(delta))) / (2 * num1)
    root2 = (-num2 - math.sqrt(abs(delta))) / (2 * num1)
    print("root 1: ", root1)
    print("root 2 : ", root2)


try:
    number1 = int(input("enter number 1 :"))
    if number1 <= 0 or number1 >= 1000:
        print("enter between 0 and 1000")
    number2 = int(input("enter number 2 :"))
    if number2 <= 0 or number2 >= 1000:
        print("enter between 0 and 1000")
    number3 = int(input("enter number 3 :"))
    if number3 <= 0 or number3 >= 1000:
        print("enter between 0 and 1000")
    quad(number1, number2, number3)
except ValueError:
    print("Please enter numbers in valid range.")