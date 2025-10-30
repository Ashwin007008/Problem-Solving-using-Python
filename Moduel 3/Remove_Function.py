"""
Problem Statement
Last saved: 1:33 AM
Given a string, remove all occurrences of the letter "b" and the substring "ac" from it. Do this by going through the string only once.

You need to make changes directly in the string and keep track of the updated string as you go through it.

Input Format:

A string str that may contain letters "b" and the substring "ac".
Output Format:

A string with all occurrences of "b" and "ac" removed, in the same order as they appear.
Example 1:

Input: 
aacbacc

Output:
ac  

Explanation:
We first remove the "b", resulting in "aacacc". Then, we remove the "ac" substring,
which gives us "ac".
Example 2:

Input: 
aacb 

Output:
a  

Explanation:
We first remove the "b", resulting in "aac". Then, we remove the "ac" substring, 
which leaves us with "a".
Constraints:

The input string str will contain only lowercase English letters (a-z).

The string will not be empty.
"""
s = input().strip()
result = ""

i = 0
while i < len(s):
    if s[i] == 'b':  # skip 'b'
        i += 1
    elif s[i] == 'a' and i + 1 < len(s) and s[i + 1] == 'c':  # skip 'ac'
        i += 2
    else:
        result += s[i]
        i += 1

print(result)
