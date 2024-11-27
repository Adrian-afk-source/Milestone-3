def C5_Introduction():
    print("Player is in transport van")
    C5_Decisions()
    return False
def C5_Decisions():
    print("Pick what you want to do?")
    print("1. Driving to the prison")
    print("2. Going home and relaxing")
    O = int(input())
    match O:
        case 1:
            Drivingtotheprison()
        case 2:
            Goinghomeandrelaxing()
def Drivingtotheprison():
    print("Player drives to the prison")
    C5_Decisions()
def Goinghomeandrelaxing():
    print("Player goes home and relaxs")
    return
    