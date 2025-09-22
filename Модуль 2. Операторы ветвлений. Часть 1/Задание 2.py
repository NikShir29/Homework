number1 = int(input("Введите число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
question = int(input("Введите 1 для максимума, 2 для минимума или 3 для среднеарифмитического: "))

if question == 1:
    if number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number3 and number2 > number1:
        print(number2)
    else:
        print(number3)
if question == 2:
    if number1 < number2 and number1 < number3:
        print(number1)
    elif number2 < number1 and number2 < number3:
        print(number2)
    else:
        print(number3)
if question == 3:
    sum = number1 + number2 + number3
    print(sum / 3)