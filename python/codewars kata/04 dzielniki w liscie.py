
num = int(input("please enter a number"))
a = []

for liczba in range (1, num + 1):
    if num % liczba == 0:
        a.append(liczba)
print(a)
