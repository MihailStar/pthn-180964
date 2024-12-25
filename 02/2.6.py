# 1
rating = ["чудовищно", "не фонтан", "середнячок", "недурно", "отлично"]
student_to_rating = {"Dony Jepp": 0, "Mill Buray": 1, "Lorlando Bum": 3}
for s, r in student_to_rating.items():
    print(f"{s} вёл себя сегодня {rating[r]}")


# 2
student: list[int] = []
student.append(5)
student.extend([2, 3, 4])
student[student.index(2)] = 1
del student[student.index(3)]
del student[student.index(4)]
print(student)


# 3
from collections import Counter
# result: tuple[str, str, *tuple[int, ...]]
pupil, subject, *grades = result
counter = Counter(grades)
print(f"Имя: {pupil}")
print(f"Предмет: {subject}")
for grade in range(1, 6):
    print(f"Количество {grade}: {counter.get(grade, 0)}")


# 4
print(f"[{input().split(' ')}]")


# 5
print(sorted(dony_jepp + mill_burey + lorlando_bum, reverse=False))
print(sorted(dony_jepp + mill_burey + lorlando_bum, reverse=True))


# 6
student = []
student.extend([["Политология"], ["Физкультура"], ["География"]])
student[student.index(["Политология"])].extend([5, 5, 5])
student[student.index(["Физкультура"])].extend([3, 3, 3])
student[student.index(["География"])].extend([4, 4, 4])
print(student)


# 7
p1, p2, p3, *p4, p5 = present
print(p1, p2, p3, p4, p5)
