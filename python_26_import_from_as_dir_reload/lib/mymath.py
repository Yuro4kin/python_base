# файл будет состоять из одной константы и трех функций

PI = 3.1415
print("Значение PI: ", PI)

# функция находит max из двух чисел a и b  
def max2(a, b):
         return a if(a > b) else b

# функция находит max из трех чисел a, b, c  
def max3(a, b, c):
         return max2(a, max2(b, c))

# функция находит сумму тех величин, которые передаем в качестве аргументов 
def sum(*vals):
         print("mysum_catalog_lib: ")
         S = 0
         for x in vals:
                   S += x
         return S

# Подключим модуль mymath.py к нашей программе
