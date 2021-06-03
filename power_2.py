"""
   * Author - Indrajeet
   * Date - 01/06/2021
   * Time - 06:25
   * Title - Power of 2
"""


def power_2(n):
    if n > 30:
        print("since 2^31 overflows an int, So enter number less than 31")
        return
    i = 1
    while i < n:
        print(f"{i} power is: {2 ** i}")
        i += 1


power_2(int(input("Enter number: ")))
