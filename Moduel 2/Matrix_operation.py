"""
You are given two matrices 𝐴 and 𝐵. Write a program that performs the following operations on these matrices and prints the result for each operation:

Addition of matrices 𝐴 and 𝐵
Subtraction of matrix 𝐵 from 𝐴
Multiplication of matrices 𝐴 and 𝐵
Transpose of matrix 𝐴
Diagonal sum of matrix 𝐴 and matrix 𝐵
Input Format
The first line contains two integers 𝑛 and 𝑚 - the number of rows and columns for both matrices. The next 𝑛 lines contain 𝑚 integers each representing the elements of matrix 𝐴. The next 𝑛 lines contain 𝑚 integers each representing the elements of matrix 𝐵.

Output Format
Print the results of each operation as described below.

Example:

Input:
2 2  
1 2   
3 4  
5 6  
7 8  

Output:
Addition:  
6 8   
10 12   
Subtraction:  
-4 -4   
-4 -4   
Multiplication:  
19 22   
43 50   
Transpose of A:  
1 3   
2 4   
Diagonal Sum of A: 5   
Diagonal Sum of B: 13   

Explanation:
1) Addition: [[1+5 2+6] [3+7 4+8]] = [[6 8] [10 12]]
2) Subtraction: [[1-5 2-6] [3-7 4-8]] = [[-4 -4] [-4 -4]]
3) Multiplication: [[1\*5+2\*7 1\*6+2\*8] [3\*5+4\*7 3\*6+4\*8]] = [[19 22] [43 50]]
4) Transpose of A: [[1 3] [2 4]]
5) Diagonal Sum of A: 1+4 = 5
6) Diagonal Sum of B: 5+8 = 13
Constraints:

1 ≤ n,m ≤ 10^2
n=m

"""
def print_matrix(matrix):     #function to print matrix       
    for row in matrix:       #iterate through each row
        for val in row:       #iterate through each value in the row
            print(val, end=" ")  #print value with a space
        print()   #new line after each row

def add_matrices(A, B):      #function to add two matrices
    n = len(A)         #number of rows
    m = len(A[0])      #number of columns
    result = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)] #list comprehension to add matrices
    return result  #return the result

def subtract_matrices(A, B):  #function to subtract two matrices
    n = len(A)      #number of rows
    m = len(A[0])   #number of columns
    result = [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)] #list comprehension to subtract matrices
    return result #return the result

def multiply_matrices(A, B): #function to multiply two matrices
    n = len(A)     #number of rows
    m = len(A[0]) #number of columns
    result = [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(m)] for i in range(n)] #list comprehension to multiply matrices
    return result #return the result

def transpose_matrix(A): #function to transpose a matrix
    n = len(A)    #number of rows
    m = len(A[0]) #number of columns
    result = [[A[j][i] for j in range(n)] for i in range(m)] #list comprehension to transpose matrix
    return result #return the result

def diagonal_sum(A): #function to calculate diagonal sum of a matrix
    n = len(A)    #number of rows
    total = sum(A[i][i] for i in range(n)) #sum of diagonal elements
    return total #return the total


if __name__ == "__main__":   #main function
    import sys        #import sys module to read input
    input = sys.stdin.read  #read all input at once
    data = input().split()  #split input into a list
    index = 0             #initialize index to 0
    #Step 1
    # # The program asks: "How many rows and columns do you want?"
    n = int(data[index])     # "How many rows?" 
    m = int(data[index + 1])  # "How many columns?" 
    index += 2
    # It builds two grids A and B with your numbers
    A = []  # First grid 
    B = []  # Second grid 
    for i in range(n):
        A.append([int(data[index + j]) for j in range(m)])
        #print("Row", i + 1, "of A:", A[i]), A[i] is the ith row of matrix A
        index += m
    for i in range(n):
        B.append([int(data[index + j]) for j in range(m)])
        #print("Row", i + 1, "of B:", B[i]), B[i] is the ith row of matrix B
        index += m
    
    print("Addition:")
    add_result = add_matrices(A, B)
    print_matrix(add_result)
    
    print("Subtraction:")
    sub_result = subtract_matrices(A, B)
    print_matrix(sub_result)
    
    print("Multiplication:")
    mul_result = multiply_matrices(A, B)
    print_matrix(mul_result)
    
    print("Transpose of A:")
    trans_result = transpose_matrix(A)
    print_matrix(trans_result)
    
    print("Diagonal Sum of A:", diagonal_sum(A))
    print("Diagonal Sum of B:", diagonal_sum(B))


# Example Input:
# 2 2
# 1 2       
# 3 4
# 5 6
# 7 8   
# Example Output:       
# Addition:
# 6 8
# 10 12
# Subtraction:
# -4 -4         
# -4 -4
# Multiplication
# 19 22
# 43 50
# Transpose of A:
# 1 3
# 2 4
# Diagonal Sum of A: 5
# Diagonal Sum of B: 13

# using numpy
"""import numpy as np"""
import numpy as np
def main():
    n, m = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(n)])
    B = np.array([list(map(int, input().split())) for _ in range(n)])
    
    print("Addition:")
    print(A + B)
    
    print("Subtraction:")
    print(A - B)
    
    print("Multiplication:")
    print(np.dot(A, B))
    
    print("Transpose of A:")
    print(A.T)
    
    print("Diagonal Sum of A:", np.trace(A))
    print("Diagonal Sum of B:", np.trace(B))
if __name__ == "__main__":
    main()
# Example Input:
# 2 2
# 1 2
# 3 4
# 5 6
# 7 8
