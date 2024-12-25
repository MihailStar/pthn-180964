# 1
for i in range(1, int(input()) + 1):
    if i % 90 == 0 and i % 220 == 0 and i % 888 == 0:
        print(i, end=" ")


# 2
my_iterator = iter(my_list)
while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break


# 3
print(sum(map(lambda row: sum(row), list_in)))


# 4
print("№:", "Имя:", sep=" " * 3)
for num, name in enumerate(list_q, 1):
    print(num, name, sep=" " * 4)


# 5
from math import inf
grades = tuple(int(d) for d in input().split())
max_grade = -inf
counter = 0
for grade in grades:
    if grade > max_grade:
        max_grade = grade
for grade in grades:
    if grade == max_grade:
        counter += 1
print(f"Самая высокая оценка: {max_grade}")
print(f"Количество: {counter} шт")


# 6
for subject, estimate in zip(subjects, estimates):
    print(f"{subject}:", ", ".join(map(str, estimate)))


# 7
grades = tuple(int(d) for d in input().split())
result: list[list[int]] = [[] for _ in range(5)]
for grade in grades:
    result[grade - 1].append(grade)
print(result)
