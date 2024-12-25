# 1
names = open("people_names.txt", encoding="utf-8")
print(names.read())
names.close()


# 2
with open("people_names.txt", encoding="utf-8") as names:
    print(names.readline())
    print(names.readline())
    print(names.readline())


# 3
with open("people_names.txt", encoding="utf-8") as names:
    list_file = names.readlines()
    print(list_file[3])


# 4
with open("people_names.txt", encoding="utf-8") as names:
    print(names.readline(), end="")
    print(names.readline(), end="")
    names.seek(0)
    print(names.readline(), end="")


# 5
with open("people_names.txt", encoding="utf-8") as names:
    for line in names:
        print(line.strip())


# 6
with open("people_names.txt", encoding="utf-8") as names:
    my_list = [line.strip() for line in names]
    print(my_list)


# 7
data = {"велосипед": 10, "самокат": 20, "мопед": 30}
with open("magazine.txt", "w", encoding="utf-8") as file:
    for key, value in data.items():
        file.write(f"{key} = {value}\n")


# 8
new_data = {"вертолёт": 40, "поезд": 50, "катер": 60}
with open("magazine.txt", "a", encoding="utf-8") as file:
    for key, value in new_data.items():
        file.write(f"{key} = {value}\n")


# 9
last_data = {"гироскутер": 70, "автобус": 80, "трамвай": 90}
with open("magazine.txt", "a+", encoding="utf-8") as file:
    for key, value in last_data.items():
        file.write(f"{key} = {value}\n")
    file.seek(0)
    print(file.read())
