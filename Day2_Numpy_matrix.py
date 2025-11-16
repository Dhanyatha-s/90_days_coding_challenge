"""
Project : Matrix Calculator from Scratch
operations: Add, multiply, Transpose, determinant
Handle Different matrix sizes
Compare your result with Numpy functions
"""
# About Matrix

"""

Matrix: Rectangular arrangement in col x row, (A X B)

Dimention: A(2 x 3) :-> 2 row 3 col

Add : A + B  (condition: Same size of matrix get added)

Multiply : A X B (condition: Only If Col of A = row of B)
Example A (2 × 3) × B (3 × 2)

            First row with First Col  and Firts row with second Col

Transpose Matrix:
    Convert Row into Col
    col Into Row

    row = col
    col = row

    

Determinant : 
        only fro Square matrix (2 x 2) 4x 4.....

        | a  b |
        | c  d |

        |A| = |ad - bc|
        
        a x d --> first elem of first row with last elem of second col (somthing like this)

        if 3 X 3
        ∣A∣=a(ei−fh)−b(di−fg)+c(dh−eg)

"""

# This is from stractch fro addition and mulriplication without using np.array([][])
"""

def addition_from_scratch():
    # Build your own addition without numpy
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    
    return result

def addition_with_numpy():
    # Then compare with numpy
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    return matrix_a + matrix_b
"""

# We calculate  NumPy arrays using np.array() Like this np.array([[],[]])

import numpy as np

def addition():

    matrix_a = np.array([[1,2],
                        [3,4]]) # 2 x 2

    matrix_b = np.array([[5,6],
                        [7,8]])

    # Addition

    matrixAddition = matrix_a + matrix_b
    print(f"Matrix of A: {matrix_a}")

    print(f"\nMatrix of B: {matrix_b}")

    print(f"\nMatrix Addition is: {matrixAddition}")

    

def multiplication():

    #  Conditon to remember row A = col B
    mat_a = np.array([[1,2,4],
                            [3,4,6]]) # 2 x 3

    mat_b = np.array([[5,6],
                            [7,8],
                            [9,10]])

#  Perform matrix multiplication using the @ operator
    # matrixMultipy = mat_a * mat_b  --> this is not the right way

    matrixMultipy = mat_a @ mat_b 

    print("Matrix of A: ")

    for row in mat_a:
        print(row)

    print("\nMatrix of B:")
    for row in mat_b:
        print(row)

    print(f"\nMatrix Addition is: ")
    for row in matrixMultipy:
        print(row)


def matrixTranspose():
    matrix = []
    row_size = int(input("Enter the value for row: "))
    col_size = int(input("Enter the value for col: "))

    for i in range(row_size):
        row_value = []

        for j in range(col_size):
            
            value = int(input(f"Enter value for position ({i+1}, {j+1}): "))
            row_value.append(value)
        matrix.append(row_value)


    transposed = [[0 for _ in range(col_size)] for _ in range(row_size)]
            

    for row in range(row_size):
        for col in range(col_size):
            transposed[col][row] = matrix[row][col]
            

    print("Original Matrix")
    for row in matrix:
        print(row)

    print("Transposed Matrix")
    for row in transposed:
        print(row)

    


    return transposed

    
def MatrixDeterminant():
    matrix = []
    row_size = int(input("Enter the size of row: "))
    col_size = int(input("Enter the size of col: "))

    for i in range(row_size):
        row = []
        for j in range(col_size):

            value = int(input(f"Enter the value for Position ({i+1},{j+1}):"))
            row.append(value)

        matrix.append(row)

    # matrix structure: [[a, b], [c, d]]
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    # The formula: determinant = (a * d) - (b * c)
    determinant = (a * d) - (b * c)

    # matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]
    for row in matrix:
        print(row)
    print(f"The Determinant of the Matrix 2 x 2 is : {determinant}")

while True:
    print("--- Choose from the menu ---")
    print("1. Matrix Addition ")
    print("2. Matrix Multiplication ")
    print("3. Matrix Transpose ")
    print("4. Determinant")
    print("0. Exit")


    choice = int(input("Enter The Operation No. to calculate"))

    if choice == 1:
        addition()

    if choice == 2:
        multiplication()

    if choice == 3:
        # a = [[1,2],[3,4]]
        matrixTranspose()

    if choice == 4:
        MatrixDeterminant()

    if choice == 0:
        exit()