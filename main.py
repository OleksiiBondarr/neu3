# -*- coding: utf-8 -*-
import Image, numpy as np
import random
import matplotlib.pyplot as plt
#импорт картинок и преобразование их в матрицы нулей и единиц
num = []
num.append(np.array(Image.open('big0.bmp').convert('L')))
num.append(np.array(Image.open('big1.bmp').convert('L')))
num.append(np.array(Image.open('big2.bmp').convert('L')))
num.append(np.array(Image.open('big3.bmp').convert('L')))
num.append(np.array(Image.open('big4.bmp').convert('L')))
num.append(np.array(Image.open('big5.bmp').convert('L')))
num.append(np.array(Image.open('big6.bmp').convert('L')))
num.append(np.array(Image.open('big7.bmp').convert('L')))
num.append(np.array(Image.open('big8.bmp').convert('L')))
num.append(np.array(Image.open('big9.bmp').convert('L')))
errorAmount = 0

numr = np.zeros((10, 324))
for k in range(0, 10, 1):
    count = 0
    for i in range(0, 18, 1):
        for j in range(0, 18, 1):
            if num[k][i][j] == 255:
                numr[k][count] = 1
            else:
                numr[k][count] = 0
            count += 1
noised = np.zeros((324, 324))
noisecount = np.zeros(10)
print numr
for k in range(0, 10, 1):
    count = 0
    for i in range(0, 40, 1):
        noised[k][i] = numr[k][i]
rancou = []
f = 324

#функция добавления шума к картинкам - инвертируем n пикселей (shum)
def noised(chosen, shum):
    count = 0
    numrNoised = np.zeros((324))
    checkrand = np.zeros((324))
    numrNoised = numr[chosen]
    if shum > 0:
        while True:
            ran = random.randint(0, 323)
            if not (ran in checkrand):
                if numrNoised[ran] == 0:
                    numrNoised[ran] = 1
                    count += 1
                else:
                    numrNoised[ran] = 0
                    count += 1
                checkrand[count] = ran
            if count == shum:
                break
    max_f = np.zeros(10, dtype=float)
    for i in range(0,10,1):
        mult = 0
        for j in range(0, 324, 1):
            mult = mult + numrNoised[j]*w[i][j]
        max_f[i] = mult
    max_i = 0
    max1 = max_f[max_i]
    for i in range(0, 10, 1):
        if max_f[i]> max1:
            max1 = max_f[i]
            max_i = i
    return max_i



words = []
for i in range(0,10,1):
    words.append(i)

eta = 0.000001
sigma = 0.00001
w = np.zeros((10, 324))


def init_weight():
    for i in range(0,10,1):
        for j in range(0,324,1):
            w[i][j]=numr[i][j]

#ф-ція налаштування наших коефіцієнтів w
#реалізований алгоритм иереж Кохонена


def learn():
    init_weight()
    max_f = np.zeros(10)
    iterAmount = 1000
    randomnum = random.randint(0, 9)
    for i in range(0,iterAmount,1):
        for j in range(0,10,1):
            mult =0
            for k in range(0,324,1):
                mult += numr[randomnum][k]*w[j][k]
            max_f[j] = mult
        max_i = 0
        max1 = max_f[max_i]
        for j in range(0, 10, 1):
            if max_f[j] > max1:
                max1=max_f[j]
                max_i = j
        eta_h=eta*np.exp(-i/iterAmount)
        sigma_h=sigma*np.exp(-i*np.log(sigma)/iterAmount)
        for j in range(0, 324, 1):
            h = np.exp(-((numr[max_i][j] - numr[randomnum][j]) * (numr[max_i][j] - numr[randomnum][j])) / (2 * sigma_h * sigma_h))
            w[max_i][j] += + eta_h * h * (numr[randomnum][j] - w[max_i][j])

# графік залежності к-сті інвертованих пікселів і помилок
def test():
    mas = np.zeros((40, 1))
    for j in range(0, 40, 1):
        for i in range(0, 10,1):
            answer = noised(i, j)
            print i, answer
            if i != answer:
                mas[j][0] += 1
        plt.plot(j,mas[j][0], 'bo', label='sampled', c='b')
    plt.show()

learn()
test()