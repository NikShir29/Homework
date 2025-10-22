range_start = int(input("Введите начало таблицы умножения: "))
range_end = int(input("Введите конец таблицы умножения: "))

for i in range(range_start, range_end + 1):
    for j in range(range_start, range_end + 1):
        print("%5d" % (i * j), end="")
    print()