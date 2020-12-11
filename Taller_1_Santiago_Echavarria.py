from funciones import funciones
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import plotly.express as px


if __name__ == '__main__':
    df = pd.read_csv('Pablo.csv', sep=';', index_col=0, decimal=",")
    df = df.astype(float)

    cols = ['mean', 'median', 'mfv', 'min', 'max', 'range', 'var', 'std_dev', 'q75', 'q25', 'per_mean_minus_dev',
            'per_mean_plus_dev', 'prob_mean_dev', 'intercuartile_range']
    incides = ['X1', 'X2', 'X3', 'X4', 'X5', 'Y']

    desc_datosPabloX1, sortX1, _ = funciones(df['datosPablo.X1'].tolist())
    desc_datosPabloX2, sortX2, _ = funciones(df['datosPablo.X2'].tolist())
    desc_datosPabloX3, sortX3, _ = funciones(df['datosPablo.X3'].tolist())
    desc_datosPabloX4, sortX4, _ = funciones(df['datosPablo.X4'].tolist())
    desc_datosPabloX5, sortX5, _ = funciones(df['datosPablo.X5'].tolist())
    desc_datosPabloY, sortY, _ = funciones(df['datosPablo.Y'].tolist())

    p = np.arange(len(df['datosPablo.X1']))
    percentile = p / len(df['datosPablo.X1'])

    resumen = pd.DataFrame(data=[desc_datosPabloX1, desc_datosPabloX2,
                                 desc_datosPabloX3, desc_datosPabloX4, desc_datosPabloX5, desc_datosPabloY],
                           columns=cols, index=incides)

    # resumen.to_excel('Resumen.xls')

    p = np.arange(len(df['datosPablo.X1']))
    fp = p/len(df['datosPablo.X1'])
    logX3 = np.log(np.sort(df['datosPablo.X3'].to_numpy()))

    fig = go.Figure(data=go.Scatter(x=logX3, y=fp, mode='markers'))

    fig.show()

    fig1 = make_subplots(rows=3, cols=2)
    fig2 = make_subplots(rows=3, cols=2)

    X1 = go.Histogram(x=df['datosPablo.X1'], name='X1')
    X2 = go.Histogram(x=df['datosPablo.X2'], name='X2')
    X3 = go.Histogram(x=logX3, name='X3')
    X4 = go.Histogram(x=df['datosPablo.X4'], name='X4')
    X5 = go.Histogram(x=df['datosPablo.X5'], name='X5')
    Y = go.Histogram(x=df['datosPablo.Y'], name='Y')

    box_X1 = go.Box(y=df['datosPablo.X1'], name='X1', boxmean='sd', boxpoints='all', notched=True, notchwidth=0.4)
    box_X2 = (go.Box(y=df['datosPablo.X2'], name='X2', boxmean='sd', boxpoints='all', notched=True, notchwidth=0))
    box_X3 = (go.Box(y=logX3, name='X3', boxmean='sd', boxpoints='all'))
    box_X4 = (go.Box(y=df['datosPablo.X4'], name='X4', boxmean='sd', boxpoints='all'))
    box_X5 = (go.Box(y=df['datosPablo.X5'], name='X5', boxmean='sd', boxpoints='all'))
    box_Y = (go.Box(y=df['datosPablo.Y'], name='Y', boxmean='sd', boxpoints='all'))
    
    fig1.append_trace(X1, 1, 1)
    fig1.append_trace(X2, 1, 2)
    fig1.append_trace(X3, 2, 1)
    fig1.append_trace(X4, 2, 2)
    fig1.append_trace(X5, 3, 1)
    fig1.append_trace(Y, 3, 2)

    fig2.append_trace(box_X1, 1, 1)
    fig2.append_trace(box_X2, 1, 2)
    fig2.append_trace(box_X3, 2, 1)
    fig2.append_trace(box_X4, 2, 2)
    fig2.append_trace(box_X5, 3, 1)
    fig2.append_trace(box_Y, 3, 2)

    fig1.show()
    fig2.show()

