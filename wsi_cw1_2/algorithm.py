import numpy as np
from autograd import grad

def steepestDescent(x, function, steps, step_ratio):
    for i in range (steps):
        grad_fun = grad(function)
        gradient = grad_fun(x)
        x -= step_ratio * (gradient)
        print (x, "value = ", function(x))
    return x
