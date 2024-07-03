import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2,0, 0, 0]


plt.pie(x, labels=mylabels, startangle=0, explode=myexplode, shadow=True)
plt.legend(title = "Fruits", loc='upper right')
plt.legend

plt.show()