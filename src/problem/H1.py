import numpy as np

Bound = [-0.5, 0.5]
best_v = 0
pop_size = 30
vir_num = 100
max_iterations = 12000


def Func(X):
    # X[X == 0] = 0.00000001
    f = np.sin(10 * X * np.pi) / (10 * X * np.pi)
    Z = np.sum(np.abs(f), axis=0)
    return Z
