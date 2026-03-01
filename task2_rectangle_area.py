def rectangle_area(a, b = None):
    if a == 0 or b == 0:
        return 0
    if b:
        s = a * b
        return f'Площадь прямоугольника: {s}'
    else:
        s = a * a
        return f'Площадь квадрата: {s}'
print(rectangle_area(7.5))
print(rectangle_area(4, 3))
print(rectangle_area(0, 0))
print(rectangle_area(3.5, 6.89))
print(rectangle_area(5, 9))