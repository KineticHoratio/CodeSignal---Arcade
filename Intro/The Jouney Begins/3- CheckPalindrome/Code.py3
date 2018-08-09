### Function
def checkPalindrome(inputString):

    if inputString[::-1] == inputString:
    
        return True
    
    else:
    
        return False
        
### Test
 inputString = ["aabaa","abcd","a","az","abacaba"]

for i in range(len(inputString)):
    
    print(checkPalindrome(inputString[i]))
 
