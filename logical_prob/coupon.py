"""
   * Author - Indrajeet
   * Date - 05-06-2021
   * Time - 9:50 AM
   * Title - Generate distinct coupon number
"""
import random


def generate_coupon():
    chr_arr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    permission = True
    while permission:
        coupon = ''
        grant = input("Grant me a permission 'Yes' or 'No': ").lower()
        if grant == "yes":
            while len(coupon) < 5:
                new_rand = random.choice(chr_arr)
                if new_rand in coupon:
                    continue
                coupon += new_rand
            print(coupon)
        else:
            permission = False
            print("permission granted FAIL !")
            return


generate_coupon()
