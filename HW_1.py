import math


# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24,
#  57, 55, 70, 75, 65, 84, 90, 150
# Посчитать  среднее арифметическое,
# среднее квадратичное отклонение, смещенную и
# несмещенную оценки дисперсий для данной выборки.


numbers = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24,
           57, 55, 70, 75, 65, 84, 90, 150]

mean = sum(numbers) / len(numbers)
print(f'Cреднее арифметическое: {mean: .2f}')


stddev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / len(numbers))
print(f'\nCреднее квадратичное отклонение: {stddev: .4f}')


var = sum((x - mean) ** 2 for x in numbers) / len(numbers)
print('\nСмещенная оценка дисперсии: ', var)

unbiased_var = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
print(f'\nНесмещенная оценка дисперсии: {unbiased_var: .4f}')
