import random
def estimatepi(n):
    success = 0.0
    for i in range(0,n):
        x = random.random()
        y = random.random()
        z = x*x + y*y
        if z  < 1.0:
            success = success + 1.0
    
    return 4.0 * (success/n)


####################unit_test#############


def unit_test():
    print(estimatepi(1000000))


unit_test()
            
