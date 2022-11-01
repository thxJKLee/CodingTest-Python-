N = int(input())  # 맵의 크기

move = input().split()
myLoc = [1, 1]

for _ in range(len(move)):
    if move[_] == "L":
        if myLoc[1] > 1:
            myLoc[1] -= 1
    elif move[_] == "R":
        if myLoc[1] < N:
            myLoc[1] += 1
    elif move[_] == "U":
        if myLoc[0] > 1:
            myLoc[0] -= 1
    elif move[_] == "D":
        if myLoc[0] < N:
            myLoc[0] += 1

print(f"{myLoc[0]} {myLoc[1]}")
