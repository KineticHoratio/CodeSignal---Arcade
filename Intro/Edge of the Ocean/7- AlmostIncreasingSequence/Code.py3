def seq(y):
        x = []
        for i in range(len(y)-1):
            
            if y[i+1]>y[i]:
                x.append(True)
            else:
                x.append(False)
                break
        
        if False in x:
        
            return False
        
        else:
            return True
        
def almostIncreasingSequence(sequence):
    
    y = []    
    for i in range(len(sequence)):
    
        y.append(seq(sequence[:i]+sequence[i+1:]))
        
    if True in y:
        
        return True
    
    else:
        return False
