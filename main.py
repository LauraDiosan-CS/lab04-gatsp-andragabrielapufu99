import sys
from Utils import TSP
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
                if elem == "INT_MAX":
                    row.append(sys.maxsize)
                else:
                    row.append(int(elem))
            matrix.append(row)
        file.close()
        return matrix
    except IOError as ie:
        raise ie
def main():
    try:
        print("File : matrix.txt")
        matrix = readMatrix("matrix.txt")
        V = len(matrix)
        TSP(matrix,V)

        print("\nFile : easy_03_tsp.txt")
        matrix = readMatrix("easy_03_tsp.txt")
        V = len(matrix)
        TSP(matrix, V)

        print("\nFile : medium_01_tsp.txt")
        matrix = readMatrix("medium_01_tsp.txt")
        V = len(matrix)
        TSP(matrix, V)

        print("\nFile : hard_01_tsp.txt")
        matrix = readMatrix("hard_01_tsp.txt")
        V = len(matrix)
        TSP(matrix, V)
    except IOError as ie:
        print(ie)
main()