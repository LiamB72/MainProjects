# Most of the program was realized by me, however the engine on itself, was coded by my teacher, as a base for us.

from scripts.variables import *
from scripts.spriteLoader import *
from scripts.UILoader import *

# initialisation graphique
pygame.init()
pygame.display.set_caption("Dungeon Game!")
font = pygame.font.SysFont("Comic Sans", 20)


def mapLoad(mapLayout, mapNb):
    global difficulty

    # Map 1
    if mapNb == 1:
        if difficulty == 1:
            file = open("mapLayouts\map011.csv", "r")
        elif difficulty == 2:
            file = open("mapLayouts\map012.csv", "r")

    # Map 2
    elif mapNb == 2:
        if difficulty == 1:
            file = open("mapLayouts\map021.csv", "r")
        elif difficulty == 2:
            file = open("mapLayouts\map022.csv", "r")

    # Map 3
    elif mapNb == 3:
        if difficulty == 1:
            file = open("mapLayouts\map031.csv", "r")
        elif difficulty == 2:
            file = open("mapLayouts\map032.csv", "r")

    # Reads the file
    c = csv.reader(file, delimiter=",")

    # Input the file's content in a 2D array
    for ligne in c:
        mapLayout.append(ligne)

    # Close the file
    file.close()

    return mapLayout


mapLoad(mapLayout, mapNb)

# print(len(mapLayout), len(mapLayout[0]))

# ----------------------------------- #
# 0 North, 1 East, 2 South, 3 West
if difficulty == 1:
    d = 2
    x = 1
    y = 7
elif difficulty == 2:
    d = 0
    x = 13
    y = 6
elif difficulty == 0:
    d = 2
    x = 1
    y = 7
# ----------------------------------- #


def showText(x, y, txt):
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher, (x, y))


def endScreen():
    fenetre.blit(img4, (0, 0))


def keySprite(xSprite, ySprite):
    fenetre.blit(imgKey, (xSprite, ySprite))


def showWallNorth():
    # background 0
    global x, y
    base()
    if y > 2:
        if mapLayout[y - 3][x - 1] == "0":
            b01()
        if mapLayout[y - 3][x + 1] == "0":
            b02()
        if mapLayout[y - 3][x] == "0":
            b03()
    # background 1
    if y > 1:
        if mapLayout[y - 2][x - 1] == "0":
            b11()
        if mapLayout[y - 2][x + 1] == "0":
            b12()
        if mapLayout[y - 2][x] == "0":
            b13()
    # background 2
    if mapLayout[y - 1][x - 1] == "0":
        b21()
    if mapLayout[y - 1][x + 1] == "0":
        b22()
    if mapLayout[y - 1][x] == "0":
        b23()
    # background 3
    if mapLayout[y][x - 1] == "0":
        b31()
    if mapLayout[y][x + 1] == "0":
        b32()


def showWallSouth():
    # background 0
    global x, y
    base()
    if y < len(mapLayout) - 3:
        if mapLayout[y + 3][x + 1] == "0":
            b01()
        if mapLayout[y + 3][x - 1] == "0":
            b02()
        if mapLayout[y + 3][x] == "0":
            b03()
    # background 1
    if y < len(mapLayout) - 2:
        if mapLayout[y + 2][x + 1] == "0":
            b11()
        if mapLayout[y + 2][x - 1] == "0":
            b12()
        if mapLayout[y + 2][x] == "0":
            b13()
    # background 2
    if mapLayout[y + 1][x + 1] == "0":
        b21()
    if mapLayout[y + 1][x - 1] == "0":
        b22()
    if mapLayout[y + 1][x] == "0":
        b23()
    # background 3
    if mapLayout[y][x + 1] == "0":
        b31()
    if mapLayout[y][x - 1] == "0":
        b32()


def showWallEast():
    # background 0
    global x, y
    base()
    if x < len(mapLayout[0]) - 3:
        if mapLayout[y - 1][x + 3] == "0":
            b01()
        if mapLayout[y + 1][x + 3] == "0":
            b02()
        if mapLayout[y][x + 3] == "0":
            b03()
    # background 1
    if x < len(mapLayout[0]) - 2:
        if mapLayout[y - 1][x + 2] == "0":
            b11()
        if mapLayout[y + 1][x + 2] == "0":
            b12()
        if mapLayout[y][x + 2] == "0":
            b13()
    # background 2
    if mapLayout[y - 1][x + 1] == "0":
        b21()
    if mapLayout[y + 1][x + 1] == "0":
        b22()
    if mapLayout[y][x + 1] == "0":
        b23()
    # background 3
    if mapLayout[y - 1][x] == "0":
        b31()
    if mapLayout[y + 1][x] == "0":
        b32()


