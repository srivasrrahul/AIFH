import math

def getLength(v1,v2,dataLength):
    if dataLength == -1:
        return len(v1)

    return dataLength

def euclidean(v1,v2,dataLength = -1):
    sumDistance  = 0.0
    for i in range(0,getLength(v1,v2,dataLength)):
        d  = (float)(v1[i]) - (float)(v2[i])
        sumDistance = sumDistance + d*d
    
    return math.sqrt(sumDistance)

def manhattan(v1,v2,dataLength = -1):
    sumDistance = 0.0
    for i in range(0,getLength(v1,v2,dataLength)):
        d = abs((float)(v1[i]) - (float)(v2[i]))
        sumDistance = sumDistance + d

    return sumDistance


def chebyshev(v1,v2,dataLength = -1):
    maxDistance = 0.0
    for i in range(0,getLength(v1,v2,dataLength)):
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

if __name__ == "__main__":
    unit_test()
