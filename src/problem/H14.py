import numpy as np

Bound = [-1.28, 1.28]
vir_num = 30
best_v = 0

pop_size = 100
max_iterations = 100000


def Func(X):
    p = np.sum(X, axis=0)
    Z = np.exp(0.5 * p)
    Z = Z - 1
    Z = abs(Z)
    return Z
