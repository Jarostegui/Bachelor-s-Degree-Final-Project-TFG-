import numpy as np
from datos import datos
import estrategia
import matplotlib.pyplot as plt
import time
import random

class entorno(object):
	numIteraciones = 0
	threshold = 0

	def __init__(self, numIteraciones, threshold):
		self.numIteraciones = numIteraciones
		self.threshold = threshold
		return

	def recomendar(self, dataset, estrategiaActual):
		start = time.time()

		aciertosList = []
		novedadList = []
		ildList = []
		unexpectednessList = []
		giniList = []

		novedadPlot = []
		recomendPlot = []
		aciertosPlot = []
		novedadActual = 1

		epoca = 0
		aciertos = 0
		intentos = 0

		for j in range(self.numIteraciones):
			keys = list(dataset.ratings.keys())
			random.shuffle(keys)

			print("Epoca: "+str(j+1))

			for usuario in keys:
				timeA = []
				epoca += 1
				result = estrategiaActual.choose(dataset, usuario, epoca)
				intentos += 1

				if result in dataset.ratings[usuario].keys():
					dataset.items[result][1] += 1
					if float(dataset.ratings[usuario][result]) > self.threshold:
						estrategiaActual.update(dataset, usuario, result)
						aciertos += 1

				#Novedad: Media de 1-popularidad de todos los items recomendados
				numerador = (1 - dataset.getPorcentajeAcierto(result)) - novedadActual
				denominador = (j+1) * len(dataset.yaRecomendado)
				novedadActual = novedadActual + numerador / denominador

				dataset.yaRecomendado[usuario].append(result)
				dataset.porRecomendar[usuario].remove(result)
				aciertosPlot.append(aciertos)

				novedadPlot.append(novedadActual)
				recomendPlot.append(epoca)

		aciertosFinal = aciertos/intentos

		#Unexpectedness@10
		for usuario in dataset.ratings.keys():
			unexpectednessList.extend(dataset.Unexpectedness(usuario))

		#ILD@10
		for usuario in dataset.ratings.keys():
			ildList.extend(dataset.ILD(usuario))

		#Gini
		listaGiniAux = []
		listaGiniAux = sorted(dataset.items, key=dataset.getIntentosItem)
		contador = 1
		for item in listaGiniAux:
			valueGini = (2 * contador - len(dataset.items) - 1) * (dataset.items[item][1] / (self.numIteraciones * len(dataset.yaRecomendado)))
			contador += 1
			giniList.append(valueGini)

		end = time.time()
		#γ
		#Ɛ
		#α
		#β
		#κ
		plt.plot(recomendPlot, novedadPlot)
		plt.title('k = 10')
		plt.ylabel('Novedad')
		plt.xlabel('Iteraciones')
		plt.ylim(ymin=0, ymax=1)
		plt.show()

		plt.plot(recomendPlot, aciertosPlot)
		plt.title('k = 10')
		plt.ylabel('Aciertos')
		plt.xlabel('Iteraciones')
		plt.ylim(ymin=0)
		plt.xlim(xmin=0)
		plt.show()

		print("______")
		print("ILD@10: "+str(round(np.mean(ildList), 4)))
		print("Unexpectedness@10: "+str(round(np.mean(unexpectednessList), 4)))
		print("Novedad: "+str(round(novedadActual, 4)))
		print("Gini: "+str(round(np.mean(giniList), 4)))
		print("Aciertos: "+str(round(aciertosFinal, 4)))
		print(str(round(end - start, 4))+"s")

		return aciertosPlot, novedadPlot
