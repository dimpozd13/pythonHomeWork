def square(a, b):
    s = int(a) * int(b)
    return s


a = input("Введите одну сторону прямогугольника: ")
b = input("Введите вторую сторону прямогугольника: ")
print("Площадь прямоугольника равна: {}".format(square(a, b)))
