def call_counter(func):
    call_count = {}

    def wrapper(*args, **kwargs):
        if func.__name__ not in call_count:
            call_count[func.__name__] = 1
        else:
            call_count[func.__name__] += 1

        count = call_count[func.__name__]

        print(f"Функция {func.__name__} вызвана {count} раз")
        print(f"Аргументы: {args}")

        if kwargs:
            print(f"Именованные аргументы: {kwargs}")

        result = func(*args, **kwargs)

        return result

    return wrapper


@call_counter
def add(a, b):
    return a + b


@call_counter
def repeat(text, n):
    return text * n


@call_counter
def multiply(x, y):
    return x * y


def main():
    print("Декоратор")

    print("\n1. Функция сложения:")

    result1 = add(2, 3)
    print(f"Результат: {result1}")
    print()

    result2 = add(10, 5)
    print(f"Результат: {result2}")
    print()

    result3 = add(7, 8)
    print(f"Результат: {result3}")
    print()

    print("\n2. Функция повторения строки:")

    result4 = repeat('Hi', 3)
    print(f"Результат: '{result4}'")
    print()

    result5 = repeat('Hello', 2)
    print(f"Результат: '{result5}'")
    print()

    print("\n3. Именованные аргументы:")

    result6 = repeat(text='ABC', n=4)
    print(f"Результат: '{result6}'")
    print()

    print("\n4. Функция умножения:")

    result7 = multiply(5, 6)
    print(f"Результат: {result7}")
    print()

    result8 = multiply(3, 4)
    print(f"Результат: {result8}")
    print()

main()