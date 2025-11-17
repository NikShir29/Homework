user_text = input("Введите текст: ")
reserved_words = input("Введите список зарезервированных слов через пробел: ")
lowercase_text = user_text.lower()
lowercase_reserved = reserved_words.lower()
reserved_words_list = lowercase_reserved.split()

for word in reserved_words_list:
    if word in lowercase_text:
        lowercase_text = lowercase_text.replace(word, word.upper())

print(lowercase_text)