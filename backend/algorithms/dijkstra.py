import heapq

def dijkstra_steps(graph):

    steps = []
    dist = {node: float('inf') for node in graph}
    start = list(graph.keys())[0]

    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)

        steps.append({
            "action": "visit",
            "node": node,
            "distance": d
        })

        for nei, w in graph[node]:

            new_dist = d + w

            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(pq, (new_dist, nei))

                steps.append({
                    "action": "update",
                    "node": nei,
                    "distance": new_dist
                })

    return steps