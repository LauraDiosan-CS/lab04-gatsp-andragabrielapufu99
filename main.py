from City import City
from GA import GA
def readData():
    listOfCities = []
    file = open("berlin52.txt","r")
    content =  file.read().strip().split("\n")
    index = 0
    for i in range(6,len(content)-1):
        params = content[i].split(" ")
        nameCity = params[0]
        xCoordCity = float(params[1])
        yCoordCity = float(params[2])
        city = City(index,nameCity,xCoordCity,yCoordCity)
        listOfCities.append(city)
        index += 1
    file.close()
    return listOfCities
def readMatrix(filename):
    try:
        file = open(filename, "r")
        content = file.read().split("\n")
        n = int(content[0])
        matrix = []
        for i in range(1, n + 1):
            line = content[i]
            elems = line.strip().split(",")
            row = []
            for elem in elems:
                row.append(int(elem))
            matrix.append(row)
        file.close()
        return matrix
    except IOError as ie:
        raise ie

def main():
    gaParam = {}  # dictionar pt parametrii algoritmului genetic
    gaParam['dimensiunePopulatie'] = 250
    gaParam['numarGeneratii'] = 1500

    probParam = {}  # dictionar pt parametrii problemei
    cities = readData()
    matrix =[]
    for i in range(len(cities)):
        row = []
        for j in range(len(cities)):
            d = cities[i].measureDistance(cities[j])
            row.append(d)
        matrix.append(row)

    probParam['matrix'] = matrix
    probParam['noNodes'] = len(matrix)
    ga = GA(gaParam, probParam)
    ga.initializarePopulatie()
    solution = ga.generational()
    print(solution)


main()
