my_list = [1, 145, 1, 8, 4, 32, 27, 4, 145, 7, 33]
my_new_list = [n for n in my_list if my_list.count(n) == 1]
print(my_new_list)