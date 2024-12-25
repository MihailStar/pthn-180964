# 1
try:
    a, b = map(int, (input(), input()))
    print(a / b)
except ValueError:
    print("Ошибка. Буквы вместо чисел")
except ZeroDivisionError:
    print("Ошибка. Делить на ноль нельзя")


# 2
word = input()
if word == "Вселенная":
    answer = "Поздравляю, это правильный ответ!"
try:
    print(answer)
except NameError:
    print("Неправильный ответ")


# 3
def change_balance(money: object) -> None:
    global balance
    try:
        money = int(money)
    except ValueError:
        print("Введите число")
        return
    balance += money
    print(balance)
balance = 1000
change_balance(input())


# 4
try:
    exec(input())
    exec(input())
except Exception as e:
    print(type(e).__name__)


# 5
balance = 1000
def change_balance(money: object) -> None:
    global balance
    status = "успешно"
    try:
        money = int(money)
    except ValueError:
        status = "с ошибкой"
        print("Вы ввели слово")
    else:
        if money > balance:
            status = "с ошибкой"
            print("Недостаточно средств на балансе")
        else:
            balance -= money
            print(f"Снято денег с баланса: {money}")
    finally:
        print(f"Операция прошла {status}")
change_balance(input())


# 6
def get_age(age: object) -> None:
    if type(age) is not int or age <= 0:
        raise ValueError("Возраст должен быть положительным целым числом")
    print(age)
try:
    get_age(value)
except Exception as e:
    print(e)
