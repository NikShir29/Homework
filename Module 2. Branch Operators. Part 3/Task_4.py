manager1_sell = int(input("Введите уровень продаж менеджера Артёма: "))
manager2_sell = int(input("Введите уровень продаж менеджера Елизаветы: "))
manager3_sell = int(input("Введите уровень продаж менеджера Анны: "))
manager1_salary = 200
manager2_salary = 200  #Базовая зарплата = 200 долларов. К ней мы прибавляем проценты от продаж, введенных выше.
manager3_salary = 200
manager1_percent = 0
manager2_percent = 0   #Вводим переменные процентов для дальнейших вычислений.
manager3_percent = 0
best_worker = 0        #Переменная для определения лучшего работника.

if manager1_sell < 500 and manager1_sell >= 0:
    manager1_percent = manager1_sell * 3 / 100         #Вычисляем проценты от продаж (3%), если объем продаж < 500 долларов.
    manager1_salary += manager1_percent                #Прибавляем к базовой зарплате (200) проценты от продаж.
elif manager1_sell >= 500 and manager1_sell < 1000:
    manager1_percent = manager1_sell * 5 / 100         #Вычисляем проценты от продаж (5%), если объем продаж >= 500 и < 1000.
    manager1_salary += manager1_percent                #Прибавляем к базовой зарплате (200) проценты от продаж.
elif manager1_sell >= 1000:
    manager1_percent = manager1_sell * 8 / 100         #Вычисляем проценты от продаж (8%), если объем продаж >= 1000.
    manager1_salary += manager1_percent                #Прибавляем к базовой зарплате (200) проценты от продаж.
else:
    print("Ошибка ввода для первого менеджера.")       #Выводится ошибка, если ввести негативный уровень продаж.

if manager2_sell < 500 and manager2_sell >= 0:
    manager2_percent = manager2_sell * 3 / 100
    manager2_salary += manager2_percent
elif manager2_sell >= 500 and manager2_sell < 1000:
    manager2_percent = manager2_sell * 5 / 100
    manager2_salary += manager2_percent                #Повторение всего, что выше. Теперь для второго менеджера.
elif manager2_sell >= 1000:
    manager2_percent = manager2_sell * 8 / 100
    manager2_salary += manager2_percent
else:
    print("Ошибка ввода для второго менеджера.")

if manager3_sell < 500 and manager3_sell >= 0:
    manager3_percent = manager3_sell * 3 / 100
    manager3_salary += manager3_percent
elif manager3_sell >= 500 and manager3_sell < 1000:
    manager3_percent = manager3_sell * 5 / 100         #Повторение всего, что выше. Теперь для третьего менеджера.
    manager3_salary += manager3_percent
elif manager3_sell >= 1000:
    manager3_percent = manager3_sell * 8 / 100
    manager3_salary += manager3_percent
else:
    print("Ошибка ввода для третьего менеджера.")

if manager1_salary > manager2_salary and manager1_salary > manager3_salary:
    manager1_salary += 200
    best_worker = 1
elif manager2_salary > manager1_salary and manager2_salary > manager3_salary:    #Определение лучшего работника по объему зарплаты.
    manager2_salary += 200                                                       #Начисление лучшему работнику премии в 200 долларов.
    best_worker = 2
elif manager3_salary > manager1_salary and manager3_salary > manager2_salary:
    manager3_salary += 200
    best_worker = 3

if manager1_sell >= 0:
    print(f"Зарплата менеджера Артёма за этот месяц: {manager1_salary}")
if manager2_sell >= 0:
    print(f"Зарплата менеджера Елизаветы за этот месяц: {manager2_salary}")      #Вывод зарплаты.
if manager3_sell >= 0:
    print(f"Зарплата менеджера Анны за этот месяц: {manager3_salary}")

if best_worker == 1:
    print("Лучший работник месяца: Артём. Ему начислена премия в 200 долларов.")
elif best_worker == 2:
    print("Лучший работник месяца: Елизавета. Ей начислена премия в 200 долларов.")  #Вывод лучшего работника.
elif best_worker == 3:
    print("Лучший работник месяца: Анна. Ей начислена премия в 200 долларов.")
else:

    print("Лучшего работника в этом месяце нет.")            #Если высшая з/п одинаковая как минимум у двух людей, лучшего работника нет.
