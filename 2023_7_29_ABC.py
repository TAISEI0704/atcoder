# S = input(str())

# if S == 'ACE' or S == 'BDF' or S == 'CEG' or S == 'DFA' or S == 'EGB' or S == 'FAC' or S == 'GBD':
#     print('Yes')
# else:
#     print('No')
# 
# 
# N, M = map(int,input().split())
# grid = [input() for _ in range(N)]

# for i in range(1,N-8):
#     for j in range(1,M-8):
#         # if grid[i][j] == '#' and grid[i][j+1] == '#' and grid[i][j+2] == '#' and
#         for k in range(3):
#             for l in range(3):
#                 if grid[i+k][j+l] == '#' and grid[i+6+k][j+6+l] == '#':


N, M = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

X = 0


for i in range(N):
    if A[0] > B[M-1]:
        X = B[M-1]+1
        break

    if A[i] >= B[i]:
        if i >= M-i:
            X = A[i]
            break

print(X)


    
