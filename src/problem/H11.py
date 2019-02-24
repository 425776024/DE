import numpy as np

m = 10
Bound = [0, 3.1415926]
vir_num = 10
best_v = -9.66

pop_size = 10
max_iterations = 20000


# (0,pi),-9.66
def Func(X):
    if len(X.shape) == 1:
        X = X[:, np.newaxis]
    d_range = np.arange(1, X.shape[0] + 1).T[:, np.newaxis]
    s1 = np.sin(X)
    s2 = np.sin(d_range * (X ** 2) / np.pi) ** (2 * m)
    d = s1 * s2
    Z = -np.sum(d, axis=0)[0]
    return Z
