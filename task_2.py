my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {my_list}")
new_list = []
pos = 1
for el in my_list:
    if len(my_list) == pos:
        break
    if my_list[pos] > el:
        new_list.append(my_list[pos])
    pos += 1
print(f"Новый список: {new_list}")