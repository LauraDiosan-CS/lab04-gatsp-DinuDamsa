class Input:
    def __init__(self, matrix, src, dest):
        self.__matrix = matrix
        self.__src = src
        self.__dest = dest

    def getMatrix(self):
        return self.__matrix

    def getSrc(self):
        return self.__src

    def getDestination(self):
        return self.__dest
