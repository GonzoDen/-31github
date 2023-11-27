import heapq

def dijkstra(N, S, F, graph):
    distance = [float('inf')] * N
    distance[S - 1] = 0
    parent = [-1] * N

    priority_queue = [(0, S - 1)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > distance[current_vertex]:
            continue

        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight != -1 and distance[current_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_vertex] + weight
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance[neighbor], neighbor))

    path = []
    cur_vertex = F - 1
    while cur_vertex != -1:
        path.append(cur_vertex + 1)
        cur_vertex = parent[cur_vertex]

    if path[-1] == S:
        path.reverse()
        print(*path)
    else:
        print(-1)

N, S, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dijkstra(N, S, F, graph)
