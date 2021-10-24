## definicje funkcji
def result_(pl1, pl2):
    if pl1 == pl2:
        return "draw"
    elif (pl1 == "R" and pl2 == "S") or (pl1 == "S" and pl2 == "P") or (pl1 == "P" and pl2 == "R"):
        return "player 1 wins!"
    elif (pl2 == "R" and pl1 == "S") or (pl2 == "S" and pl1 == "P") or (pl2 == "P" and pl1 == "R"):
        return "Player 2 wins!"


## definicja menu
def menu():
    print("Welcome. This program is a basic rock, paper, scissors game.")
    print("Please enter your selection")
    print("1. Run program")
    print("2. Credits")
    print("3. Quit")
    return input("Choose 1-3")

## blok main()
def main():
## deklaracje pustych zmiennych
    result = ""
    choice = ""
## główna pętla    
    while choice !="3":
        choice = menu()
## główne mięso        
        if choice == "1":
            pl1 = input("Player 1, please choose R-ock, P-aper, S-cissors:")
            while pl1 != "R" and pl1 != "S" and pl1 != "P":
                pl1 = input("Player 1, wrong input! Please choose R-ock, P-aper, S-cissors:")
            pl2 = input("Player 2, please choose R-ock, P-aper, S-cissors:")
            while pl2 != "R" and pl2 != "S" and pl2 != "P":
                pl2 = input("Player 2, wrong input! Please choose R-ock, P-aper, S-cissors:")
            result = result_(pl1, pl2)
            #print(result)
            #print(pl1)
            #print(pl2)
        elif choice == "2":
            print("2019, ŁP")
        elif choice == "3":
            print("See you!")
            break
        else:
            print("Wrong selection, please enter 1, 2 or 3")
        if result != "":
            print("")
            print(result)
            print("")

## oszczędzamy zasoby
if __name__ == "__main__":
    main()
    
# trudność 2,5 / 5

