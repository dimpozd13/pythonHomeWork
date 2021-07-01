a = input("Введите число: ")
b = input("Введите второе число: ")
oper = input("Введите оператор: ")

if oper == "-":
    print("Разница = {}".format(int(a) - int(b)))
elif oper == "+":
    print("Сумма = {}".format(int(a) + int(b)))
else:
    print("Так еще не умею")
