from matplotlib import pyplot as plt
import numpy as np

pow2 = lambda x: x ** 2
# Creates a 100 element numpy array, ranging evenly from -1 to 1
t = np.linspace(-1., 1., 100)
plt.plot(t, list(map(pow2, t)), 'xb')
plt.show()
