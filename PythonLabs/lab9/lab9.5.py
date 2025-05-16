import numpy as np
from scipy.stats import multivariate_normal
import time

def my_logpdf(X, m, C):
    D = len(m)
    X_centered = X - m
    C_inv = np.linalg.inv(C)
    C_det = np.linalg.det(C)

    constant = -0.5 * (D * np.log(2 * np.pi) + np.log(C_det))
    logpdf_values = np.empty(X.shape[0])
    for i, x in enumerate(X_centered):
        logpdf_values[i] = constant - 0.5 * x @ C_inv @ x
    return logpdf_values

# Тестовые данные
N, D = 1000, 5
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.cov(X, rowvar=False)

# Проверка точности
logpdf_my = my_logpdf(X, m, C)
logpdf_scipy = multivariate_normal(m, C).logpdf(X)
print("Max absolute difference:", np.max(np.abs(logpdf_my - logpdf_scipy)))

# Сравнение скорости
start = time.time()
my_logpdf(X, m, C)
print("My implementation took:", time.time() - start, "seconds")

start = time.time()
multivariate_normal(m, C).logpdf(X)
print("SciPy implementation took:", time.time() - start, "seconds")