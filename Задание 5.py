# Задание 5
def my_func():
    new_itog = 0
    symbol = False
    while symbol == False:
        numbers = input("Введите строку чисел или ^ для выхода ").split()
        itog = 0
        for l in range(len(numbers)):
            if numbers[l] == '^':
                symbol = True
                break
            else:
                itog = itog + int(numbers[l])
        new_itog = new_itog + itog
        print(new_itog)


print(my_func())
