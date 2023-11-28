import heapq

def dijkstra(N, d, v, R, routes):
    graph = {i: [] for i in range(1, N + 1)}

    for route in routes:
        dep, dep_time, dest, arr_time = route
        graph[dep].append((dest, dep_time, arr_time))

    distance = {i: float('inf') for i in range(1, N + 1)}
    distance[d] = 0

    priority_queue = [(0, d)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > distance[current_vertex]:
            continue

        for neighbor, dep_time, arr_time in graph[current_vertex]:
            if dep_time >= distance[current_vertex] and arr_time < distance[neighbor]:
                distance[neighbor] = arr_time
                heapq.heappush(priority_queue, (arr_time, neighbor))

    if distance[v] == float('inf'):
        return -1
    else:
        return distance[v]

N = int(input())
d, v = map(int, input().split())
R = int(input())
routes = [list(map(int, input().split())) for _ in range(R)]

result = dijkstra(N, d, v, R, routes)
print(result)
