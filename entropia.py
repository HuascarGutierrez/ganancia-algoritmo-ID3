import math
def entropia(p,n,d):
    ent= -p/d*math.log(p/d,2) -n/d*math.log(n/d,2)
    return ent