def showWallWest():
    # background 0
    global x, y
    base()
    if x > 2:
        if mapLayout[y + 1][x - 3] == "0":
            b01()  # Left Wall 3 tiles away
        if mapLayout[y - 1][x - 3] == "0":
            b02()  # Right Wall 3 tiles away
        if mapLayout[y][x - 3] == "0":
            b03()  # Center wall 3 tiles away
    # background 1
    if x > 1:
        if mapLayout[y + 1][x - 2] == "0":
            b11()
        if mapLayout[y - 1][x - 2] == "0":
            b12()
        if mapLayout[y][x - 2] == "0":
            b13()
    # background 2
    if mapLayout[y + 1][x - 1] == "0":
        b21()
    if mapLayout[y - 1][x - 1] == "0":
        b22()
    if mapLayout[y][x - 1] == "0":
        b23()
    # background 3
    if mapLayout[y + 1][x] == "0":
        b31()
    if mapLayout[y - 1][x] == "0":
        b32()


def showWalls():
    if d == 0:
        showWallNorth()
        # print("North", end=" ")
    if d == 1:
        showWallEast()
        # print("East", end=" ")
    if d == 2:
        showWallSouth()
        # print("South", end=" ")
    if d == 3:
        showWallWest()
        # print("West", end=" ")
    # print(y, x)


def base():
    fenetre.blit(img0, (0, 0))
    if debugMod == True:
        showMapMenu(0, 352)
    elif debugMod == False:
        showMapMenu(450, 0)


def keyInput(keyPressed):
    global x, y, d, unlockedKeys, mapNb, fenetre, showMap
    if keyPressed in ["e", "z", "a", "q", "s", "d", "w", "y", "v"]:
        if showMap == 0:
            if (
                (keyPressed == "d" and d == 0)
                or (keyPressed == "z" and d == 1)
                or (keyPressed == "q" and d == 2)
                or (keyPressed == "s" and d == 3)
            ) and mapLayout[y][x + 1] != "0":
                x = x + 1
            elif (
                (keyPressed == "z" and d == 0)
                or (keyPressed == "q" and d == 1)
                or (keyPressed == "s" and d == 2)
                or (keyPressed == "d" and d == 3)
            ) and mapLayout[y - 1][x] != "0":
                y = y - 1
            elif (
                (keyPressed == "q" and d == 0)
                or (keyPressed == "s" and d == 1)
                or (keyPressed == "d" and d == 2)
                or (keyPressed == "z" and d == 3)
            ) and mapLayout[y][x - 1] != "0":
                x = x - 1
            elif (
                (keyPressed == "s" and d == 0)
                or (keyPressed == "d" and d == 1)
                or (keyPressed == "z" and d == 2)
                or (keyPressed == "q" and d == 3)
            ) and mapLayout[y + 1][x] != "0":
                y = y + 1

            elif keyPressed == "e":
                d = (d + 1) % 4

            elif keyPressed == "a":
                d = (d - 1) % 4

        if not debugMod:
            if keyPressed == "w":
                showMap += 1
                if showMap == 0:
                    fenetre = fenetre = pygame.display.set_mode((448, 326))
                elif showMap == 1:
                    fenetre = fenetre = pygame.display.set_mode((900, 326))

                if showMap > 0:
                    showMap = -1

        if debugMod == True:
            if keyPressed == "w":
                unlockedKeys += 1
                print(unlockedKeys)
            if keyPressed == "y":
                x = int(input("What x cord? : "))
                y = int(input("What y cord? : "))
            if keyPressed == "v":
                changeMap(mapNb + 1, 1, 1, 1)
        showWalls()


def showMapMenu(positionX, positionY):
    for yCol in range(len(mapLayout)):
        for xLigne in range(len(mapLayout[0])):
            if mapLayout[yCol][xLigne] == "0":
                pygame.draw.rect(
                    fenetre,
                    NOIR,
                    [
                        positionX + xLigne * CARRE,
                        positionY + yCol * CARRE,
                        CARRE,
                        CARRE,
                    ],
                )
            elif mapLayout[yCol][xLigne] == "3":
                pygame.draw.rect(
                    fenetre,
                    ROUGE,
                    [
                        positionX + xLigne * CARRE,
                        positionY + yCol * CARRE,
                        CARRE,
                        CARRE,
                    ],
                )
            elif mapLayout[yCol][xLigne] == "2":
                pygame.draw.rect(
                    fenetre,
                    VERT,
                    [
                        positionX + xLigne * CARRE,
                        positionY + yCol * CARRE,
                        CARRE,
                        CARRE,
                    ],
                )
            else:
                pygame.draw.rect(
                    fenetre,
                    BLANC,
                    [
                        positionX + xLigne * CARRE,
                        positionY + yCol * CARRE,
                        CARRE,
                        CARRE,
                    ],
                )
    if debugMod:
        pygame.draw.rect(
            fenetre, BLEU, [positionX + x * CARRE, positionY + y * CARRE, CARRE, CARRE]
        )


