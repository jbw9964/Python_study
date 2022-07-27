
# from random import *
# import heapq
# list = [0]
# for i in range(1000) : 
#     value = randint(1, 100)
#     list.append(value)
#     pass

# heapq.heapify(list)
# print(list)
# # heapq._heapify_max(list)

import time

from collections import deque
import sys
input = sys.stdin.readline

List = list(map(int, input().split()))
start = time.time()
List.insert(0, 0)

# List = list

Min_heap = False
Max_heap = False

if List[1] < List[2] : Min_heap = True
else : Max_heap = True

Queue = deque()
Queue.append(List[1])
Length = len(List) - 1
index_count = 1
while True : 
    if 2 * index_count + 1 > Length and 2 * index_count > Length : break
    
    Parent = Queue.popleft()

    Child = []
    Child.append(List[2 * index_count])
    if not 2 * index_count + 1 > Length : 
        Child.append(List[2 * index_count + 1])

    for child in Child : 
        
        if Min_heap : 
            if child > Parent : 
                Queue.append(child)
            else : Min_heap = False

        else : 
            if child < Parent : 
                Queue.append(child)
            else : Max_heap = False
        
    if not Min_heap and not Max_heap : break
    index_count += 1


if not Min_heap and not Max_heap : 
    print(-1)
elif Min_heap : 
    print(1)
else : print(2)

end = time.time() - start

print(end, 'sec')