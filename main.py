from GA import GA
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
    try:
        gaParam = {}  # dictionar pt parametrii algoritmului genetic
        gaParam['dimensiunePopulatie'] = 10
        gaParam['numarGeneratii'] = 100

        probParam = {}  # dictionar pt parametrii problemei
        print("File : matrix.txt")
        matrix = readMatrix("matrix.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga1 = GA(gaParam,probParam)
        ga1.initializarePopulatie()
        solution = ga1.generational()
        print(solution)

        print("\nFile : easy_03_tsp.txt")
        matrix1 = readMatrix("easy_03_tsp.txt")
        probParam['matrix'] = matrix1
        probParam['noNodes'] = len(matrix1)
        ga2 = GA(gaParam, probParam)
        ga2.initializarePopulatie()
        solution = ga2.generational()
        print(solution)

        print("\nFile : medium_01_tsp.txt")
        matrix = readMatrix("medium_01_tsp.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga3 = GA(gaParam, probParam)
        ga3.initializarePopulatie()
        solution = ga3.generational()
        print(solution)

        print("\nFile : hard_01_tsp.txt")
        matrix = readMatrix("hard_01_tsp.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga4 = GA(gaParam, probParam)
        ga4.initializarePopulatie()
        solution = ga4.generational()
        print(solution)

        print("\nFile : easy1.txt")
        matrix = readMatrix("easy1.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga5 = GA(gaParam, probParam)
        ga5.initializarePopulatie()
        solution = ga5.generational()
        print(solution)

        print("\nFile : easy2.txt")
        matrix = readMatrix("easy2.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga6 = GA(gaParam, probParam)
        ga6.initializarePopulatie()
        solution = ga6.generational()
        print(solution)

        print("\nFile : easy3.txt")
        matrix = readMatrix("easy3.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga7 = GA(gaParam, probParam)
        ga7.initializarePopulatie()
        solution = ga7.generational()
        print(solution)

        print("\nFile : mediumF.txt")
        matrix = readMatrix("mediumF.txt")
        probParam['matrix'] = matrix
        probParam['noNodes'] = len(matrix)
        ga8 = GA(gaParam, probParam)
        ga8.initializarePopulatie()
        solution = ga8.generational()
        print(solution)

    except IOError as ie:
        print(ie)
main()