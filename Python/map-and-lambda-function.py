cube = lambda x: x**3


def fibonacci(n):
    if n == 0:
        return []

    if n == 1:
        return [0, ]

    fibonacci_numbers = [0, 1]

    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i-1] +
                                 fibonacci_numbers[i-2])

    return fibonacci_numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n)))
