import random

def shuffle_words(text):
    words = text.split()
    shuffled_words = words.copy()

    random.shuffle(shuffled_words)

    result = ' '.join(shuffled_words)

    print(result)
    return result

shuffle_words("кофе чай какао")