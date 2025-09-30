operator1 = int(input("Выберите своего оператора. 1 для МегаФона, 2 для Теле2, 3 для МТС: "))
operator2 = int(input("Выберите оператора собеседника. 1 для МегаФона, 2 для Теле2, 3 для МТС: "))
cost = int(input("Введите стоимость разговора: "))

if operator1 < 1 or operator1 > 3:
    print("Ошибка ввода.")
elif operator2 < 1 or operator2 > 3:
    print("Ошибка ввода.")
else:
    if operator1 == operator2:
        print(f"Стоимость разговора: {cost}")
    elif operator1 == 1 and operator2 == 2:
        print(f"Стоимость разговора: {cost * 1.80}")
    elif operator1 == 1 and operator2 == 3:
        print(f"Стоимость разговора: {cost * 1.60}")
    elif operator1 == 2 and operator2 == 1:
        print(f"Стоимость разговора: {cost * 1.20}")
    elif operator1 == 2 and operator2 == 3:
        print(f"Стоимость разговора: {cost * 2}")
    elif operator1 == 3 and operator2 == 1:
        print(f"Стоимость разговора: {cost * 1.40}")
    else:
        print(f"Стоимость разговора: {cost * 1.50}")