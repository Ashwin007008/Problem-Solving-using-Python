"""
Problem Statement

Write a program that counts the number of positions in a string where an uppercase letter follows directly after a lowercase letter.

Input Format:

A string consisting of both uppercase and lowercase letters.
Output Format:

An integer representing the count of positions where an uppercase letter follows a lowercase letter.
Constraints:

The string will contain only English alphabet letters.
The string length will be between 1 and 1000.
Example 1:

Input: 
heLLo  

Output: 
1  

Explanation: 
In the string "heLLo", the pair "eL" is one position where an uppercase letter (L) follows a lowercase letter (e).
Example 2:

Input: 
HeLLoWorld  

Output: 
2  

Explanation: 
In "HeLLoWorld", the pairs are:
- "eL" and "oW", so there are 2 positions.
Example 3:

Input: 
hello  

Output: 
0  

Explanation: 
There are no lowercase letters followed by uppercase letters in the string.
"""


s = input().strip()

count = 0

# Loop through the string and check each pair of adjacent characters
for i in range(len(s) - 1):
    #i, means current index
    #range, means loop through a sequence of numbers
    #(len(s) - 1) means length of string s minus 1, to avoid index out of range error

    if s[i].islower() and s[i + 1].isupper():
        count += 1

# Output
print(count)

