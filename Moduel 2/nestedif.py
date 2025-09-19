"""what is nested if else with example
        Nested if-else statements are conditional statements that are placed 
inside another if or else block. This allows for more complex decision
-making processes by enabling multiple layers of conditions to be evaluated."""


# Example 1: Checking if a number is positive, negative, or zero
num = int(input("Example 1 :Enter a number: "))  # Take number input from user
if num > 0:
    print("Positive number")
    # If number is greater than 0, print positive
    if num % 2 == 0:
        print("Even positive number")  # Nested: check if even
    else:
        print("Odd positive number")   # Nested: else odd
elif num == 0: # elif is used to check another condition if the previous if condition is false
    print("Zero")  # If number is zero
else:
    print("Negative number")  # If number is less than 0


########################################################################################################################################################################

#### Example 2: Checking eligibility for voting and driving
age = int(input("Example 2 :Enter your age: "))  # Take age input from user
if age >= 18:
    print("Eligible to vote")
    if age >= 21:
        print("Eligible to drive a car")  # Nested: check if can drive
    else:
        print("Not eligible to drive a car")  # Nested: else not eligible
else:
    print("Not eligible to vote")

####################################################################################################################################################################################################################################################################

# Example 3: Checking grade based on marks
marks = int(input("Example 3:Enter your marks: "))  # Take marks input from user
if marks >= 60:
    print("First Division")
    if marks >= 90:
        print("Excellent!")  # Nested: check for excellence
    else:
        print("Good job!")   # Nested: else good job
elif marks >= 45:
    print("Second Division")
else:
    print("Fail")

#########################################################################################################################################################################

# Example 4: Checking if a character is a vowel or consonant
char = input("Example 4:Enter a character: ")  # Take character input from user
if char.isalpha():
    if char.lower() in 'aeiou':
        print("Vowel")  # Nested: check if vowel
    else:
        print("Consonant")  # Nested: else consonant
else:
    print("Not an alphabet")

#########################################################################################################################################################################

# Example 5: Checking if a year is a leap year
year = int(input("Example 5:Enter a year: "))  # Take year input from user
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")  # Nested: divisible by 400
        else:
            print("Not a leap year")  # Nested: not divisible by 400
    else:
        print("Leap year")  # Nested: not divisible by 100
else:
    print("Not a leap year")

#########################################################################################################################################################################

#Example 6: Checking if a number is prime or composite
num = int(input("Example 6:Enter a number greater than 1: "))  # Take number input from user
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Composite number")  # Nested: found a divisor
            break
    else:
        print("Prime number")  # No divisors found
else:
    print("Number should be greater than 1")

#########################################################################################################################################################################
# Example 7: Checking if a person is eligible for a senior citizen discount
age = int(input("Example 7:Enter your age: "))  # Take age input from user
if age >= 60:
    print("Eligible for senior citizen discount")
    if age >= 80:
        print("Extra discount available")  # Nested: check for extra discount
    else:
        print("Standard senior citizen discount")  # Nested: standard discount
else:
    print("Not eligible for senior citizen discount")
#########################################################################################################################################################################
# Example 8: Checking if a number is in a specific range
num = int(input("Example 8:Enter a number: "))  # Take number input from user
if 1 <= num <= 100:
    print("Number is between 1 and 100")
    if num < 50:
        print("Number is in the lower half")  # Nested: check lower half
    else:
        print("Number is in the upper half")  # Nested: upper half
else:
    print("Number is out of range")
#########################################################################################################################################################################
# Example 9: Checking if a person is eligible for a job based on age and experience
age = int(input("Example 9:Enter your age: "))  # Take age input from user
experience = int(input("Enter your years of experience: "))  # Take experience input from user
if age >= 18:
    if experience >= 2:
        print("Eligible for the job")  # Nested: check experience
    else:
        print("Not enough experience")  # Nested: not enough experience
else:
    print("Not eligible for the job")
#########################################################################################################################################################################
# Example 10: Checking if a number is a multiple of 3 and 5
num = int(input("Example 10:Enter a number: "))  # Take number input from user
if num % 3 == 0:
    if num % 5 == 0:
        print("Multiple of both 3 and 5")  # Nested: multiple of both
    else:
        print("Multiple of 3 only")  # Nested: multiple of 3 only
else:
    if num % 5 == 0:
        print("Multiple of 5 only")  # Nested: multiple of 5 only
    else:
        print("Not a multiple of 3 or 5")  # Not a multiple of either
#########################################################################################################################################################################   
# Example 11: Cheching Exam Results
Maths = int(input("Example 11:Enter your marks: "))  # Take marks input
Science = int(input("Enter your marks: "))  # Take marks input
English = int(input("Enter your marks: "))  # Take marks input
Social_Studies = int(input("Enter your marks: "))  # Take marks input
total = Maths + Science + English + Social_Studies
percentage = (total / 400) * 100
Average = total / 4
print(f"Total Marks: {total}, Percentage: {percentage}%, Average: {Average}")
"""     
            And Gate      \       OR Gate            \ NOT Gate
    A      B     A and B  \   A      B     A or B    \ A not A 
    True  True  = True    \ True  True  = True
    True  False = False   \ True  False = True
    False True  = False   \ False True  = True
    False False = False   \ False False = False
"""
if Maths >= 35 and Science >= 35 and English >= 35 and Social_Studies >= 35:
    print("Passed")
    if (Maths >= 75 and Science >= 75 and English >= 75 and Social_Studies >= 75):
        print("Distinction")
    elif (Maths >= 60 and Science >= 60 and English >= 60 and Social_Studies >= 60):
        print("First Division")
    elif (Maths >= 50 and Science >= 50 and English >= 50 and Social_Studies >= 50):
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Failed")
#########################################################################################################################################################################
# Example 12: Exam Result using Nested if-else and with logical operators (AND, OR, NOT
Maths = int(input("Example 12:Enter your marks: "))  # Take marks input
Science = int(input("Enter your marks: "))  # Take marks input
English = int(input("Enter your marks: "))  # Take marks input
Social_Studies = int(input("Enter your marks: "))  # Take marks input
total = Maths + Science + English + Social_Studies
percentage = (total / 400) * 100
Average = total / 4     
print(f"Total Marks: {total}, Percentage: {percentage}%, Average: {Average}")
"""
            And Gate      \       OR Gate            \    NOT Gate
    A      B     A and B  \   A      B     A or B    \     A not A 
    True  True  = True    \ True  True  = True
    True  False = False   \ True  False = True
    False True  = False   \ False True  = True
    False False = False   \ False False = False
"""
if (Maths >= 35 and Science >= 35 and English >= 35 and Social_Studies >= 35):
    print("Passed")
    if (Maths >= 75 and Science >= 75 and English >= 75 or Social_Studies >= 35):
        print("Distinction")
    elif (Maths >= 60 and Science >= 60 and English >= 60 and Social_Studies >= 60):
        print("First Division")
    elif (Maths >= 50 and Science >= 50 and English >= 50 and Social_Studies >= 50):
        print("Second Division")
    else:
        print("Third Division")
else:
    print("Failed")
#########################################################################################################################################################################