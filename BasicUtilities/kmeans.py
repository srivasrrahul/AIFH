import distance
import random
from distance import euclidean

class Observation(object):
    def __init__(self,observation):
        self.observation = list(observation)
        self.clusterId = -1

    def getObservation(self):
        return self.observation

    def getValue(self,index):
        return self.observation[index]

    def updateCluster(self,clusterId):
        self.clusterId = clusterId

    def getClusterId(self):
        return self.clusterId
        
class Cluster(object):
    def __init__(self,dataLength):
        self.observationLst = []
        self.dataLength = dataLength
        self.centroid = []
        
    def getDataLength(self):
        return self.dataLength

    def addObservation(self,observation):
        self.observationLst.append(observation)

    def calculateCentroid(self):
        self.centroid = []

        for i in range(0,self.dataLength):
            x = 0.0
            for observation in self.observationLst:
                #print("Data Length is "+str(self.dataLength))
                x = x + observation.getValue(i)
            self.centroid.append(x)

        if len(self.observationLst) > 0:
            for i in range(0,len(self.centroid)):
                self.centroid[i] = self.centroid[i] / len(self.observationLst)
            
        return self.centroid

    def getCentroid(self):
        return self.centroid
    
    def getObservations(self):
        return self.observationLst
        

def assignment(clusters,findNearestCluster):
    updatedClusters = list(clusters)
    done = True
    for clusterId in range(0,len(clusters)):
        j = 0
        for observation in clusters[clusterId].getObservations():
            targetCluster,distance = findNearestCluster(observation,clusters)
            if targetCluster != observation.getClusterId():
                updatedClusters[clusterId].getObservations()[j].updateCluster(targetCluster)
                observation = updatedClusters[clusterId].getObservations().pop(j)
                updatedClusters[targetCluster].addObservation(observation)
                
                done = False

            j = j + 1
                
    
    return done,updatedClusters


def findNearestClusterAlgo(observation,clusters):
    minDistance = 100000.0 #max value
    minClusterId = 0
    clusterId = 0
    for cluster in clusters:
        centroid = cluster.getCentroid()
        distance = euclidean(observation.getObservation(),centroid,cluster.getDataLength())
        if distance < minDistance:
            minDistance = distance
            minClusterId = clusterId

        clusterId = clusterId + 1
    
    return minClusterId,minDistance

            
def update(clusters):
    for cluster in clusters:
        cluster.calculateCentroid()

    return clusters


def fillNonEmptyClusters(clusters):
    i = 0
    for cluster in clusters:
        observations = cluster.getObservations()
        if (len(observations) == 0):
            print("Cluster with index " + str(i) + " has 0 length")
            done = False
            while (done == False):
                sourceIndex = random.randint(0,len(clusters)-1)
                if (sourceIndex != i):
                    sourceCluster = clusters[sourceIndex]
                    sourceObservationLst = sourceCluster.getObservations()
                    if (len(sourceObservationLst) > 1):
                        #Remove a random element from observation
                        indexToBeRemoved = randmom.randint(0,len(sourceObservationLst)-1)
                        observationToBeRemoved = sourceObservationLst[indexToBeRemoved]
                        observationToBeRemoved.updateCluster(i)
                        observations.append(observationToBeRemoved)
                        sourceObservationLst.pop(indexToBeRemoved)
                        done = True

        i = i + 1


    
def repeat(clusters):
    while 1:
        done,clusters = assignment(clusters,findNearestClusterAlgo)
        if done == True:
            print("Algo finished")
            return clusters
        else:
            print("Algo continuing")
            clusters = update(clusters)
        
        
        
def randomInitialization(observationLst,observationDataLength,clusterCount):
    clusters = []
    for i in range(0,clusterCount):
        c = Cluster(observationDataLength)
        clusters.append(c)
    

    for observation in observationLst:
        clusterIndex = random.randint(0,clusterCount-1)
        obs = Observation(observation)
        obs.updateCluster(clusterIndex)
        clusters[clusterIndex].addObservation(obs)

    fillNonEmptyClusters(clusters)
    update(clusters)
    return clusters


#Unit test to be added later
def unit_test():
    fd = open("irisdataset.csv","r")
    text = fd.readline()
    observationLst = []
    while text != "":
        text = fd.readline()
        if text == "":
            break

        text = text.replace("\r","")
        text = text.replace("\n","")
        #print(text)
        lst = text.split(",")
        x=[]
        for element in lst:
            try:
                number = float(element)
                x.append(number)
            except:
                x.append(element)
                break
        observationLst.append(x)

    clusters = randomInitialization(observationLst,len(observationLst[0])-1,3)
    repeat(clusters)
    for cluster in clusters:
        print("Inside a new Cluster")
        print(str(cluster.getCentroid()))
        for observation in cluster.getObservations():
            print(observation.getObservation())

    #print(str(observationLst))
    
if __name__ == "__main__":
    unit_test()
    
    
    
    
        
                
                
                
            
