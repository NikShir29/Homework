number = int(input("Введите число: "))
degree = int(input("Введите, в какую степень от 0 до 7 возвести число: "))

if degree < 0 or degree > 7:
    print("Ошибка ввода.")
else:
    print(number ** degree)