def changeMap(mapNumber, xPlayer, yPlayer, directionPlayer):
    global x, y, d, mapNb, unlockedKeys, timeNow, startTime, stopClock, fenetre, debugMod

    # Player Coords
    x = xPlayer
    y = yPlayer
    d = directionPlayer

    # Reset Variables
    unlockedKeys = 0
    timeNow = 0
    stopClock = 0
    startTime = False

    # Setting Up Map (#)
    mapNb = mapNumber

    # Clearing the map 2D array
    mapLayout.clear()
    print("Map No.", mapNb - 1, "deloaded")

    # Clearing the screen
    pygame.draw.rect(fenetre, NOIR, [0, 0, 450, 1000])
    pygame.draw.rect(fenetre, NOIR, [450, 0, 1000, 260])

    # Loading the next map
    mapLoad(mapLayout, mapNumber)

    # Show the new set of walls
    showWalls()

    # Debug ONLY - Setting up the gameplay screen size
    if debugMod:
        fenetre = pygame.display.set_mode((448, 640))
    elif not debugMod:
        fenetre = pygame.display.set_mode((448, 326))

    # Refresh the gameplay screen
    print("Loaded Map No.", mapNb)
    pygame.display.flip()

    return x, y, d, mapNb, unlockedKeys, timeNow, startTime, stopClock


def timeWall():
    global unlockedKeys, stopClock, startTime, difficulty, timeNow

    #### Difficulty: Normal ####
    if difficulty == 1:

        # First timer
        if x == 1 and y == 1 and unlockedKeys == 2:
            stopClock = int(time.perf_counter())  ## Initialize the clock
            print("You Have 25 Seconds to Complete this first Dungeon!")
        if unlockedKeys == 3:

            # Debugging

            if debugMod:
                print(
                    "<35 :",
                    (timeNow - stopClock < 35),
                    " >=35:",
                    (timeNow - stopClock >= 35),
                )

            # Lesser than 35s and the tile = 1
            if timeNow - stopClock < 35:
                mapLayout[5][23] = "1"

            # Bigger than 35s and the tile = 0
            elif timeNow - stopClock >= 35:
                mapLayout[5][23] = "0"
                unlockedKeys = 2
                print("Times out!")

    #### Difficulty: Hard ####
    elif difficulty == 2:

        if mapNb == 1:
            ## Door 1
            if x == 7 and y == 7 and unlockedKeys == 2:
                stopClock = int(time.perf_counter())  ## Initialize the clock
                print("You Have 25 Seconds to Complete this first Dungeon!")
            if unlockedKeys == 2:

                # Debugging
                if debugMod:
                    print(
                        "<25 :",
                        (timeNow - stopClock < 25),
                        " >=25:",
                        (timeNow - stopClock >= 25),
                    )

                # Lesser than 25s and the tile = 1
                if timeNow - stopClock < 25:
                    mapLayout[4][2] = "1"

                # Bigger than 25s and the tile = 0
                elif timeNow - stopClock >= 25:
                    mapLayout[4][2] = "0"
                    unlockedKeys = 1
                    print("Times out!")

            ## Door 2
            if x == 21 and y == 10 and unlockedKeys == 6:
                stopClock = int(time.perf_counter())  ## Initialize the clock
                print("You Have 25 Seconds to Complete this first Dungeon!")
            if unlockedKeys == 7:

                # Debugging
                if debugMod:
                    print(
                        "<15 :",
                        (timeNow - stopClock < 15),
                        " >=15:",
                        (timeNow - stopClock >= 15),
                    )

                # Lesser than 15s and the tile = 1
                if timeNow - stopClock < 15:
                    mapLayout[13][19] = "1"

                # Bigger than 15s and the tile = 0
                elif timeNow - stopClock >= 15:
                    unlockedKeys = 6
                    mapLayout[13][19] = "0"
                    print("Times out!")
        # Map 2
        if mapNb == 2:

            if x == 22 and y == 1 and unlockedKeys == 7:
                stopClock = int(time.perf_counter())  ## Initialize the clock
                print("You got 50 seconds to reach the end!")
            if unlockedKeys == 8:

                ## Debugging ##

                if debugMod:
                    print(
                        "<50 :",
                        (timeNow - stopClock < 50),
                        " >=50:",
                        (timeNow - stopClock >= 50),
                    )

                ##-----------##

                # Lesser than 50s and the tile = 1
                if timeNow - stopClock < 50:
                    mapLayout[1][19] = "1"

                # Bigger than 50s and the tile = 0
                elif timeNow - stopClock >= 50:
                    unlockedKeys = 7
                    mapLayout[1][19] = "0"
                    print("Times out!")

    if debugMod:
        print("time:", stopClock)
        print("timeNow:", timeNow)
        print("Unlocked Keys:", unlockedKeys)


