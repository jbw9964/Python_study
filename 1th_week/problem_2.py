
import sys
input = sys.stdin.readline

N = int(input())
List = list(map(int, input().split()))
List = [[i, v] for i, v in enumerate(List, 1)]

List = sorted(List, key=lambda x : x[1], reverse=True)

Team_1 = []
Team_2 = []

sum_1 = 0
sum_2 = 0
for student, power in List : 
    
    if sum_1 < sum_2 : 
        sum_1 += power
        Team_1.append(student)
        
    else : 
        sum_2 += power
        Team_2.append(student)

Team_1.sort()
Team_2.sort()

print()
if Team_1[0] < Team_2[0] : 
    for i in Team_1 : 
        print(i, end=' ')
    print()
    for i in Team_2 : 
        print(i, end=' ')
    print()
    print(sum_1, sum_2)
else : 
    for i in Team_2 : 
        print(i, end=' ')
    print()
    for i in Team_1 : 
        print(i, end=' ')
    print()
    print(sum_2, sum_1)
