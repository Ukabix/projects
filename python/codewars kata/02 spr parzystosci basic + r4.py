
def main():
    num = ""
    while True:
        num = input("please enter a number")
        if not num.isnumeric():
            print("This is not a number! Try again.")
        else:
            numint = int(num)
            reszta2 = numint % 2
            reszta4 = numint % 4
            if reszta2 != 0: #dla int ciąg jak (n/2)+1, toteż:
                            #zawsze prawdziwe dla r4 >0,
                            #nie wystąpi r4=0
                print("This is an odd number")
            elif reszta4 == 0:
                print("This number is divisable by 4")
            elif reszta2 == 0:
                print("This is not an odd number")

if __name__ == "__main__":
    main()


