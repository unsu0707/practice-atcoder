H, W = map(int, input().split())
A = [list(map(int, input().split())) for l in range(H)]
w_sum = []
for i in range(W):
    sum = 0
    for j in range(H):
        sum += A[j][i]
    w_sum.append(sum)
for i in range(H):
    h_sum = 0
    for j in range(W):
        h_sum += A[i][j]
    result = []
    for j in range(W):
        result.append(w_sum[j] + h_sum - A[i][j])
    print(*result)