import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', size=18)
fig, axes = plt.subplots(1,2)

fig.suptitle("Comparativa Algoritmos")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/EGreedy0.1/aciertosPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[0].plot(aciertosPlot, "y", label="Ɛ-Greedy0.1")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/Greedy/aciertosPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[0].plot(aciertosPlot, "b", label="Greedy")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/KNN10/aciertosPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[0].plot(aciertosPlot, "g", label="u-knn10")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/Random/aciertosPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[0].plot(aciertosPlot, "r", label="Random")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/Thompson1-100-2/aciertosPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[0].plot(aciertosPlot, "k", label="Thompson1-100-2")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/UCB0.01/aciertosPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[0].plot(aciertosPlot, "chocolate", label="UBC0.01")


##################################################################################################################################################################

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/EGreedy0.1/novedadPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[1].plot(aciertosPlot, "y", label="Ɛ-Greedy0.1")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/Greedy/novedadPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[1].plot(aciertosPlot, "b", label="Greedy")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/KNN10/novedadPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[1].plot(aciertosPlot, "g", label="u-knn10")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/Random/novedadPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[1].plot(aciertosPlot, "r", label="Random")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/Thompson1-100-2/novedadPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[1].plot(aciertosPlot, "k", label="Thompson1-100-2")

aciertosPlot = []
fichero = open("ResultadosTFG/ComparativaAlg/UCB0.01/novedadPlot.txt", 'r')
lineas = fichero.read().splitlines()
for l in lineas:
    aciertosPlot.append(float(l))
axes[1].plot(aciertosPlot, "chocolate", label="UBC0.01")


axes[0].set_ylabel("Aciertos")
axes[0].set_xlabel("Iteración")
axes[0].set_xlim(xmin=0)
axes[0].set_ylim(ymin=0)

axes[1].set_ylabel("Novedad")
axes[1].set_xlabel("Iteración")
axes[1].set_ylim([0, 1])

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc=(0.15, 0.60))

plt.show()


# fichero = open("ResultadosTFG/Thompson/1-100/tiempos.txt", 'r')
# lineas = fichero.read().splitlines()
# iter = []
# tiempo = []
# for l in lineas:
#     l = l.split(" ")
#     iter.append(float(l[0]))
#     tiempo.append(float(l[1]))
#
# plt.ylabel("Segundos")
# plt.xlabel("κ")
# plt.plot(iter, tiempo, marker='o')
# plt.show()
