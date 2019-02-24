import numpy as np

Bound = [-10, 10]
vir_num = 30
best_v = 0

pop_size = 100
max_iterations = 100000


def Func(X):
    f=np.abs(X*np.sin(X)+0.1*X)
    Z = np.sum(f, axis=0)
    return Z
