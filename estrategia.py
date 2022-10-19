import numpy as np
from datos import datos
from abc import ABCMeta,abstractmethod
import math
import random
import time
from heapq import nlargest


class estrategia(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def choose(self, datos, usuario, epoca):
        return 0

class EpsilonGreedyPolicy(estrategia):
    epsilon = 0

    def __init__(self, epsilon):
        self.epsilon = epsilon

    def __str__(self):
        return "EGreedy"

    def choose(self, datos, usuario, epoca):
        if np.random.random() < self.epsilon:
            return random.choice(list(datos.porRecomendar[usuario]))
        else:
            return datos.getItemPuntuacionMaxima(usuario)

    def update(self, dataset, usuario, result):
        dataset.items[result][0] += 1

class GreedyPolicy(estrategia):

    def __init__(self):
        return

    def __str__(self):
        return 'Greedy'

    def choose(self, datos, usuario, epoca):
        return datos.getItemPuntuacionMaxima(usuario)

    def update(self, dataset, usuario, result):
        dataset.items[result][0] += 1


class RandomPolicy(estrategia):

    def __init__(self):
        return

    def __str__(self):
        return 'Random'

    def choose(self, datos, usuario, epoca):
        return random.choice(list(datos.porRecomendar[usuario]))

    def update(self, dataset, usuario, result):
        dataset.items[result][0] += 1


class UCBPolicy(estrategia):
    gamma = 0
    datos = 0
    epoca = 0

    def __init__(self, gamma):
        self.gamma = gamma

    def __str__(self):
        return 'UCB'

    def choose(self, datos, usuario, epoca):
        self.datos = datos
        self.epoca = epoca

        maximum = max(datos.porRecomendar[usuario], key = self.calcular)
        return maximum

    def calcular(self, k):
        if self.datos.items[k][1] == 0:
            return 0
        else:
            porcentajeAcierto = self.datos.getPorcentajeAcierto(k)
            exploration = math.sqrt(self.gamma * np.log(self.epoca) / self.datos.items[k][1])

            return porcentajeAcierto + exploration

    def update(self, dataset, usuario, result):
        dataset.items[result][0] += 1

class ThompsonSamplingPolicy(estrategia):
    alfaCero = 1
    betaCero = 1
    #{Item : [0,1)]}
    betaDist = {}
    k = 0
    contador = 0

    def __init__(self, a, b, k):
        self.alfaCero = a
        self.betaCero = b
        self.k = k
        self.contador = k

    def __str__(self):
        return 'Thompson'

    def reCalcular(self, datos):
        for k in datos.items.keys():
            self.betaDist[k] = random.betavariate(datos.items[k][0] + self.alfaCero, datos.items[k][1] - datos.items[k][0] + self.betaCero)
        return

    def choose(self, datos, usuario, epoca):
        if self.contador == self.k:
            self.contador = 0
            self.reCalcular(datos)
        self.contador += 1
        maximum = max(datos.porRecomendar[usuario], key = self.betaDist.get)
        #Recalcular el item recomendado
        self.betaDist[maximum] = random.betavariate(datos.items[maximum][0] + self.alfaCero, datos.items[maximum][1] - datos.items[maximum][0] + self.betaCero)

        return maximum

    def update(self, dataset, usuario, result):
        dataset.items[result][0] += 1

class knn(estrategia):
    k = 0
    dataset = 0
    usuarios = 0
    items = 0
    #{Usuario, {Item, rating}}
    ratings = {}
    #{Usuario, {Usuario, interseccion}}
    similitudes = {}
    #{Usuario, numRatingsPositivos}
    numRatingsPositivos = {}
    #{Item, [Usuarios]}
    usuariosPuntuadoItem = {}

    def __init__(self, dataset, k, usuarios, items):
        self.k = k
        self.dataset = dataset
        self.usuarios = usuarios
        self.items = items

        #Interseccion |u| y |v|
        for u in usuarios:
            self.ratings[u] = {}
            self.similitudes[u] = {}
            self.numRatingsPositivos[u] = 0
            for v in usuarios:
                if u != v:
                    self.similitudes[u][v] = 0

        for i in items:
            self.usuariosPuntuadoItem[i] = []

    def __str__(self):
        return 'Knn'

    def choose(self, datos, usuario, epoca):
        self.dataset = datos
        result = {}
        usuariosSimilares = self.getTopK(usuario, self.k)

        for v in usuariosSimilares:
            interseccion = self.similitudes[usuario][v]
            try:
                similitud = interseccion / (self.numRatingsPositivos[usuario] + self.numRatingsPositivos[v] - interseccion)
            except:
                similitud = 0

            items = self.ratings[v].keys()
            keys = list(items)

            for i in keys:
                if i not in self.dataset.yaRecomendado[usuario]:
                    if i not in result:
                        result[i] = 0
                    if float(self.ratings[v][i]) > 3.0:
                        result[i] += similitud

        if not result:
            return random.choice(list(self.dataset.porRecomendar[usuario]))
        else:
            return max(result)

    def update(self, dataset, usuario, result):
        dataset.items[result][0] += 1
        self.ratings[usuario][result] = 5.0
        self.usuariosPuntuadoItem[result].append(usuario)
        self.numRatingsPositivos[usuario] += 1
        for u in self.usuariosPuntuadoItem[result]:
            intersecc = len(list(set(self.ratings[usuario]).intersection(self.ratings[u])))
            self.similitudes[usuario][u] = intersecc
            self.similitudes[u][usuario] = intersecc

    def getTopK(self, usuario, k):
        keys = list(self.similitudes[usuario])
        random.shuffle(keys)
        kHighest = nlargest(k , keys, key = self.similitudes[usuario].get)
        return kHighest
