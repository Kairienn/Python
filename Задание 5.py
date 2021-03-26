def summary():
    try:
        with open('my_file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры, разделенные пробелами \n')
            file_obj.writelines(line)
            number = line.split()
            print(sum(map(int, number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильный номер.')


summary()
