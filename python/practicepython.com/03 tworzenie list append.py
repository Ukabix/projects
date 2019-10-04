a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

#basic
#for liczba in a:
#    if liczba < 5:
#        print(liczba)

#extra 1
#for liczba in a:
#    if liczba < 5:
#        x.append(liczba)
#        print(x)

#extra 2
print([liczba for liczba in a if liczba < 5])

#extra 3
# num = int(input("Please give a number"))
#for liczba in a:
#   if liczba < num :
#       x.append(liczba)
#       print(x)
