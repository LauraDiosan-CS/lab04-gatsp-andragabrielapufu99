from Cromozom import Cromozom

POP_SIZE = 10
global V

def cooldown(temp):
    return (90*temp)/100

def TSP(matrix,N):
    V = N
    #numarul generatiei
    gen = 1

    #numarul de iteratiial unei generatii
    gen_thres = 5

    population = []

    #creez o populatie
    for i in range(POP_SIZE):
        temp = Cromozom()
        temp.createCromozom(V)
        temp.setFitness(temp.calcFitness(matrix,temp.getReprezentare()))
        population.append(temp)

    print("POPULATIA INITIALA")
    for x in population:
        print("Cromozom : "+str(x.getReprezentare())+" Fitness : "+str(x.getFitness()))

    temperature = 10000

    while temperature>1000 and gen <= gen_thres:
        sorted(population,key=lambda x:x.getFitness())
        print("\nTemperatura curenta : "+str(temperature))
        new_population = []
        for i in range(POP_SIZE):
            p1 = population[i]
            while True:
                #caut cel mai bun copil
                new_g = p1.mutatedGene(V)
                new_cromo = Cromozom()
                new_cromo.setReprezentare(new_g)
                new_cromo.setFitness(new_cromo.calcFitness(matrix,new_cromo.getReprezentare()))

                if new_cromo.getFitness() <= population[i].getFitness():
                    #il adaug pe cel mai bun in noua populatie
                    new_population.append(new_cromo)
                    break
                else:
                    """inca nu am gasit cel mai bun copil, dar ofer sansa celorlalti 
                    gasiti pana acum de a intra in noua populatie daca probabilitatea > 0.5 
                    (pot obtine un material genetic bun din ei)"""
                    prob = pow(2.7,-1*((new_cromo.getFitness()-population[i].getFitness())/temperature))
                    if prob > 0.5:
                        new_population.append(new_cromo)
                        break

        #scad temperatura
        temperature = cooldown(temperature)
        population = new_population

        print("Generatia "+str(gen))
        for i in range(POP_SIZE):
            print("Cromozom : "+str(population[i].getReprezentare()) + " Fitnes : " + str(population[i].getFitness()))

        gen += 1 #trecem la urmatoarea generatie
