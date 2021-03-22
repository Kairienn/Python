from itertools import count
from math import factorial


def fact():
    for x in count(1):
        yield factorial(x)


crie = fact()
counter = 0
for z in crie:
    if counter < 7:
        print(z)
        counter += 1
    else:
        break
