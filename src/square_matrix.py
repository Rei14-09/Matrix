'''
With the matrix done, check if it is square. 
A square matrix has the same number of rows and columns. 
If it is not square, return False. 
If it is square, return True.
'''


def check_square_matrix(matrix):

    assert isinstance(matrix,list)    

    if not matrix:
        return False
    for fila in matrix: 

        assert isinstance(fila, list)
        
        if len(fila) != len(matrix):
            return False
    else:
        return True


if __name__ == "__main__":
    assert check_square_matrix([[1, 0], [0, 1]]) == True
    # >>> True
    assert check_square_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == True
    # >>> True
    assert check_square_matrix([[1, 0], [0, 1], [1, 0]]) == False
    # >>> False
    assert check_square_matrix([]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0, 0]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0]]) == False
    # >>> False
    assert check_square_matrix([[1, 0], [1, 1]]) == True
    # >>> True
    assert check_square_matrix([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]) == True
    # >>> True
    assert check_square_matrix([[1,1,1], [1,1,1], [1,1,1], [2,2,2]]) == False
    # >>> False
    assert check_square_matrix([[2,2], [2,2], [2,2], [2,2]]) == False
    # >>> False
    assert check_square_matrix([[1,1], [1,1], [1,1]]) == False   
    # >>> False