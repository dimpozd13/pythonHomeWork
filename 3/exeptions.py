"""
try:
    print(1/0)
except ZeroDivisionError as e:
    print("Exception!")
    print(e)

try:
    dict = {"key": 23}
    print(dict["keys"])
except KeyError as e:
    print("Got it ", e)

try:
    raise TypeError("Test message")
except TypeError as e:
    print(e)

try:
    print('Fine')
except KeyError:
    print("Nope.")
else:
    print("Else")
finally:
    print("Finally")"""

x = int(input("Введите число: "))
if x % 2 == 0:
    try:
        raise ValueError("ValueError")
    except ValueError as ve:
        print(ve)
elif x <= 0:
    try:
        raise TypeError("TypeError")
    except TypeError as te:
        print(te)
elif x > 10:
    try:
        raise IndexError("IndexError")
    except IndexError as ie:
        print(ie)