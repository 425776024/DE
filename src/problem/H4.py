import numpy as np

Bound = [-5.12, 5.12]
vir_num = 100
best_v = 0

pop_size = 30
max_iterations = 12000

# (-5.12, 5.12),0
def Func(X):
    f=np.square(X)
    Z = np.sum(f, axis=0)
    return Z
