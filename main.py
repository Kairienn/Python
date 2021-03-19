# my_list = ["abc", 123, int(45), {15: 'xyz'}]
# print(my_list)
# for l in my_list:
#   print(l, type(l))


# list = ["1", "2", "3", "X", "Y", "Z", "A", "B", "C"]
# counter = 0
# for i in range(int(len(list) / 2)):
#    list[counter], list[counter + 1] = list[counter + 1], list[counter]
#    counter += 2
#print(list)

# month = int(input("Месяц "))
# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
# if month in winter:
#    print("Winter")
# elif month in spring:
#    print("Spring")
# elif month in summer:
#    print("Summer")
# elif month in autumn:
#    print("Autumn")

# winter = dict.fromkeys([12, 1, 2],"winter")
# winter[3] = "spring"
# winter[4] = "spring"
# winter[5] = "spring"
# winter[6] = "summer"
# winter[7] = "summer"
# winter[8] = "summer"
# winter[9] = "autumn"
# winter[10] = "autumn"
# winter[11] = "autumn"
# if month in winter.keys():
#    print(winter[month])


# list = input("Слова")
# for x in enumerate(list.split()):
#    if len(x[1]) > 10:
#       x = (x[0], x[1][:9])
#    print(x)


# new = int(input("Новый эелемент "))
# my_list = [146, 53, 17, 8, 1]
# my_list.append(new)
# my_list.sort()
# my_list.reverse()
# print(my_list)

# counter = 1
# my_list = []
# list1 = []
# list2 = []
# list3 = []
# list4 = []
# numbers_of_tovar = int(input("Введите количество товаров "))
# while counter <= numbers_of_tovar:
#    tovar = str(input("Введите название "))
#    price = int(input("Введите цену "))
#    number = int(input("Введите количество "))
#    ed_izm = str(input("Единицы измерения "))
#    dict = {"название": tovar, "цена": price, "количество": number, "ед": ed_izm}
#    itog = (counter, dict)
#    counter += 1
#    my_list.append(itog)
#    list1.append(tovar)
#    list2.append(price)
#    list3.append(number)
#    list4.append(ed_izm)
# for x in my_list:
#    print(x)
# dict1 = {"название": list1, "цена": list2, "количество": list3, "ед": list4}
# print(dict1)

