import numpy as np
from scipy.stats import pearsonr

# Данные роста и массы студентов
height = np.array([171, 181, 175, 182, 189, 183, 182, 176, 190, 181, 179, 173, 171, 170, 160, 187, 175])
weight = np.array([48, 80, 72, 67, 82, 73, 72, 127, 100, 70, 72, 73, 67, 60, 60, 69, 79])

# Вычисление выборочного коэффициента корреляции используя формулу
n = len(height)
mean_height = np.mean(height)
mean_weight = np.mean(weight)
covariance = np.sum((height - mean_height) * (weight - mean_weight)) / n
std_dev_height = np.sqrt(np.sum((height - mean_height) ** 2) / n)
std_dev_weight = np.sqrt(np.sum((weight - mean_weight) ** 2) / n)
correlation_formula = covariance / (std_dev_height * std_dev_weight)

# Вычисление выборочного коэффициента корреляции с помощью функции pearsonr
correlation_scipy, _ = pearsonr(height, weight)

print("Выборочный коэффициент корреляции (формула):", correlation_formula)
print("Выборочный коэффициент корреляции (scipy.stats.pearsonr):", correlation_scipy)
