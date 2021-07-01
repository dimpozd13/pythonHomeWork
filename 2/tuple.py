tuple = (1.23, 1.04, 1.6, 1.8, 1.2)

max = 0
min = tuple[0]
for i in tuple:
    if i < min:
        min = i
    elif i > max:
        max = i

print("max = {}".format(max))
print("min = {}".format(min))