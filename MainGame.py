import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
def main():
    c = 1
    N = input("What is your name?")
    gameisrunning = True
    while gameisrunning:
        match c:
            case 1:
                c=Chapter1.C1_Introduction()
            case 2:
                c=Chapter2.C2_Introduction()
            case 3:
                c=Chapter3.C3_Introduction()
            case 4:
                c=Chapter4.C4_Introduction()
            case 5:
                gameisrunning=Chapter5.C5_Introduction()  

main() 

