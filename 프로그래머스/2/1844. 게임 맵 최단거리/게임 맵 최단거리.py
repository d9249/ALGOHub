# bfs를 쓰겠다
from collections import deque

def solution(maps):
    max = len(maps) #maps 배열의 행
    print(max)
    may = len(maps[0]) # maps 배열의 열
    print(may)
    check = [[0] * may for i in range(max)]
    print(check)
    # check에다가는 그냥 순서만 표시 (순서 == 방문여부)
    # 방문 가능성 (=벽인지 아닌지)는 maps에서 처리
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = deque([(0,0)])
    check[0][0] = 1

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i] ,x+dx[i]
            if 0<=ny<max and 0<=nx<may:
                if check[ny][nx] == 0 and maps[ny][nx] == 1:
                    check[ny][nx] = check[y][x] + 1
                    q.append((ny,nx))
    if check[max-1][may-1] == 0: # 방문하지 못했다면
        return -1
    else:
        return check[max-1][may-1]