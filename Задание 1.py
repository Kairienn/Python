my_file = open("my_file.txt", "w")
text = input("Введите текст \n")
while text:
    my_file.writelines(text)
    text = input("Введите текст ")
    if not text:
        break
my_file.close()
my_file = open("my_file.txt", "r")
x = my_file.readlines()
print(x)
my_file.close()

