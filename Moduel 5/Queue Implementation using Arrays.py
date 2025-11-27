queue = []   # initialize empty queue
front = -1   # initialize front pointer
rear = -1    # initialize rear pointer

def is_empty():                           # check if queue is empty
    return front == -1 and rear == -1  # return true if empty, false otherwise

def enqueue(item):              # add an item to the queue
    global front, rear          # declare front and rear as global variables
    if is_empty():              # if queue is empty
        front = rear = 0        # set front and rear to 0
    else:                       # if queue is not empty
        rear += 1               # increment rear pointer
    queue.append(item)          # add item to the queue

def dequeue():                   # remove and return an item from the queue
    global front, rear           # declare front and rear as global variables
    if is_empty():               # if queue is empty
        return -1                # return -1
    item = queue[front]          # get the front item
    front += 1                   # increment front pointer
    if front > rear:             # if queue becomes empty after dequeue
        front = rear = -1        # reset front and rear pointers
    return item                  # return the dequeued item

def peek():                      # get the front item without removing it
    if is_empty():               # if queue is empty
        return -1                # return -1
    return queue[front]          # return the front item

# Enqueue items
n = int(input())  # number of items to enqueue
arr = list(map(int, input().split()))[:n] # read n items
for i in range(n):  # loop through each item
    enqueue(arr[i]) # enqueue the item

# Dequeue items
while not is_empty():  # while queue is not empty
    print(dequeue())   # dequeue and print each item