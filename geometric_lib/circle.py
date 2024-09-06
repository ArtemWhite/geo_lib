import math

def area_C(r):
    return math.pi * r * r
''' 
    принимает число r - радиус,
    возводит его в квадрат,
    умножате на константное число π,
    возвращает площадь круга
        например:
            def area_C(3):
            return math.pi * 3 * 3    Ответ: 28.2743338823 
'''


def perimeter_C(r):
    return 2 * math.pi * r
'''
    принимает число r - радиус,
    умножате на константное число π и 2,
    возвращает периметр круга
        например:
            def perimeter_C(5):
            return 2 * math.pi * 5     Ответ: 31.4159265359
'''
