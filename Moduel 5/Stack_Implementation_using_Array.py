def push(stack, x, s):  # Push element x onto stack of size s
    # If stack is full
    if len(stack) == s:    # Check if stack size has reached maximum
        print("stack overflow")    # Print overflow message
        return
    stack.append(x)       # Add element to stack


def pop(stack):           
    # If stack is empty
    if len(stack) == 0:
        print("stack underflow")    # Print underflow message
        return
    print(stack.pop())    # Remove and print top element from stack 


def top(stack):  
    # If stack is empty
    if len(stack) == 0:
        print("stack underflow")    # Print underflow message
        return
    print(stack[-1])    # Print top element of stack
    pass

def main():
    # Read number of operations and maximum stack size
    N, S = map(int, input().split())    # Read N and S
    
    stack = [] # Initialize empty stack
    
    for _ in range(N):    # Loop through each operation
        operation = input().strip()        # Read operation
        
        if operation.startswith("push"):     # Check if operation is push
            _, x = operation.split()
            push(stack, int(x), S)
        elif operation == "pop":    # Check if operation is pop
            pop(stack)  
        elif operation == "top":    # Check if operation is top
            top(stack)

if __name__ == "__main__":
    main()