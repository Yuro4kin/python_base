# 12.1 1. Пользователь вводит произвольные целые числа и нужно создать словарь,
#         у которого ключами будут только четные числа, а значениями – квадраты этих чисел.

# 1
d = {}
for n in input("Введите числa через запятую: ").replace(",", " ").split():
    n = int(n)
    if n % 2 == 0:
        d.setdefault(n, n ** 2)
print(d)


# 2
print(dict([[i, int(i)**2] for i in input('input: ').split() if int(i) % 2 == 0]))

# 3
b = {}                                       # Создаём пустой словарь
a = int(input("Введите целое число: "))
while a != 0:                                # Создаём условие для выхода из цикла
    a = int(input("Введите целое число: "))  # Продолжаем вводить числа
    if a % 2 == 0:                           # Если введённое число делится на 2 без остатка (чётное) то:
        b[a] = a ** 2                        # Добавляем в словарь это число в качестве ключа, а в виде значения этого числа его квадрат
        print(b)


# 4  Циклы в словарях
d3 = {a: a**2 for a in range(1, 6)}
print(d3)