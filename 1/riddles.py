i = 0
j = 0


def condition(name, answer):
    if str.lower(str(name)) == str.lower(str(answer)):
        print("Правильно")
        global i
        i += 1
    else:
        print("Неправильно")
        global j
        j += 1


dict = {"Сколько пальцев у человека на руке? - ": 5,
        "Сколько пальцев у человека на ноге? - ": 5,
        "сколько всего пальцев и на ногах и на руках? - ": 20,
        "Как меня зовут - ": "Dima"
        }

for key in dict:
    condition(input(key), dict[key])


print("Всего вопросов было {}".format(i + j))
print("Правильных ответов {}".format(i))
print("Неправильных ответов {}".format(j))
