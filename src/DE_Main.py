import time
import numpy as np
import src.problem.H1 as H1
import src.problem.H2 as H2
import src.problem.H3 as H3
import src.problem.H4 as H4
import src.problem.H5 as H5
import src.problem.H6 as H6
import src.problem.H7 as H7
import src.problem.H8 as H8
import src.problem.H9 as H9
import src.problem.H10 as H10
import src.problem.H11 as H11
import src.problem.H12 as H12
import src.problem.H13 as H13
import src.problem.H14 as H14
import src.problem.H15 as H15
import src.problem.H16 as H16

import matplotlib.pyplot as plt


class DE_Algorithm():
    pop_size = 0
    Cross_Rate = 0.00
    Mutation_Rate = 0.00
    Generation_Num = 10000
    test_func = None
    Population = []  # 记录种群适应度
    success_tag = 0

    def __init__(self, pop_size, c_rate, m_rate, g_num, test_func):
        self.pop_size = pop_size
        self.Cross_Rate = c_rate
        self.Mutation_Rate = m_rate
        self.Generation_Num = g_num
        self.test_func = test_func

    def create_pop(self):
        cld_x = self.bound[0] + (self.bound[1] - self.bound[0]) * np.random.rand(self.vir_num, self.pop_size)
        return cld_x

    def Func(self, X):
        f = self.test_func.Func(X)
        return f

    def select(self, ui, i):
        p = ui
        pre_p = self.Population[:, i]

        f = self.Func(p)
        pre_f = self.Func(pre_p)
        if f < pre_f:
            pre_p[:] = p[:]

        if f < self.best_fv:
            self.best_fv = f
            self.best_child[:] = p[:]

    def mutate(self, p1, p2):

        f = 0.5 + 1.5 * np.random.rand()  # 缩放因子
        d = f * (p1 - p2)
        temp_p = self.best_child + d
        temp_p[temp_p > self.bound[1]] = self.bound[0] + (self.bound[1] - self.bound[0]) * np.random.rand()
        temp_p[temp_p < self.bound[0]] = self.bound[0] + (self.bound[1] - self.bound[0]) * np.random.rand()
        return temp_p

    def Crossover(self, p1, vi):
        ui = np.zeros(self.vir_num)
        k = np.random.random_integers(0, self.vir_num - 1)
        for j in range(0, self.vir_num):
            if np.random.random() < self.Cross_Rate or j == k:
                ui[j] = vi[j]
            else:
                ui[j] = p1[j]
        return ui

    def init(self):
        self.bound = self.test_func.Bound
        self.vir_num = self.test_func.vir_num
        self.Population = self.create_pop()

        self.best_child = self.Population[:, 0]
        self.best_fv = self.Func(self.best_child)

    def evolution(self):
        for g in range(self.Generation_Num):
            # pre_Population = np.copy(self.Population)
            for i in range(self.pop_size):
                k, j = np.random.randint(self.pop_size), np.random.randint(self.pop_size)
                while j == i or k == i or j == k:
                    k, j = np.random.randint(self.pop_size), np.random.randint(self.pop_size)
                p = self.Population[:, i]
                p1, p2 = self.Population[:, k], self.Population[:, j]

                vi = self.mutate(p1, p2)
                ui = self.Crossover(p, vi)
                self.select(ui, i)
            if g % 1000 == 0:
                print('g：%s,best fv:%s' % (g, self.best_fv))
            if abs(self.best_fv - self.test_func.best_v) < 0.00001:
                self.success_tag = 1
            if abs(self.best_fv - self.test_func.best_v) < 0.000001:
                break


def run(i, test_func):
    test_func = test_func
    pop_size = test_func.pop_size
    max_iterations = test_func.max_iterations

    de = DE_Algorithm(pop_size, 0.3, 1, max_iterations, test_func)
    de.init()
    t1 = time.time()
    de.evolution()
    t2 = time.time()
    print('第%d 次, best value:%s;X:%s;coust time:%s' % (i, de.best_fv, de.best_child, t2 - t1))
    return de.best_fv, de.success_tag


run(0, H9)
