number1 = int(input("Введите первое число, обозначающее начало диапазона: "))
number2 = int(input("Введите второе число, обозначающее конец диапазона: "))
even = 0
odd = 0
multiple_of_9 = 0
average = 0

for num in range(number1, number2 + 1):
    if num % 2 == 0:
        even += num
print(f"Сумма четных чисел в диапазоне от {number1} до {number2}: {even}")

for num in range(number1, number2 + 1):
    if num % 2 == 1:
        odd += num
print(f"Сумма нечетных чисел в диапазоне от {number1} до {number2}: {odd}")

for num in range(number1, number2 + 1):
    if num % 9 == 0:
        multiple_of_9 += num
print(f"Сумма чисел, кратных 9-ти в диапазоне от {number1} до {number2}: {multiple_of_9}")

for num in range(number1, number2 + 1):
    average = sum(range(number1, number2 + 1)) / len(range(number1, number2 + 1))
print(f"Среднеарифмитическое чисел в диапазоне от {number1} до {number2}: {average}")