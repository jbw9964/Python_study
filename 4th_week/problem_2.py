
def DFS(Visit_table : list, Process_table : list, E : list, V : int, N : int) -> int : 
    
    if Visit_table[V] and Process_table[V] : return True

    Visit_table[V] = True
    Process_table[V] = True
    Result = False
    for i in range(N) : 
        if E[V][i] == 1 : 
            Result = DFS(Visit_table, Process_table, E, i, N)
            Visit_table[i] = False
            Process_table[i] = False
    
    return Result


import sys
input = sys.stdin.readline

N = int(input())

E = []
for _ in range(N) : 
    E.append(list(map(int, input().split())))

Cycle = -1

for V in range(N) : 
    
    Visit_table = [False for i in range(N)]
    Process_table = [False for i in range(N)]
    
    Cycle = DFS(Visit_table, Process_table, E, V, N)
    
    if Cycle == 1 : break

if Cycle == 1 : print(1)
else : print(-1)

