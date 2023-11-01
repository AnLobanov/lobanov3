import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3,100)
y = lambda x: np.sin(x) * np.cos(x)

plt.plot(x, y(x))
plt.show()