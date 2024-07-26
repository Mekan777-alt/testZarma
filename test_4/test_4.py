def generate_squares_list_comprehension(n):
    """
    Оптимизация с использованием генераторов списков
    """
    numbers = [i for i in range(1, n + 1)]
    squares = [number ** 2 for number in numbers]
    return squares


def generate_squares_map(n):
    """
    Оптимизация с использованием функции map
    """
    numbers = range(1, n + 1)
    squares = list(map(lambda x: x ** 2, numbers))
    return squares


def main():
    n = 1000000

    squares_list_comprehension = generate_squares_list_comprehension(n)

    squares_map = generate_squares_map(n)

    assert squares_list_comprehension == squares_map, "Результаты методов не совпадают"

    print("Оба метода работают правильно и дают одинаковый результат.")


if __name__ == '__main__':
    main()
