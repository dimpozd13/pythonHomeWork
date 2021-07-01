matrix = [
    [1, 10, 12],
    [4, 23, 1],
    [94, 32, 1],
    [1, 2, 0]
]


"""Выводим матрицу построчно
print(matrix[0][0], matrix[0][1], matrix[0][2])
print(matrix[1][0], matrix[1][1], matrix[1][2])
print(matrix[2][0], matrix[2][1], matrix[2][2])
print(matrix[3][0], matrix[3][1], matrix[3][2])"""
i = 0
while i <= 3:
    j = 0
    while j <= 2:
        print(matrix[i][j], end=' ')
        j += 1
    print('')
    i += 1
print('\n')
"""Выводим матрицу столбиками
print(matrix[0][0], matrix[1][0], matrix[2][0], matrix[3][0])
print(matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1])
print(matrix[0][2], matrix[1][2], matrix[2][2], matrix[3][2])"""
i = 0
while i <= 2:
    j = 0
    while j <= 3:
        print(matrix[j][i], end=' ')
        j += 1
    print('')
    i += 1



