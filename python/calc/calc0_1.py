
print("Witaj w kalkulatorze v0.1. To zupełnie bazowa wersja. Do dzieła -> wybierz działanie i podaj liczby")

a = input("Wybierz działanie: +, -, *, /")
num1 = float(input("Podaj pierwszą liczbę"))
num2 = float(input("Podaj kolejną liczbę"))


if a == "+":
    print(num1, a, num2, "=", num1 + num2)
elif a == "-":
    print(num1, a, num2, "=", num1 - num2)
elif a == "*":
    print(num1, a, num2, "=", num1 * num2)
elif a == "/":
    print(num1, a, num2, "=", num1 / num2)

