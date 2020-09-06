import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

X = np.array([13,56,34,21,14.8,56,21,21,21,34,12.6,15.4])

X_Ord = np.sort(X)

p = np.arange(len(X))
fp = p/(len(X))

print(np.where(fp > 0.25))
print(np.where(fp < 0.25))

fig, ax = plt.subplots()
plt.axhline(y=0.25, color="black", linestyle="-")
plt.axhline(y=0.5, color="black", linestyle="-")
plt.axhline(y=0.75, color="black", linestyle="-")
plt.axhline(y=0.125, color="black", linestyle="--")
ax.scatter(X_Ord, fp, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()
# abline(h=0.25); abline(h=0.5); abline(h=0.75)

