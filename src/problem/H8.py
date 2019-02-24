import numpy as np

Bound = [-500, 500]
vir_num = 100
best_v = 0
pop_size = 10
max_iterations = 12000


# (-500,500),-12569.5
def Func(X):
    if len(X.shape) == 1:
        X = X[:, np.newaxis]
    s1 = np.sin(np.sqrt(np.abs(X)))
    Z = 418.9828 * vir_num + np.sum(-X * s1, axis=0)
    return Z[0]
