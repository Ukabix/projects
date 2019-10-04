# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

# deklaracje funkcji
# input


def podaj_liczbe(komenda):
    return int(input(komenda))


def liczba_pierwsza_spr(liczba):
    if liczba == 1:
        liczba_pierwsza = False
    elif liczba == 2:
        liczba_pierwsza = True
    else:
        liczba_pierwsza = True
# ciąg dla parzystych, popraw
        for liczba_spr in range(2,):
            if liczba % 2 == 0:
                liczba_pierwsza = False
                break
    return liczba_pierwsza


def liczba_pierwsza_print(liczba):
    liczba_pierwsza = liczba_pierwsza_spr(liczba)
    if liczba_pierwsza:
        descriptor = ""
    else:
        descriptor = "not "
    print(liczba, " is ", descriptor, "prime.", sep="", end="\n\n")


# never ending loop
# nie podoba mi się ta pętla


while 1 == 1:
    liczba_pierwsza_print(podaj_liczbe("Enter a number to check. Ctl-C to exit."))
