from collections import deque  # import deque for queue implementation

def modifyQueue(q, k):   # function to reverse first K elements of the queue
    stack = []  # initialize empty stack
    # Step 1: Pop first K elements from queue and push onto stack
    for _ in range(k):   # loop K times, where K is the number of elements to reverse
                         #why use _ ? because we don't need the loop variable
                         # we just need to repeat the action K times
                         #why because we don't need the loop variable, we just need to repeat the action K times
        stack.append(q.popleft())
    # Step 2: Push stack elements back to queue (reversed order)
    while stack:
        q.appendleft(stack.pop())  # push elements from stack back to queue
                                   # appendleft is used to add elements to the front of the deque, which helps in reversing the order
                                   # since we are popping from stack (LIFO), the last element pushed onto stack will be the first to be added back to the queue
                                   # this effectively reverses the order of the first K elements in the queue
    # Step 3: Move the reversed K elements to the rear to restore order
    q.rotate(-k) # rotate the queue to move the first K elements to the rear, maintaining the order of the remaining elements
                    # rotate(-k) shifts the elements to the left by K positions
    return q

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    q = deque(map(int, data[2:2+N]))
    result = modifyQueue(q, K)
    print(' '.join(map(str, result)))