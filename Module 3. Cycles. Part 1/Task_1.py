number1 = int(input("Введите число, обозначающее начало диапазона: "))
number2 = int(input("Введите число, обозначающее конец диапазона: "))

for number in range(number1, number2 + 1):
    if number % 7 == 0:
        print(f"Это число кратно семи: {number}")