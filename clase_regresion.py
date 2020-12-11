import statsmodels.formula.api as sm
import numpy as np
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

x=[0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y=[3.76,4.98,6.03,7.46,9.4,10.67,11.6]
frame = {'x': x, 'y': y}
df = pd.DataFrame(frame)
model1 = 'x~y'
lm1 = sm.ols(formula = model1, data = df).fit()
print(lm1.summary())
df.corr()**2
fig = sm.graphics.influence_plot(lm1)
fig.tight_layout(pad=1.0)
fig.show()

