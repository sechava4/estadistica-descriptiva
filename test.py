import statistics as st
import statsmodels as sm
import pandas as pd
import numpy as np

def funciones (a):
    media = st.mean(a)
    mediana = st.median(a)
    ordenados = sorted(a)
    moda = st.mode(a)
    range_ = max(a)-min(a)
    var = st.variance(a)
    dev = st.stdev(a)
    df = pd.Series(a)
    quantile = df.quantile([0, 0.25, 0.5, 0.75, 1], interpolation='linear')  #mediana de cada una de las partes
    q75, q25 = np.percentile(a, [75, 25])
    q50 = np.percentile(a, [50])
    print(q50)
    rango_intercuartil = q75 - q25
    print(q75, q25)
    return media,mediana,ordenados,moda,range_,var,dev,quantile, rango_intercuartil

if __name__ == '__main__':
    a = [1, 1, 4, 6, 2, 2, 3, 9, 10, 11, 5, 2, 4]
    df = pd.Series(a)
    b=a.copy()
    b.append(178)
    media,mediana,ordenados,moda,range_,var,dev, quantile, rango_intercuartil = funciones(a)
    media2, mediana2, ordenados2, moda2, range_2, var2, dev2, quantile2, rango_intercuartil2 = funciones(b)