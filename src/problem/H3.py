import numpy as np

Bound = [-5.12, 5.12]
vir_num = 100
best_v = 0

pop_size = 30
max_iterations = 12000

# (-5.12, 5.12),0
def Func(X):
    Z = np.sum(X ** 2 - 10 * np.cos(2 * np.pi * X) + 10, axis=0)
    return Z
