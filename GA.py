import random
from Cromozom import Cromozom
from matplotlib import pyplot as plt
class GA:
    def __init__(self,paramGA,paramProblema):
        self.__populatie = []
        self.__paramGA = paramGA
        self.__paramProblema = paramProblema

    def initializarePopulatie(self):
        #generatia 0
        for i in range(self.__paramGA['dimensiunePopulatie']):
            reprezentareIndivid = [] # genotip cromozom
            while len(reprezentareIndivid)!=self.__paramProblema['noNodes']:
                gena = random.randint(0,self.__paramProblema['noNodes']-1)
                if gena not in reprezentareIndivid:
                    reprezentareIndivid.append(gena)
            fitnessIndivid = self.fitnessFunction(reprezentareIndivid)
            individ = Cromozom(reprezentareIndivid,fitnessIndivid)
            self.__populatie.append(individ)

    def fitnessFunction(self,reprez):
        f = 0
        matrix = self.__paramProblema['matrix']
        for i in range(len(reprez) - 1):
            f += matrix[reprez[i]][reprez[i + 1]]
        f += matrix[reprez[len(reprez)-1]][reprez[0]]
        return f

    def selectie(self):
        #selectie turnir
        limita = len(self.__populatie) * 20// 100
        vmax = 1000000
        index = 0
        for i in range(limita):
            if self.__populatie[i].getFitness() < vmax:
                vmax = self.__populatie[i].getFitness()
                index = i
        return self.__populatie[index]

    def incrucisare(self,mother,father):
        #incrucisare ordonata

        pos1 = random.randint(-1, self.__paramProblema['noNodes']-1)
        pos2 = random.randint(-1, self.__paramProblema['noNodes']-1)

        if (pos2 < pos1):
            aux = pos1
            pos1 = pos2
            pos2 = aux

        k = 0
        newrepres1 = mother.getReprezentare()[pos1: pos2]
        for el in mother.getReprezentare()[pos2:] + mother.getReprezentare()[:pos2]:
            if (el not in newrepres1):
                if (len(newrepres1) < self.__paramProblema['noNodes'] - pos1):
                    newrepres1.append(el)
                else:
                    newrepres1.insert(k, el)
                    k += 1
        descendent1 = Cromozom(newrepres1,self.fitnessFunction(newrepres1))

        newrepres2 = father.getReprezentare()[pos1: pos2]
        for el in father.getReprezentare()[pos2:] + father.getReprezentare()[:pos2]:
            if (el not in newrepres2):
                if (len(newrepres2) < self.__paramProblema['noNodes'] - pos1):
                    newrepres2.append(el)
                else:
                    newrepres2.insert(k, el)
                    k += 1
        descendent2 = Cromozom(newrepres2,self.fitnessFunction(newrepres2))
        return descendent1,descendent2

    def mutatie(self,individ):
        # mutatie prin insertie
        pos1 = random.randint(0, len(individ.getReprezentare())-1)
        pos2 = random.randint(0, len(individ.getReprezentare())-1)
        if (pos2 < pos1):
            aux = pos1
            pos1 = pos2
            pos2 = aux
        newReprezentare = individ.getReprezentare()
        el = newReprezentare[pos2]
        del newReprezentare[pos2]
        newReprezentare.insert(pos1 + 1, el)
        individ.setReprezentare(newReprezentare)
        individ.setFitness(self.fitnessFunction(newReprezentare))
        return individ

    def getPopulatie(self):
        return self.__populatie

    def getBestCromozom(self):
        minimFitness = self.__populatie[0].getFitness()
        index = 0
        for i in range(1, len(self.__populatie)):
            if self.__populatie[i].getFitness() < minimFitness:
                minimFitness = self.__populatie[i].getFitness()
                index = i
        return self.__populatie[index]

    def generational(self):

        bestFitness = self.getBestCromozom().getFitness()
        allFitness = [bestFitness]
        print("Best fitness : " +str(bestFitness))
        print("Best repres : "+str(self.getBestCromozom().getReprezentare()))
        print()
        for i in range(self.__paramGA['numarGeneratii']):
            populatieNoua = [self.getBestCromozom()]
            while (len(populatieNoua)!=self.__paramGA['dimensiunePopulatie']):
                # selectez 2 parinti
                mother = self.selectie()
                father = self.selectie()

                # obtin cei 2 descendenti prin incrucisare
                descendenti = self.incrucisare(mother, father)

                # mutez descendentii
                descendent1 = self.mutatie(descendenti[0])
                descendent2 = self.mutatie(descendenti[1])

                # selectez cel mai bun descendent
                if descendent1.getFitness() < descendent2.getFitness():
                    bestOne = descendent1
                else:
                    bestOne = descendent2

                # compar cel mai bun descendent cu parintii
                if bestOne.getFitness() > mother.getFitness():
                    if(mother not in populatieNoua):
                        bestOne = mother

                if bestOne.getFitness() > father.getFitness():
                    if father not in populatieNoua:
                        bestOne = father
                populatieNoua.append(bestOne)

            self.__populatie = populatieNoua

            b = self.getBestCromozom().getFitness()
            allFitness.append(b)
            if b!=bestFitness:
                bestFitness = b
                print("Best fitness : " + str(bestFitness))
                print("Best repres : " + str(self.getBestCromozom().getReprezentare()))
                print()

        plt.plot(allFitness, '-b', label="TSP GA Fitness")
        plt.show()
        return self.getBestCromozom()
