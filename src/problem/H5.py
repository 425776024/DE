import numpy as np

Bound = [-1, 2]
vir_num = 100
best_v = -1.85 * vir_num

pop_size = 30
max_iterations = 12000


def Func(X):
    f = X * np.sin(10 * np.pi * X)
    Z = -np.sum(f, axis=0)
    return Z
