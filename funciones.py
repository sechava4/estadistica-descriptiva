import statistics as st
import statsmodels as sm
import pandas as pd
import numpy as np


def funciones(a):
    media = np.mean(a)
    mediana = np.median(a)
    ordenados = np.sort(a)
    (values, counts) = np.unique(a, return_counts=True)
    ind = np.argmax(counts)
    moda = a[ind]
    #moda = np.bincount(a).argmax()
    range_ = max(a)-min(a)
    var = np.var(a)
    dev = np.std(a)
    df = pd.Series(a)
    quantile = df.quantile([0, 0.25, 0.5, 0.75, 1], interpolation='linear')  #mediana de cada una de las partes
    q75, q25 = np.percentile(a, [75, 25])
    idx_minus = np.searchsorted(ordenados, media - dev, side="left")
    idx_plus = np.searchsorted(ordenados, media + dev, side="left")
    rango_intercuartil = q75 - q25
    p = np.arange(len(a))
    percentile = p / len(a)
    per_mean_plus_dev = percentile[idx_plus]
    per_mean_minus_dev = percentile[idx_minus]
    prob_mean_dev = per_mean_plus_dev - per_mean_minus_dev
    return np.array([media, mediana, moda, min(a), max(a), range_, var, dev, q75, q25, per_mean_minus_dev,
                     per_mean_plus_dev, prob_mean_dev, rango_intercuartil]), ordenados, quantile


if __name__ == '__main__':
    a = [1, 1, 4, 6, 2, 2, 3, 9, 10, 11, 5, 2, 4]
    a = np.array(a)
    b = a.copy()
    b = np.append(b, 178)
    datos, ordenados, quantile = funciones(a)
    datos2, ordenados2, quantile2 = funciones(b)
