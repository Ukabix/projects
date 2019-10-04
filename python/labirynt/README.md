# labirynt
Notatki i pomysły:

Mapa:
Założenie

    012 
    345 
    678 

- czy generować po każdym ruchu:
przez funcję if + print jak niżej?

def map_generator
    if lokacja == 5:
        print("012")
        print("34X")
        print("678")
    elif lokacja == 6: itd
- czy doczepić do funkcji 


Interakcje z menu:
    P-odnieś klucz
    U-żyj klucza
    N-orth
    S-outh
    W-est
    E-ast
- może spróbować input z numerycznej? skróci ilość tur do wygrania, do rozważenia

To do:
    Losowa generacja lokalizacji klucza! 
    - funkcja random dla lokacji 1 do 8 - 7 (startowa)
    if gameturn == 0:
        loklist2 = [0, 1, 2, 3, 4, 5, 6, 8]
        keylok = random.choice(loklist2)
        print(keylok)  # spr
    return keylok
    
    powiązanie z lokacjami poprzez:
    
    if  keylok == 1:
        lok1_has_key = True
    elif keylok ==1:
        lok2_has_key = True
    [...]
    
    Losowe eventy? 
    - powiedzmy 3 -> funkcja random założonego P (powiedzmy 10% dla każdej lokacji, generowane za każdym razem przy jej odwiedzeniu
    
    switch
        ranenc = random.randint(0,10)
            if ranenc == 0:
                #event
    
    Limit tur na ukończenie labiryntu? - czemu nie, można też dodać coś z time i ustawić limit na 2 minuty?
    Jakaś grafika na ukończenie? - jak to zrobić? -> import asset.gif? i podpiąć do funkcji "game_win"?




