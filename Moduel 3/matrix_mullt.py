# Use print() to print to the console
# Read the first matrix dimensions
n, m = map(int, input().split())                 #n is number of rows and m is number of columns
A = [list(map(int, input().split())) for _ in range(n)] # Read the first matrix

# Read the second matrix dimensions
p, q = map(int, input().split()) #p is number of rows and q is number of columns
B = [list(map(int, input().split())) for _ in range(p)] # Read the second matrix

# Check for compatibility
if m != p:   #if number of columns in first matrix is not equal to number of rows in second matrix
    print("Incompatible dimensions") #print error message
else:
    # Initialize result matrix
    C = [[0 for _ in range(q)] for _ in range(n)] #resultant matrix will have dimensions n x q
    # Matrix multiplication
    for i in range(n):         #iterate through rows of first matrix
        for j in range(q):     #iterate through columns of second matrix
            for k in range(m): #iterate through columns of first matrix
                C[i][j] += A[i][k] * B[k][j]   #multiply and add to result matrix
    # Print result matrix
    for row in C:  #iterate through each row of result matrix
        print(" ".join(map(str, row)))  #print each row as space separated values

#output formatting explanation
"""
The output is formatted to display the result
 of each operation on the matrices in a clear and concise manner. 
 Each operation's result is printed with a descriptive label, 
 followed by the resulting matrix or value. The matrices are printed row by row, 
 with elements separated by spaces. This makes it easy to read and understand 
 the results of the matrix operations.
"""
#output
"""Grid A: 2 rows, 3 columns [2×3]     Grid B: 3 rows, 2 columns [3×2]
✅ Can multiply! (3 = 3)
Grid A: 2 rows, 4 columns [2×4]     Grid B: 3 rows, 2 columns [3×2]  
❌ Can't multiply! (4 ≠ 3)
Step 1: Take ROW 0 from Grid A → [1, 2]
Step 2: Take COLUMN 0 from Grid B → [5, 7]  
Step 3: Do the dance: (1×5) + (2×7) = 5 + 14 = 19! ✨
Grid A = [1 2]    Grid B = [5 6]    Result = [19 22]    
            [3 4]             [7 8]             [43 50] 
How we get 19:
- Take A's first row [1, 2] and B's first column [5, 7]
- Dance: (1×5) + (2×7) = 5 + 14 = 19! ✨

"""