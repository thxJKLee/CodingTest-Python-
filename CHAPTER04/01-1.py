N = int(input())  # 맵의 크기

move = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for dir in move:
    for i in range(len(move_types)):
        if move_types[i] == dir:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny


print(f"{x} {y}")
