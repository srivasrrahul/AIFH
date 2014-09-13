
#Utilities for normalization/denormalization

def normalizedOrdinal(lowData,highData,lowNormalized,highNormalized,value):
    dataRange = highData  - lowData
    realDataPercentage = value/dataRange
    width = highNormalized - lowNormalized
    widthDistance = realDataPercentage * width
    return lowNormalized + widthDistance

def deNormalizeOrdinal(lowData,highData,lowNormalized,highNormalized,normalizedValue):
    widthDistance = normalizedValue - lowNormalized
    widthPercentage = widthDistance / (highNormalized - lowNormalized)
    cataegoryNumber = (highData - lowData) * widthPercentage
    return cataegoryNumber

def normalizedQuantitative(lowData,highData,lowNormalized,highNormalized,value):
    dataRange = highData - lowData
    normalizedRange = highNormalized - lowNormalized
    dRange = value - lowData
    dPct = dRange / dataRange
    dNorm = normalizedRange * dPct
    return lowNormalized + dNorm


def deNormalizeQuantitative(lowData,highData,lowNormalized,highNormalized,normalizedValue):
    distanceFromLowerBound = normalizedValue - lowNormalized
    dRange = distanceFromLowerBound/(highNormalized-lowNormalized)
    distanceActual = dRange * (highData-lowData)
    distanceRelative = lowData + distanceActual
    return distanceRelative


################ UNIT TEST ######################################
def unit_test():
    normalizedValue = normalizedOrdinal(0.0,14.0,-1.0,1.0,7.0)
    print("Normalized Value is " + str(normalizedValue))
    print(deNormalizeOrdinal(0.0,14.0,-1.0,1.0,normalizedValue))

    x = normalizedQuantitative(100.0,4000.0,-1.0,1.0,1000.0)
    print(deNormalizeQuantitative(100.0,4000.0,-1.0,1.0,x))




unit_test()
          
    
