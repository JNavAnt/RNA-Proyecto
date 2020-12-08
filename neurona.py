import math
from random import random

class neurona():
    entrada = [random() * 100, random() * 100]
    salida = [0, 0]


    entradaCorrecta = [1,1]
    salidaCorrecta = [0, 0]
    h1 = [0, 0]
    w1 = [[random(), random()], [random(), random()]]
    w2 = [[random(), random()], [random(), random()]]
    bias1 = [0.5, 0.5]
    bias2 = [0.5, 0.5]
    aprendizaje = 0.5

    class puntoEntrada:
        x = 0
        y = 0

        def __init__(self, x, y):
            self.x = x;
            self.y = y;

    def activacion(self, suma):
        suma = 1 / (1 + math.exp(suma))
        return suma;

    def valorCorrecto(self):
        suma = 0
        for i in range(0, len(self.h1)):
            suma = self.bias1[i]
            for j in range(0, len(self.entradaCorrecta)):
                suma += self.w1[i][j] * self.entradaCorrecta[j]
                self.h1[i] = self.activacion(suma)
        suma = 0

        for i in range(0, len(self.salidaCorrecta)):
            suma = self.bias2[i]
            for j in range(0, len(self.h1)):
                suma += self.w2[i][j] * self.h1[j]
                self.salidaCorrecta[i] = self.activacion(suma)


    def clasificacion(self):
        suma = 0
        for i in range(0, len(self.h1)):
            suma = self.bias1[i]
            for j in range(0, len(self.entrada)):
                suma += self.w1[i][j] * self.entrada[j]
                self.h1[i] = self.activacion(suma)
        suma = 0
        for i in range(0, len(self.salida)):
            suma = self.bias2[i]
            for j in range(0, len(self.h1)):
                suma += self.w2[i][j] * self.h1[j]
                self.salida[i] = self.activacion(suma)



    def df(self, x):
        derivada = self.activacion(x) * (1 - (self.activacion(x)));
        return derivada;

    def entrenamiento(self):
        dy = []
        dh = []
        error = 0
        for i in range(0, len(self.salida)):
            print(i)
            error = (1 if self.entrada[1] < 2 * self.entrada[0] else -1) - self.salida[i]
            dy.insert(i, error * self.df(self.salida[i]))
            print(dy)


        for i in range(0, len(self.h1)):
            for j in range(0, len(self.h1)):
                error = self.w2[i][j] * dy[j]
                dh.insert(j, error * self.df(self.h1[i]))

        for i in range(0, len(self.bias2)):
            self.bias2[i] = self.bias2[i] + self.aprendizaje * dy[i];

        for i in range(0, len(self.bias1)):
            self.bias1[i] = self.bias1[i] + self.aprendizaje * dh[i];

        for i in range(0, len(self.h1)):
            for j in range(0, len(self.h1)):
                self.w2[i][j] += self.aprendizaje * self.h1[j] * dy[j];
                print("W2 " , self.w2[i][j])

        for i in range(0, len(self.h1)):
            for j in range(0, len(self.h1)):
                self.w1[i][j] += self.aprendizaje * self.entrada[j] * dh[j];

