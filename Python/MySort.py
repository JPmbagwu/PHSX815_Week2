#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:11:17 2023

@author: johnpaulmbagwu
"""

import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

#################
# MySort class
#################
# class to sort lists of objects in different ways
class MySort:
    """A crappy sorting class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.m_random = rng.Random(seed)

    # sorts array using bubble sort
    def BubbleSort(self, array):
        n = len(array)

        for i in range(n):
            # Create a flag that will allow the function to
            # terminate early if there's nothing left to sort
            already_sorted = True

            # Start looking at each item of the list one by one,
            # comparing it with its adjacent value. With each
            # iteration, the portion of the array that you look at
            # shrinks because the remaining items have already been
            # sorted.
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    array[j], array[j + 1] = array[j + 1], array[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if already_sorted:
                break

        return array

    # sorts array using insertion sort
    def InsertionSort(self, array):
        # Loop from the second element of the array until
        # the last element
        for i in range(1, len(array)):
            # This is the element we want to position in its
            # correct place
            key_item = array[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if `key_item` is smaller than its adjacent values.
            while j >= 0 and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition j to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1

            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            array[j + 1] = key_item

        return array

    # sorts array using quicksort
    def QuickSort(self, array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        low, same, high = [], [], []

        # Select your `pivot` element randomly
        pivot = array[int(self.m_random.rand()*len(array))]

        for item in array:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
        return self.QuickSort(low) + same + self.QuickSort(high)

    # sorts array using default Python sort
    def DefaultSort(self, array):
        array.sort()

        return array