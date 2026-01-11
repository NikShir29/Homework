def zero_column(matrix, col_index):
    result = []

    for row in matrix:
        new_row = row.copy()

        if col_index < len(new_row):
            new_row[col_index] = 0

        result.append(new_row)

    return result


def test_zero_column():
    print("Обнуление столбца")

    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    print("Исходная матрица:")
    print(matrix)

    columns_to_test = [2, 0, 4, 1]

    for col in columns_to_test:
        print(f"\nОбнуляем столбец {col}:")

        result_matrix = zero_column(matrix, col)

        print(result_matrix)


test_zero_column()