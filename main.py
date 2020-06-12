"""
Act-4 : Simuler la propagation d'une onde périodique
Juin 2020 -
Pour arrêter ctrl+C si depuis terminal, sinon avec l'arrêt de l'éditeur
"""


#####IMPORTS#####
from matplotlib import pyplot
from math import *


#####VARIABLES#####
L = 1000  # Longueur de la corde
longueurOnde = int(L/3)  # Longueur d'onde (inférieur à L/2)
f = 20  # fréquence minimale
periode = int(10**3/f)  # periode (1/f)
amplitude = 200  # Amplitude (arbitraire)
scale = 20  # Echelle pour optimisation RAM
liste_x = []
liste_y = []


#####GRAPHIQUE#####
pyplot.clf()
pyplot.axis([0,L,(-L/2),(L/2)])
pyplot.xlabel("x (mm)")
pyplot.ylabel("y (mm)")
pyplot.title("propagation d'une onde sinusoïdale")


#####FONCTIONS#####
"""
Tracé de la première page
"""
for i in range(L):  # Calcul des premières valeurs sans tracé, pour meilleures performances
    liste_x.append(i)
    liste_y.append(amplitude*(sin((2*pi)/(periode)-(2*pi*i)/(longueurOnde))))
for i in range(int(len(liste_x)/scale)):  # Optimisation du tracé, selon l'échelle
    pyplot.plot(liste_x[:scale*i],liste_y[:scale*i])
    pyplot.pause(0.001)

"""
Tracé infini, à désactiver si besoin
"""
i = L-1
while 1:
    i += 1
    liste_x.append(i)
    liste_y.append(amplitude*(sin((2*pi)/(periode)-(2*pi*i)/(longueurOnde))))
    if i%scale == 0:
        pyplot.axis([i - L, i, (-L / 2), (L / 2)])
        pyplot.plot(liste_x[:scale * i], liste_y[:scale * i])
        pyplot.pause(0.01)



