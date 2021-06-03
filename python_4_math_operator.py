# int     - для целочисленных значенй
# float   - для вещественных значений
# complex - для комплексных
# /,//    - деление
# %       - остаток деления
# **      - возведение в степень
# Операнд - то к чему применяется оператор
# Унарный оператор - который применяется к одному операнду

# Унарный минус
a = 1; a = -a
print(a)

# Бинарный минус - применяется к двум операндам
b = 1; c = 2
d = c-b
print(d)

# Умножение, сложение
e = 2; f = -5.8; g = 2.3
print( (e+f)*g )

# Деление вещественное
h = 3; i = 2
j = h/i
print(j)

# Деление целочисленное //
k = 3; l = 2
m = k//l
print(m)

# Остаток от деления % (7 входит один раз в 5 - остается число 2)
# Остаток от деления % (5 ни разу не входит в 4 - это 0 раз, остается остаток от деления 4)
# Остаток от деления % (находим ближайшее наименьшее число кратное 5, это -10, и остаток берется как разность -9-(-10)=-9+10=1  "ИМЕТЬ ВВИДУ ПРИ ПЕРЕНОСЕ ПРОГРАМ с С++ на Python) )

n = 7; o = 5
p = n%o
print(p)

n1 = 4; o1 = 5
p1 = n1%o1
print(p1)

n2 = -9; o2 = 5
p2 = n2%o2
print(p2)

# x**y - возведение в степень работет справа на лево
x = 2; y = 5
print(x**y)

# x1**y1 - возведение в степень вещ. числа (1/2 квадратный корень с 1.96)
x1 = 1.96; y1 = 0.5
print(x1**y1)

# x1**y1 - возведение в степень вещ. числа (кубический корень из 27)
# (1/3) - нужно брать в скобки
x2 = 27; y2 = 1/3
print(x2**y2)

# x**y - возведение в степень работет справа на лево (сначала 3 в 2 = 9, затем 2 в 9 = 512)
x3 = 2; y3 = 3; z3 = 2
print(x3**y3**z3)

# Оператор присваивания, увеличить или уменьшить переменное на определенное число
# Переменную i увеличиваем на 1, переменную r уменьшаем на 2
# Приоритет у операции присваивания наименьший => сначала сложение или вычитание => потом присваивание
# 5 + 1 = 6 -> затем переменная i ссылается на объект 6
i = 5; r = 3
i = i + 1
r = r - 2
print(i, r)

i1 = 6; r1 = 4
i1 += 1       # i = i + 1 
r1 -=  2      # j = j - 2
print(i1, r1)

i *=3
r /=4
print(i, r)

a1 = 5; b1 = 10
a1 **= 2
b1 //= 3
print(a1, b1)

# Комплексные числа
a2 = 1 + 2j
b2 = 2 -3j
print(a2 + b2)
print(a2-b2)
print(a2*b2)
print(a2/b2)
print(a2**b2)

# Комплексные числа
a3 = 1 + 2j
b3 = 2 -3j
print(a3.real)  # a.real - взять действительную часть комплексного числа
print(b3.imag)  # b.imag - взять мнимую часть комплексного числа

# Делаем комплексно сопряженное число из переменной а3 =>   1 - 2j
sa = a3.conjugate();
print(sa)

# Арифметические операции - встроенные ФУНКЦИИ для работы с числами
# abs(x)                - вычисляет модуль числа
# round(x)              - округляет x до ближайшего целого
# min(x1, x2,...,x_n)   - находит минимальное среди указанных чисел
# max(x1, x2,...,x_n)   - находит максимальное, среди указанных чисел
#pow(x, y)              - воводит x в степень y

# >>> abs(-5)
# 5
xy = abs(-5)
print(xy)

xz = round(2.5)
print(xz)

yz = round(2.51)
print(yz)

xx = pow(2, 3)
print(xx)

# Библиотека MATH - подключил в консоли Shell
import math
a22 = 2.4
b22 = math.cos(a22)
print(b22)
print(math.floor(1.7) )
print(math.ceil(1.7) )
print(math.sqrt(2.56) )

# >>> math.ceil(5.3) - округление до наибольшего целого
# 6
# >>> math.floor(5.3) - округление до наибольшего целого
# 5
