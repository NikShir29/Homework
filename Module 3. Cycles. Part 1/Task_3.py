number1 = int(input("Введите число, обозначающее начало диапазона: "))
number2 = int(input("Введите число, обозначающее конец диапазона: "))

for number in range(number1, number2 + 1):
    if number % 3 == 0 and number % 5 != 0:
        print(f"Fizz: {number}")
    elif number % 5 == 0 and number % 3 != 0:
        print(f"Buzz: {number}")
    elif number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz: {number}")
    else:
        print(f"Число не кратно ни 5, ни 3: {number}")