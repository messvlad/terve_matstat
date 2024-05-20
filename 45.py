from scipy.stats import norm

# Задание 5
# Проверяем биномиальное распределение для количества мальчиков в семьях с двумя детьми
# Вероятность рождения мальчика равна 0.515
total_families = 17036
boys_both = 4529
girls_both = 4019
mixed = 8488

# Ожидаемое количество мальчиков
expected_boys = total_families * 2 * 0.515

# Наблюдаемое количество мальчиков
observed_boys = boys_both * 2 + mixed

# Стандартное отклонение для биномиального распределения
std_dev = (total_families * 2 * 0.515 * (1 - 0.515)) ** 0.5

# Z-оценка
z_score = (observed_boys - expected_boys) / std_dev

# Вычисление p-значения
p_value_2 = 2 * (1 - norm.cdf(abs(z_score)))
print("p-значение для задания 5:", p_value_2)
