import math


class City:

    def __init__(self,index,name,x,y):
        self.__index = index
        self.__name = name
        self.__x = x
        self.__y = y

    def getIndex(self):
        return self.__index

    def getName(self):
        return self.__name

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def measureDistance(self,city):
        if city.__eq__(self):
            return 0
        # returneaza distanta dintre orasul curent si orasul dat ca parametru
        difX = city.getX()-self.__x
        difY = city.getY()-self.__y
        distance = math.sqrt(math.pow(difX,2)+math.pow(difY,2))
        return distance

    def __eq__(self, other):
        return other.getX()==self.__x and other.getY()==self.__y

    def __str__(self):
        return "Orasul "+self.__name+" cu coordonatele x="+str(self.__x)+". y="+str(self.__y)