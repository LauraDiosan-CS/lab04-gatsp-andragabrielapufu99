import sys
import random

class Cromozom:
    def __init__(self):
        self.__reprezentare = []
        self.__fitness = 0

    def createCromozom(self,V):
        reprez = []
        while True:
            if len(reprez)== V:
                reprez.append(reprez[0])
                break
            temp = random.randint(0,V-1)
            if temp not in reprez:
                reprez.append(temp)
        self.__reprezentare = reprez

    def calcFitness(self,matrix,reprez):
        f = 0
        for i in range(len(reprez)-1):
            if matrix[reprez[i]][reprez[i+1]] == sys.maxsize:
                return sys.maxsize
            f += matrix[reprez[i]][reprez[i+1]]
        return f

    def getReprezentare(self):
        return self.__reprezentare

    def getFitness(self):
        return self.__fitness

    def setReprezentare(self,newReprez):
        self.__reprezentare = newReprez

    def setFitness(self,newFitness):
        self.__fitness = newFitness

    def lessthan(self,otherCromo):
        return self.__fitness < otherCromo.getFitness()

    def mutatedGene(self,V):
        #swap
        newR = self.__reprezentare
        while True:
            r = random.randint(1,V-1)
            r1 = random.randint(1,V-1)
            if r!=r1 :
                aux = newR[r]
                newR[r] = newR[r1]
                newR[r1] = aux
                break
        return newR

