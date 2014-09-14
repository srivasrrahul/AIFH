import math

def euclidean(v1,v2):
    if (len(v1) != len(v2)):
        raise Exception('length is invalid')
    
    sumDistance  = 0.0
    for i in range(0,len(v1)):
        d  = (float)(v1[i]) - (float)(v2[i])
        sumDistance = sumDistance + d*d
    
    return math.sqrt(sumDistance)

def manhattan(v1,v2):
    if (len(v1) != len(v2)):
        raise Exception('length is invalid')

    sumDistance = 0.0
    for i in range(0,len(v1)):
        d = abs((float)(v1[i]) - (float)(v2[i]))
        sumDistance = sumDistance + d

    return sumDistance


def chebyshev(v1,v2):
    if (len(v1) != len(v2)):
        raise Exception('length is invalid')

    maxDistance = 0.0
    for i in range(0,len(v1)):
        d = abs((float)(v1[i]) - (float)(v2[i]))
        if (d > maxDistance):
            maxDistance = d

    return maxDistance
    


def unit_test():
    v1=[0.0,1.0,1.2]
    v2=[0.1,1.1,1.3]
    print(euclidean(v1,v2))
    print(manhattan(v1,v2))
    print(chebyshev(v1,v2))


unit_test()
