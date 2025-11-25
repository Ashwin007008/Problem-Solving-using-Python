def push(stack, x, s):
    # If stack is full
    if len(stack) == s:
        print("stack overflow")
        return
    stack.append(x)


def pop(stack):
    # If stack is empty
    if len(stack) == 0:
        print("stack underflow")
        return
    print(stack.pop())


def top(stack):
    # If stack is empty
    if len(stack) == 0:
        print("stack underflow")
        return
    print(stack[-1])
    pass

def main():
    # Read number of operations and maximum stack size
    N, S = map(int, input().split())
    
    stack = []
    
    for _ in range(N):
        operation = input().strip()
        
        if operation.startswith("push"):
            _, x = operation.split()
            push(stack, int(x), S)
        elif operation == "pop":
            pop(stack)
        elif operation == "top":
            top(stack)

if __name__ == "__main__":
    main()