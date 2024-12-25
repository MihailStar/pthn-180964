# 1
if input() == "start":
    print("Запускаю программу")


# 2
cities = input().split()
print(
    f"Слово{' ' if cities[0][-1].lower() == cities[1][0].lower() else ' не '}подходит"
)


# 3
match input():
    case "металл":
        print("жёлтый")
    case "бумага":
        print("синий")
    case "стекло":
        print("зелёный")
    case "пластик":
        print("оранжевый")
    case _:
        print("ручная сортировка")


# 4
list_name = ["Джони Депп", "Джеки Чан", "Билли Айлиш"]
name = input()
if name not in list_name:
    print("Мошенник!")


# 5
from re import fullmatch
print(fullmatch(r"[A-Z][^\s]+[0-9]", input()) is not None)


# 6
opening_time, closing_time, day_off_of_week = input().split()
opening_time, closing_time = int(opening_time), int(closing_time)
time, day_of_week = input().split()
time = int(time)
if day_of_week == day_off_of_week or time < opening_time or time >= closing_time:
    print("Закрыто")
else:
    print("Открыто")


# 7
login = input()
password = input()
if login == "admin":
    if password == "read":
        print("Редактор в режиме чтения")
    elif password == "edit":
        print("Редактор в режиме редактирования")
    else:
        print("Неправильный пароль")
else:
    print(f"Пользователь {login}")


# 8
if isinstance(request[0], (int, float)) and isinstance(request[2], (int, float)):
    print("Алон, всё нормально, это числа!")
else:
    print("Алон, исправь строки на числа!")
