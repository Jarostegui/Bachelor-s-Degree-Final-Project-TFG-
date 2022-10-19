import numpy as np
from datos import datos
import estrategia as ES
import matplotlib.pyplot as plt
import entorno as EN
import time
import random
import os
random.seed()

def ejecutar():
	numIteraciones = 100
	threshold = 3.0

	k = 30
	epsilon = 0.1
	gamma = 0.01

	alfa = 1
	beta = 100
	iteracionesActualizar = 2

	dataset = datos('Datos/ratingsML1MTrain.csv', 'Datos/tags1M.csv')
	entorno = EN.entorno(numIteraciones, threshold)

	#estrategia = ES.EpsilonGreedyPolicy(epsilon)

	#estrategia = ES.RandomPolicy()

	#estrategia = ES.GreedyPolicy()

	#estrategia = ES.UCBPolicy(gamma)

	#estrategia = ES.ThompsonSamplingPolicy(alfa, beta, iteracionesActualizar)

	estrategia = ES.knn(dataset, k, dataset.ratings, dataset.items)

	aciertosPlot, novedadPlot = ejecucion(dataset, estrategia, entorno, numIteraciones, threshold, epsilon, gamma, k, iteracionesActualizar)

	fileAciertos = open("ResultadosTFG/KNN/30/aciertosPlot.txt", "w")
	fileNovedad = open("ResultadosTFG/KNN/30/novedadPlot.txt", "w")
	#fileDatos = open("ResultadosTFG/ComparativaAlg/KNN10/datos.txt", "w")
	#fileDatos.close()
	#
	for i in aciertosPlot:
		fileAciertos.write(str(i)+"\n")
	fileAciertos.close()

	for i in novedadPlot:
		fileNovedad.write(str(i)+"\n")
	fileNovedad.close()


def ejecucion(dataset, estrategia, entorno, numIteraciones, threshold, epsilon, gamma, k, iteracionesActualizar):
	print("\n")
	print("#################################")
	print(estrategia)
	print("numIteraciones: "+str(numIteraciones))
	print("threshold: "+str(threshold))
	print("epsilon: "+str(epsilon))
	print("gamma: "+str(gamma))
	print("k:" +str(k))
	print("iteracionesActualizar: "+str(iteracionesActualizar))

	return entorno.recomendar(dataset, estrategia)

if __name__ == "__main__":
	print("\n")
	print("************************************************")
	print("*******************EJECUTANDO*******************")
	print("************************************************")
	ejecutar()
