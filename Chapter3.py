def C3_Introduction():
    print("Player is in Briefing room")
    C3_Decisions()
    return 4
def C3_Decisions():
    print("What do you want to do?")
    print("1. Talk with SWAT")
    print("2. Get into police cruiser")
    O = int(input())
    match O:
        case 1:
            TalkwithSWAT()
        case 2:
            Getintopolicecruiser()
def TalkwithSWAT():
    print("Player talks with SWAT")
    C3_Decisions()
def Getintopolicecruiser():
    print("Player gets into police cruiser")
    return
    
