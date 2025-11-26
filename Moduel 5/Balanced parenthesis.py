def areBracketsBalanced(expr):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in expr:
        # if it's an opening bracket → push
        if ch in "([{":
            stack.append(ch)
        # if it's a closing bracket → stack must not be empty
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    # finally stack must be empty
    return len(stack) == 0

# Driver Code

expr = input()

	# Function call
if areBracketsBalanced(expr):
    print("true")
else:
	print("false")