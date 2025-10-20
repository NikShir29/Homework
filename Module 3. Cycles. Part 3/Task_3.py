count = 0
for number in range(100, 10000):
    s = str(number)
    if len(s) == len(set(s)):
        count += 1
print(f"Количество чисел с разными цифрами: {count}")