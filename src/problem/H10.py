import numpy as np

Bound = [-600, 600]
vir_num = 100
best_v = 0

pop_size = 30
max_iterations = 12000

# (-600, 600),0
def Func(X):
    if len(X.shape) == 1:
        X = X[:, np.newaxis]
    m = X.shape[0]
    x_sum = np.sum(X ** 2, axis=0) / 4000
    d = np.arange(1, m + 1, 1)
    d = np.sqrt(d)[:, np.newaxis]
    v = X / d
    x_cos = np.cos(v)
    cos_sum = np.cumprod(x_cos, axis=0)
    cos_sum = cos_sum[-1, :]
    Z = x_sum - cos_sum + 1
    return Z[0]
