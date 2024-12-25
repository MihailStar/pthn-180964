# 1
print(list(map(int, input().split("."))))


# 2
print([float(input()) for _ in range(3)])


# 3
number = int(str(num1) + str(num2))
print(number)


# 4
point1 = float(input())
point2 = float(input())
distance = abs(point1 - point2)
print(round(distance, 1))


# 5
name_str = input()
print(f"Название: {name_str}")
number_int = int(input())
print(f"Количество: {number_int} шт")
specs = input().split()
spec1, spec2, spec3 = specs
print(f"Описание товара: {', '.join(specs)}")
price1, price2, price3 = map(float, input().split())
print(f"Приблизительная цена: {price1}, {price2}, {price3}")
review = input()
print(review)


# 6
print(
    f"Максимальное значение валюты: {max(exchange_rate) if exchange_rate else 'неизвестно'}"
)
print(
    f"Минимальное значение валюты: {min(exchange_rate) if exchange_rate else 'неизвестно'}"
)


# 7
grades = [int(d) for d in input().split()]
print(f"Оценка за четверть: {round(sum(grades) / len(grades))}")

# 7
from statistics import mean
grades = [int(d) for d in input().split()]
print(f"Оценка за четверть: {round(mean(grades))}")


# 8
print("".join(sorted(list(input().lower()))))
