rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("my_file_4.txt", "r") as file:
    for l in file:
        l = l.split(" ", 1)
        new_file.append(rus[l[0]] + " " + l[1])
    print(new_file)

with open("my_file_4_new.txt", "w") as file_2:
    file_2.writelines(new_file)


