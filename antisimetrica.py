def es_antisimetrica(matriz):
    
    if len(matriz) == 0:
        return False
    for fila in matriz:
        if len(fila) != len(matriz):
            return False

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != -matriz[j][i]:
                return False
                
    return True

if __name__ == '__main__':

  assert es_antisimetrica([[0, 1, 2], [-1, 0, 3],[-2, -3, 0]]) == True
  #>>> True
  assert es_antisimetrica([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == True
  #>>> True
  assert es_antisimetrica([[0, 1, 2], [-1, 0, -2], [2, 2,  3]]) == False
  #>>> False
  assert es_antisimetrica([[1, 2, 5],[0, 1, -9],[0, 0, 1]]) == False
  #>>> False
  passert es_antisimetrica([[1,0,0,0],[0,1,1,0],[0,0,0,1]]) == False
  #>>>False
  assert es_antisimetrica([[1,0,0,0,0,0,0,0,0]]) == False
  #>>>False 
