# рекурсивные и лямбда-функции, функции с произвольным числом аргументов
# функцию можно вызывать саму из себя.
# пример рекурсивной функции - вычисление числа в степени n (n – целое число)
# x**n, n - целое число

def exponent (x, n):                # функция называется exponent, с аргументами x, n - степень 
    if n == 0:                      # если n = 0, возвращает 1, любое число в степени 0 = 1.
        return 1
    else:                           # иначе по рекурсии будем вычислять степень числа x
        return x*exponent(x, n-1)   # будем вызывать туже функцию exponent, с аргументом n-1

print( exponent(3, 5) )

# x в степени n, это x * x в степени n-1
# 1. взять вычисленные значения на предыдущем шаге, умножить это на x
# 2. получим значение на текущем шаге

#  x^n = x*x^n-1    =    x*pow(x,n-1)
# Стек вызовов - эта функция , помещается в стек вызовов функции
# чтобы знать в каком порядке какие функции были вызваны

# pow(2, 3)                      - изначально в стеке вызовов x = 2, n = 3
# if n == 0: return 1            - т.к. x = 2, n = 3 пойдем на иначе
# else: return x*pow(x, n-1)     - вызовем такую же функцию pow но с значениями x = 2 , n = 2

# pow(2, 2)                      - в результате в стеке вызов получится x = 2, n = 2
# if n == 0: return 1            - т.к. x = 2, n = 2 пойдем на иначе
# else: return x*pow(x, n-1)     - вызовем такую же функцию pow но с значениями x = 2 , n = 1

# pow(2, 1)                      - в результате в стеке вызов получится x = 2, n = 1
# if n == 0: return 1            - т.к. x = 2, n = 1 пойдем на иначе
# else: return x*pow(x, n-1)     - вызовем такую же функцию pow но с значениями x = 2 , n = 0

# pow(2, 0)                      - в результате в стеке вызов получится x = 2, n = 0
# if n == 0: return 1            - т.к. x = 2, n = 0 return 1 , выполнение  данной функции завершается

# возвращаемся на уровень вверх, т.к. ф-ция pow возвратила 1, то будет х*1 (ф-ция pow(2,1) возвратит просто x) - > перешли на уровень вверх
# получается x*x = x^2, переходим на верх
# получаем x*x*x = x^3, полученное значение будет возвращать рекурсивная функция

# Функции с произвольным числом аргументов
y, z = (1, 2)                    # две переменные, а дальше значение в кортежах
# y, z = (1, 2, 3, 4)            # error
y1, *z1 = (1, 2, 3, 4)           # y1 - первое значение, z1 - возьмет все остальные значения
                                 # z1 - получится список, состоящий из всех остальных элементов кортежа
*y2, z2 = (1, 2, 3, 4)           # y2 -  возьмет все первые три значения, z2 -последнее значение

y3, *z3 = [1, "a", True, 4]       # работа со списками, необязательно использовать кортеж, в z3 - возьмет все остальные три значения

*x4, y4, z4 = "Hello world!"       # работа со строками, последние два символа в y4 и z 4
                                   # оператор * упаковывает оставшиеся значения в список

#x4                                # выполнить не можем, идет упаковка, упакованных данных

# Оператор * обратная операция   - распаковывать данные

for x1 in range(-5, 6):              # есть цикл, перебирает данные от -5 до 5
    print(x1, end="_ _")                   # в самом цикле будем выводить значение x в консоль
    
# Функция range ожидает два числовых значения, а мы список передаем, выход *
# можем потавить перед *a, список будет распакован в два значения
# for x2 in range(a):

a = [-5, 6]
for x2 in range(*a):                 # for x2 in range(a):
    print(x2, end=" ") 

# Определить случай распаковывание * и упаковывание * данных

# Если выполняется присвоение данных переменной с оператором *, то данные упаковываются. Например, *y, x = 1,2,3.
# *y, x = 1,2,3 - данные упаковываются
# Если выполняется передача списка с указанием оператора *, то происходит его распаковка. Например, range(*[-5,6]).
# range(*[-5,6]) - распаковка данных

# Можем объявлять функции с произвольным числом аргументов
def myFunc(*args):                      # объявили функцию myFunc , аргумент укажем (*args)
    print(args)                         # внутри функции выведем (args)
myFunc()                                # вызвали функцию без аргумента           # получили кортеж с соответствующим числом аргуметов 0 
myFunc(1)                               # вызвали функцию с одним аргументом      # получили кортеж с соответствующим числом аргуметов 1
myFunc(1, 2)                            # вызвали функцию с двумя аргументами     # получили кортеж с соответствующим числом аргуметов 2
myFunc(1, 3, "hello")                   # вызвали функцию с тремя аргументами     # получили кортеж с соответствующим числом аргуметов 3

