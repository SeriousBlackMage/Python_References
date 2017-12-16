import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3, 100)
y = np.exp(x)

plt.plot(x,y)
plt.xlabel('$x$')
plt.ylabel('$exp(x)$')
plt.show()
