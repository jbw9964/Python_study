
N = int(input())

D = [[0] for _ in range(N + 1)]
D[1] = [1]
D[2] = [1, 2, 1]

for i in range(3, N + 1) : 

    D[i] = [v for v in D[i - 1]]        # N - 1 층 옮김
    D[i].append(i)                      # N 층 옮김
    
    for sequence in D[i - 1] :          # N - 1 층 다시 옮김
        D[i].append(sequence)

for i, v in enumerate(D[N]) : 
    print(v, end=' ')
    if i % 10 == 9 : print()
print()
