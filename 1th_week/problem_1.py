
import sys
input = sys.stdin.readline

N, T = map(int, input().split())

List = list(map(int, input().split()))
List.sort()

while True : 
    if List[len(List) - 1] + List[0] >= T : 
        List.pop()
    elif List[len(List) - 1] + List[0] + List[1] > T : 
        List.pop()
    else : break

# for value in List : 
#     print(value, end=' ')
# print()

D = [[0 for i in range(len(List))] for i in range(3)]

for i, v in enumerate(List) : 
    D[0][i] = [v, i]


for j in range(len(List)) : 
    
    for k in range(len(List) - 1, -1, -1) : 
        if k == j : continue
        if D[0][k][0] + List[j] <= T : 
            D[1][j] = [List[j] + D[0][k][0], {j, k}]
            break

D[1].sort()

for j in range(len(List)) : 
    
    for k in range(len(List) - 1, -1, -1) : 
        
        if j in D[1][k][1] : continue
        if D[1][k][0] + List[j] <= T : 
            D[2][j] = List[j] + D[1][k][0]
            break

print(max(D[2]))




# for i in range(1, 3) : 
    
#     for j in range(len(List)) : 
        
#         temp_max = 0
#         for k in range(len(List), -1, -1) : 
#             if k == j : continue
#             if D[i - 1][k] + List[j] <= T : 
#                 D[i][j] = [List[j] + D[i - 1][k], ]
                
                
#                 break
        
#         D[i] += temp_max
    
#     D.sort()
    
    
#     pass




