def binarySearch(array, x, low, high):              #function to perform binary search
    while low <= high:                              #while low index is less than or equal to high index
        mid = (low + high) // 2                     #find mid index
        if array[mid] == x:                         #if element is found
            return mid                              #return index of the element
        elif array[mid] < x:                        #if element is greater than mid element
            low = mid + 1                           #search in the right half
        else:                                       #if element is less than mid element
            high = mid - 1                           #search in the left half
    return -1                                        #if element is not found


N = int(input())                                     #number of elements
array = list(map(int, input().split()))[:N]                    #list of elements, [:N] to limit the list to N elements
x = int(input())                                     #element to be searched, x is the target value

result = binarySearch(array, x, 0, len(array) - 1)   #function call,0 and len(array)-1 are the low and high indices
"""0 mentions the starting index of the list and len(array)-1 mentions the last index of the list
    len(array) gives the total number of elements in the list, so len(array)-1 gives the last index of the list
    -1 is subtracted because the index starts from 0"""                                                         
                                                    

if result != -1:               #result is not -1, means element is found
    print(result)              #print index of the element
else:                          #if element is not found
    print(-1)                  #print -1
