#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Elman reccurent network
# Copyright (C) 2011  Nicolas P. Rougier
#
# Distributed under the terms of the BSD License.
# -----------------------------------------------------------------------------
# This is an implementation of the multi-layer perceptron with retropropagation
# learning.
# -----------------------------------------------------------------------------
import numpy as np


def sigmoid(x):
    '''Сигмовидная функция с использованием tanh'''
    return np.tanh(x)


def dsigmoid(x):
    '''Производное сигмовидной железы выше'''
    return 1.0 - x ** 2


class Elman:
    ''' Сеть Эльмана '''

    # конструктор класса
    def __init__(self, *args):
        ''' Инициализация персептрона с заданными размерами.  '''

        self.shape = args
        n = len(args)

        # Строить слои
        self.layers = []

        # Входной слой (+1 единица для смещения + размер первого скрытого слоя)
        # np.ones(size) - возвращает массив из единиц
        self.layers.append(np.ones(self.shape[0] + 1 + self.shape[1]))

        # Скрытый слой (и) + выходной слой
        for i in range(1, n):
            self.layers.append(np.ones(self.shape[i]))

        # Построить матрицу весов
        self.weights = []
        for i in range(n - 1):
            # вернет матрицу
            self.weights.append(np.zeros((self.layers[i].size, self.layers[i + 1].size)))

        # dw проведет последнее изменение в весах (для импульса)
        # [0, ] * число - вернет массив с колличеством элементов умноженое на число со значением на первый множетель
        self.dw = [0, ] * len(self.weights)

        # Сбросить вес
        self.reset()

    def reset(self):
        ''' Сбросить вес '''

        for i in range(len(self.weights)):
            Z = np.random.random((self.layers[i].size, self.layers[i + 1].size))
            self.weights[i][...] = (2 * Z - 1) * 0.25

    def propagate_forward(self, data):
        ''' Распространение данных из входного слоя в выходной слой. '''

        # Установить входной слой с данными
        self.layers[0][:self.shape[0]] = data
        # и первый скрытый слой
        self.layers[0][self.shape[0]:-1] = self.layers[1]

        # Распространение от слоя 0 до слоя n-1 с использованием сигмоида в качестве функции активации
        for i in range(1, len(self.shape)):
            # Propagate activity
            self.layers[i][...] = sigmoid(np.dot(self.layers[i - 1], self.weights[i - 1]))

        # Возвращение вывода
        return self.layers[-1]

    def propagate_backward(self, target, lrate=0.1, momentum=0.1):
        ''' Ошибка обратного распространения, связанная с целевым использованием скорости. '''

        deltas = []

        # Compute error on output layer
        error = target - self.layers[-1]
        delta = error * dsigmoid(self.layers[-1])
        deltas.append(delta)

        # Ошибка вычисления на скрытых слоях
        for i in range(len(self.shape) - 2, 0, -1):
            delta = np.dot(deltas[0], self.weights[i].T) * dsigmoid(self.layers[i])
            deltas.insert(0, delta)

        # Обновление весов
        for i in range(len(self.weights)):
            layer = np.atleast_2d(self.layers[i])
            delta = np.atleast_2d(deltas[i])
            dw = np.dot(layer.T, delta)
            self.weights[i] += lrate * dw + momentum * self.dw[i]
            self.dw[i] = dw

        # Return error
        return (error ** 2).sum()


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt

    # Example 1: изучение простого временного ряда
    # -------------------------------------------------------------------------

    # создаем сеть
    network = Elman(4, 8, 4)
    samples = np.zeros(6, dtype=[('input', float, 4), ('output', float, 4)])
    """"
    samples = np.zeros(6, dtype=[('input', float, 4), ('output', float, 4)])
    
    ПОЯСНЕНИЯ 
        где - 
        первый аргумент - 6 это колличество записей в массиве
    
        в аргументе dtype передаются дла других массива 
            1 - name - input
            2 - тип значений float 
            3 - значение о кол-ве записей в этом массиве 
        
    ПРИМЕР: 
        bb = np.zeros(6, dtype=[('input', float, 4), ('output', float, 2)])

        array([([0., 0., 0., 0.], [0., 0.]), ([0., 0., 0., 0.], [0., 0.]),
               ([0., 0., 0., 0.], [0., 0.]), ([0., 0., 0., 0.], [0., 0.]),
               ([0., 0., 0., 0.], [0., 0.]), ([0., 0., 0., 0.], [0., 0.])],
              dtype=[('input', '<f8', (4,)), ('output', '<f8', (2,))])
              
    ПЕРЕДАЧА ЗНАЧЕНИЙ
         samples[0] = (1, 0, 0, 0), (0, 1, 0, 0)
    
    ПОЛУЧЕНИЕ ЗНАЧЕНИЙ
        samples['input'][n]
        где: 
            [inputs] - массивы закрепленные за этим именем
            [n] - индекс массива 
    """
    samples[0] = (1, 0, 0, 0), (0, 1, 0, 0)
    samples[1] = (0, 1, 0, 0), (0, 0, 1, 0)
    samples[2] = (0, 0, 1, 0), (0, 0, 0, 1)
    samples[3] = (0, 0, 0, 1), (0, 0, 1, 0)
    samples[4] = (0, 0, 1, 0), (0, 1, 0, 0)
    samples[5] = (0, 1, 0, 0), (1, 0, 0, 0)
    for i in range(5000):
        n = i % samples.size
        network.propagate_forward(samples['input'][n])
        network.propagate_backward(samples['output'][n])
    for i in range(samples.size):
        o = network.propagate_forward(samples['input'][i])
        print('Sample %d: %s -> %s' % (i, samples['input'][i], samples['output'][i]))
        print('Network output: %s' % (o == o.max()).astype(float))
        print()
