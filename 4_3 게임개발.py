import sys

n, m = map(int,input().split(" "))
# 게임 지도 크기 n행 m열
x,y,direc = map(int,input().split(" "))

game = []
for _ in range(m):
    game.append(list(map(int,input().split()))) 


d = [[0]* m for i in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 북 동 남 서

def turnleft():
    global direc
    direc -= 1
    if direc == -1:
        direc = 3
count = 0; turn = 0; 
while True:
    turnleft()
    tmp_x = x + dx[direc]; tmp_y = y + dy[direc]
# 돌면 갈곳을 임시변수에 저장
    if ((game[tmp_x][tmp_y] == 0) & (d[tmp_x][tmp_y] == 0)):
        d[tmp_x][tmp_y] = 1; x = tmp_x; y = tmp_y
        count += 1
        turn = 0
# 갈곳이 없으니 돌겠습니다
    else:
        turn += 1
# 네변 돌았다는것은 그 갈곳이없는것이겠죠
    if turn == 4:
        tmp_x = x - dx[direc]; tmp_y = y - dy[direc]
        if game[tmp_x][tmp_y] == 1:
            break
        else:
            x = tmp_x; y = tmp_y
            turn = 0
# 되돌아갔으니 돌았던것을 초기화해줍시다
print(count)