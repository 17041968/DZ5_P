#Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.
import random

size = 10
numbers = [random.randint(1, 10) for i in range(size)]
print(numbers)
index = random.randint(0, size - 1)
result = [numbers[index]]

while index < size:
	index = random.randint(index + 1, size)
	if index < size:
		if numbers[index] > result[-1]:
			result.append(numbers[index])
		
print(result)
