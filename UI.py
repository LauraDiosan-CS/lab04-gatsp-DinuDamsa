import matplotlib.pyplot as plt

from dataLayer.Repository import Repository, parseFile
from logicLayer.GA import GA
from logicLayer.Solver import Solver

repo = Repository('D:\\AN2SEM2\\AI\\lab4\\input.txt')
solv = Solver(repo)
solv.solveAll()

gaParam = {'popSize': 4, 'noGen': 10000}
# matrix = repo.getData().getMatrix()
matrix = parseFile()


def fcEval(repres):
    val = 0
    for i in range(len(repres) - 1):
        val += matrix[repres[i]][repres[i + 1]]
    val += matrix[repres[-1]][repres[0]]
    return val


problParam = {'function': fcEval, 'noNodes': len(repo.getData().getMatrix())}

# store the best/average solution of each iteration (for a final plot used to anlyse the GA's convergence)
allBestFitnesses = []
allAvgFitnesses = []
generations = []

ga = GA(gaParam, problParam)
ga.initialisation()
ga.evaluation()

for g in range(gaParam['noGen']):
    # plotting preparation
    allPotentialSolutionsX = [c.repres for c in ga.population]
    allPotentialSolutionsY = [c.fitness for c in ga.population]
    bestSolX = ga.bestChromosome().repres
    bestSolY = ga.bestChromosome().fitness
    allBestFitnesses.append(bestSolY)
    allAvgFitnesses.append(sum(allPotentialSolutionsY) / len(allPotentialSolutionsY))
    generations.append(g)
    ga.oneGenerationElitism()

    bestChromo = ga.bestChromosome()
    print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(
        bestChromo.fitness))

print(min(allBestFitnesses))
best, = plt.plot(generations, allBestFitnesses, 'ro', label='best')
mean, = plt.plot(generations, allAvgFitnesses, 'bo', label='mean')
plt.legend([best, (best, mean)], ['Best', 'Mean'])
plt.show()
