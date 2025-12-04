def sum_of_subarrays(arr, k):      # function to calculate sum of all contiguous subarrays of size k
    n = len(arr)                          # length of the array
    window_sum = sum(arr[:k])             # sum of the first window
    print(window_sum, end=' ')            # print the sum of the first window
    for i in range(k, n):                 # slide the window from start to end of the array
        window_sum += arr[i] - arr[i - k] # update the window sum
        print(window_sum, end=' ')        # print the updated window sum

if __name__ == "__main__":                # main function
    n, k = map(int, input().split())      # read n and k
    arr = list(map(int, input().split())) # read the array
    sum_of_subarrays(arr, k)              # call the function to calculate sum of subarrays