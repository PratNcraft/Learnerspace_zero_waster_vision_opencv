import numpy as np
#np.random.rand()-floating pt no.[0.0,1.0)
# np.random.rand(d0, d1, ..., dn) 
# i.e. .rand(2,3) give 2x3 matrix
# np.random.randint(low, high, size)
#one way-
#array1=np.arange(0,225).reshape(15,15) 
np.random.seed(0)#ensures same values next time when executed
arr2=np.random.randint(0,225, size=(15,15))

#task 1.creata a new array where all elements less than 
#threshold(120) are set to zero and rest remain the same 

#np.where(condition, value_if_true, value_if_false) returns a new array by applying the 
#condition element-wise.
arr3=np.where(arr2<120,0,arr2)

# task 2- pyt function that prints boundary ele of matrix from top-left in clockwise dirctn.

def boundary_transversal(matrix):
    rows, cols = matrix.shape

    # Top row
    for j in range(cols):
        print(matrix[0][j], end=' ')
    
    # Right column (excluding top and bottom corners)
    for i in range(1, rows - 1):
        print(matrix[i][cols - 1], end=' ')
    
    # Bottom row (in reverse)
    for j in range(cols - 1, -1, -1):
        print(matrix[rows - 1][j], end=' ')
    
    # Left column (in reverse, excluding corners)
    for i in range(rows - 2, 0, -1):
        print(matrix[i][0], end=' ')


#new numpy array replaceing all odd ele with 0 and even by 1
new_matrix = np.where(arr2 % 2 == 0, 1, 0)

for i in range(15):
    for j in range(15):
        print(new_matrix[i][j])