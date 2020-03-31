import sys
import random

class Cromozom:
    def __init__(self,reprezentare,fitness):
        self.__reprezentare = reprezentare
        self.__fitness = fitness

    def getReprezentare(self):
        return self.__reprezentare

    def getFitness(self):
        return self.__fitness

    def setReprezentare(self,newReprez):
        self.__reprezentare = newReprez

    def setFitness(self,newFitness):
        self.__fitness = newFitness

    def __str__(self):
        return "Reprezentare :  " + str(self.__reprezentare) + " Fitness : " + str(self.__fitness) + "\n"
