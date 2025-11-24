import random

random_integers = [random.randint(-100, 101) for count in range(10)]
print(random_integers)

min_number = min(random_integers)
print(f"Минимальное число: {min_number}")

max_number = max(random_integers)
print(f"Максимальное число: {max_number}")

negative_count = 0
for number in random_integers:
    if number < 0:
        negative_count += 1
print(f"Количество отрицательных чисел: {negative_count}")

positive_count = 0
for number in random_integers:
    if number > 0:
        positive_count += 1
print(f"Количество положительных чисел: {positive_count}")

total_zeros = 0
for num in random_integers:
    total_zeros += str(num).count("0")
print(f"Количество нулей: {total_zeros}")