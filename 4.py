from scipy.stats import binom_test

# Задание 4
# Подбрасываем две монеты 100 раз
# Определяем события A, B, C и D
# A = 2 орла, B = 2 решки, C = орел и решка, D = решка и орел

# Количество наблюдений для каждого события
counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

# Моделируем эксперимент
import random
for _ in range(100):
    coin1 = random.choice(['О', 'Р'])
    coin2 = random.choice(['О', 'Р'])
    outcome = coin1 + coin2
    if outcome == 'ОО':
        counts['A'] += 1
    elif outcome == 'РР':
        counts['B'] += 1
    elif outcome == 'ОР' or outcome == 'РО':
        counts['C'] += 1
    else:
        counts['D'] += 1

# Проверяем гипотезу о равновероятном распределении событий A, B, C и D
p_value = binom_test([counts['A'], counts['B'], counts['C'], counts['D']], p=0.25)
print("p-значение для задания 4:", p_value)

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

# Проверяем гипотезу
p_value_2 = binom_test(observed_boys, n=total_families*2, p=0.515)
print("p-значение для задания 5:", p_value_2)
