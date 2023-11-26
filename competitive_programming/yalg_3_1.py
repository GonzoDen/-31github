def shortest_distance(N, S, F, graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] != -1 and graph[k][j] != -1:
                    if graph[i][j] == -1 or graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]

    return graph[S - 1][F - 1]

N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = shortest_distance(N, S, F, graph)

if result == float('inf'):
    print(-1)
else:
    print(result)
