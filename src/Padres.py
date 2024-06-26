import numpy as np
import random


class Padres:

    def __init__(self, fitness, individuos, num_individuos):
        self.fitness = fitness
        self.individuos = individuos
        self.num_individuos = num_individuos


    def seleccion_padres_por_torneo(self, k):
        padres = np.empty_like(self.individuos)

        # identificar el mejor individuo
        mejor_individuo = self.individuos[np.argmin(self.fitness)]

        # garantizar que el mejor individuo pasa como padre
        padres[0] = mejor_individuo

        # seleccionar los demás padres usando torneo
        for i in range(1, self.num_individuos):
            # escogemos tres individuos aleatorios
            indices_aleatorios = random.sample(range(0, self.individuos.shape[0]), k)
            # obtenemos sus fitness
            fitness_seleccionados = [self.fitness[pos] for pos in indices_aleatorios]
            # escogemos el individuo con mejor fitness de los k elegidos (que será el menor)
            pos_mayor_fitness = 0
            indiviudo_mayor_fitness = self.individuos[indices_aleatorios[pos_mayor_fitness], :]
            for j in range(1, k):
                if fitness_seleccionados[j] < fitness_seleccionados[pos_mayor_fitness]:
                    pos_mayor_fitness = j
                    indiviudo_mayor_fitness = self.individuos[indices_aleatorios[pos_mayor_fitness], :]
            # guardamos el individuo con mayor fitness como uno de los padres
            padres[i] = indiviudo_mayor_fitness

        return padres
    
    
