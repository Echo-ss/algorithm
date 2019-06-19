import sys
# sys.stdin.readline() 여러줄을 읽어들이는 게 빠르다. ( sys.stdin.readline() > rwa_input() > input() )
from collections import deque 
# pop()을 사용하면 n번째를 n-1번째로 옮기는 작업을 하기때문에 O(n)의 원인이 된다. 위처럼 양방향 queue 모듈을 import해서 사용한다.
sys.setrecursionlimit(10**8)
# 재귀함수가 있는 경우, 재귀 최대 깊이를 설정하자. 기본치가 작기 때문에 런타임 에러가 나올 수 있다.


a = []       # 사과가 담길 리스트 선언
q = deque()  # deque 선언


m,n = map(int, sys.stdin.readline().split())                   # 첫 번째줄, 사과박스 가로,세로 값 받기
q = deque(maxlen=m*n+1)                                        # 값이 익은 사과 배열 위치를 넣을 크기

for i in range(n):                                             # 사과들 배열 위치 받기
    a.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if int(a[i][j]) == 1:                                  # 익은 사과는 queue에 넣어 bfs 돌릴 초기값 구성
            q.append((i, j))
            
def bfs():                                                     # 너비우선탐색 return 없는 함수 선언
    dx = [-1, 0, 1, 0]                                         # 익은 사과 상하좌우 탐색하기 위한 값, 전역으로 안한건 bfs에서만 쓰일거기 때문에 굳이 메모리 차지하게 선언할 필요 없어서이다. 
    dy = [0, 1, 0, -1]
    while q:
        x,y = q.popleft()                                      # popleft() 익은 사과들어 있는 큐에서 왼쪽의 배열을 삭제하고 값은 반환한다.
        for i in range(4):                                     # 상하좌우 탐색을 반복하기 위한
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:         # 배열 값이 상자에서 벗어나면 continue
                continue
            if a[nx][ny]:                                      # 사과가 0이 아닐 때 continue, 0이면 익은 사과(Vertex) + 1 한 값을 탐색된 덜 읽은 사과 배열값에 더해주며 익은 사과로 교체 그리고 큐에 집어넣는다.
                continue
            a[nx][ny] = a[x][y] + 1                            # +1 하는 이유는, 모든 사과가 익었다면 solve에서 결과 반환 시 -1 하여 0 으로 만들기 위해서이다
            q.append((nx, ny))

def solve():                                                   # bfs 끝낸 사과 상자 풀기
    bfs()                                                      # bfs 함수 호출
    result = 0                                                 # 결과를 저장할 변수 선언
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:                                   # 사과들 중에서 0이 있으면 모두 익지 않았으므로 '-1' 반환
                return -1
            elif a[i][j] > result:                             # 사과가 0이 아니면 얼마만에 익었는지 상자안에서 탐색 순번이 마지막인 값을 찾아 변수에 저장 
                result = a[i][j]
    
    return result-1                                            # 상하좌우 사과들 익게 하면서 처음에 Vertex에 +1한 값을 빼주고 반환
    
print(solve())                                                 # 사과 상자 푸기위한 작업 solve 호출!