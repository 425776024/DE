import numpy as np

Bound = [-1.28, 1.28]
vir_num = 30
best_v = 0

pop_size = 100
max_iterations = 100000


def Func(X):
    i = np.arange(1, vir_num + 1)
    rdm = np.random.rand()
    if rdm == 1:
        rdm = 0.9999999999
    Z = np.sum(i * (X ** 4), axis=0) + rdm
    return Z
