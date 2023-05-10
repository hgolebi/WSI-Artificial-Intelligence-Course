
import numpy as np
from autograd import grad
import matplotlib.pyplot as plt

def steepestDescent(x, function, steps, step_ratio):
    x_list = []
    xcopy = x.copy()
    x_list.append(xcopy)
    for i in range (steps):
        grad_fun = grad(function)
        gradient = grad_fun(x)
        x -= step_ratio * (gradient)
        x_copy = x.copy()
        x_list.append(x_copy)
    return x, x_list

def plotDrawing(function, point_list, dim0, dim1):
    MIN_X = -100
    MAX_X = 100
    MIN_Y = -100
    MAX_Y = 100

    PLOT_STEP = 0.5

    x_arr = np.arange(MIN_X, MAX_X, PLOT_STEP)
    y_arr = np.arange(MIN_Y, MAX_Y, PLOT_STEP)
    X, Y = np.meshgrid(x_arr, y_arr)
    Z = np.empty(X.shape)

    max_dim = len(point_list[0])

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            arr = []
            for dim in range(max_dim):
                if dim == dim0:
                    arr.append(X[i, j])
                elif dim == dim1:
                    arr.append(Y[i, j])
                else:
                    arr.append(1)
            Z[i, j] = function(np.array(arr))

    plt.contour(X, Y, Z, 20)
    prev = []
    for point in point_list:
        if len(prev) > 0:
            delta = point - prev

            plt.arrow(prev[dim0], prev[dim1], delta[dim0], delta[dim1], head_width=0.1, head_length=0.3, fc='k', ec='k')
        prev = point
    plt.plot(point_list[0][dim0], point_list[0][dim1], point_list[-1][dim0], point_list[-1][dim1], marker='o')
    plt.show()

def booth(vector):
    x = vector[0]
    y = vector[1]
    return ((x + 2*y -7)*(x + 2*y -7) + (2*x + y - 5)*(2*x + y - 5))