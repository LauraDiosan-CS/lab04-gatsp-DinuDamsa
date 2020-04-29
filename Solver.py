from domain.Solution import Solution


class Solver:
    def __init__(self, repo):
        self.__repo = repo

    def solveAll(self):
        with open("solutionn.txt", "w") as file:
            data = self.__repo.getData()
            solTSP = self.solveTsp()

            solPath = self.solveMinDist(data.getSrc() - 1, data.getDestination() - 1)
            file.write(str(solTSP))
            file.write("\n")
            file.write(str(solPath))

    def solveTsp(self):
        return self.__detPathCost(self.__repo.getData().getMatrix(), 0)

    def solveMinDist(self, src, destination):
        return self.__detPathCost(self.__repo.getData().getMatrix(), src, destination)

    def __detPathCost(self, matrix, start, end=None):
        CONST_INF = 9999999999
        actualNode = start
        visited = [actualNode]
        cost = 0
        noOfNodes = len(matrix)
        while end not in visited and len(visited) < noOfNodes:
            lst = [el for el in matrix[actualNode]]
            while lst.index(min(lst)) in visited:
                lst[lst.index(min(lst))] = CONST_INF
            cost += min(lst)
            actualNode = lst.index(min(lst))
            visited.append(lst.index(min(lst)))
        if end is None:
            cost += matrix[visited[-1]][start]
        return Solution(visited, cost)