def myFunc1(*arg1):                     # объявили функцию myFunc , аргумент укажем (*args)
    for arg2 in arg1:                   # переберем кортеж arg1 с помощью цикла
        print(arg2)                     # внутри функции выведем (arg2)
myFunc1(1, 3, "hello", "world")         # перебрали аргументы и вывели в консоль, получили функцию , в которую можно передавать произвольное число аргументов

# Реализуем универсальную функцию для вычисления суммы переданных ей элементов
def mySum(*args):                       # объявили функцию mySum , указали произвольное число аргументов (*args)
    S = 0                               # внутри функции выполним суммирование этих аргументов
    for arg in args:                    # перебираем список и суммируем каждое значение
        S += arg
    return S                            # возвращаем результат
print( mySum(1, 2, 3, 4, 5) )           # вызовем функцию с 5 аргументами
                                        # функция работает с произвольным числом аргументов

# Варианты определения аргументов функции 
# передадим для функции именнованные аргументы
# vocab превращается в словарь
# ключ - это имя аргумента - arg1, значение это 1
# мы знаем как перебирать элементы словаря

def myFuncVocabulary(xx, yy, *lst, sep="sep", end="end", **vocab):     # объявили функцию myFuncVocabulary, аргумент укажем (**vocab - именованные аргументы, произвольный список),
                                         # *lst - список из обычных аргументов неименованных.
                                         # неименованные аргументы должны следовать перед именованными
                                         # x, y - обычные аргументы
    print(xx, yy, lst)                                    
    print(sep, end)                      # sep="sep", end="end" - если при вызове функции не указали, то принимают значения которые прописали               
    for name, value in vocab.items():    # name - имя аргумента, value - значение, укажем что перебирать будем коллекцию vocab, и вызовем у коллекции vocab метод items
        print(name, value)               # выведем в консоль имя и значение соответствующих именованных аргументов
    # print(vocab)                       # внутри функции выведем (vocab)
    
# def myVocab(*vocab):                   # объявили функцию mySum , указали произвольное число аргументов (*args)
#    V = 0                               # внутри функции выполним суммирование этих аргументов
#    for voc in vocab:                   # перебираем список и суммируем каждое значение
#        V += voc
#    return V                            # возвращаем результат

print(myFuncVocabulary(1,2,3, sep="$", arg1=1, arg2=2, arg3=3) ) # вызовем функцию с именоваными и неименоваными аргументами,
                                                                  #( sep="$" - sep принимает символ $, а значение sep)
                                                                  # значения 1 и 2 будут относится в x, y
                                                                  # значение 3 в lst
                                                                  # функция работает с произвольным числом аргументов
                                                                  # error - еслинеименованые аргументы функции


                                                                  
# Анонимные - лямбда функции

# Функция отображения из списка тех элементов, для которых ф-ция func возвращает значение true

def showElements(lst1, func):
    for x1 in lst1:
        if func(x1):             # если func, т.е. __odd, от x возвратит True, тогда
            print(x1)            # печатаем в консоль x, отображение всех нечетных элементов

def __odd(x1):
    return True if x1 % 2 != 0 else False

# вызовем функцию showElements следующим образом
aa = [1,2,3,4,5,6,7]                 # передали список a, и функцию __odd
showElements(aa, __odd)              # второй аргумент func будет ссылаться на функцию __odd
                                     # вызываем функцию odd через синоним func

# изменим селектор __odd и мы теперь хотим выбирать все четные значения 
# получается нужно создать новую функцию __odd и передать ссылку в showElements вторым аргументом             
# это неудобно, будем использовать лямбду функцию

# Анонимные - лямбда функции - объявляются в любом месте программы по следующему синтаксису
# lambda arg1, arg2,  ... : выражение
# lambda список необязат. аргументов : один оператор

r = lambda h, m: h + m             # переменной r присваиваем лямбду функцию, у нее два аргумента h и m, складывается два числа h, m
printL = r(1, 2)                   # переменную r через лямбду функцию мы можем вызвать
                                   # лямбда функция возвращает сумму h m (результат работы :оператора)

# выберем четные элементы с помощью lambda функции
bb = [11,22,33,44,55,66,77]       # передали список bb, и лямбду функцию 
showElements(bb, lambda x1: True if x1%2==0 else False)  # укажем лямбду функцию вторым аргументом
# lambda / один аргумент x / тернарный условный оператор / будет возвращать истину / если x будет нацело делиться на два / иначе будет возвращать False
                   
# если анонимная функция не принимает никаких аргументов, то здесь ничего не пишется, кроме : и оператора
pp = lambda : "hello world"         # лямбда функция будет возвращать строчку
printPP = pp()                                # вызов лямбда функции для консоли
