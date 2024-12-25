# 1
number = int(input())
def foo(number: int) -> None:
    if number % 2 == 0:
        print("Число чётное")
    else:
        print("Число нечётное")
foo(number)


# 2
line = input()
def foo_2(string: str) -> float | None:
    try:
        return float(string)
    except ValueError:
        return None
print(foo_2(line))


# 3
def check_login_password(
    *,
    login: str,
    password: str,
    check_login: str = "admin",
    check_password: str = "admin"
) -> bool:
    return login == check_login and password == check_password
authorization = check_login_password(login=input(), password=input())
print(authorization)


# 4
def super_sum(*nums: int) -> int:
    return sum(nums)
num1 = super_sum(1, 2, 3)
num2 = super_sum(10, 20, 30, 40)
num3 = super_sum(100, 200, 300, 400, 500)
num4 = super_sum()


# 5
def super_minus(**kwargs: int) -> int:
    result = kwargs.pop("super_plus") if "super_plus" in kwargs else 0
    if not kwargs:
        return result
    nums = iter(kwargs.values())
    result += next(nums)
    for num in nums:
        result -= num
    return result
num1 = super_minus(n1=10, n2=2, n3=5)
num2 = super_minus(n1=100, n2=20, n3=50, n4=10, n5=10, n6=5)
num3 = super_minus(super_plus=500, n1=100, n2=300, n3=200)
num4 = super_minus()


# 6
def buy() -> None:
    def check_balance() -> bool:
        return price < balance
    print("Покупка осуществлена" if check_balance() else "Недостаточно средств")
balance = int(input())
price = int(input())
buy()


# 7
def buy() -> None:
    def check_balance() -> bool:
        return price < balance
    def change_balance() -> None:
        global balance
        balance -= price
    if check_balance():
        change_balance()
        print("Покупка осуществлена")
    else:
        print("Недостаточно средств")
def show_balance() -> None:
    print(f"Ваш баланс: {balance}")
balance = int(input())
price = int(input())
buy()
show_balance()
