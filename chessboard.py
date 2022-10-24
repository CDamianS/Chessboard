# chessboard.py
# Edrick Galicia Villanueva, Carlos Damián Suárez Bernal
#

import random


def createBoard():
    b = []
    shape = "@"
    for row in range(8):
        r = []
        for col in range(8):
            r.append(shape)
            if col < 7:
                if shape == "@":
                    shape = "#"
                else:
                    shape = "@"
        b.append(r)
    return b


def printBoard(b):
    for r in range(8):
        for c in range(8):
            print(b[r][c], end=" ")
        print()
    print()


def placek(b):
    rk = random.randint(0, 7)
    ck = random.randint(0, 7)
    b[rk][ck] = "k"
    return b


def find(piece, b):
    for r in range(8):
        for c in range(8):
            if b[r][c] == piece:
                foundAt = [r, c]
                return foundAt
    return None


def placeK(b):
    posk = find("k", b)
    rk = posk[0]
    ck = posk[1]

    distR = 0
    distC = 0
    rK = 0
    cK = 0

    while distR <= 1 and distC <= 1:
        rK = random.randint(0, 7)
        cK = random.randint(0, 7)

        distR = abs(rk - rK)
        distC = abs(ck - cK)

    b[rK][cK] = "K"
    return b


def placeQ(b):
    posk = find("k", b)
    rk = posk[0]
    ck = posk[1]

    posK = find("K", b)
    rK = posk[0]
    cK = posk[1]

    rQ = random.randint(0, 7)
    cQ = random.randint(0, 7)
    while (rQ == rk and cQ == cK) or (rQ == rK and cQ == ck):
        rQ = random.randint(0, 7)
        cQ = random.randint(0, 7)
    b[rQ][cQ] = 'Q'
    return b


def isMoveInside(move):
    row = move[0]
    col = move[1]
    if row >= 0 and row <= 7 and col >= 0 and col <= 7:
        return True
    else:
        return False


def findMovementsFork(b):
    posk = find("k", b)
    rk = posk[0]
    ck = posk[1]

    neighboursk = [[rk, ck + 1], [rk - 1, ck + 1], [rk - 1, ck],
                   [rk - 1, ck - 1], [rk, ck - 1], [rk + 1, ck - 1],
                   [rk + 1, ck], [rk + 1, ck + 1]]

    positionsk = []
    for n in neighboursk:
        if isMoveInside(n):
            positionsk.append(n)
    return positionsk

    posK = find("K", b)
    rK = posK[0]
    cK = posK[1]

    neighboursK = [[rK, cK + 1], [rK - 1, cK + 1], [rK - 1, cK],
                   [rK - 1, cK - 1], [rK, cK - 1], [rK + 1, cK - 1],
                   [rK + 1, cK], [rK + 1, cK + 1]]

    positionsK = []
    for n in neighboursK:
        if isMoveInside(n):
            positionsK.append(n)
    return positionsK

    positions = []
    for n in neighboursK:
        if n not in neighboursK and n not in neighboursQ:
            positions.append(n)
    return positions


def findMovementsForQ(b):
    posk = find("k", b)
    rk = posk[0]
    ck = posk[1]

    posK = find("K", b)
    rK = posk[0]
    cK = posk[1]

    posQ = find("Q", b)
    rQ = posQ[0]
    cQ = posQ[1]

    r = rQ
    c = cQ
    positions = []
    check = False

    for c in range(cQ - 1, -1, -1):
        if b[rQ][c] == "K":
            break
        if b[rQ][c] == "k":
            check = True
        positions.append([rQ, c])

    for c in range(cQ + 1, 8, +1):
        if b[rQ][c] == "K":
            break
        if b[rQ][c] == "k":
            check = True
        positions.append([rQ, c])

    for r in range(rQ - 1, -1, -1):
        if b[cQ][r] == "K":
            break
        if b[cQ][r] == "k":
            check = True
        positions.append([cQ, r])

    for r in range(rQ + 1, 8, -1):
        if b[cQ][r] == "K":
            break
        if b[cQ][r] == "k":
            check = True
        positions.append([cQ, r])

    while r < 8 and c >= 0:
        if b[r][c] == "K":
            break
        if b[r][c] == "k":
            check = True
        positions.append([r], [c])

        r -= 1  #up
        c += 1  #right

    while r < 8 and c >= 0:
        if b[r][c] == "K":
            break
        if b[r][c] == "k":
            check = True
        positions.append([r], [c])

        r -= 1  #up
        c -= 1  #left

    while r < 8 and c >= 0:
        if b[r][c] == "K":
            break
        if b[r][c] == "k":
            check = True
        positions.append([r], [c])
        r += 1  #down
        c += 1  #right

    while r < 8 and c >= 0:
        if b[r][c] == "K":
            break
        if b[r][c] == "k":
            check = True
        positions.append([r], [c])

        r += 1  #down
        c -= 1  #left

    neighborsQ = [[rQ, c], [cQ, r], [r, c]]


Choice = int(input())
board = []

if Choice == 1:
    board = createBoard()
    board = placek(board)
    board = placeK(board)
    board = placeQ(board)
else:
    for r in range(8):
        line = input()
        line = line.strip()
        row = line.split(" ")
        board.append(row)

printBoard(board)
movesk = findMovementsFork(board)
print("Black King Moves:", movesk)
