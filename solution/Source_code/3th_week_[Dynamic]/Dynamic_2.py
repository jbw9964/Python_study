
N = int(input())

import time

start = time.time()

D = [True for _ in range(N + 1)]

for i in range(2, N + 1) : 
    if D[i] :                           # i 가 소수
        for j in range(2, N // i + 1) : 
            D[j * i] = False            # j * i = i 의 배수
        
for i in range(2, N + 1) : 
    if D[i] : print(i, end=' ')
print()

end = time.time()

print(end - start, 'sec')