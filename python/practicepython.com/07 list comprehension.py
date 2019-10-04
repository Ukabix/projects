## Let’s say I give you a list saved in a variable:
## a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
## Write one line of Python that takes this list a
## and makes a new list that has only the even elements of this list in it.

## deklaracje:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# a_even = []

## pojedynczo:
# for liczba in a:
#    if liczba % 2 == 0:
#        a_even.append(liczba)
# print(a_even)

## jedna linia:
## funkcja
# a_even = [liczba for liczba in a if liczba % 2 == 0]
## cały program:

print([liczba for liczba in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if liczba % 2 == 0])

# lub

# print([liczba for liczba in a if liczba % 2 == 0]) # przy poprzedniej deklaracji a -> czy i jak mogę deklarować a = [] w tej linii?

## trudność: 1/5
