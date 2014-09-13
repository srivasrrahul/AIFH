import math

def createMatrix(N):
    #It creates N*N-1
    x = []
    for i in range(0,N):
        x.append([])

    for i in range(0,N):
        for j in range(0,N-1):
            x[i].append(0.0)

    return x

def printMatrix(lst):
    for i in range(0,len(lst)):
        print(str(lst[i]))

def createLookup(N):
    lst = createMatrix(N)
    lst[0][0] = -1.0
    lst[1][0] = 1.0
    # for i in range(0,len(lst[0])):
    #     lst[0][i] = -1.0
    
    # for i in range(0,len(lst[0])):
    #     lst[len(lst)-1][i] = 1.0

        #lst[len(lst)-1][0] = 1.0
    for k in range(2,N):
        n = k*1.0
        f = math.sqrt(n*n-1.0)/n
        
        for i in range(0,k):
            for j in range(0,k-1):
                lst[i][j] *= f
        
            r = -1.0 /n
            #print(r)
        
            for i in range(0,k):
                lst[i][k-1] = r


            for i in range(0,k-1):
                lst[k][i] = 0.0
        
            lst[k][k-1] = 1.0

    return lst

def scaleLst(lowData,highData,lowNormalized,highNormalized,lst,N):
    for i in range(0,N):
        for j in range(0,N-1):
            lst[i][j] = ((lst[i][j] - lowData)/(highData - lowData)) * (highNormalized - lowNormalized) + lowNormalized

    return lst
    
###############################################UNIT TEST#################################
def unit_test():
    lst = createLookup(5)
    printMatrix(lst)
    lst = scaleLst(-1.0,1.0,-1.0,1.0,lst,5)
    
unit_test()
    
