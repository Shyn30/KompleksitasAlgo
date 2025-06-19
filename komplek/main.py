from code import Graph

def load_graph(filename):
    g = Graph()
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                u, v, w = parts[0], parts[1], int(parts[2])
                g.add_edge(u, v, w)
    return g

# Simulasi
g = load_graph('graph_jarkom.txt')

start_node = 'A'

print("BFS dari node", start_node, ":", g.bfs(start_node))
print("DFS dari node", start_node, ":", g.dfs(start_node))
print("Dijkstra dari node", start_node, ":", g.dijkstra(start_node))
print("Bellman-Ford dari node", start_node, ":", g.bellman_ford(start_node))
