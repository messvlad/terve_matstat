import numpy as np
from scipy.stats import norm
'''
# Задание 1
mean_weight = 1.01  # Средний вес пакета
nominal_weight = 1.0  # Номинальный вес пакета
std_dev = 0.01  # Среднеквадратическое отклонение
n = 16  # Размер выборки

# Расчет Z-статистики
z = (mean_weight - nominal_weight) / (std_dev / np.sqrt(n))

# Расчет p-значения
p_value = norm.cdf(z)

print("Задание 1:")
print(f"p-значение: {p_value}, {'нулевая гипотеза отвергается' if p_value < 0.05 else 'нулевая гипотеза принимается'}")

# Задание 2
mean_size = 3.88  # Средний размер отверстия
nominal_size = 4.00  # Нормативный размер
std_dev = 0.20  # Среднеквадратическое отклонение
n = 25  # Размер выборки

# Расчет Z-статистики
z = (mean_size - nominal_size) / (std_dev / np.sqrt(n))

# Расчет p-значения
p_value = norm.cdf(z)

print("\nЗадание 2:")
print(f"p-значение: {p_value}, {'нулевая гипотеза отвергается' if p_value < 0.01 else 'нулевая гипотеза принимается'}")
'''
# Задание 3
weights = np.array([40.1, 50.0, 49.7, 50.5, 48.1, 50.3, 49.7, 51.6, 49.8, 50.1, 49.7, 48.8, 51.4, 49.1, 49.6, 50.9, 48.5, 52.0, 50.7, 50.6])
nominal_weight = 50.0  # Номинальный вес
alpha = 0.10  # Уровень значимости

# Расчет среднего и стандартного отклонения выборки
sample_mean = np.mean(weights)
sample_std = np.std(weights, ddof=1)

# Расчет t-статистики
t = (sample_mean - nominal_weight) / (sample_std / np.sqrt(len(weights)))

# Расчет p-значения
p_value = 2 * (1 - norm.cdf(abs(t)))

print("\nЗадание 3:")
print(f"p-значение: {p_value}, {'нулевая гипотеза принимается' if p_value > alpha else 'нулевая гипотеза отвергается'}")
'''
# Задание 4
# a) Для случая выборочной дисперсии S^2 = 0.29
squared_var_a = 0.29  # Выборочная дисперсия
null_hypothesis_a = 0.18  # Нулевая гипотеза

# Расчет t-статистики
t_a = (squared_var_a - null_hypothesis_a) / (np.sqrt(squared_var_a / 17))

# Расчет p-значения
p_value_a = 1 - norm.cdf(t_a)

print("\nЗадание 4a:")
print(f"p-значение: {p_value_a}, {'нулевая гипотеза принимается' if p_value_a > 0.05 else 'нулевая гипотеза отвергается'}")

# b) Для случая выборочной дисперсии S^2 = 0.29
squared_var_b = 0.29  # Выборочная дисперсия
null_hypothesis_b = 0.18  # Нулевая гипотеза

# Расчет t-статистики
t_b = (squared_var_b - null_hypothesis_b) / (np.sqrt(squared_var_b / 17))

# Расчет p-значения
p_value_b = 1 - norm.cdf(t_b)

print("\nЗадание 4b:")
print(f"p-значение: {p_value_b}, {'нулевая гипотеза принимается' if p_value_b > 0.05 else 'нулевая гипотеза отвергается'}")
'''