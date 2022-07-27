
N = int(input())

import time

start = time.time()

D = [True for _ in range(N + 1)]

for i in range(2, N + 1) : 
    if D[i] : 
        for j in range(2, N // i + 1) : 
            D[j * i] = False
        
for i in range(2, N + 1) : 
    if D[i] : print(i, end=' ')
print()

end = time.time()

print(end - start, 'sec')