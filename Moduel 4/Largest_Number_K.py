# Use print() to print to the console
# Input
s, k = input().split() # Split input into string s and integer k
k = int(k) # Convert k to integer

# Initialize variable to store the largest number
max_num = 0 # Start with 0 as the smallest possible number

# Loop through string to check all consecutive K-digit numbers
for i in range(len(s) - k + 1): # Ensure we don't go out of bounds
    current_num = int(s[i:i + k]) # Extract K-digit number and convert to integer
    if current_num > max_num: # Compare with current maximum
        max_num = current_num # Update maximum if current is larger

# Output
print(max_num)