def plusMinus(a, b):
    if a > 0 and b > 0:
        print(a + b)
    elif a < 0 and b < 0:
        print(a - b)
    else:
        print(0)


def twoMax(a, b, c):
    list = [a, b, c]
    a1 = max(list)
    list.remove(a1)
    a2 = max(list)
    print(a1, a2)


def two(list, bl):
    if bl == False:
        newList = []
        for i in list:
            if i % 2 == 0:
                newList.append(i)
        print(newList)
    else:
        newList = []
        for i in list:
            if i % 2 != 0:
                newList.append(i)

        print(newList)


def sumAll(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


def maxMin(*numbers):
    min = numbers[0]
    max = numbers[0]
    for i in numbers:
        if i <= min:
            min = i
        elif i >= max:
            max = i

    return min, max

print(maxMin(5, 1, 2, 3, 4, -1))
