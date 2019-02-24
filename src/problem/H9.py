import numpy as np

Bound = [-5.12, 5.12]
vir_num = 100
best_v = 0
pop_size = 10
max_iterations = 12000


def Func(X):
    f = np.floor(X)
    Z = 6 * vir_num + np.sum(f, axis=0)
    return Z
