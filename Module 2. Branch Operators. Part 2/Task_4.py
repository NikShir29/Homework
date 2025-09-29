number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

if number1 != number2:
    if number1 > number2:
        print(number2, number1)
    else:
        print(number1, number2)
else:
    print("Числа равны.")