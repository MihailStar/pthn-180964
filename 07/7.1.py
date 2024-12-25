# 1
from typing import Generator, Sequence, TypeVar
T = TypeVar("T")
def cut_name(lst: Sequence[Sequence[T]]) -> Generator[Sequence[T], None, None]:
    for n in lst:
        yield n[:4]
my_list = ["Алон", "Эйли", "Крут Кобэйн", "Стивен Сингл"]
names = cut_name(my_list)
print(next(names))
print(next(names))
print(next(names))
print(next(names))


# 2
from typing import Generator, TypeVar
T = TypeVar("T")
def slice_generator(lst: list[T], slice_size: int) -> Generator[list[T], None, None]:
    for i in range(0, len(lst), slice_size):
        yield lst[i : i + slice_size]
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(*slice_generator(my_list, 3), sep="\n")


# 3
from typing import Generator
def foo(number: int) -> Generator[int, None, None]:
    while True:
        number *= 2
        yield number
number = int(input())
gen = foo(number)
for i in range(number):
    print(next(gen))


#
from typing import Generator
def check_password(password: str) -> bool:
    true_password = "ЭйлиВанЛав"
    return true_password == password
def password_attempts() -> Generator[str, None, None]:
    while True:
        if check_password(input()):
            yield "Добро пожаловать!"
        else:
            yield "Пароль неверный!"
input_password = password_attempts()
for i in range(5):
    print(next(input_password))


# 4
print([person for person in persons if person.istitle()])


# 5
print(*(k for k, v in computer_products.items() if 15_000 <= v <= 20_000), sep="\n")


# 6
print([int(d) ** 2 for d in input().split()])


# 7
color = input()
print([k for k in product if product[k] == color])


# 8
print({name: "Стажер" for name in input().split()})


# 9
new_product = {k for k in product if product[k] == 2024}
sorted_product = sorted(new_product)
print(sorted_product)
