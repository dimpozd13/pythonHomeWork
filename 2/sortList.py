list = [1, 2, 6, 23, 20, 12, 13]
length = len(list)
newList = []
i = 0

while i < length:
    newList.append(min(list))
    list.remove(min(list))
    i += 1

print(newList)