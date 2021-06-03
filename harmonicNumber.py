"""
   * Author - Indrajeet
   * Date - 02/06/2021
   * Time - 07:15
   * Title - Harmonic Number
"""


# n th n^\text{th}


def harmonic(num):
    if num <= 0:
        print(f"you entered: {num}, but number must be greater than 0")
        return
    i = 1
    total = 0
    while i <= num:
        print(f"1/{i}")
        total += 1 / i
        i += 1
    print(f"here is harmonic of your number {total}")


harmonic(int(input("Enter the number to find harmonic: ")))