def two_sum(nums, target):                     # function to find two indices such that their values sum to target
    left = 0                                   # initialize left pointer
    right = len(nums) - 1                      # initialize right pointer
    while left < right:                        # loop until pointers meet
        s = nums[left] + nums[right]           # calculate sum of values at pointers
        if s == target:                        # check if sum equals target
            return [left, right]               # return the indices if found
        elif s < target:                       # if sum is less than target
            left += 1                          # move left pointer to the right
        else:
            right -= 1                          # move right pointer to the left
    return [-1]                                 # If no pair found, return -1

n = int(input())                                # read number of elements
arr = list(map(int, input().split()))           # read the elements
target = int(input())                           # read the target sum

result = two_sum(arr, target)                   # call the function to find indices
print(*result)                                  # print the result