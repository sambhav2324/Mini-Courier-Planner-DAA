import heapq

def dijkstra(graph, start, destination):
    if start not in graph or destination not in graph:
        return float("inf"), []
    distances = {node: float("inf") for node in graph}
    previous = {}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, node = heapq.heappop(queue)
        if current_distance != distances[node]:
            continue
        if node == destination:
            break
        for neighbor, weight in graph[node].items():
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights.")
            candidate = current_distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                previous[neighbor] = node
                heapq.heappush(queue, (candidate, neighbor))
    if distances[destination] == float("inf"):
        return float("inf"), []
    path, node = [], destination
    while node != start:
        path.append(node)
        node = previous[node]
    path.append(start)
    path.reverse()
    return distances[destination], path
