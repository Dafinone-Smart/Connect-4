
gameList = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [
    " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]


def boardGame(games):
    print(" _"*7)
    for column in range(6):
        print("| " * 8)
        for row in range(7):
            if row != 6:
                print(games[column][row] + "_", end="")
                # print(games[column][row])
            else:
                print(games[column][row] + "_")
                # print(games[column][row])


def checkColumnWin():
    while (True):
        def checker():
            for i in range(0, len(gameList)):
                if i < len(gameList) - 3:
                    if gameList[i][s] == gameList[i + 1][s] == gameList[i + 2][s] == gameList[i + 3][s] == playerCounter:
                        return True
                        break
        for s in range(7):
            if checker() is True:
                return True
                break
            s += 1
            if s == 7:
                return False
                break


def checkRowWin():
    while (True):
        def checker():
            for i in range(0, len(gameList)):
                if i < len(gameList) - 2:
                    if gameList[s][i] == gameList[s][i + 1] == gameList[s][i + 2] == gameList[s][i + 3] == playerCounter:
                        return True
                        break
        for s in range(6):
            if checker() is True:
                return True
                break
            s += 1
            if s == 6:
                return False
                break


def updateInput1():
    if gameList[counter][selector] == " ":
        if playerCounter == "X":
            gameList[counter][selector] = playerCounter
            print(gameList)
            # check if player has won here
            if checkColumnWin() is True:
                print("You have won!")
                boardGame(gameList)
                exit()
            if checkRowWin() is True:
                print("You have won!")
                boardGame(gameList)
                exit()
            boardGame(gameList)
        return True
        #Player = 2


def updateInput2():
    if gameList[counter][selector] == " ":
        if playerCounter == "O":
            gameList[counter][selector] = playerCounter
            print(gameList)
            # check if player has won here
            if checkColumnWin() is True:
                print("You have won!")
                boardGame(gameList)
                exit()
            if checkRowWin() is True:
                print("You have won!")
                boardGame(gameList)
                exit()
            boardGame(gameList)
        return True
        #Player = 1


Player = 1

while(True):
    if Player == 1:
        playerCounter = input(f"Player {Player}: ")
        selector = int(
            input(f"Player {Player} enter column (0 - 6): "))
        counter = -1
        t = 0

        def checkColumn():
            for items in gameList[counter]:
                global t
                if items == " ":
                    t += 1
        checkColumn()
        if t > 0:
            if updateInput1() is True:
                Player = 2
            else:
                counter -= 1
                while gameList[counter][selector] != " ":
                    counter -= 1
                    if counter == -6:
                        if gameList[counter][selector] != " ":
                            print("This column is filled up!")
                            break
                updateInput1()
                Player = 2
        else:
            counter -= 1
            checkColumn()
            if updateInput1() is True:
                Player = 2
            else:
                counter -= 1
                while gameList[counter][selector] != " ":
                    counter -= 1
                    if counter == -6:
                        if gameList[counter][selector] != " ":
                            print("This column is filled up!")
                            break
                updateInput1()
                Player = 2
    else:
        playerCounter = input(f"Player {Player}: ")
        selector = int(
            input(f"Player {Player} enter column (0 - 6): "))
        counter = -1
        t = 0

        def checkColumn():
            for items in gameList[counter]:
                global t
                if items == " ":
                    t += 1
        checkColumn()
        if t > 0:
            if updateInput2() is True:
                Player = 1
            else:
                counter -= 1
                while gameList[counter][selector] != " ":
                    counter -= 1
                    if counter == -6:
                        if gameList[counter][selector] != " ":
                            print("This column is filled up!")
                            break
                updateInput2()
                Player = 1
        else:
            counter -= 1
            checkColumn()
            if updateInput2() is True:
                Player = 1
            else:
                counter -= 1
                while gameList[counter][selector] != " ":
                    counter -= 1
                    if counter == -6:
                        if gameList[counter][selector] != " ":
                            print("This column is filled up!")
                            break
                updateInput2()
                Player = 1


boardGame(gameList)
