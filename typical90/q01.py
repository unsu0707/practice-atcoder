N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
 
def check(x):
    pre = 0
    num = 0
    for i in range(N):
        if A[i] - pre > x:
            pre = A[i]
            num += 1
    
    if L - pre > x:
        num += 1
    
    return (num >= K + 1)
 
left, right = -1, L+1
while right - left > 1:
    mid = (left+right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
 
print(left+1)
