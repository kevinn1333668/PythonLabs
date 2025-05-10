import numpy as np
from scipy.stats import multivariate_normal
import time

def logpdf_custom(X, m, C):
    D = X.shape[1]
    C_inv = np.linalg.inv(C)
    det_C = np.linalg.det(C)
    diff = X - m

    exponent = -0.5 * np.sum(diff @ C_inv * diff, axis=1)
    norm_const = -0.5 * (D * np.log(2 * np.pi) + np.log(det_C))

    return exponent + norm_const

# Тестируем функцию
X = np.random.randn(1000, 3)
m = np.array([0, 0, 0])
C = np.eye(3)

# Сравниваем скорость
start_custom = time.time()
custom_result = logpdf_custom(X, m, C)
print("Custom время:", time.time() - start_custom)

start_scipy = time.time()
scipy_result = multivariate_normal(m, C).logpdf(X)
print("Scipy время:", time.time() - start_scipy)

# Сравним точность
print("Точность (макс. разница):", np.abs(custom_result - scipy_result).max())