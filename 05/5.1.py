# 1
print(tuple(input().split()))


# 2
print(t1 + t2)


# 3
print(tuple(sorted(tuple_orig)))


# 4
right_answer = tuple(input().split())
person_answer = tuple(input().split())
counter = 0
for index in range(len(right_answer)):
    if right_answer[index] == person_answer[index]:
        counter += 1
print(counter)


# 5
words = input().split()
print(len(words) - len(set(words)))


# 6
all_checks = set(map(int, input().split()))
print("Осуществляем возврат" if int(input()) in all_checks else "Такой суммы нет")


# 7
print(
    sorted(
        set(
            name
            for name in input().split() + ["Алон", "Эйли"]
            if not name.startswith("Р")
        )
    )
)

# 7
print(
    sorted(
        name
        for name in set(input().split() + ["Алон", "Эйли"])
        if not name.startswith("Р")
    )
)


# 8
# `|`
print(sorted(set(input().split()).union(set(input().split()))))


# 9
# `-`
storage_a = set(input().split())
storage_b = set(input().split())
must_be = set(input().split())
print(f"Склад 1: {sorted(must_be.difference(storage_a))}")
print(f"Склад 2: {sorted(must_be.difference(storage_b))}")


# 10
# `&`
line_1 = set(input().split())
line_2 = set(input().split())
line_3 = set(input().split())
line_4 = set(input().split())
print(len(line_1.intersection(line_4)) + len(line_2.intersection(line_3)))


# 11
# `^`
print(*sorted(set(input().split()).symmetric_difference(set(input().split()))))
