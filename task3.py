#Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
import random

size = 10
numbers = [random.randint(1, 10) for i in range(size)]
uniqNumbers = set(numbers)
numbers.sort()
print(numbers)
count = list(filter(lambda x: x > 1, [numbers.count(i) for i in uniqNumbers]))
print(f'количество повторяющихся элементов {sum(count)}')
print(f'список уникальных элементов {uniqNumbers}')