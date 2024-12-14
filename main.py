import random

# Список значений для заполнения матрицы
values = [-15, -4, -2, -7, 0, 3, 5, 12, 7]

# Случайное определение высоты и ширины матрицы в пределах от 4 до 8
height = random.randint(4, 8)
width = random.randint(4, 8)

# Создание матрицы с заданной высотой и шириной, заполненной случайными значениями из списка 'values'
matrix = [[random.choice(values) for i in range(width)] for k in range(height)]

# Печать матрицы
for arr in matrix:
    for num in arr:
        print(num, end=" ")
    print()

# Инициализация суммы нечетных чисел
sum = 0

# Перебор всех элементов матрицы и суммирование нечетных чисел
for i in matrix:
    for k in i:
        if k % 2 != 0:
            sum += k

# Вывод суммы нечетных чисел
print("Сумма нечетных чисел:", sum)
