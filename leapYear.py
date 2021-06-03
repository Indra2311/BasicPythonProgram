"""
   * Author - Indrajeet
   * Date - 01/06/2021
   * Time - 05:43
   * Title - Leap Year
"""


def leap(user_year):
    if user_year < 1000:
        print(
            f"your entered year is {user_year} that is not a four digit number.")
        return
    if user_year % 400 == 0 or user_year % 4 == 0 and user_year % 100 != 0:
        print(f"yes, {user_year} is a leap year ")
    else:
        print(f"NO, {user_year} is not a leap year")


leap(int(input("Enter Year: ")))
