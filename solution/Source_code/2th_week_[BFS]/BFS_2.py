
from random import *
import heapq

temp = []
for i in range(100) : 
    temp.append(randint(1, 100))
heapq._heapify_max(temp)

import time

import sys
input = sys.stdin.readline

# List = list(map(int, input().split()))
List = temp
start = time.time()
List.insert(0, 0)

# List = list

Min_heap = False
Max_heap = False

if List[1] <= List[2] and List[1] <= List[3]: Min_heap = True
else : Max_heap = True

Length = len(List) - 1
index_count = 1
while True : 
    if 2 * index_count + 1 > Length and 2 * index_count > Length : break

    Parent = List[index_count]

    Child = []
    Child.append(List[2 * index_count])
    if not 2 * index_count + 1 > Length : 
        Child.append(List[2 * index_count + 1])

    for child in Child : 
        
        if Min_heap and child < Parent : 
            Min_heap = False
            break
        
        elif Max_heap and child > Parent : 
            Max_heap = False
            break
        
    if not Min_heap and not Max_heap : break
    index_count += 1

if not Min_heap and not Max_heap : 
    print(-1)
elif Min_heap : 
    print(1)
else : print(2)

end = time.time() - start

print(end, 'sec')