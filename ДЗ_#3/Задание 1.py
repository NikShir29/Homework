number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
question = int(input("Введите 1 для умножения или 2 для сложения: "))

multiplication = number1 * number2 * number3
addition = number1 + number2 + number3

if question == 1:
    print(multiplication)
if question == 2:
    print(addition)