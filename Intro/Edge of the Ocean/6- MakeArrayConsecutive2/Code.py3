# Function
def makeArrayConsecutive2(statues):
    a = min(statues)
    b = max(statues)
    
    x = list(range(a,b))
    
    y = 0
    
    for i in range(len(x)):
        if x[i]  not in statues:
            y += 1
            
    return y
    
# Test

statues = [[6, 2, 3, 8],[0,3],[5, 4, 6],[6, 3]]

for i in range(len(statues)):
    
    print(makeArrayConsecutive2(statues[i]))
