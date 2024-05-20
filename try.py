import numpy as np
from scipy.stats import t

# Задание 3
weights = np.array([40.1, 50.0, 49.7, 50.5, 48.1, 50.3, 49.7, 51.6, 49.8, 50.1, 49.7, 48.8, 51.4, 49.1, 49.6, 50.9, 48.5, 52.0, 50.7, 50.6])
nominal_weight = 50.0  # Номинальный вес
alpha = 0.10  # Уровень значимости

# Расчет среднего и стандартного отклонения выборки
sample_mean = np.mean(weights)
sample_std = np.std(weights, ddof=1)
n = len(weights)

# Расчет t-статистики
t_statistic = (sample_mean - nominal_weight) / (sample_std / np.sqrt(n))

# Расчет p-значения
df = n - 1  # Степени свободы
p_value = 2 * (1 - t.cdf(abs(t_statistic), df))

print("\nЗадание 3:")
print(f"p-значение: {p_value}, {'нулевая гипотеза принимается' if p_value > alpha else 'нулевая гипотеза отвергается'}")
