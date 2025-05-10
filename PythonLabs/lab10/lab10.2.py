import numpy as np
import matplotlib.pyplot as plt

ratios = [(3,2), (3,4), (5,4), (5,6)]
t = np.linspace(0, 2*np.pi, 1000)

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
axes = axes.flatten()

for ax, ratio in zip(axes, ratios):
    x = np.sin(ratio[0]*t)
    y = np.sin(ratio[1]*t)
    ax.plot(x, y)
    ax.set_title(f"{ratio[0]} : {ratio[1]}")
    ax.axis('equal')
    ax.grid(True)

plt.tight_layout()
plt.show()