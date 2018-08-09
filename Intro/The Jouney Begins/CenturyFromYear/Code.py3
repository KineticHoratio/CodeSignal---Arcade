# Solve 1
def centuryFromYear(year):

    return int((year - 1) / 100) + 1

# Solve 2
def centuryFromYear(year):
    import math
    
    return math.ceil(year/100)
