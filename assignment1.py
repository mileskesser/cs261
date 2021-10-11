# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Python Fundamentals Review
# Due Date: October 11th 2021
# Description:

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
            return (min, max)

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
    left = 0
    right = arr.length() - 1

    while left < right:

        # Holds first value as value, makes first value the last, makes the last value the holder value
        value = arr[left]
        arr[left] = arr[right]
        arr[right] = value

        left += 1
        right -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------
"""def rotate(arr: StaticArray, steps: int) -> StaticArray:
    Takes an array and number of steps as parameter and returns array rotated 'steps' indexes

    # Initializes new array and copies elements from original array to new array
    new_arr = StaticArray(arr.length())
    index = 0
    while index < arr.length():
        new_arr[index] = arr[index]
        index += 1

    # If steps is zero, no rotation needed
    if steps == 0:
        new_arr = arr

    # If steps is negative, move elements to the left
    if steps < 0:
        if steps % arr.length() == 0:
            steps = arr.length()
        else:
            steps = (steps % arr.length()) * -1
            '''new_arr = arr[steps:] + arr[:steps]
            index = 0
            for value in arr[steps:]:
                new_arr[index] = value
                index += 1

            for value in arr[:steps]:
                new_arr[(arr.length()) - steps] = value
                steps -= 1'''

    # If steps is positive, move elements to the right
    if steps > 0:
        if steps % arr.length() == 0:
            steps = arr.length()
        else:
            steps = steps % arr.length()
            '''new_arr = arr[-steps:] + arr[:-steps]
            index = 0
            for value in arr[-steps:]:
                new_arr[index] = value
                index += 1

            i = steps
            for value in arr[:(arr.length()) - (steps)]:
                new_arr[i] = value
                i += 1'''
    return new_arr"""

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
"""def sa_range(start: int, end: int) -> StaticArray:
    Takes two integers as a parameter and returns an array containing all
    consecutive elements in between the two

    
    count = 0
    while count < len(range(start, end)):
        count += 1
    new_arr = StaticArray(count+1)

    index = 0
    if start == end and new_arr.length() == 1:
        new_arr[0] = start

    if end > start:
        while start < end + 1:
            new_arr[index] = start
            index += 1
            start += 1

    if end < start:
        while start > end - 1:
            new_arr[index] = start
            index += 1
            start -= 1

    return new_arr"""


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

        currentValue = arr[index]
        position = index

        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = currentValue
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
        if(not arr[index] == arr[index-1]):
              count += 1
              array2[index] = arr[index]
        index += 1

    # Initializes a new array, initializes holder variables to 0
    new_array = StaticArray(count)
    final_index = 0
    temp_index = 0

    # populates new array from second array with elements not duplicated in second array
    while temp_index < array2.length():
        if(array2[temp_index] is not None):
            new_array[final_index] = array2[temp_index]
            final_index += 1
        temp_index += 1

    return new_array
# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
def count_sort(arr: StaticArray) -> StaticArray:
    """Takes an array as a parameter and returns an array sorted in descending order"""

    # Initializes new array and copies elements from original array
    new_arr = StaticArray(arr.length())
    index = 0
    while index < arr.length():
        new_arr[index] = arr[index]
        index += 1

    index = 0
    while index < arr.length():

        # Sorts elements in array in ascending order using insertion sort
        currentValue = new_arr[index]
        position = index

        while position > 0 and new_arr[position-1] > currentValue:
            new_arr[position] = new_arr[position-1]
            position = position-1

        new_arr[position] = currentValue
        index += 1

    # Initializes final array with elements from new array
    final_arr = StaticArray(arr.length())
    index = 0
    while index < arr.length():
        final_arr[index] = new_arr[index]
        index += 1

    # Reverses order of sorted array in descending order
    n = 0
    l = arr.length()-1
    while n < arr.length():
        final_arr[n] = new_arr[l]
        n += 1
        l -= 1

    return final_arr

