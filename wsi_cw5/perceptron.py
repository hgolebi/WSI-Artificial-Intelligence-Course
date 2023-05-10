# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:51:50 2021

@author: RafaĹ Biedrzycki
Kodu tego mogÄ uĹźywaÄ moi studenci na Äwiczeniach z przedmiotu WstÄp do Sztucznej Inteligencji.
Kod ten powstaĹ aby przyspieszyÄ i uĹatwiÄ pracÄ studentĂłw, aby mogli skupiÄ siÄ na algorytmach sztucznej inteligencji.
Kod nie jest wzorem dobrej jakoĹci programowania w Pythonie, nie jest rĂłwnieĹź wzorem programowania obiektowego, moĹźe zawieraÄ bĹÄdy.

Nie ma obowiÄzku uĹźywania tego kodu.
"""

import numpy as np
import random
from math import tanh
import matplotlib.pyplot as plt


#ToDo tu prosze podac pierwsze cyfry numerow indeksow
p = [4,9]

L_BOUND = -5
U_BOUND = 5

def q(x):
    return np.sin(x*np.sqrt(p[0]+1))+np.cos(x*np.sqrt(p[1]+1))
    #return np.sin(2 * x)

x = np.linspace(L_BOUND, U_BOUND, 100)
y = q(x)

np.random.seed(1)


# f logistyczna jako przykĹad sigmoidalej
def activation(x):
    return tanh(x) * 2

#pochodna fun. 'sigmoid'
def d_activation(x):
    return (1 - tanh(x) ** 2) * 2

#f. straty
def nloss(y_out, y):
    return (y_out - y) ** 2

#pochodna f. straty
def d_nloss(y_out, y):
    return 2*( y_out - y )

class DlNet:
    def __init__(self, x, y, layers):
        self.x_data = x
        self.y_data = y
        self.y_out = 0
        self.HIDDEN_L_SIZE = layers
        self.LR = 0.003
        self.l1w = [np.random.uniform(-1, 1) for x in range(self.HIDDEN_L_SIZE)]       # layer 1 weights
        self.l1b = [np.random.uniform(-1, 1) for x in range(self.HIDDEN_L_SIZE)]       # layer 1 biases
        self.l2w = [np.random.uniform(-1, 1) for x in range(self.HIDDEN_L_SIZE)]       # layer 2 weights
        self.l2b = np.random.uniform(-1, 1)                                   # layer 2 bias



#ToDo


    def forward(self, x):
        y = 0
        for i in range(self.HIDDEN_L_SIZE):
            neuron = activation(x * self.l1w[i] + self.l1b[i])
            y += neuron * self.l2w[i]
        y += self.l2b
        return y
#ToDo

    def predict(self, x):
        return activation(self.forward(x))

    def backward(self, x, y):
        y_predicted = self.predict(x)
        aux1 = d_nloss(y, y_predicted)
        aux2 = d_activation(self.forward(x))
        aux_sum = self.forward(x)
        for i in range(self.HIDDEN_L_SIZE):
            aux_neuron = self.l1w[i] * x + self.l1b[i]

            w1_loss = aux1
            w1_loss *= self.l2w[i]
            w1_loss *= aux2
            w1_loss *= x
            w1_loss *= d_activation(aux_neuron)
            b1_loss = aux1
            b1_loss *= self.l2w[i]
            b1_loss *= aux2
            b1_loss *= d_activation(aux_neuron)

            w2_loss = aux1
            w2_loss *= activation(aux_neuron) * d_activation(aux_sum)

            self.l1w[i] += self.LR * w1_loss
            self.l1b[i] += self.LR * b1_loss
            self.l2w[i] += self.LR * w2_loss
        self.l2b += self.LR * aux1 * d_activation(aux_sum)
#ToDo

    def train(self, x_set, y_set, epochs):
        for ep in range(0, epochs):
            for it in range(0, len(x_set)):
                x, y = (x_set[it], y_set[it])
                self.backward(x, y)
            # if ep == epochs - 1:
            #     total_loss = 0
            #     for it in range(0, len(x_set)):
            #         total_loss += nloss(y_set[it], self.predict(x_set[it]))
            #     msg = f'FINAL LOSS ON {self.HIDDEN_L_SIZE} layer size:' + str(total_loss / len(x_set))

    def loss_msg(self):
        total_loss = 0
        for it in range(0, len(self.x_data)):
            total_loss += nloss(self.y_data[it], self.predict(self.x_data[it]))
        return total_loss / len(self.x_data)


#ToDo

file = open("losses.txt", "w")
for i in range(1, 31):
    #  gotowy skrypt do sprawdzenia różnych rozmiarów warstwy ukrytej
    #  trzeba tylko zmienić pokazywanie wykresu na zapis do pliku, najlepiej z jakims oznaczeniem które jest które
    #  polecam odpalić i zostawić w spokoju bo może kilka(naście) minut zająć
    nn = DlNet(x,y, i)
    yf = [nn.predict(x) for x in nn.x_data]
    nn.train(x, y, 2000)

    yh = [nn.predict(x) for x in nn.x_data]




    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x,y, 'r')
    plt.plot(x,yh, 'b')
    # plt.plot(x,yf, 'g')

    name = "images/" + str(i) + "_neuron(s)"
    plt.savefig(name)
    plt.close()
    # plt.show()

    loss = str(nn.loss_msg())
    msg = f'Final loss on {nn.HIDDEN_L_SIZE} layer size: {loss}\n'
    file.write(msg)
file.close()