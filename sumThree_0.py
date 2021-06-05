"""
   * Author - Indrajeet
   * Date - 03-06-2021
   * Time - 6:02 PM
   * Title - Read in N integers and counts the number of triples that sum to exactly 0.
"""


def find_triples(arr, n):
    """
    :param arr: containing all the elements
    :param n: number of elements
    :return:
    """
    found = True
    count = 0
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])
                    found = True
                    count = count + 1
    print("The number of triples is: ", count)

    # If no triplet with 0 sum found in array
    if not found:
        print(" not exist ")


while True:
    try:
        array = []
        length = int(input("Enter length of array: "))
        for i in range(length):
            temp = int(input("Enter numbers: "))
            array.append(temp)
        find_triples(array, length)
        break
    except ValueError:
        print("Check the input")
