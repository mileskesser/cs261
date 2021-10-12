# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Python Fundamentals Review
# Due Date: October 11th 2021
# Description: Assignment 1

import random
import string
from static_array import *
# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
def min_max(arr: StaticArray) -> ():
    """Takes array and returns the minimum and maximum numbers"""

    # Initializes min and max to first element in array
    minimum = arr[0]
    maximum = arr[0]

    index = 0
    while index < arr.length():

        # If next element is larger, set new max
        if arr[index] > maximum:
            maximum = arr[index]

        # If next element is smaller, set new min
        if arr[index] < minimum:
            minimum = arr[index]

        index += 1

        # If all elements evaluated, return min / max
        if index == arr.length():
            return (minimum, maximum)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
def fizz_buzz(arr: StaticArray) -> StaticArray:
    """Takes array as parameter and replaces elements divisible by 3 with 'fizz',
    elements divisible by 5 with 'buzz' and elements divisible by both 3 and 5 with 'fizzbuzz'"""

    # Initializes new array
    new_arr = StaticArray(arr.length())
    index = 0

    # Copies elements from original array to new array
    while index < arr.length():
        new_arr[index] = arr[index]
        index += 1

    for index in range(0, arr.length()):

        num = arr[index]

        # If value at index is divisible only by 3 change to 'fizz'
        if num % 3 == 0 and num % 5 != 0:
            new_arr[index] = "fizz"

        # If value at index is divisible only by 5 change to 'buzz'
        if num % 5 == 0 and num % 3 != 0:
            new_arr[index] = "buzz"

        # If value at index is divisible by both 3 and 5 change to 'fizzbuzz'
        if num % 5 == 0 and num % 3 == 0:
            new_arr[index] = "fizzbuzz"

        # If value at index is not divisible by either 3 or 5 leave element in place
        elif num % 5 != 0 and num % 3 != 0:
            new_arr[index] = num

    return new_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------
def reverse(arr: StaticArray) -> None:
    """Takes array as parameter and reverses the array in place"""

    # Initialize first and last place holders
    first = 0
    second = arr.length() - 1

    while first < second:

        # Holds first value as value, makes first value the last, makes the last value the holder value
        value = arr[first]
        arr[first] = arr[second]
        arr[second] = value

        first += 1
        second -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------
def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """Takes an array and number of steps as parameter and returns array rotated 'steps' indexes"""

    # Initializes new array and copies elements from original array to new array
    new_arr = StaticArray(arr.length())
    index = 0
    while index < arr.length():
        new_arr[index] = arr[index]
        index += 1

    # If steps is zero, no rotation needed
    if steps == 0:
        return new_arr
    elif steps > 0:
        steps = (steps % arr.length())
    else:
        steps = ((steps*-1) % arr.length())*-1 + arr.length()
    index = steps
    temp1 = new_arr[0]
    while index != 0:
        temp2 = new_arr[index]
        new_arr[index] = temp1
        temp1 = temp2
        index = (index + steps) % new_arr.length()
    new_arr[index] = temp1
    return new_arr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
def sa_range(start: int, end: int) -> StaticArray:
    """Takes two integers as a parameter and returns an array containing all
    consecutive elements in between the two"""

    # Initializes new_arr
    temp = start-end
    if temp < 0:
      temp = temp * -1
    new_arr = StaticArray(temp+1)

    # Returns start number if length is one
    index = 0
    if start == end and new_arr.length() == 1:
        new_arr[0] = start

    # If numbers go in positive direction
    elif start < end:
        while start < end + 1:

            new_arr[index] = start
            index += 1
            start += 1

    #  # If numbers go in negative direction
    elif start > end:
        while start > end - 1:

            new_arr[index] = start
            index += 1
            start -= 1

    return new_arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
