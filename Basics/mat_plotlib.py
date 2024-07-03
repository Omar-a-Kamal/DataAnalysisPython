import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 25])

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
x3 = np.array([4, 3, 4, 5])
y3 = np.array([7, 5, 9, 14])

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family': 'serif', 'color': 'blue', 'size':20}
font2 = {'family': 'serif', 'color': 'darkred', 'size':15}

# plt.plot(ypoints, marker = 'o', ms = 20 , mec= 'r', mfc = 'k', linestyle = ':')
# plt.plot(xpoints)
#plt.plot(x1, y1, x2, y2, x3, y3)

plt.plot(x, y)

plt.title("Chart Title", fontdict=font1, loc='left')
plt.xlabel("Average 33", fontdict=font2, loc='right')
plt.ylabel("Average 7y", fontdict=font2, loc='bottom')
plt.grid()
plt.show()