import numpy as np

Bound = [-32.768, 32.768]
vir_num = 100
best_v = 0

pop_size = 30
max_iterations = 12000

def Func(X):
    if len(X.shape) == 1:
        X = X[:, np.newaxis]
    m = X.shape[0]
    x_sum = -0.02 * np.sqrt(np.sum(X ** 2, axis=0) / m)
    cos_sum = np.exp(np.sum(np.cos(2 * np.pi * X), axis=0) / m)
    Z = 20 + np.exp(1) - 20 * np.exp(x_sum) - cos_sum
    return Z
