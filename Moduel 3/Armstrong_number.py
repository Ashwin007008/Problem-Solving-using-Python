# Python Program (with NumPy)
import numpy as np

def is_armstrong(num):
    # Convert number into a list of its digits
    digits = np.array(list(map(int, str(num))))
    power = len(digits)
    
    # Use numpy to compute each digit raised to the power and sum them
    total = np.sum(np.power(digits, power))
    
    # Check and return result
    if total == num:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"

# Input from user
n = int(input())
print(is_armstrong(n))

"""Explanation

Convert number to digits:

digits = np.array(list(map(int, str(num))))


Example → 371 → [3, 7, 1]

Find number of digits:

power = len(digits)


→ 3

Raise each digit to that power using NumPy:

np.power(digits, power)


→ [27, 343, 1]

Sum them up using NumPy:

np.sum(np.power(digits, power))


→ 371

Compare with original number:

If equal → “Armstrong number”

Else → “Not an Armstrong number”

"""