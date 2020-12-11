import time
from random import *
userScore = 0
computerScore = 0
i = 1
bruh = 0

phRow1 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow2 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow3 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow4 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow5 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow6 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow7 = [0, 0, 0, 0, 0, 0, 0, 0]
phRow8 = [0, 0, 0, 0, 0, 0, 0, 0]

ehRow1 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow2 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow3 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow4 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow5 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow6 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow7 = [0, 0, 0, 0, 0, 0, 0, 0]
ehRow8 = [0, 0, 0, 0, 0, 0, 0, 0]

row1 = [0, 0, 0, 0, 0, 0, 0, 0]
row2 = [0, 0, 0, 0, 0, 0, 0, 0]
row3 = [0, 0, 0, 0, 0, 0, 0, 0]
row4 = [0, 0, 0, 0, 0, 0, 0, 0]
row5 = [0, 0, 0, 0, 0, 0, 0, 0]
row6 = [0, 0, 0, 0, 0, 0, 0, 0]
row7 = [0, 0, 0, 0, 0, 0, 0, 0]
row8 = [0, 0, 0, 0, 0, 0, 0, 0]

cRow1 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow2 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow3 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow4 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow5 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow6 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow7 = [0, 0, 0, 0, 0, 0, 0, 0]
cRow8 = [0, 0, 0, 0, 0, 0, 0, 0]

def playerHitMap():
    print(".", "1", "2", "3", "4", "5", "6", "7", "8")
    print("1", phRow1[0], phRow1[1], phRow1[2], phRow1[3], phRow1[4], phRow1[5], phRow1[6], phRow1[7])
    print("2", phRow2[0], phRow2[1], phRow2[2], phRow2[3], phRow2[4], phRow2[5], phRow2[6], phRow2[7])
    print("3", phRow3[0], phRow3[1], phRow3[2], phRow3[3], phRow3[4], phRow3[5], phRow3[6], phRow3[7])
    print("4", phRow4[0], phRow4[1], phRow4[2], phRow4[3], phRow4[4], phRow4[5], phRow4[6], phRow4[7])
    print("5", phRow5[0], phRow5[1], phRow5[2], phRow5[3], phRow5[4], phRow5[5], phRow5[6], phRow5[7])
    print("6", phRow6[0], phRow6[1], phRow6[2], phRow6[3], phRow6[4], phRow6[5], phRow6[6], phRow6[7])
    print("7", phRow7[0], phRow7[1], phRow7[2], phRow7[3], phRow7[4], phRow7[5], phRow7[6], phRow7[7])
    print("8", phRow8[0], phRow8[1], phRow8[2], phRow8[3], phRow8[4], phRow8[5], phRow8[6], phRow8[7])

def enemyHitMap():
    print(".", "1", "2", "3", "4", "5", "6", "7", "8")
    print("1", ehRow1[0], ehRow1[1], ehRow1[2], ehRow1[3], ehRow1[4], ehRow1[5], ehRow1[6], ehRow1[7])
    print("2", ehRow2[0], ehRow2[1], ehRow2[2], ehRow2[3], ehRow2[4], ehRow2[5], ehRow2[6], ehRow2[7])
    print("3", ehRow3[0], ehRow3[1], ehRow3[2], ehRow3[3], ehRow3[4], ehRow3[5], ehRow3[6], ehRow3[7])
    print("4", ehRow4[0], ehRow4[1], ehRow4[2], ehRow4[3], ehRow4[4], ehRow4[5], ehRow4[6], ehRow4[7])
    print("5", ehRow5[0], ehRow5[1], ehRow5[2], ehRow5[3], ehRow5[4], ehRow5[5], ehRow5[6], ehRow5[7])
    print("6", ehRow6[0], ehRow6[1], ehRow6[2], ehRow6[3], ehRow6[4], ehRow6[5], ehRow6[6], ehRow6[7])
    print("7", ehRow7[0], ehRow7[1], ehRow7[2], ehRow7[3], ehRow7[4], ehRow7[5], ehRow7[6], ehRow7[7])
    print("8", ehRow8[0], ehRow8[1], ehRow8[2], ehRow8[3], ehRow8[4], ehRow8[5], ehRow8[6], ehRow8[7])

