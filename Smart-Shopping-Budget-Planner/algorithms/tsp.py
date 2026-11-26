from algorithms.dijkstra import dijkstra

def nearest_neighbor_tsp(graph, start, destinations, return_to_start=True):
    remaining = set(destinations)
    remaining.discard(start)
    route = [start]
    total = 0
    current = start
    while remaining:
        choices = []
        for candidate in remaining:
            distance, path = dijkstra(graph, current, candidate)
            if path:
                choices.append((distance, candidate, path))
        if not choices:
            raise ValueError("At least one destination is unreachable from the current store.")
        distance, next_store, path = min(choices, key=lambda item: (item[0], item[1]))
        total += distance
        route.extend(path[1:])
        current = next_store
        remaining.remove(next_store)
    if return_to_start and current != start:
        distance, path = dijkstra(graph, current, start)
        if not path:
            raise ValueError("Cannot return to the starting location.")
        total += distance
        route.extend(path[1:])
    return route, total
