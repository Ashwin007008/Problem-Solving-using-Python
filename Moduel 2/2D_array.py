# 2D_array & Matrix.py
# 2D Arrays and Matrices 


#Example of a comprehensive educational lesson on 2D arrays and matrices
import time

def pause_for_explanation(seconds=2):                              #seconds to wait for explanation
    """Pause for student comprehension"""
    time.sleep(seconds)

def print_section_header(title):
    """Print formatted section headers"""
    print("\n" + "=" * 60)
    print(f"📖 {title}")
    print("=" * 60)

def print_subsection(title):
    """Print formatted subsection headers"""
    print(f"\n🔹 {title}")
    print("-" * 40)

# =================== LESSON START ===================

print_section_header("2D ARRAYS AND MATRICES - COMPREHENSIVE LESSON")
print("Welcome to today's programming lesson!")
print("Today we'll learn about 2D Arrays and Matrices - important data structures in computer science.")
pause_for_explanation()

# =================== PART 1: FUNDAMENTAL CONCEPTS ===================

print_section_header("PART 1: UNDERSTANDING DATA STRUCTURES")

print_subsection("What is a Data Structure?")
print("• A data structure is a way to organize and store data in computer memory")
print("• Think of it like organizing books in a library - you need a system!")
print("• Examples: Lists, Arrays, Dictionaries, Trees, etc.")
pause_for_explanation()

print_subsection("From 1D to 2D: The Evolution")
print("\n1D Array (One Dimension):")
simple_list = [10, 20, 30, 40, 50]
print(f"   {simple_list}")
print("   ↑ This is like a single row of lockers")

print("\n2D Array (Two Dimensions):")
grid = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("   [[10, 20, 30],")
print("    [40, 50, 60],")
print("    [70, 80, 90]]")
print("   ↑ This is like a grid of lockers with rows AND columns")
pause_for_explanation()

# =================== PART 2: 2D ARRAYS IN DETAIL ===================

print_section_header("PART 2: 2D ARRAYS - STRUCTURE AND ACCESS")

print_subsection("Real-World Analogy: Classroom Seating Chart")
classroom = [
    ["Alice", "Bob", "Charlie"],
    ["Diana", "Eve", "Frank"],
    ["Grace", "Henry", "Ivy"]
]

print("Imagine a classroom with 3 rows and 3 columns of desks:")
for i, row in enumerate(classroom):
    print(f"Row {i}: {row}")

print("\n📍 Coordinate System (Row, Column):")
print("• Programming uses (0,0) as the starting point (top-left)")
print("• Row numbers: 0, 1, 2 (counting from top)")
print("• Column numbers: 0, 1, 2 (counting from left)")
pause_for_explanation()

print_subsection("Accessing Elements - The Address System")
print(f"• Student at position (0,1): {classroom[0][1]}")
print(f"• Student at position (1,2): {classroom[1][2]}")
print(f"• Student at position (2,0): {classroom[2][0]}")
print("\nSyntax: array_name[row_index][column_index]")
pause_for_explanation()

# =================== PART 3: MATRICES - MATHEMATICAL PERSPECTIVE ===================

print_section_header("PART 3: MATRICES - THE MATHEMATICAL VIEW")

print_subsection("What Makes a Matrix Special?")
print("• A matrix is a 2D array specifically used for mathematical operations")
print("• Matrices have special properties and rules")
print("• Used in advanced math, physics, computer graphics, and AI")
pause_for_explanation()

print_subsection("Matrix Notation and Terminology")
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Matrix A (2×3 matrix - 2 rows, 3 columns):")
for i, row in enumerate(matrix_a):
    print(f"   {row}")

print("\n📊 Matrix Properties:")
print(f"• Dimensions: {len(matrix_a)} rows × {len(matrix_a[0])} columns")
print(f"• Element A[0][1] = {matrix_a[0][1]}")
print(f"• Element A[1][2] = {matrix_a[1][2]}")
pause_for_explanation()

# =================== PART 4: PRACTICAL APPLICATIONS ===================

print_section_header("PART 4: REAL-WORLD APPLICATIONS")

print_subsection("Application 1: Game Development - Chessboard")
chessboard = [
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
]

print("Chess game board representation:")
print("   A B C D E F G H")
for i, row in enumerate(chessboard): #i is row index, row is the list of pieces,(enumerate(chessboard) gives index and value)
    print(f"{8-i}  {' '.join(row)}") #8-i to print row numbers from 8 to 1

print(f"\nQueen's position: Row 0, Column 3 = {chessboard[0][3]}")
pause_for_explanation()

print_subsection("Application 2: Image Processing")
# Simulate a simple 5x5 grayscale image (0=black, 255=white)
image_matrix = [
    [0,   50,  100, 150, 200],
    [25,  75,  125, 175, 225],
    [50,  100, 150, 200, 250],
    [75,  125, 175, 225, 255],
    [100, 150, 200, 250, 255]
]

print("Digital Image as a Matrix (Grayscale values 0-255):")
for row in image_matrix:
    print("   " + " ".join(f"{val:3d}" for val in row))

