
from matplotlib import markers
import matplotlib.pyplot as plt
import cec2017
import numpy as np

from cec2017.functions import f1, f2, f3

def booth(vector):
    x = vector[0]
    y = vector[1]
    return ((x + 2*y -7)*(x + 2*y -7) + (2*x + y - 5)*(2*x + y - 5))


MAX_X = 100
PLOT_STEP = 0.5

max_dim = 10
dim1 = 0
dim2 = 1

x_arr = np.arange(-MAX_X, -60, PLOT_STEP)
y_arr = np.arange(-70, -40, PLOT_STEP)
X, Y = np.meshgrid(x_arr, y_arr)
Z = np.empty(X.shape)

q=f1

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        arr = []
        for dim in range(max_dim):
            if dim == dim1:
                arr.append(X[i, j])
            elif dim == dim2:
                arr.append(Y[i, j])
            else:
                arr.append(0)
        Z[i, j] = q(np.array(arr))

plt.contour(X, Y, Z, 20)
# plt.arrow(0,0,3,3, head_width=0, head_length=0, fc='k', ec='k')
# plt.arrow(3,3,0,3, head_width=0, head_length=0, fc='k', ec='k')\
plt.plot(0,0,3,3, marker='o')
plt.show()
