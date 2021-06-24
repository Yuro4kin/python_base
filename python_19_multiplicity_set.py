# Множество (set) – это неупорядоченная коллекция уникальных элементов.
# Для создания множества используется следующий синтаксис:
# {значение1, значение2, …, значениеN}

a = {1,2,3,"hello"}                 # множество а состоящее из элементов (в фигурных скобках числовые значения и строка)
                                    # объявление похоже на словарь, но в словаре еще указываются ключи
                                    # в множествах ключей нет, только значения
aa = {1,2,3,"hello", 1,2,3,"hello"} # множествах нет дублирующих значений - дублирующий неунекальный элемент не добавляется                                 
print(a, type(a))

# Ключевая особенность множества - в этой коллекции автоматически отбрасываются все дубли

# В качестве значений множества можно использовать любой неизменяемый тип: числа, строки, кортежи
b = {1,1,"hi","hi",("a","b"), ("a","b")}
#  число / строка / кортеж
# Множество – это неупорядоченная коллекция print: число / кортеж / строка 

# Создаем пустое множество  помощью функции set
bb = set()
print(type(bb))

b1 = {}                            # создается пустой словарь а не множество
print(type(b1))

# В качестве аргумента укажем любой итерируемый объект:
b2 = set("hello world!")           # множество состоящее из уникальных элементов этого итерируемого объекта
                                   # все дубли отброшены, оставлены уникальные символы
b3 = set([1,1,2,3,5,3,2,1])        # вместо строки укажем коллекцию, т.е список - получим множество уникальных элементов этого списка 

# Создадим множество с помощью функции range
b4 = set(range(7))

# Использование множеств в программах
# Нам нужно удалить все повторяющиеся элементы в списке a == >
# Создадим множетво на основе этого списка == >
# И далее из этого множества b получим обратно список a, используя функцию list

a1 = [1,2,3,43,2,4,3,2,1]           # нам нужно из списка удалить все дубли
bs = set(a1)                        # сначала переведем в множество из уникальных значений
a1 = list(bs)                       # затем переведем,  обратно в список, используя функцию list

a1 = list(set(a1))                  # две последние операции можно объединить в одну вот так - краткая форма
                                    # удаляем все неунекальные элементы

# обратимся по отдельному индексу к элементу множества НЕ МОЖЕМ
# bs[0]                             # error
# setAA[0]                          # error
# Как перебрать все элементы множества? Используем цикл for
setA1 = {7,6,5,4,3}                 # есть множество setA 
for x in setA1:                     # цикл for, и перебираем все коллекцию setA1
   print(x)                         # выводим в консоль
                                    
# Методы добавления/удаления элементов в множестве
b5 = set([1,1,2,3,5,3,2,1])         # добавим в коллекцию, т.е список множество новый элемент
b5.add(7)                           # метод add добавит элемент, если такого еще нет
b5.update(["a", "b", (10,12),(1,2)])# метод update добавит список элементов в множество
# добавим: строку / кортеж / кортеж # кортеж и строки - это разные элементы 
b5.update("abrakadabra")            # список, значения которого будет добавлен в множество, с проверкой их уникальности
                                    # в качестве аргумента метода update можно указывать любой перебираемый объект

# Удаление элемента по значению используется метод .discard()
b5.discard(3)
# при повторном вызове метода b5.discard(3) множество не изменяется
b5.discard(3)                       # множество не изменяется
b5.remove(2)                        # метод для удаления элемента по значению – remove 
#b5.remove(2)                       # error - данный метод возвращает ошибку при попытке удаления несуществующего значения , т.к. значение __ в множестве уже нет.

b5.pop()                            # метода pop - возвращает удаляемое значение, а сам удаляемый элемент оказывается, в общем-то, случайным, т.к. множество – это неупорядоченный список
                                    # pop выбирает случайный элемент которвый будет удален
print("метод pop - возвращает удаляемое значение: ", b5.pop())

# c = set()
# c.pop()                           # error - метод pop для пустого множества

# Метод clear - удалить все элементы, в результате получим пустое множество
b6 = set([1,1,2,3,5,3,2,1])
b6.clear()                          # пустое множество

# Операции над множествами
# функция len()
# Для определения длины (числа уникальных элементов) множества используется функция len:
a2 = {"abc", (1,2), 5, 4, True}
len(a2)                             # используется функция len()
print("Число элементов множества a2: ", len(a2))

