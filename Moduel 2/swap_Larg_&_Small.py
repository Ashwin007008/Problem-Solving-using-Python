"""
You are given an array of integers. Your task is to write a program to swap the largest and smallest element in the array.

Input:

The first line contains an integer n, the size of the array.
The second line contains n space-separated integers, representing the elements of the array.
Output:

Print the modified array after swapping the largest and smallest elements.
Example 1:

Input:

5  
10 2 3 4 1  
Output:

1 2 3 4 10
Explanation:

The largest element (10) and smallest element (1) are swapped in the array.
Example 2:

Input:

6  
15 8 20 5 10 3  
Output:

15 8 3 5 10 20
Explanation:

The largest element (20) and smallest element (3) are swapped in the array.
"""

# Use print() to print to the console
# Read input values
n = int(input())                                   # Size of the array
arr = list(map(int, input().split()))              # Array elements

# Find index of smallest and largest elements
min_index = arr.index(min(arr))                    # Index of smallest element
max_index = arr.index(max(arr))                    # Index of largest element

# Swap them

arr[min_index], arr[max_index] = arr[max_index], arr[min_index] 
"""
what is happened in the below line of code?
Index:  0   1  2  3  4
Array: [10, 2, 3, 4, 1]
        ↑           ↑
     max_index   min_index
"""
# Python creates a temporary tuple on the right side
# temp = (arr[max_index], arr[min_index])  # temp = (10, 1)
# Then it unpacks the tuple into the left side
# arr[min_index], arr[max_index] = temp
# This effectively swaps the values at min_index and max_index

# Print the modified array
print(*arr)
