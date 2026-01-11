def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []
    for number in range(2, n + 1):
        if is_prime[number]:
            primes.append(number)
    return primes


def test_sieve():
    print("Решето Эратосфена")

    try:
        n = int(input("Введите верхнюю границу для поиска простых чисел: "))

        if n < 0:
            print("Введите положительное число.")
            return

        primes = sieve_of_eratosthenes(n)

        print(f"\nПростые числа от 2 до {n}:")
        print(primes)

        print(f"\nВсего найдено {len(primes)} простых чисел.")

    except ValueError:
        print("Введите целое число.")

test_sieve()