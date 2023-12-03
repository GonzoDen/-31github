N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            dp[i][j] = 1
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

max_side = max(max(row) for row in dp)
print(max_side)
