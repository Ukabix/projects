
## Funkcja działanie:

def dzialanie(num1, num2):
    if a == "+":
##        print("=", num1 + num2)
        return num1 + num2
    elif a == "-":
##        print("=", num1 - num2)
        return num1 - num2
    elif a == "*":
##        print("=", num1 * num2)
        return num1 * num2
    elif a == "/":
##        print("=", num1 / num2)
        return num1 / num2


print("Witaj w kalkulatorze v0.2. W tej wersji program liczy poprzez wywołanie funkcji. Wybierz działanie i podaj liczby")

a = input("Wybierz działanie: +, -, *, /")
num1 = float(input("Podaj pierwszą liczbę"))
num2 = float(input("Podaj kolejną liczbę"))

print(num1, a, num2, "=", dzialanie(num1, num2))
