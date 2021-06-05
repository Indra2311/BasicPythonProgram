"""
   * Author - Indrajeet
   * Date - 04-06-2021
   * Time - 12:50 PM
   * Title - Calculate the wind chill using given formula
"""

def windcill(t, v):

    if t > 50 or v > 120 or v < 30:
        if t > 50:
            return f"formula is not valid for {t} it must be greater than {t}"
        else:
            return f"formula is not valid for {v} it must be greater than {v} "
    return round((35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)), 3)


t, v = map(int, input("Enter value of t and v: ").split(","))
print(windcill(t, v))
