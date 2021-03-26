my_file_2 = open("my_file_2.txt", "r")
y = my_file_2.readlines()
print(f'Количество строк: {len(y)}')
my_file_2 = open("my_file_2.txt", "r")
while True:
    z = my_file_2.readline().split()
    if not z:
        break
    print(z)
    print(f'Кол-во слов: {len(z)}')
my_file_2.close()



