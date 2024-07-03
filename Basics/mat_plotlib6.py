import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.subplot(1,2,1)
plt.bar(x,y, color='red', width=0.1)

plt.subplot(1,2,2)
plt.barh(x,y, height=0.1)

plt.show()