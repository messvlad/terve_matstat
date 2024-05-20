import numpy as np
from scipy.stats import chi2_contingency

# Данные о выпадении секторов на каждом барабане
observed = np.array([[5, 10, 5], [14, 7, 14], [10, 3, 6]])

# Проверяем гипотезу о независимости вращения барабанов
chi2_independence, p_value_independence, _, _ = chi2_contingency(observed)
print("p-значение для гипотезы о независимости вращения барабанов:", p_value_independence)

# Ожидаемое равномерное распределение
expected_uniform = np.full(observed.shape, observed.sum() / (observed.shape[0] * observed.shape[1]))

# Проверяем гипотезу о равновероятности выпадения секторов на каждом барабане
chi2_uniform, p_value_uniform = chi2_contingency(observed, correction=False)[:2]
print("p-значение для гипотезы о равновероятности выпадения секторов на каждом барабане:", p_value_uniform)

# Выводим результаты
alpha = 0.05
if p_value_independence < alpha:
    print("Отвергаем гипотезу о независимости вращения барабанов.")
else:
    print("Не отвергаем гипотезу о независимости вращения барабанов.")

if p_value_uniform < alpha:
    print("Отвергаем гипотезу о равновероятности выпадения секторов на каждом барабане.")
else:
    print("Не отвергаем гипотезу о равновероятности выпадения секторов на каждом барабане.")

# Сравнение фактических и ожидаемых значений для проверки нечестности производителя
print("Фактические значения:")
print(observed)
print("Ожидаемые равномерные значения:")
print(expected_uniform)
