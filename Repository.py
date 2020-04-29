from domain.Input import Input


class Repository:
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__data = None

    def getData(self):
        if self.__data is None:
            self.__data = self.__loadFromFile()
        return self.__data

    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            matrix = []
            no = int(f.readline())
            for i in range(no):
                matrix.append([float(value) for value in f.readline().split(",")])
            source = 0
            dest = 0
            return Input(matrix, source, dest)


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def parseFile():
    n = 51
    tpl = []
    with open("D:\\AN2SEM2\\AI\\lab4\\codedFile.txt", "r") as f:
        for line in range(n):
            node, x, y = f.readline().split(" ")
            tpl.append((int(node), int(x), int(y)))

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    print(tpl)
    for pct1 in tpl:
        for pct2 in tpl:
            # print(pct2[2])

            matrix[pct1[0] - 1][pct2[0] - 1] = dist(pct1[1], pct2[1], pct1[2], pct2[2])
            matrix[pct1[0] - 1][pct2[0] - 1] = dist(pct1[1], pct2[1], pct1[2], pct2[2])
    return matrix
