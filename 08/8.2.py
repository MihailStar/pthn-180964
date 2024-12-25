# 1
from pprint import pprint
pprint(wookie, sort_dicts=False)


# 2
from math import ceil
number_of_pupils = int(input())
print(ceil(number_of_pupils / 24))


# 3
from string import ascii_letters, digits
password = input()
for char in password:
    if char in ascii_letters or char in digits:
        continue
    print(False)
    break
else:
    print(True)


# 4
import random
def magic_cube() -> int:
    return random.randint(1, 6)


# 5
import random
def winner_selection(names: list[str]) -> str:
    return random.choice(names)


# 6
from copy import deepcopy
person1 = deepcopy(person)
person1["Ваше имя"] = ""
person1["Причина изучения программирования"] = ""
person1["Возраст"] = ""
person1["Ваши интересы"].extend([""])
