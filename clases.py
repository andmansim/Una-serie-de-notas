from collections import Counter
from math import *
import matplotlib.pyplot as plt



class JMPEstadisticas:

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica #columna notas

    def calculoMediaAritmetica(self):
    
        n = self.caracteristica.count()
        print(n)
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica 
    
    def calculoMediana(self):
        mediana = 0
        caracteristica = self.caracteristica.sort_values() #ordena valores
        caracteristica = caracteristica.reset_index(drop=True)
        n = self.caracteristica.count()

        par = False;
        if (n % 2 == 0):
            print("La cantidad de observaciones es par.")
            par = True

        if par:
            rango = (n / 2); 
            print("RANGO = "+str(rango))
            rangoPython = rango-1 
            valor1 = caracteristica[rangoPython] 
            valor2 = caracteristica[rangoPython+1]
            mediana = valor1 +((valor2-valor1)/2)
        else:
            rango = ((n + 1) / 2)
            rangoPython = rango - 1
            mediana = caracteristica[rangoPython]

        return [mediana, rango]
    
    def calculoModa(self):
        moda = Counter(self.caracteristica)
        return moda

    def calculoVarianzaDesviacionTipica(self):
        n = self.caracteristica.count()
        mediaAritmetica = self.caracteristica.mean()
        varianza = 0
        c3 = 0
        for valorObservacion in self.caracteristica:

            c1 = valorObservacion - mediaAritmetica
            c2 = c1 * c1
            c3 = c3 + c2

        varianza = c3 / (n - 1)

        desviacionTipica = sqrt(varianza)

        return ([varianza, desviacionTipica])