def printMap():
    print(".", "1", "2", "3", "4", "5", "6", "7", "8")
    print("1", row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6], row1[7])
    print("2", row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7])
    print("3", row3[0], row3[1], row3[2], row3[3], row3[4], row3[5], row3[6], row3[7])
    print("4", row4[0], row4[1], row4[2], row4[3], row4[4], row4[5], row4[6], row4[7])
    print("5", row5[0], row5[1], row5[2], row5[3], row5[4], row5[5], row5[6], row5[7])
    print("6", row6[0], row6[1], row6[2], row6[3], row6[4], row6[5], row6[6], row6[7])
    print("7", row7[0], row7[1], row7[2], row7[3], row7[4], row7[5], row7[6], row7[7])
    print("8", row8[0], row8[1], row8[2], row8[3], row8[4], row8[5], row8[6], row8[7])

while True:
    print("//Placing phase//")
    while i < 13:
        printMap()
        print("Turn ", i)
        try:
            x = int(input("Enter an x coordinate between 1 and 8 for your battle ship: "))
            x = x - 1
            y = int(input("Enter an y coordinate between 1 and 8 for your battle ship: "))
            if x > 8 or y > 8:
                bruh = 1
            if bruh == 0:
                if y == 1:
                    row1[x] += 1
                    if row1[x] == 2:
                        row1[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 2:
                    row2[x] += 1
                    if row2[x] == 2:
                        row2[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 3:
                    row3[x] += 1
                    if row3[x] == 2:
                        row3[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 4:
                    row4[x] += 1
                    if row4[x] == 2:
                        row4[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 5:
                    row5[x] += 1
                    if row5[x] == 2:
                        row5[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 6:
                    row6[x] += 1
                    if row6[x] == 2:
                        row6[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 7:
                    row7[x] += 1
                    if row7[x] == 2:
                        row7[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
                elif y == 8:
                    row8[x] += 1
                    if row8[x] == 2:
                        row8[x] -= 1
                        print("That Square is occupied")
                        i = i - 1
        except:
            print("Enter a valid option")
            i -= 1
        if bruh == 1:
            print("Enter a valid option")
            i -= 1
        time.sleep(0.2)
        i = i + 1
        bruh = 0
    i = 0
    while i < 13:
        xComputer = randint(0, 7)
        yComputer = randint(1, 8)
        if yComputer == 1:
            cRow1[xComputer] += 1
            if cRow1[xComputer] == 2:
                cRow1[xComputer] -= 1
                i = i - 1
        elif yComputer == 2:
            cRow2[xComputer] += 1
            if cRow2[xComputer] == 2:
                cRow2[xComputer] -= 1
                i = i - 1
        elif y == 3:
            cRow3[xComputer] += 1
            if cRow3[xComputer] == 2:
                cRow3[xComputer] -= 1
                i = i - 1
        elif y == 4:
            cRow4[xComputer] += 1
            if cRow4[xComputer] == 2:
                cRow4[xComputer] -= 1
                i = i - 1
        elif yComputer == 5:
            cRow5[xComputer] += 1
            if cRow5[xComputer] == 2:
                cRow5[xComputer] -= 1
                i = i - 1
        elif y == 6:
            cRow6[xComputer] += 1
            if cRow6[xComputer] == 2:
                cRow6[xComputer] -= 1
                i = i - 1
        elif yComputer == 7:
            cRow7[xComputer] += 1
            if cRow7[xComputer] == 2:
                cRow7[xComputer] -= 1
                i = i - 1
        elif yComputer == 8:
            cRow8[xComputer] += 1
            if cRow8[xComputer] == 2:
                cRow8[xComputer] -= 1
                i = i - 1
        i = i + 1
    i = 1
    printMap()
    print("//Placing phase over//")
    print("//Shooting phase begins//")
    while i < 10:
        print("Turn ", i)
        try:
            gX = int(input("What x coordinate are you aimng at?: "))
            gY = int(input("What y coordinate are you aimng at?: "))
            gX -= 1
            time.sleep(1)
            if gY == 1:
                if cRow1[gX] == 1:
                    print("Hit!")
                    cRow1[gX] += 1
                    userScore += 100
                    phRow1[gX] = "X"
                elif cRow1[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow1[gX] = "M"
            elif gY == 2:
                if cRow2[gX] == 1:
                    print("Hit!")
                    cRow2[gX] += 1
                    userScore += 100
                    phRow2[gX] = "X"
                elif cRow2[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow2[gX] = "M"
            elif gY == 3:
                if cRow3[gX] == 1:
                    print("Hit!")
                    cRow3[gX] += 1
                    userScore += 100
                    phRow3[gX] = "X"
                elif cRow3[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow3[gX] = "M"
            elif gY == 4:
                if cRow4[gX] == 1:
                    print("Hit!")
                    cRow4[gX] += 1
                    userScore += 100
                    phRow4[gX] = "X"
                elif cRow4[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow4[gX] = "M"
            elif gY == 5:
                if cRow5[gX] == 1:
                    print("Hit!")
                    cRow5[gX] += 1
                    userScore += 100
                    phRow5[gX] = "X"
                elif cRow5[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow5[gX] = "M"
            elif gY == 6:
                if cRow6[gX] == 1:
                    print("Hit!")
                    cRow6[gX] += 1
                    userScore += 100
                    phRow6[gX] = "X"
                elif cRow6[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow6[gX] = "M"
            elif gY == 7:
                if cRow7[gX] == 1:
                    print("Hit!")
                    cRow7[gX] += 1
                    userScore += 100
                    phRow7[gX] = "X"
                elif cRow7[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow7[gX] = "M"
            elif gY == 8:
                if cRow8[gX] == 1:
                    print("Hit!")
                    cRow8[gX] += 1
                    userScore += 100
                    phRow8[gX] = "X"
                elif cRow8[gX] >= 2:
                    print("You have already hit there!")
                else:
                    print("Miss!")
                    phRow8[gX] = "M"
        except:
            print("Enter a valid option")
            i -= 1
        print("Computer's turn")
        gCX = randint(0, 7)
        gCY = randint(1, 8)
        time.sleep(1)
        if gCY == 1:
            if row1[gCX] == 1:
                print("You have been hit!")
                computerScore += 100
                ehRow1[gCX] = "X"
                row1[gCX] += 1
            elif row1[gCX] != 1:
                print("You evaded the hit!")
                ehRow1[gCX] = "M"
        if gCY == 2:
              if row2[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow2[gCX] = "X"
                  row2[gCX] += 1
              elif row2[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow2[gCX] = "M"
        elif gCY == 3:
              if row3[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow3[gCX] = "X"
                  row3[gCX] += 1
              elif row3[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow3[gCX] = "M"
        elif gCY == 4:
              if row4[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow4[gCX] = "X"
                  row4[gCX] += 1
              elif row4[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow4[gCX] = "M"
        elif gCY == 5:
              if row5[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow5[gCX] = "X"
                  row5[gCX] += 1
              elif row5[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow5[gCX] = "M"
        elif gCY == 6:
              if row6[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow6[gCX] = "X"
                  row6[gCX] += 1
              elif row6[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow6[gCX] = "M"
        elif gCY == 7:
              if row7[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow7[gCX] = "X"
                  row7[gCX] += 1
              elif row7[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow7[gCX] = "M"
        elif gCY == 8:
              if row8[gCX] == 1:
                  print("You have been hit!")
                  computerScore += 100
                  ehRow8[gCX] = "X"
                  row8[gCX] += 1
              elif row8[gCX] != 1:
                  print("You evaded the hit!")
                  ehRow8[gCX] = "M"
        else:
            print("You evaded the hit")
        print("Your hits: ")
        playerHitMap()
        print("Enemy hits: ")
        enemyHitMap()
        i += 1
        
    if userScore > computerScore:
        print("You win!")
        input()
        break
    elif userScore == computerScore:
        print("Draw!")
        input()
        break
    else:
        print("You lose!")
        input()
        break
