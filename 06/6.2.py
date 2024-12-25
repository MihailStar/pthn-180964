# 1
def input_my_desires(*desires: str) -> None:
    """"""
    for _desire in desires:
        ...
    print("Ваши желания приняты! А теперь приложите усилия для их исполнения!")
input_my_desires("")


# 2
print(
    sorted(
        map(
            lambda item: item[0],
            filter(lambda item: 17 < item[1] < 31, persons.items()),
        )
    )
)

# 2
print(sorted(filter(lambda k: 17 < persons[k] < 31, persons)))


# 3
print(
    *sorted(persons, key=lambda person: (person["bad habits"], -person["age"])),
    sep="\n"
)


# 4
print(
    *sorted(
        map(
            lambda person: person["name"],
            filter(lambda person: person["rating"] >= 4.5, persons),
        )
    ),
    sep="\n"
)


# 5
from typing import Callable
def input_kassa(s: int) -> tuple[Callable[[int], None], Callable[[], None]]:
    def operation_with_kassa(n: int) -> None:
        nonlocal s
        s += n
    def print_kassa() -> None:
        print(s)
    return (operation_with_kassa, print_kassa)
operation_with_kassa, print_kassa = input_kassa(int(input()))
operation_with_kassa(int(input()))
operation_with_kassa(int(input()))
operation_with_kassa(int(input()))
print_kassa()


# 6
from functools import wraps
from typing import Callable, ParamSpec, TypeVar
P = ParamSpec("P")
R = TypeVar("R")
def info_operation(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        global balance
        old_balance = balance
        result = func(*args, **kwargs)
        if old_balance > balance:
            print("Покупка совершена!")
        elif old_balance < balance:
            print("Баланс пополнен!")
        else:
            print("Недостаточно средств!")
        return result
    return wrapper
@info_operation
def decrease_balance(num: int) -> None:
    global balance
    if (balance - num) >= 0:
        balance -= num
@info_operation
def increase_balance(num: int) -> None:
    global balance
    balance += num
balance = int(input())
op1, op2, op3 = int(input()), int(input()), int(input())
decrease_balance(op1)
increase_balance(op2)
decrease_balance(op3)
