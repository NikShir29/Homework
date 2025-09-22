metres = int(input("Введите количество метров: "))
question = int(input("Введите 1 для перевода в мили, 2 для перевода в дюймы, 3 для перевода в ярды: "))

if question == 1:
    print(metres / 1609)
if question == 2:
    print(metres * 39.37)
if question == 3:
    print(metres * 1.094)