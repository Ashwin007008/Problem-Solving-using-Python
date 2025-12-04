def find_middle_element(arr):  # function to find the middle element of the array
    slow, fast = 0, 0               # initialize two pointers
    while fast + 2 < len(arr):  # loop until fast pointer reaches the end
        slow += 1               # move slow pointer by 1
        fast += 2               # move fast pointer by 2
    return arr[slow]           # return the middle element

N = int(input())                    # read number of elements
arr = list(map(int, input().split()))  # read the array elements
print(find_middle_element(arr))    # print the middle element of the array