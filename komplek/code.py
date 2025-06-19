from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # untuk graf tak berarah
        self.nodes.update([u, v])

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph[node]:
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        visited = set()
        result = []
        def dfs_util(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph[node]:
                    dfs_util(neighbor)
        dfs_util(start)
        return result

    def dijkstra(self, start):
        dist = {node: float('inf') for node in sorted(self.nodes)}
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            current_dist, current_node = heapq.heappop(heap)
            if current_dist > dist[current_node]:
                continue
            for neighbor, weight in self.graph[current_node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        return dist

    def bellman_ford(self, start):
        dist = {node: float('inf') for node in sorted(self.nodes)}
        dist[start] = 0

        for _ in range(len(self.nodes) - 1):
            for u in sorted(self.graph):
                for v, w in self.graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        # Deteksi siklus negatif
        for u in sorted(self.graph):
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    raise Exception("Graph contains a negative-weight cycle")
        return dist
