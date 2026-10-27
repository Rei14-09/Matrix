'''
With the matrix done, check if it is square. 
A square matrix has the same number of rows and columns. 
If it is not square, return False. 
If it is square, return True.
'''


def check_square_matrix(matrix):
    if not matrix:
        return False
    for fila in matrix: 
        if len(fila) != len(matrix):
            return False
    else:
        return True



print(check_square_matrix([[1, 0], [0, 1]]) )
# >>> True
print(check_square_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  
# >>> True
print(check_square_matrix([[1, 0], [0, 1], [1, 0]])) 
 # >>> False
print(check_square_matrix([]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0, 0]]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1]]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1]]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]))  
# >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]))
  # >>> False
print(check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]))  
# >>> False
print(check_square_matrix([[1, 0], [1, 1]]))
# >>> True
print(check_square_matrix([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])) 
# >>> True
print(check_square_matrix([[1,1,1], [1,1,1], [1,1,1], [2,2,2]]))
# >>> False
print(check_square_matrix([[2,2], [2,2], [2,2], [2,2]]))
# >>> False
print(check_square_matrix([[1,1], [1,1], [1,1]]))   
# >>> False