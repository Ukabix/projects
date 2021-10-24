
def main():
    num = ""
    while True:
        num = input("please enter a number")
        if not num.isnumeric():
            print("This is not a number! Try again.")
        else:
            numint = int(num)
            reszta = numint % 2
            if reszta > 0:
                print("This is an odd number")
            else:
                print("This is not an odd number")

if __name__ == "__main__":
    main()

