# 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
# варианты: a) 2 из 2 белые и 1 из 4 белый, b) 1 из 2х белый и 2 из 4 белые, c)0 из 2х белые и 3 из 4 белые
import numpy as np
import pandas as pd
from scipy.stats import binom
from scipy.stats import poisson


def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))


t1 = combinations(8, 2)
t2 = combinations(12, 4)

# a)
a1 = combinations(5, 2)
a2 = combinations(5, 1)
b2 = combinations(7, 3)
p1 = a1/t1
p2 = (a2*b2)/t2
pa = p1*p2
print("1. 2 из 2 белые и 1 из 4 белый", round(pa,4))

# b)
a1 = combinations(5, 1)
b1 = combinations(3, 1)
a2 = combinations(5, 2)
b2 = combinations(7, 2)
p1 = (a1*b1)/t1
p2 = (a2*b2)/t2
pb = p1*p2
print("2. 1 из 2х белый и 2 из 4 белые", round(pb,4))

# c)
a1 = combinations(3, 2)
a2 = combinations(5, 3)
b2 = combinations(7, 1)
p1 = a1/t1
p2 = (a2*b2)/t2
pc = p1*p2
print("3. 0 из 2х белые и 3 из 4 белые", round(pc,4))

p = pa+pb+pc
print("4. вероятность того, что 3 мяча белые", round(p,4))
