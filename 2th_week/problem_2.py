
import sys
input = sys.stdin.readline

from collections import deque


N = int(input())

G = []
for _ in range(N) : 
    G.append(list(map(int, input().split())))


Queue = deque()
parking_queue = deque()
Queue.append([N - 1, N - 1])

Visit_table = [[False for _ in range(N)] for _ in range(N)]
while Queue : 
    R, C = Queue.popleft()
    Visit_table[R][C] = True

    for r, c in ([R+1,C],[R-1,C],[R,C+1],[R,C-1]) :     # 아래,위,오른,왼
        
        if not (0<=r<N and 0<=c<N) : continue

        if G[r][c] == 0 and not Visit_table[r][c] : 
            Queue.append([r, c])
        elif G[r][c] == 1 and not Visit_table[r][c] : 
            Visit_table[r][c] = True
            parking_queue.append([r, c])

Result = [parking_queue[0][0], parking_queue[0][1]]
while parking_queue : 
    R, C = parking_queue.popleft()

    count = 0
    for r, c in ([R+1,C],[R-1,C]) :             # 아래,위
        
        if not (0<=r<N and 0<=c<N) : continue
        
        if G[r][c] == 1 : count += 1

    if count == 2 : 
        Result = [R, C]
        break

    count = 0
    for r, c in ([R,C+1],[R,C-1]) :             # 오른,왼
        
        if not (0<=r<N and 0<=c<N) : continue
        
        if G[r][c] == 1 : count += 1
    
    if count == 2 : 
        Result = [R, C]
        break
    
print(Result[0] + 1, Result[1] + 1)