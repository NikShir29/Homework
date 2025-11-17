user_text = input("Введите текст: ")
no_spaces_text = user_text.replace(" ", "")
no_spaces_text = no_spaces_text.lower()

print(list(no_spaces_text))
print(list(reversed(no_spaces_text)))

if list(no_spaces_text) == list(reversed(no_spaces_text)):
    print(True)
else:
    print(False)