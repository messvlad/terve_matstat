import numpy as np
from scipy import stats

# Данные для задания 6
# Средний доход и стандартное отклонение для Сковородкино
mean1 = 15230
std1 = 250
n1 = 200

# Средний доход и стандартное отклонение для Кастрюлино
mean2 = 15180
std2 = 190
n2 = 200

# Уровень значимости
alpha = 0.05

# Рассчитываем t-статистику
t_stat = (mean1 - mean2) / np.sqrt((std1**2 / n1) + (std2**2 / n2))

# Рассчитываем степени свободы
df = n1 + n2 - 2

# Рассчитываем критическое значение t-статистики для двустороннего теста
critical_value = stats.t.ppf(1 - alpha/2, df)

# Проверяем гипотезу о равенстве дисперсий с помощью теста Фишера
f_stat = std1**2 / std2**2
f_critical = stats.f.ppf(1 - alpha/2, n1-1, n2-1)

# Выводим результаты
if np.abs(t_stat) > critical_value:
    print(f"Средний доход в Сковородкино статистически значимо выше, чем в Кастрюлино"
          f" {np.abs(t_stat)} > {critical_value}")
else:
    print(f"Нет статистически значимых различий в среднем доходе между Сковородкино и Кастрюлино"
          f"{np.abs(t_stat)} <= {critical_value}")

if f_stat > 1/f_critical or f_stat < f_critical:
    print(f"Гипотеза о равенстве дисперсий отвергается")
    print(f"{f_stat} > {1/f_critical} или")
    print(f"{f_stat} < {f_critical}")
else:
    print("Гипотеза о равенстве дисперсий не отвергается")
