"""
   * Author - Indrajeet
   * Date - 02/06/2021
   * Time - 09:22
   * Title - Prime Factors
"""


def prime_factor(n):
    try:
        n = int(n)
        if n < 0:
            print(f"{n} is negative ,so its prime factor is not possible")
            return
        elif n == 0 or n == 1:
            print(n)
            return
        while n % 2 == 0:
            print(2)
            n = n / 2
        for i in range(3, int((n ** 0.5)) + 1, 2):
            while n % i == 0:
                print(i)
                n = n / i
        if n > 2:
            print(int(n))
    except ValueError:
        print(f"Prime factor is not possible for {type(n)} ")


while True:
    n = input("enter value to find prime factor: ")
    if n == "0":
        break
    prime_factor(n)