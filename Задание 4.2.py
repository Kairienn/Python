# Задание 4.2
def my_func():
    x = int(input("Значение 1 "))
    y = int(input("Значение 2 "))
    chislo = x
    counter = 0
    while counter >= y:
        chislo *= (1/x)
        counter -= 1
    return chislo


print(my_func())