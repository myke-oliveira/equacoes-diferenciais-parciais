#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

M = 300

L = 10
A = 1

x=np.linspace(0, L, 300)
fs = [4/(n*np.pi)*np.sin(n*np.pi/2)*np.sin(n*np.pi/L)*np.sin(n*np.pi/L*x) for n in range(1, M)]

plt.figure(figsize=(20, 16))
for t in (0., 1., 2., 3., 3.5, 4., 4.5, 5, 5.5, 6., 6.5, 7., 8.):
    us = [
        4/(n*np.pi)*np.sin(n*np.pi/2)*np.sin(n*np.pi/L)*np.sin(n*np.pi/L*x)*np.cos(A*n*np.pi*t/L)
        for n in range(1, M)
    ]
    u = reduce(lambda x, y: x + y, us)
    plt.figure(figsize=(20, 16))
    color = (t/(2*np.pi*L), 0, 1-t/(2*np.pi*L))
    plt.plot(x, u, label=f't= {t} s', color=color)
    plt.title(f'Onda em função de x para t={t}s')
    plt.legend(loc='upper left')
    plt.grid()
    filename = f'graficos/grafico_t={t:0.3f}s.eps'
    plt.savefig(filename)
    plt.close()

t = np.linspace(0, 8);
for x in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    us = [
        4/(n*np.pi)*np.sin(n*np.pi/2)*np.sin(n*np.pi/L) *
        np.sin(n*np.pi/L*x)*np.cos(A*n*np.pi*t/L)
        for n in range(1, M)
    ]
    u = reduce(lambda x, y: x + y, us)
    plt.figure(figsize=(20, 16))
    plt.plot(t, u, label=f'x= {x} s')
    plt.title(f'Onda em função de t para x={x}m')
    plt.legend(loc='upper left')
    plt.grid()
    filename = f'graficos/grafico_x={x:0.3f}m.eps'
    plt.savefig(filename)
    plt.close()

for i, t in enumerate(np.linspace(0, 2*np.pi*L, int(2*np.pi*L*60))):
    us = [
        4/(n*np.pi)*np.sin(n*np.pi/2)*np.sin(n*np.pi/L)*np.sin(n*np.pi/L*x)*np.cos(A*n*np.pi*t/L)
        for n in range(1, M)
    ]
    u = reduce(lambda x, y: x + y, us)
    plt.figure(figsize=(20, 16))
    plt.plot(x, u, label=f't= {t} s')
    plt.ylim(-1.1, 1.1)
    plt.grid()
    plt.savefig(filename:=f'img/onda-{i:0>5}.png')
    print(filename)
    plt.close()
