import numpy as np

Bound = [3, 13]
vir_num = 100
best_v = -1.21598 * vir_num

pop_size = 30
max_iterations = 12000


def Func(X):
    f = np.sin(X) + np.sin((2 * X / 3))
    Z = np.sum(f, axis=0)
    return Z