print("\n• Each number represents the brightness of a pixel")
print("• 0 = completely black, 255 = completely white")
print("• Computer graphics use matrices to process millions of pixels!")
pause_for_explanation()

print_subsection("Application 3: Spreadsheet Software")
spreadsheet = [
    ["Name", "Math", "Science", "English", "Average"],
    ["John", 85, 92, 78, 0],
    ["Sarah", 94, 88, 91, 0],
    ["Mike", 76, 82, 85, 0]
]

print("Spreadsheet-like data structure:")
for i, row in enumerate(spreadsheet):
    if i == 0:
        print(f"   {row}")
        print("   " + "-" * 35)
    else:
        # Calculate average for each student
        if len(row) > 3 and isinstance(row[1], int):
            avg = round((row[1] + row[2] + row[3]) / 3, 1)
            row[4] = avg
        print(f"   {row}")

print("\n• Excel, Google Sheets use 2D arrays internally")
print("• Each cell has coordinates like (row, column)")
pause_for_explanation()

# =================== PART 5: OPERATIONS AND ALGORITHMS ===================

print_section_header("PART 5: COMMON OPERATIONS")

print_subsection("Matrix Creation and Initialization")
# Create a 3x4 matrix filled with zeros
rows, cols = 3, 4
zero_matrix = [[0 for j in range(cols)] for i in range(rows)]
print("Creating a 3×4 matrix filled with zeros:")
for row in zero_matrix:
    print(f"   {row}")

# Create identity matrix
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print("\nIdentity Matrix (3×3):")
for row in identity:
    print(f"   {row}")
pause_for_explanation()

print_subsection("Matrix Traversal Algorithms")
sample_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Sample Matrix for traversal:")
for row in sample_matrix:
    print(f"   {row}")

print("\n1. Row-wise traversal:")
row_wise = []
for i in range(len(sample_matrix)):
    for j in range(len(sample_matrix[i])):
        row_wise.append(sample_matrix[i][j])
print(f"   Result: {row_wise}")

print("\n2. Column-wise traversal:")
col_wise = []
for j in range(len(sample_matrix[0])):
    for i in range(len(sample_matrix)):
        col_wise.append(sample_matrix[i][j])
print(f"   Result: {col_wise}")
pause_for_explanation()

print_subsection("Matrix Arithmetic - Addition Example")
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("Matrix Addition:")
print("Matrix 1:")
for row in matrix1:
    print(f"   {row}")
print("Matrix 2:")
for row in matrix2:
    print(f"   {row}")

# Add matrices
result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] 
          for i in range(len(matrix1))]

print("Result (Matrix 1 + Matrix 2):")
for row in result:
    print(f"   {row}")
pause_for_explanation()

# =================== PART 6: PROGRAMMING BEST PRACTICES ===================

print_section_header("PART 6: PROGRAMMING BEST PRACTICES")

print_subsection("Memory Considerations")
print("• 2D arrays use more memory than 1D arrays")
print("• For a 1000×1000 matrix of integers: ~4MB of memory")
print("• Always consider the size of your data structures")
pause_for_explanation()

print_subsection("Common Programming Patterns")
print("1. Nested loops for 2D array operations:")
print("   for i in range(rows):")
print("       for j in range(cols):")
print("           # process matrix[i][j]")
print()
print("2. List comprehension for matrix creation:")
print("   matrix = [[0 for j in range(cols)] for i in range(rows)]")
print()
print("3. Error checking for valid indices:")
print("   if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):")
print("       # safe to access matrix[row][col]")
pause_for_explanation()

# =================== PART 7: ADVANCED CONCEPTS PREVIEW ===================

print_section_header("PART 7: LOOKING AHEAD - ADVANCED CONCEPTS")

print_subsection("What You'll Learn Next")
print("• 3D Arrays and Multi-dimensional data")
print("• Matrix multiplication and linear algebra")
print("• Sparse matrices (matrices with mostly zeros)")
print("• Matrix algorithms in machine learning")
print("• Computer graphics transformations")
pause_for_explanation()

print_subsection("Career Applications")
print("Fields that heavily use matrices:")
print("• Video Game Development (3D graphics)")
print("• Artificial Intelligence and Machine Learning")
print("• Data Science and Analytics")
print("• Computer Graphics and Animation")
print("• Engineering Simulations")
print("• Cryptography and Security")
pause_for_explanation()

# =================== LESSON SUMMARY ===================

print_section_header("LESSON SUMMARY")

print("🎓 Key Takeaways:")
print("• 2D Arrays organize data in rows and columns")
print("• Matrices are mathematical 2D arrays with special operations")
print("• Index notation: array[row][column] (starting from 0)")
print("• Used everywhere: games, images, spreadsheets, AI")
print("• Essential building block for advanced programming")

print("\n📝 Practice Exercises:")
print("1. Create a 4×4 multiplication table matrix")
print("2. Write code to find the largest element in a matrix")
print("3. Implement matrix transpose (flip rows and columns)")
print("4. Create a simple tic-tac-toe game using a 3×3 matrix")

