"""
   * Author - Indrajeet
   * Date - 04-06-2021
   * Time - 9:50 AM
   * Title - Print 2 Dimensional array
"""


def array_(row, col):
    """
    :param row: denotes number of rows
    :param col: denotes number of columns
    """
    try:
        array = []
        for i in range(row):
            _array = []
            for j in range(col):
                number = int(input("Enter any number: "))
                _array.append(number)
            array.append(_array)
        print(array)
    except IndexError:
        print("Index error please check ")


row = int(input("Enter number of rows: "))
if row <= 0 or row >= 100:
    print("Enter valid input for row")
col = int(input("Enter number of cols: "))
if col <= 0 or col >= 100:
    print("Enter valid input for col")
array_(row, col)
