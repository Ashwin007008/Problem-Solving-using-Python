def areBracketsBalanced(expr):     # function to check if brackets are balanced
    stack = []                      # initialize empty stack
    pairs = {')':'(', ']':'[', '}':'{'}         # mapping of closing to opening brackets

    for ch in expr:           # iterate through each character in the expression
        # if it's an opening bracket → push
        if ch in "([{":          # check if character is an opening bracket
            stack.append(ch)     # push opening bracket onto stack
        # if it's a closing bracket → stack must not be empty
        elif ch in ")]}":     # check if character is a closing bracket
            if not stack or stack[-1] != pairs[ch]:   # check for matching opening bracket
                return False     # return false if not matched
            stack.pop()       # pop the matched opening bracket from stack

    # finally stack must be empty
    return len(stack) == 0    # return true if balanced, false otherwise

# Driver Code

expr = input()    # take input expression from user

	# Function call
if areBracketsBalanced(expr): #
    print("true")
else:     # print false if not balanced
	print("false")