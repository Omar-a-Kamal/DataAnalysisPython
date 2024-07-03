import matplotlib.pyplot as plt
import numpy as np

#plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,1)
plt.plot(x, y)
plt.title("title 1")

#plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,2)
plt.plot(x, y)
plt.title("title 2")

#plot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,3)
plt.plot(x, y)
plt.title("title 3")

#plot 4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,4)
plt.plot(x, y)
plt.title("title 4")

#plot 5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,5)
plt.scatter(x, y)
plt.title("title 5")

#plot 6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,6)
plt.plot(x, y)
plt.title("title 6")


plt.suptitle("My Store")
plt.show()

