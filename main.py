from sys import argv
script_name, time, salary, bonus = argv
print('Название скрипта: ', script_name)
print("Время работы: ", time)
print("Зарплата: ", salary)
print("Премия: ", bonus)
time = int(time)
salary = int(salary)
bonus = int(bonus)


def my_func():
    result = time * salary + bonus
    print(result)


my_func()

