# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the
# sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

import math

list = [1,1]
list.append(1+0)
print(list)

def fibonnaci():
    num = int(input("Please give a number: "))
    a = 1
    if num == 0:
        list = []
    elif num == 1:
        list = [1]
    elif num == 2:
        list = [1, 1]
    elif num > 2:
        list = [1, 1]
        while a < (num - 1): # dla num=3 -> 1x, dla 4 -> 2x itd
#            print(a)
#            print(list[a])
#            print(a-1)
#            print(list[a-1])
#            print(list[a] + list[a-1])
            list.append(list[a] + list[a-1]) # dla num=3 -> [1,1].append([1] + [1]!!! skąd tutaj 1 a nie 0???) -> dlatego że to wskazanie numeru elementu listy a nie suma, głupku! :)
#           czyli dla 3-> [1,1].append(drugi [a=1] element list [1] + pierwszy [a=0] element listy [1]
            a += 1
    return list
print(fibonnaci())
