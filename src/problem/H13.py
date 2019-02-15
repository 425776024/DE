import numpy as np

Bound = [-100, 100]
vir_num = 30
best_v = 0

pop_size = 100
max_iterations = 100000


def Func(X):
    Z = np.max(np.abs(X))
    return Z
