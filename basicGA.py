"""
Created on Mon Oct 28 15:01:19 2019

@author: mustafa-ozer
"""

import random

N = 50 # number of bits in the string
P = 50  # population size
mutationRate = 0.02
maxGen = 50
targetFitness = 50
averageFitnesses = []
bestFitnesses = []

class individual():
    def __init__(self):
        self.genes = []
        self.fitness = []

        for i in range(0, N):
            self.genes.append(random.randrange(0, 2, 1))

    def getGenes(self):
        return self.genes

    def getFitness(self):
        self.fitness = 0
        for i in range(N):
            if self.genes[i] == 1:
                self.fitness += 1
        return self.fitness


    def __str__(self):
        return self.genes.__str__()

    def returncertainGene(self,i):
        return self.genes[i]

class Population():
    def __init__(self,size):
        self.pop = []
        i = 0
        while i < size:
            self.pop.append(individual())
            i += 1


    def getPopulation(self):
        return self.pop
    
    
class geneticAlgorithm():
    

    def tournamentSelection(pop):
        offspring = Population(0)
        i = 0
        while i < P:
            parent1 = random.choice(pop.pop)
            parent2 = random.choice(pop.pop)
            if(parent1.getFitness() > parent2.getFitness()):
                offspring.pop.append(parent1)
            else:
                offspring.pop.append(parent2)
            i += 1
        offspring = geneticAlgorithm.crossoverPop(offspring)
        offspring = geneticAlgorithm.mutatePop(offspring)
        return offspring


    def mutatePop(pop):
        offspring = Population(0)
        for i in range(P):
            offspring.pop.append(geneticAlgorithm.mutateIndiv(pop.getPopulation()[i]))
        return offspring


    def mutateIndiv(indiv):
        for i in range(0,N):
            if mutationRate > random.random():
                if indiv.genes[i] == 1:
                    indiv.genes[i] = 0
                else:
                    indiv.genes[i] = 1
        return indiv


    def crossoverPop(pop):
        crossoverpopulation = Population(0)
        counter = 0 
        for i in range(0, int(P/2)):
            indiv1 = pop.getPopulation()[counter]
            indiv2 = pop.getPopulation()[counter + 1]
            mixed1, mixed2 = geneticAlgorithm.crossoverIndiv(indiv1,indiv2)
            crossoverpopulation.pop.append(mixed1)
            crossoverpopulation.pop.append(mixed2)
            counter += 1
        return crossoverpopulation     
    
    def crossoverIndiv(indiv1, indiv2):
        cross = individual()
        cross2 = individual()
        cross.genes.clear()
        cross2.genes.clear()
        breakoffpoint = random.randint(1, P)
        i = 0
        while i < P:
            if i < breakoffpoint:
                cross.genes.append(indiv1.getGenes()[i])
                cross2.genes.append(indiv2.getGenes()[i])
            else:
                cross.genes.append(indiv2.getGenes()[i])
                cross2.genes.append(indiv1.getGenes()[i])
            i += 1
        
        return cross, cross2     
    
    
def findBest(pop):
    pop.getPopulation().sort(key=lambda x: x.getFitness(), reverse=True)
    best = pop.getPopulation()[0]
    
    return best
    
    
        
   
def print_Population(pop,gen_number):
    print("\nGeneration #: ", gen_number, "/ best fitness: ", pop.getPopulation()[0].getFitness(), "\n")
    counter = 1
    totalFitness = 0
    for i in pop.getPopulation():
        print("individual :" , counter, " : ", i, " Fitness: ", i.getFitness())
        totalFitness += i.getFitness()
        counter += 1
    average = totalFitness / P
    averageFitnesses.append(average)
    bestFitnesses.append(pop.getPopulation()[0].getFitness())
    print("Average Fitness is: ", average)


def main():
    genNumber = 1
    population = Population(P)
    population.getPopulation().sort(key=lambda x: x.getFitness(), reverse=True)
    print_Population(population, genNumber)
    
    while genNumber < maxGen :
        best = findBest(population)
        if population.getPopulation()[0].getFitness() == N:
            break
        population = geneticAlgorithm.tournamentSelection(population)
        population.getPopulation().sort(key=lambda x: x.getFitness(), reverse=True)
        population.pop.remove(population.getPopulation()[P-1])
        population.pop.append(best)

        genNumber += 1


        print_Population(population,genNumber)

        import matplotlib.pyplot as plt
        plt.plot(bestFitnesses)
        plt.plot(averageFitnesses)
        plt.xlabel('Gen')
        plt.ylabel('Best Fitness')
        plt.show()


main()