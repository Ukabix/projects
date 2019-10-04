import time

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
    else:
        print("Zaraz, zaraz!")
        time.sleep(3)
        print("O nie! Nie wybrano działania, nie ma takiego liczenia!")


print("Witaj w kalkulatorze v0.3. W tej wersji program poinformuje Cię w uprzejmy sposób, że wybrałeś niodpowiednie działanie matematyczne. "
      "Wybierz działanie i podaj liczby")

a = input("Wybierz działanie: +, -, *, /")
num1 = float(input("Podaj pierwszą liczbę"))
num2 = float(input("Podaj kolejną liczbę"))

print(num1, a, num2, "=", dzialanie(num1, num2))
