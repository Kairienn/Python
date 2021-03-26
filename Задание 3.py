with open('my_file_3.txt', 'r') as my_file:
    sal = []
    low = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           low.append(i[0])
        sal.append(i[1])
print(f'Оклад < 20.000 {low}, средний оклад {sum(map(int, sal)) / len(sal)}')