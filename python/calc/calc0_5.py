import math

## definicje działań
def suma(num1, num2):
    return num1 + num2
def roznica(num1, num2):
    return num1 - num2
def iloczyn(num1, num2):
    return num1 * num2
def iloraz(num1, num2):
    return num1 / num2
def potega(num1):
    return num1 * num1
def pierwiastek(num1):
    return (math.sqrt(num1))

## definicja menu
def Menu():
    print("Witaj w kalkulatorze v0.5. W tej wersji program korzysta z definicji pojedynczych funkcji matematycznych, "
          "posiada sekcję main algorytmu oraz obsługuje moduł math (stąd pierwiastek)")
    print("Wyberz działanie")
    print("1. Suma")
    print("2. Różnica")
    print("3. Iloczyn")
    print("4. Iloraz")
    print("5. Potęga ^2")
    print("6. Pierwiastek V2")
    print("7. Wyjście")
    return (input("Wybierz 1-7"))

## blok main()
def main():
## deklaracje pustych zmiennych
    wynik = "" ##placeholder do odpowiedzi
    dzialanie1 = "" ##placeholder do odpowiedzi
    dzialanie = "" 
    while dzialanie !="7": ##główna pętla
        dzialanie = Menu()
        dzialanie1 = ""
        if dzialanie == "1":
            dzialanie1 = "suma"
            num1=float(input("Podaj pierwszą liczbę:"))
            num2=float(input("Podaj drugą liczbę:"))
            wynik = suma(num1, num2)
        elif dzialanie == "2":
            dzialanie1 = "różnica"
            num1 = float(input("Podaj pierwszą liczbę:"))
            num2 = float(input("Podaj drugą liczbę:"))
            wynik = roznica(num1, num2)
        elif dzialanie == "3":
            dzialanie1 = "iloczyn"
            num1 = float(input("Podaj pierwszą liczbę:"))
            num2 = float(input("Podaj drugą liczbę:"))
            wynik = iloczyn(num1, num2)
        elif dzialanie == "4":
            dzialanie1 = "iloraz"
            num1 = float(input("Podaj pierwszą liczbę:"))
            num2 = float(input("Podaj drugą liczbę:"))
            wynik = iloraz(num1, num2)
        elif dzialanie == "5":
            dzialanie1 = "potęga"
            num1 = float(input("Podaj liczbę:"))
            wynik = potega(num1)
        elif dzialanie == "6":
            dzialanie1 = "pierwiastek"
            num1 = float(input("Podaj liczbę:"))
            wynik = pierwiastek(num1)
        elif dzialanie == "7":
            break ## teoretycznie przydałoby się obejść break
        else:
            print("Wybierz jedno z dostępnych działań przy pomocy klawiszy 1-7.")
        if wynik != "":
            print("")
            print("Wynik działania", dzialanie1, "na liczbach ", num1, " i ", num2, " wynosi", wynik) ##poprawić dla potegi i pierwiastka, bo wyświetla num 2


main()