# Оператор in
# проверка наличия элемента в множестве используется оператор in:
print("Проверка элемента abc в множества a2: ", "abc" in a2)     # Ответ булевое значение True
# Обратный оператор not in
# проверка на невхождение элемента в множество
print("Проверка на отсутствие элемента 7 в множества a2: ", 7 not in a2)       # Ответ булевое значение True

# Пересечение множеств - для любых двух множеств
# можно вычислять их пересечение, то есть, находить значения,
# входящие в состав обоих множеств. Это делается с помощью оператора &
setA = {1,2,3,4}
setB = {3,4,5,6,7}
res = setA & setB                   # элементы 3 и 4 одновременно и множеству setA и setB
                                    # создается новое множество с соответств. значениями (исходные множества не меняются)
                                    # в переменной res сохранили результат пересечения множеств
print("Проверка на пересечение множест setA{1,2,3,4} и setB{3,4,5,6,7} : ", res)

# Результат пересечения двух множеств присвоим множеству setA
# setA = setA & setB                # длинная форма записи - выведет в консоль {3,4}
# setA &= setB                      # краткая форма записи - выведет в консоль {3,4}

setC = {9, 10, 11}
setA & setC                         # выведет в консоль set() - пустое множество, т.к. эти два множества не пересекаются

# Метод intersection - возвращает результат пересечения этих множеств
# Сами же множества остаются без изменений
setD = {1,2,3,4}
setE = {3,4,5,6,7}
setD.intersection(setE)             # эквивалент setA & setB
result = setD.intersection(setE)
print("Проверка на пересечение множест методом setD.intersection(setE) setD{1,2,3,4} и setE{3,4,5,6,7} : ", result)
setD.intersection_update(setE)      # эквивалент setA &= setB # краткая форма записи - выведет в консоль {3,4}

# Вычисление объединения двух множеств
# Получим множество состоящее из неповторяющихся значений обеих множеств
setDD = {1,2,3,4}
setEE = {3,4,5,6,7}
resDD_EE = setDD | setEE
print("множество неповторяющихся значений из обоих множеств setDD | setEE : ", resDD_EE)
setDD |= setEE                      # краткая форма записи

# Объединяем два множества методом .union()
resUnion = setDD.union(setEE)                  # Сами же множества остаются без изменений
print("Объединяем два множества setDD и setEE методом .union() : ", resUnion)

# Вычитание множеств между собой
# Элементы которые присутствуют и в множестве А и в множестве В, из ножества А будут удалены
# 3,4  - удалены, т.к. относятся и к множеству A и к множеству B

setAB = {1,2,3,4}
setBC = {3,4,5,6,7}
resMinus = setAB - setBC
print("Вычитание множеств setAB - setBC: ", resMinus)
resMinuss = setBC - setAB
print("Вычитание множеств setBC - setAB: ", resMinuss)
setAB -= setBC                      # эквивалент setAB - setBC # краткая форма записи

# Cимметричная разность - множество в котором отсутствуют повторяющиеся элементы
setAA = {1,2,3,4}
setBB = {3,4,5,6,7}
symmetryDiv = setAA ^ setBB
print("Множество, составленное из значений, не входящих одновременно в оба множества setAB ^ setBC: ", symmetryDiv)

# Сравнение множеств
comparison = setAA == setBB
print("Сравнение множеств setAA - setBB: ", comparison)

# Сравнение множеств на равенство и неравенство
# Множества считаются равными, если все элементы, входящие в одно множество,
# также принадлежат другому множеству и мощности этих множеств равны (т.е. содержат одинаковое число элементов)
setCC = {7,6,5,4,3}; setDD = {3,4,5,6,7}
equality = setCC == setDD
#equalit = setCC != setDD                    # Противоположный оператор вернет False - т.к. множества равны
print("Равные множества setCC - setDD: ", equality)

# Oператоры < , >  - определяют вхождение или не вхождение одного множества в другое
# Математически одно множество входит в другое, если все элементы первого множества принадлежат элементам второго множества
setF = {7,6,5,4,3}; setG = {3,4,5}
entry_Nonentry = setG < setF
print("Множество setG входит в множество setF: ", entry_Nonentry)
setG.add(22)                        # Добавим элемнт который не входит в множество setF - получим False
                                    # Операции < , > - будут вовзвращать False, как бы мы их не записывали 

# Для равных множеств
setH = {7,6,5,4,3}; setI = {3,4,5,6,7}
less_or_equal = setH <= setI
more_or_equal = setH >= setI
print("Множество setH меньше или равно множеству setI: ", less_or_equal)
print("Множество setH больше или равно множеству setI: ", more_or_equal)
