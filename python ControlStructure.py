# What are Control Structures?
# Control structures manage the flow of a program: the order, decisions, and repetitions.

# 1. Sequential Control Structure
# Code runs line by line, top to bottom.
print("Sequential Example:")
print("Step 1: Open the fridge")
print("Step 2: Take out the milk")
print("Step 3: Pour into glass")

# 2. Selection (Conditional) Control Structure
# Code makes decisions based on conditions.
print("\nSelection Example:")
temperature = int(input("Enter the temperature: "))
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's cool outside!")

# 3. Iteration (Looping) Control Structure
# Code repeats actions using loops.
print("\nIteration Example:")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)