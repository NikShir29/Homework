number = int(input("Введите число, либо введите 7, чтобы завершить работу: "))
sum1 = 0
min1 = []
max1 = []

while number != 7:
    sum1 += number
    min1.append(number)
    max1.append(number)
    print(f"Сумма веденных чисел: {sum1},\nМинимальное из введенных чисел: {min(min1)},\nМаксимальное из введенных чисел: {max(max1)}")
    number = int(input("Введите число, либо введите 7, чтобы завершить работу: "))
else:
    print("До свидания!")