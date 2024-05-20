from scipy.stats import poisson, geom

# Задание 9
X = 10  # Значение, полученное из примера 2
lambda_estimate = X  # Оценка параметра λ

# Вычисляем вероятность получения значения X или большего по распределению Пуассона с оценкой λ
p_value_9 = 1 - poisson.cdf(X - 1, lambda_estimate)

print("p-значение для задания 9:", p_value_9)

# Задание 11
k = 5  # Значение, полученное из примера 7
p_estimate = 1 / lambda_estimate  # Оценка параметра p

# Вычисляем вероятность получения первого успеха в k испытаниях или меньше по геометрическому распределению
p_value_11 = geom.cdf(k, p_estimate) - geom.pmf(k, p_estimate)

print("p-значение для задания 11:", p_value_11)
