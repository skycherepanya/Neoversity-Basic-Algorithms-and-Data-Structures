import networkx as nx
from task1 import G

start = "Vörösmarty tér"
end = "Keleti pályaudvar"

print(f"Шлях від {start} до {end}:")

# 1. BFS
bfs_path = nx.shortest_path(G, source=start, target=end)
print(f"BFS (Ширина): {bfs_path}")

# 2. DFS
dfs_tree = nx.dfs_tree(G, source=start)
dfs_path = nx.shortest_path(dfs_tree, source=start, target=end)
print(f"DFS (Глибина): {dfs_path}")