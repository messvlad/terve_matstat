import numpy as np
from scipy.stats import t

# Данные роста и массы студентов
height = np.array([171, 181, 175, 182, 189, 183, 182, 176, 190, 181, 179, 173, 171, 170, 160, 187, 175])
weight = np.array([48, 80, 72, 67, 82, 73, 72, 127, 100, 70, 72, 73, 67, 60, 60, 69, 79])

# Вычисление выборочного коэффициента корреляции
correlation = np.corrcoef(height, weight)[0, 1]

# Вычисление критического значения t-распределения
n = len(height)
alpha = 0.05 / 2
df = n - 2
t_critical = t.ppf(1 - alpha, df)

# Вычисление стандартной ошибки коэффициента корреляции
standard_error = np.sqrt((1 - correlation**2) / (n - 2))

# Построение доверительного интервала
confidence_interval_lower = correlation - t_critical * standard_error
confidence_interval_upper = correlation + t_critical * standard_error

print("Доверительный интервал на надежность 0.95 для коэффициента корреляции:", (confidence_interval_lower, confidence_interval_upper))