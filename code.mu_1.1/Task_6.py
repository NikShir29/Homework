word = "Автомобиль."
last_char = word[-1]

print(word)

if last_char == ".":
    last_char = word[-2]
    if last_char == "ь":
        last_char = word[-3]
if last_char == "ь":
    last_char = word[-2]

print(last_char)