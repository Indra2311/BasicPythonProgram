"""
   * Author - Indrajeet
   * Date - 01/06/2021
   * Time - 03:43
   * Title - User Input and Replace String Template
"""


def greetings(user_name):
    char_length = len(user_name)
    if char_length < 3:
        print(char_length)
        print("Name must have a min val of 3 char: ")
        return
    print(f"Hello {user_name} , how are you ?")


greetings(input("Enter the user name: "))