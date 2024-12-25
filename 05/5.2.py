# 1
data["Компания"] = "Маркософт"
data["Работа"] = "Junior Программист"
print(data)


# 2
print({subject: [] for subject in input().split()})


# 3
print({subject: [int(d) for d in input().split()] for subject in input().split()})


# 4
from collections import Counter
counter = Counter(input().split())
print({key: counter[key] for key in sorted(dict(counter))})


# 5
description.update(description_new)
print(description)


# 6
name = input()
for name_to_class_name in (class_7A, class_7B, class_3A):
    if name in name_to_class_name:
        print(name_to_class_name[name])
        break
else:
    print("Такого ученика нет")


# 7
for k, v in stock.items():
    print(
        f"Товар: {k}, {'к сожалению закончился' if v == 0 else 'остаток {v} шт'.replace('{v}', str(v))}"
    )

# 7
for k, v in stock.items():
    print(f"Товар: {k}, {f'к сожалению закончился' if v == 0 else f'остаток {v} шт'}")


# 8
print(dict.fromkeys(input().split(), 0))


# 9
grades = [
    [int(d) for d in input().split()],
    [int(d) for d in input().split()],
    [int(d) for d in input().split()],
]
for student_index, subjects in enumerate(students.values()):
    for subject_index, student_grades in enumerate(subjects.values()):
        student_grades.append(grades[student_index][subject_index])
print(students)
