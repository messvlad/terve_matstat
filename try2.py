from scipy.stats import poisson
from scipy.stats import chi2

# Новые данные из таблицы
x_values = list(range(15))
frequencies = [57, 203, 383, 525, 532, 408, 273, 139, 45, 27, 10, 4, 1, 1]

# Вычисляем среднее значение для оценки параметра λ
mean = sum(x * f for x, f in zip(x_values, frequencies)) / sum(frequencies)

# Ожидаемое распределение Пуассона
expected_counts = [poisson.pmf(x, mean) * sum(frequencies) for x in x_values]

# Вычисляем статистику хи-квадрат
chi2_statistic = sum((observed - expected) ** 2 / expected for observed, expected in zip(frequencies, expected_counts))

# Степени свободы
degrees_of_freedom = len(frequencies) - 1

# Вычисляем p-значение
p_value_10 = 1 - chi2.cdf(chi2_statistic, degrees_of_freedom)

print("p-значение для задания 10:", p_value_10)
