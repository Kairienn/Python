from itertools import count
from itertools import cycle

for n in count(int(input("Введите число: "))):
    if n > 15:
        break
    else:
        print(n)


my_list = ["xyz", "ABC", 123, 9, 8, 7]
counter = 0
for l in cycle(my_list):
    if counter > 7:
        break
    else:
        counter += 1
        print(l)
