# 1
print(input(), input(), input(), sep="")


# 2
a = "Люблю "
b = "тебя, "
c = "Эйлинсбург!"
print(a + b + c[:4] + c[-1])


# 3
a = "Люблю тебя, Петра творенье, "
b = "Эйли Биллиш"
c = " Ты удивительно прекрасна, как изумруд среди песка!"
message = f"{a[:12]}{b[:4]}{c[-1]}{c[:4]}{c[16:25]}{c[-1]}"
print(message)


# 4
code = "HДBрEуYг ,b dяh yсsдbе3л2а9л* #э9т3оb,f bяY Eнbаmпnиxс;аeлw nеeйu!"
print(*(char for index, char in enumerate(code) if index % 2), sep="")


# 5
word = input()
small = word.lower()
big = word.upper()
print(small, big, sep="\n")


# 6
text = input()
message = text[:].replace("1", "П").replace("2", "и").replace("3", "е")
print(message)


# 7
from re import match
password = input()
test1 = password[0].isupper()
test2 = bool(match(r"^[A-Za-z][A-Za-z0-9_]*$", password))
check_password = test1 + test2
print(check_password == 2)

# 7
print(bool(__import__("re").match(r"^[A-Z][A-Za-z0-9_]*$", input())))
