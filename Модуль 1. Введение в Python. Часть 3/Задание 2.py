numbers = int(input("Введите четырехзначное число: "))
numbers = list(str(numbers))
sum = 1
digit_count = len(numbers)

if digit_count > 4 or digit_count < 4:
    print("Вы ввели неверное число!")
else:
    for number in numbers:
        sum = sum * int(number)
    print(sum)