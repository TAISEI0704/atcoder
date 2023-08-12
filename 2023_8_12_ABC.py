N = int(input())
C = []
A = []

for _ in range(N):
    c = int(input())
    a = list(map(int, input().split()))

    C.append(c)
    A.append(a)

X = int(input())

min_betters = []
length = 110

for i in range(1, N+1):
    if X in A[i-1]:
        item_length = len(str(A[i-1]))
        if item_length < length:
            min_betters = []
            min_betters.append(i)
            length = item_length
        elif item_length == length:
            min_betters.append(i)

print(min_betters)



