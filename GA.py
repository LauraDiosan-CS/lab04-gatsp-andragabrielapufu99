import random
from Cromozom import Cromozom

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
        #selectie proportionala (ruleta)
        sorted(self.__populatie,key =lambda x:x.getFitness())
        sumaFitness = 0
        n = len(self.__populatie)
        for i in range(n):
            sumaFitness += self.__populatie[i].getFitness()
        ruleta = []
        aux = 0
        for i in range(n):
            aux += self.__populatie[i].getFitness()/sumaFitness
            ruleta.append(aux)
        alegere = random.uniform(ruleta[0],ruleta[len(ruleta)-1])

        for i in range(len(ruleta)):
            if alegere<ruleta[i]:
                return self.__populatie[i]

    def incrucisare(self,mother,father):
        #incrucisare ordonata

        child1 = [-1 for _ in range(self.__paramProblema['noNodes'])] #genotip descendent1
        child2 = [-1 for _ in range(self.__paramProblema['noNodes'])] #genotip descendent2

        #g1,g2 pozitiile subsirului ales
        g1 = random.randint(0, self.__paramProblema['noNodes']-1)
        g2 = random.randint(0, self.__paramProblema['noNodes']-1)
        while g1 == g2:
            g2 = random.randint(0, self.__paramProblema['noNodes']-1)

        if g1>g2:
            aux=g1
            g1=g2
            g2=aux

        for i in range(g1,g2+1):
            child1[i] = mother.getReprezentare()[i]
            child2[i] = father.getReprezentare()[i]

        for i in range(g2+1,len(child1)):
            if father.getReprezentare()[i] not in child1:
                child1[i] = father.getReprezentare()[i]
            if mother.getReprezentare()[i] not in child2:
                child2[i] = mother.getReprezentare()[i]
        index = 0
        for i in range(len(child1)):
            if father.getReprezentare()[i] not in child1 and -1 in child1:
                while child1[index]!=-1:
                    index += 1
                child1[index]=father.getReprezentare()[i]
        index = 0
        for i in range(len(child2)):
            if mother.getReprezentare()[i] not in child2 and -1 in child2:
                while child2[index]!=-1:
                    index += 1
                child2[index] = mother.getReprezentare()[i]

        fitnessChild1 = self.fitnessFunction(child1)
        fitnessChild2 = self.fitnessFunction(child2)

        descendent1 = Cromozom(child1,fitnessChild1)
        descendent2 = Cromozom(child2,fitnessChild2)

        return descendent1,descendent2

    def mutatie(self,individ):
        # mutatie prin interschimbare
        newReprezentare = []
        g1 = random.randint(0,len(individ.getReprezentare())-1)
        g2 = random.randint(0,len(individ.getReprezentare())-1)
        while g1==g2:
            g2 = random.randint(0, len(individ.getReprezentare())-1)
        r = individ.getReprezentare()
        aux = r[g1]
        r[g1] = r[g2]
        r[g2] = aux
        individ.setReprezentare(r)
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
        print("Best fitness : " +str(bestFitness))
        print("Best repres : "+str(self.getBestCromozom().getReprezentare()))
        print()
        for i in range(self.__paramGA['numarGeneratii']):
            populatieNoua = [self.getBestCromozom()]
            for j in range(self.__paramGA['dimensiunePopulatie']-1):
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
            if b!=bestFitness:
                bestFitness = b
                print("Best fitness : " +str(bestFitness))
                print("Best repres : " + str(self.getBestCromozom().getReprezentare()))
                print()
        return self.getBestCromozom()