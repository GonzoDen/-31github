import heapq

def dijkstra(N, K, roads, A, B):
    graph = {i: [] for i in range(1, N + 1)}

    for road in roads:
        a, b, l = road
        graph[a].append((b, l))
        graph[b].append((a, l))

    distance = [float('inf')] * (N + 1)
    distance[A] = 0

    priority_queue = [(0, A)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > distance[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            if distance[current_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_vertex] + weight
                heapq.heappush(priority_queue, (distance[neighbor], neighbor))

    if distance[B] == float('inf'):
        return -1
    else:
        return distance[B]

N, K = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(K)]
A, B = map(int, input().split())

result = dijkstra(N, K, roads, A, B)
print(result)
