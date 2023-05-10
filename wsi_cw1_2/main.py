import numpy as np
from cec2017.functions import f1, f2, f3
from algorithms import steepestDescent, plotDrawing, booth

UPPER_BOUND = 100
DIMENSIONALITY = 10


def showResults(point, func, repetitions=0, step_ratio=0, if_print=False, dimension_x=0, dimension_y=1):
    if func == booth:
        reps = 100
        ratio = 0.05
    if func == f1:
        reps = 150
        ratio = 0.000000008
    if func == f2:
        reps = 2000
        ratio = 0.00000000000000002
    if func == f3:
        reps = 2000
        ratio = 0.000000009

    if repetitions:
        reps = repetitions
    if step_ratio:
        ratio = step_ratio

    print(point, func(point))
    final_point, point_list = steepestDescent(point, func, reps, ratio)
    print(final_point, func(final_point))

    if if_print:
        plotDrawing(func, point_list, dimension_x, dimension_y )

    return final_point

#wylosuj punkt x:
x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY)

showResults(x, f1, if_print=True, dimension_x=3, dimension_y=5)