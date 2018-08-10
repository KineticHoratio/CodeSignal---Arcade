def matrixElementsSum(matrix):
    
    for i in range(len(matrix)-1):
  
        for j in range(len(matrix[0])):
            
            if matrix[i][j] == 0:
                
                matrix[i+1][j] = 0
       
    suma = 0
    
    for i in range(len(matrix)):
        
        suma += sum(matrix[i])
        
    return suma
