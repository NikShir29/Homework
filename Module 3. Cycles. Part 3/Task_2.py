count = 0
for i in range(100, 1000):
    s = str(i)
    if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
        count += 1
print(f"Количество целых чисел с двумя одинаковыми цифрами: {count}")