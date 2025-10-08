length = int(input("Введите длину линии: "))
symbol = input("Введите символ для заполнения линии: ")
length_add = 0

while length_add < length:
    print(f"""{symbol}""")
    length_add += 1
else:
    print("Линия построена :)")