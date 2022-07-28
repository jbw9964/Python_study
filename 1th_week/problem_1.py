
# 풀이 변경 : brutal force

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

temp_max = 0
for i in range(len(List) - 1, 1, -1) : 
    
    target = T - List[i]
    for j in range(i - 1, 0, -1) : 
        
        if target - List[j] > 0 : 
            temp_target = target - List[j]

            for k in range(j - 1, -1, -1) : 
                
                if List[k] <= temp_target : 
                    temp_max = max(List[i] + List[j] + List[k], temp_max)
                    break
                
print(temp_max)