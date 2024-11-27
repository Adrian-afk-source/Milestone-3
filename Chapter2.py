def C2_Introduction():
    print("Welcome Boss!")
    C2_Decisions()

    return 3
def C2_Decisions():
    print("What do you want to do first?")
    print("1. Look through past records")
    print("2. Talk to witnesses")
    print("3. Case files")
    print("4. Go to briefing room")
    O = int(input())
    match O:
        case 1:
           pastrecords()
        case 2:
            Talktowitnesses()
        case 3:
            Casefiles()
        case 4:
            GoToBriefingRoom()
def pastrecords():
    print("Player looks through past records")
    C2_Decisions()
def Talktowitnesses():
    print("Player talks to witnesses")
    C2_Decisions()
def Casefiles():
    print("Player looks over case files")
    C2_Decisions()
def GoToBriefingRoom():
    print("Player goes over to the briefing room")
    print("Player speaks with officers in the briefing room")
    return