def keyUnlocker(xAxis, yAxis, previousKeyUnlocked, nextKeyUnlocked):
    global x, y, unlockedKeys, mapNb

    if x == xAxis and y == yAxis and unlockedKeys == previousKeyUnlocked:
        unlockedKeys = nextKeyUnlocked
        if unlockedKeys == 1:
            print(unlockedKeys, "key unlocked")
        elif unlockedKeys > 1:
            print(unlockedKeys, "keys unlocked")

    # KEY 1
    if unlockedKeys >= 1 and difficulty == 1 and mapNb == 1:
        mapLayout[13][8] = "1"
    if unlockedKeys >= 1:
        keySprite(460, 270)

    # KEY 2
    if unlockedKeys >= 2:
        keySprite(494, 270)

    # KEY 3
    if unlockedKeys >= 3 and difficulty == 1 and mapNb == 1 and x == 18 and y == 13:
        mapLayout[13][20] = "0"
        mapLayout[13][22] = "0"
        mapLayout[12][21] = "1"
        mapLayout[14][21] = "3"
        print("Timer Stopped! Congrats for reaching the end!")
    if unlockedKeys >= 3:
        keySprite(528, 270)

    # KEY 4
    if unlockedKeys >= 4:
        keySprite(562, 270)

    # KEY 5
    if unlockedKeys >= 5 and difficulty == 2 and mapNb == 1:
        mapLayout[12][9] = "1"
    if unlockedKeys >= 5:
        keySprite(596, 270)
    
    # KEY 6
    if unlockedKeys >= 6 and difficulty == 2 and mapNb == 1:
        mapLayout[5][21] = "1"
    if unlockedKeys >= 6:
        keySprite(630, 270)

    # KEY 7
    if unlockedKeys >= 7:
        keySprite(664, 270)


showWalls()

# ----- Game Loop ----- #
loop = True
while loop == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            keyInput(event.unicode)
            if event.key == pygame.K_ESCAPE:
                loop = False
    # ----- Debugging ----- #
    if debugMod:
        pygame.draw.rect(fenetre, NOIR, [0, 330, 1000, 40])
        showText(280, 335, "x:")
        showText(300, 335, x)
        showText(330, 335, "y:")
        showText(350, 335, y)
    # --------------------- #

    if difficulty == 1:
        # Map No.1
        if mapNb == 1:
            timeWall()
            keyUnlocker(3, 11, 0, 1)
            keyUnlocker(7, 6, 1, 2)
            keyUnlocker(1, 1, 2, 3)

            if x == 21 and y == 14:
                changeMap(2, 1, 1, 1)
        # Map No.2
        elif mapNb == 2:
            for i in range(2):
                mapLayout[14 - i][21] = "0"

            if x == 18 and y == 1:
                changeMap(3, 1, 1, 1)

        # Map No.3
        elif mapNb == 3:
            if x == 22 and y == 21:
                pygame.draw.rect(fenetre, NOIR, [0, 0, 10000, 10000])
                fenetre = pygame.display.set_mode((400, 300))
                endScreen()
                showMap = 0
                pygame.display.flip()
                time.sleep(3)
                break

    elif difficulty == 2:
        if mapNb == 1:
            timeWall()
            keyUnlocker(11, 9, 0, 1)
            keyUnlocker(7, 7, 1, 2)
            keyUnlocker(1, 1, 2, 3)
            keyUnlocker(2, 10, 3, 4)
            keyUnlocker(20, 1, 4, 5)
            keyUnlocker(1, 12, 5, 6)
            keyUnlocker(21, 10, 6, 7)
            keyUnlocker(19, 13, 7, 8)
            if x == 19 and y == 6:
                if debugMod:
                    height = 640
                else:
                    height = 320
                changeMap(2, 2, 1, 2)

        if mapNb == 2:
            timeWall()
            keyUnlocker(5, 7, 0, 1)
            keyUnlocker(9, 7, 1, 2)
            keyUnlocker(4, 13, 2, 3)
            keyUnlocker(9, 13, 3, 4)
            keyUnlocker(18, 12, 4, 5)
            keyUnlocker(21, 7, 5, 6)
            keyUnlocker(17, 5, 6, 7)
            keyUnlocker(22, 1, 7, 8)

            if x == 20 and y == 1:
                changeMap(3, 1, 1, 1)
    timeNow = int(time.perf_counter())

    pygame.display.flip()

pygame.quit()
