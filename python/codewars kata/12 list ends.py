# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.

import random

def listCreate():
    num = random.randint(1,10)
    print(num)
    list1 = list(range(1, num + 1))
    print(list1)
    return list1


def listOrder(num):
    list2 = []
    list2.extend([num[0], num[-1]])
    #print(list2)
    return list2


print(listOrder(listCreate()))
