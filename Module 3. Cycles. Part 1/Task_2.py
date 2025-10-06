number1 = int(input("Введите число, которое обозначает начало диапазона: "))
number2 = int(input("Введите число, которое обозначает конец диапазона: "))
numbers_5 = 0

for number in range(number1, number2 + 1):
    print(f"Число из диапазона: {number}")

for number in reversed(range(number1, number2 + 1)):
    print(f"Число из диапазона в убывающем порядке: {number}")

for number in range(number1, number2 + 1):
    if number % 7 == 0:
        print(f"Число, кратное семи: {number}")

for number in range(number1, number2 + 1):
    if number % 5 == 0:
        numbers_5 += 1

print(f"Количество чисел, кратных 5: {numbers_5}")