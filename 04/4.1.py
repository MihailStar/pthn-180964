# 1
print(*(i for i in range(1, 6)))


# 2
stop, step = map(int, input().split())
print([i for i in range(step, stop + 1, step)])


# 3
password = input()
counter = 0
while True:
    if password == input():
        print("вошли в почту")
        break
    else:
        counter += 1
        if counter % 3 == 0:
            print("три раза уже неправильно, соберись!")
        else:
            print("неправильный пароль")


# 4
from random import randint, seed
seed(333)
counter = 0
while True:
    counter += 1
    if randint(1, 3) == 3:
        break
print(counter)


# 5
for item in list_in:
    print(item)


# 6
print(*(i for i in range(int(input()) + 1)))


# 7
op_a = int(input())
for op_b in range(1, 10):
    print(op_a, "*", op_b, "=", op_a * op_b)


# 8
print(*sorted(list_num, reverse=True)[:4])


# 9
words = input().split()
for word in words:
    if word.lower() in ("эээ", "типа", "короче", "ну", "как бы"):
        print("Слова паразиты обнаружены")
        break
else:
    print("Слов паразитов не обнаружено")


# 10
from functools import reduce
print(reduce(lambda result, row: result + row, list_in, []))