def is_sorted(arr: StaticArray) -> int:
    """Takes an array as a parameter and returns a 1 if elements are in strictly
    ascending order, -1 if elements are in strictly descending order, and 0 if
    elements in array are neither in strictly ascending or descending order"""

    # Initializes ascending, descending, answer to 0, 0, and None respectively
    ascending = 0
    descending = 0
    answer = None

    index = 0
    while index < arr.length()-1:

        # Increase ascending for each pair of elements in ascending order
        if arr[index+1] > arr[index]:
            ascending += 1

        # Increase descending for each pair of elements in descending order
        if arr[index+1] < arr[index]:
            descending += 1
        index += 1

    # If ALL elements in ascending order return 1
    if ascending == arr.length()-1:
        answer = 1
    # If ALL elements in descending order return -1
    if descending == arr.length()-1:
        answer = -1
    # If ALL elements not in ascending or descending order return 0
    if ascending != arr.length()-1 and descending != arr.length()-1:
        answer = 0
    # For arrays length 1, array = ascending
    if arr.length() == 1:
        answer = 1

    return answer
# ------------------- PROBLEM 7 - SA_SORT -----------------------------------
def sa_sort(arr: StaticArray) -> None:
    """Takes an array as a parameter and sorts it in place using insertion sort"""

    index = 0
    while index < arr.length():

        # Assigns current value and creates holder variable
        current_value = arr[index]
        position = index

        # All values in array set to new holder
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1

        # Assign to new position
        arr[position] = current_value
        index += 1

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
def remove_duplicates(arr: StaticArray) -> StaticArray:
    """Takes an array as a parameter and returns an array with
    all duplicate elements removed from array"""

    # Initializes second array and copies elements from original
    array2 = StaticArray(arr.length())
    count = 1
    array2[0] = arr[0]
    index = 1
    while index < len(range(1, array2.length()))+1:
        if not arr[index] == arr[index-1]:
              count += 1
              array2[index] = arr[index]
        index += 1

    # Initializes a new array, initializes holder variables to 0
    new_array = StaticArray(count)
    final_index = 0
    temp_index = 0

    # Populates new array from second array with elements not duplicated in second array
    while temp_index < array2.length():
        if(array2[temp_index] is not None):
            new_array[final_index] = array2[temp_index]
            final_index += 1
        temp_index += 1

    return new_array
# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
def count_sort(arr: StaticArray) -> StaticArray:
    """Takes an array as a parameter and returns an array sorted in descending order"""

    # Find the min and max in array
    minimum = arr[0]
    maximum = arr[0]
    index = 0
    while index < arr.length():
        if arr[index] > maximum:
            maximum = arr[index]
        if arr[index] < minimum:
            minimum = arr[index]
        index += 1

    # Initialize new array with max+1 zeros
    new_arr = StaticArray(maximum - minimum + 1)

    i = 0
    while i < new_arr.length():
        new_arr[i] = 0
        i += 1

    # Initialize final array size of input array
    final_arr = StaticArray(arr.length())

    # For each value in input array, increase corresponding position in new_arr by 1
    temp = 0
    while temp < arr.length():
        value = arr[temp]
        new_arr[value - minimum] += 1
        temp += 1

        # Add number at index with previous number to represent next index
    num = 1
    while num < new_arr.length():
        new_arr[num] += new_arr[num - 1]
        num += 1

    index = 0
    new_arr = rotate(new_arr, 1)
    new_arr[0] = 0
    while index < arr.length():
        final_arr[new_arr[arr[index] - minimum]] = arr[index]
        new_arr[arr[index] - minimum] += 1
        index += 1

    # Reverses sorted array
    first = 0
    second = final_arr.length() - 1
    while first < second:
        # Holds first value as value, makes first value the last, makes the last value the holder value
        value = final_arr[first]
        final_arr[first] = final_arr[second]
        final_arr[second] = value

        first += 1
        second -= 1

    return final_arr



# ------------------- BASIC TESTING -----------------------------------------
if __name__ == "__main__":
    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))
    print('\n# min_max example 2')









    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))
    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))
    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)
    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)
    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)
    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3**14)
    rotate(arr, -3**15)







    print(f'Finished rotating large array of {array_size} elements')
    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))
    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)
    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')
    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)
    print('\n# count_sort example 1')







    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')
    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')
