def C1_Introduction():
    print("Welcome!")
    C1_Decisions()
    return 2
def C1_Decisions():
    print("Which do you want to do?")
    print("1. Put on clothes")
    print("2. Do Hygiene")
    print("3. Leave the house")
    O = int(input())
    match O:
        case 1:
            Getdressed()
        case 2:
            Hygiene()
        case 3:
            Leave()
        case _:
            print("Thats not an option!")
def Getdressed():
    print("Player gets dressed") 
    C1_Decisions()
def Hygiene():
    print("Player is all cleaned up")
    C1_Decisions()
def Leave():
    print("Player grabs badge, gun, keys and leaves the house ")
    print("Player drives off to work")
    return 