print("\n� Remember:")
print("• Master the basics before moving to complex operations")
print("• Practice with small examples first")
print("• Think about real-world applications")
print("• 2D arrays are everywhere in computer science!")

print("\n" + "=" * 60)
print("📚 End of Lesson - Questions and Discussion Time!")
print("=" * 60)


"""
Introduction to 2D Arrays and Matrices
Hey Kalvians! Welcome to the lesson on 2D Arrays and Matrices!
Remember how in the last lesson, we efficiently searched for elements in a sorted 1D array using binary search?
Now, let's explore how we can structure and manipulate data that's organized in rows and columns.

Imagine you're managing seating arrangements in a cinema hall or organizing data in a spreadsheet. How do you efficiently store and access information in such a grid-like structure?

In this lesson, you'll learn how to use 2D arrays to neatly organize data, access specific elements, and perform operations on them, just like managing seats in a cinema or cells in a spreadsheet!
So let's uncover the magic behind it, and explore 2D Arrays!

A 2D array is like a table or a grid, where data is organized in rows and columns. It's incredibly useful for representing data that has a natural two-dimensional structure.



Image Credits: Leetcode

📚 Learning Objectives:
Understand the concept of a 2D array and its structure.

Learn how to create, initialize, and access elements in a 2D array.

Implement nested loops to efficiently process 2D array elements.

Apply 2D arrays to solve problems involving grid structures and element identification, such as finding border elements and calculating sums.

💡 What is a 2D Array?
A 2D array, also known as a matrix or grid, is an array of arrays.

Think of it as a table with rows and columns. Each element is accessed using two indices: one for the row and one for the column.

Useful for representing images, game boards, spreadsheets, etc.

A cinema hall where each seat is identified by a row number and seat number.

Declaring and Initializing a Matrix in 🐍 Python
A matrix (2D array) in Python is declared as follows:

matrix = []  # Declared as an empty 2D array (list of lists)
You can also initialize a matrix during declaration:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Declaring and Initializing a Matrix in 💻 C++
A matrix (2D array) in Cpp is declared as follows:

int matrix[3][4];  // Declared 2D array with 3 rows and 4 columns
You can also initialize a matrix during declaration:

int matrix[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};
How to Represent Grid Data
2D arrays are perfect for representing data that has a natural grid-like structure. Think of a chessboard, a spreadsheet, or even the pixels on your computer screen.

Each element in the 2D array represents a specific location in the grid. For example, in a chessboard, array[0][0] could represent the top-left square, and array[7][7] could represent the bottom-right square.

The first index typically represents the row number, and the second index represents the column number.

🛠️ How to Read Input to Fill a 2D Array and printing the same
Reading input to fill a 2D array means taking values from the user (or any input source) and storing them row by row and column by column into a matrix-like structure.

Python
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at row {i+1}, column {j+1}: "))
        row.append(element)
    matrix.append(row)

print("The 2D array is:")
for row in matrix:
    print(row)
C++
cpp
#include <iostream>
using namespace std;

int main() {
    int rows, cols;
    cout << "Enter the number of rows: ";
    cin >> rows;
    cout << "Enter the number of columns: ";
    cin >> cols;

    // Assuming maximum size of 100x100
    int matrix[100][100];

    // Input elements
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << "Enter element at row " << i+1 << ", column " << j+1 << ": ";
            cin >> matrix[i][j];
        }
    }

    // Output the matrix
    cout << "The 2D array is:" << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

🔄 This process involves:
Knowing the dimensions of the matrix (number of rows and columns).

Using nested loops:

The outer loop iterates over rows.
The inner loop iterates over columns.
For each combination of row and column, the program:

✅ Prompts the user for input.
✅ Reads the value.
✅ Stores it in the correct position of the matrix.
Alternatively you can watch this video to understand all about 2D arrays and matrices in Python programming.


Alternatively you can watch this video to understand all about 2D arrays and matrices in Cpp programming.


🎯 Activity Time! — Treasure Island Pathfinding
Imagine you're a cartographer 🗺️ building a digital map of Treasure Island.

Your Mission:
Represent the Island as a 2D array:

0: Safe zone (beach, grassland)
1: Moderate danger (forest)
2: High danger (swamps, quicksand)
Define the Island Size: e.g., 5x5 or 7x7.

Mark the Safest Path from (0, 0) to (rows-1, cols-1) by:

Calculating risk for all right/down paths.
Selecting the one with the minimum risk.
Marking the safest path with -1.
Implementation Hints:
Initialize your island (2D array).
Use recursion to explore all paths and compute total risks.
Store and mark the path with least risk.
Print the updated grid showing the safest path.
Don't worry if you're stuck — your mentor will guide you!
"""

# Example Solution in Python
# Read the dimension of the square matrix
n = int(input())

# Initialize the matrix
matrix = []

# Input the matrix elements row by row
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Initialize variable to store the border sum
border_sum = 0

# Calculate sum of border elements
for i in range(n):
    for j in range(n):
        # Condition for border elements
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            border_sum += matrix[i][j]

# Print the result
print("Sum of border elements:", border_sum)
