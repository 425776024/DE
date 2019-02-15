import numpy as np

Bound = [-30, 30]
vir_num = 30
best_v = 0

pop_size = 30
max_iterations = 100000


# (-30,30),0

def Func(X):
    if len(X.shape) == 1:
        X = X[:, np.newaxis]
    x1 = X[1:]
    x2 = X[:-1]
    Z = np.sum(100 * (x1 - x2 ** 2.0) ** 2 + (x2 - 1) ** 2.0, axis=0)
    return Z[0]
