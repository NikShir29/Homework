number_str = input("Введите целое число: ")
new_number_str = number_str.replace('3', '').replace('6', '')
new_number = int(new_number_str)

print(f"Число без цифр 3 и 6: {new_number}")