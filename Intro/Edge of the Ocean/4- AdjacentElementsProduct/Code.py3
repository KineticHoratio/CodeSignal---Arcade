# Function
def adjacentElementsProduct(inputArray):

    temp = []
    for i in range(len(inputArray)-1):
    
        temp.append(inputArray[i]*inputArray[i+1])
        
    return max(temp)
    
# Test

array = [[3, 6, -2, -5, 7, 3],[5, 1, 2, 3, 1, 4],[9, 5, 10, 2, 24, -1, -48]]

for i in range(len(array)):
    
    print(adjacentElementsProduct(array[i]))
