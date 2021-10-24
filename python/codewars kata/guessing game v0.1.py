foo = "cośtam"
liczba_prob = 5


def main():
    proba = ""
    proba_n = 0
    brak_prob = False
    while proba != foo and not(brak_prob): ## Z war 1 -> 2, teoretycznie można drugi war ominąć
        if proba_n < liczba_prob:
            proba_n += 1
            proba = input("Podaj słowo: ")
            print("Pozostało Ci ", liczba_prob - proba_n, "prób odgadnięcia słowa" )
        else:
            brak_prob = True
            ## dla spr -> print(brak_prob)
    if brak_prob:
        print("Przegrywasz, nie pozostała żadna próba odganięcia.")
    else:
        print("wygrywasz")

if __name__ == "__main__":
    main()
