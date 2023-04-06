import numpy as np
import pandas as pd
from scipy.stats import  binom
from scipy.stats import  poisson

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

#1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

sal = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
#считаем среднее арифметическое
sa=sal.sum()/sal.size
sa2=sal.mean()

#создаём массив квадратов разности
soq=(sal-sa)**2
#считаем СКО
std=(soq.sum()/sal.size)**0.5
stdd=(soq.sum()/(sal.size-1))**0.5

std_=sal.std()
stdd_=sal.std(ddof=1)

#считаем дисперсию смещенная оценка
var=soq.sum()/sal.size
var2=sal.var()

#считаем дисперсию несмещенная оценка
vue=soq.sum()/(sal.size-1)
vue2=sal.var(ddof=1)

print("1. Среднее арифметическое ",sa,sa2)
print("2. Среднее квадратичное отклонение ",std,std_)
print("3. дисперсия смещенная оценка ",var,var2)
print("4. дисперсия несмещенная оценка ",vue,vue2)