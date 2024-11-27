def C4_Introduction():
    print("Player is in police cruiser")
    C4_Decisions()
    return 5
def C4_Decisions():
    print("What do you want to do?")
    print("1. Drive to suspects house")
    print("2. Go into suspects house")
    print("3. Arrest suspect")
    print("4. put suspect in transport van")
    O = int(input())
    match O:
        case 1:
            Drivetosuspectshouse()
        case 2:
            Gointosuspectshouse()
        case 3:
            Arrestsuspect()
        case 4:
            Putsuspectintransportvan()
def Drivetosuspectshouse():
    print("Player drives to suspects house")
    C4_Decisions()
def Gointosuspectshouse():
    print("Player goes into suspects house")
    C4_Decisions()
def Arrestsuspect():
    print("Player arrests suspect")
    C4_Decisions()
def Putsuspectintransportvan():
    print("Player puts suspect in transport van")
    return
