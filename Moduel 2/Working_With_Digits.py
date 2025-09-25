# Use print() to print to the console
# Read input
num = int(input()) 

# Ensure it's a 4-digit number
if 1000 <= num <= 9999: # check if number is 4-digit
    digits = [int(d) for d in str(num)]   # convert number to list of digits,
    # (for)means for each digit in the string of number convert it to integer and store it in list
    #(d)means digit, where d is each character in the string representation of number
    #(str(num)) means convert number to string.

    total = sum(digits)                   # sum of digits
    maximum = max(digits)                 # maximum digit
    minimum = min(digits)                 # minimum digit

    print("Sum of digits:", total)
    print("Maximum digit:", maximum)
    print("Minimum digit:", minimum)
else:
    print("Invalid input! Please enter a 4-digit number.")
