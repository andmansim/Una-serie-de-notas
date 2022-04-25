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