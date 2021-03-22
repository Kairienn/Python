my_list = [5, 3, 7, 0, 27, 19, 100, 108]
my_new_list = [l for number, l in enumerate(my_list) if my_list[number-1]<my_list[number]]
print(my_list)
print(my_new_list)