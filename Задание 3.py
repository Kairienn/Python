# Задание 3
def my_func():
    a = int(input("Значение 1 "))
    b = int(input("Значение 2 "))
    c = int(input("Значение 3 "))
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)


print(my_func())