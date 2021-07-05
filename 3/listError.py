list = [1, 2, 3, 4, 5, 12, 12, 19]
i = int(input("Input index of element: "))
try:
    print(list[i])
except IndexError:
    print("Такого индекса нет!")
