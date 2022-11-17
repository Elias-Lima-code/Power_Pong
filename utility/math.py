
def clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

def sum_tuples(t1,t2):
    return (t1[0]+t2[0], t1[1]+ t2[1])

def between(value, min, max, inclusive = True):
    if inclusive:
        return value >= min and value <= max
    return value > min and value < max